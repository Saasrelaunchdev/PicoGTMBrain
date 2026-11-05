#!/usr/bin/env python3
"""Pico GTM Brain over HTTP. Python 3.9+, standard library only.

Two doors for tools that cannot start a local process:

  REST  /v1/...  load sets, lint, ledger lookups, search, files, metrics, tripwires, the portable layer.
                 Described by adapters/http/openapi.json, for ChatGPT custom GPT Actions, n8n, Zapier, Make,
                 Dify, Flowise, Slack bots, and any language with an HTTP client.
  MCP   /mcp     the tools, resources, and prompts of tools/mcp_server.py over MCP Streamable HTTP with JSON
                 responses, for remote MCP clients such as custom connectors in Claude and ChatGPT.

    python3 tools/http_server.py                                  # http://127.0.0.1:8765, loopback only
    PICO_BRAIN_TOKEN=$(openssl rand -hex 32) python3 tools/http_server.py --host 0.0.0.0

Read only by design. A hosted copy's disk is disposable, so durable writes go through git: the CLI, the stdio
MCP server, or the ingest-event workflow, which adapters/http/github-dispatch.openapi.json describes.

With PICO_BRAIN_TOKEN set, every route except /health and /openapi.json needs `Authorization: Bearer <token>`,
and /mcp also accepts the token as its last path segment (/mcp/<token>) for clients that only take a URL.
Without a token the server refuses to bind anywhere but loopback, and rejects cross-site browser origins.
"""
import argparse
import hmac
import ipaddress
import json
import os
import re
import sys
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, unquote, urlsplit

sys.path.insert(0, str(Path(__file__).resolve().parent))
import brain  # noqa: E402
import mcp_server  # noqa: E402

TOKEN = os.environ.get("PICO_BRAIN_TOKEN", "")
DEFAULT_URL = "http://127.0.0.1:8765"
REPO = "Saasrelaunchdev/PicoGTMBrain"
MAX_BODY = 1_000_000
OPEN_PATHS = {"/health", "/openapi.json"}
LOCAL_ORIGIN = re.compile(r"^https?://(localhost|127\.0\.0\.1|\[::1\])(:\d+)?$")
AUDIENCES = ["merchants", "implementers"]
LOOKUP_KINDS = ["feature", "claim", "term", "decision", "metric"]

ROUTES = [  # method, path pattern, handler name
    ("GET", r"/health", "health"),
    ("GET", r"/openapi\.json", "openapi"),
    ("GET", r"/v1/tasks", "tasks"),
    ("GET", r"/v1/context/(?P<task>[a-z-]+)", "context"),
    ("POST", r"/v1/lint", "lint"),
    ("GET", r"/v1/lookup/(?P<kind>[a-z]+)", "lookup"),
    ("GET", r"/v1/search", "search"),
    ("GET", r"/v1/file", "file"),
    ("GET", r"/v1/metrics", "metrics"),
    ("GET", r"/v1/tripwires", "tripwires"),
    ("GET", r"/v1/portable", "portable"),
]


class BadRequest(Exception):
    pass


# ================================================================ REST handlers: (status, payload, content type)

JSON = "application/json; charset=utf-8"
MARKDOWN = "text/markdown; charset=utf-8"


def h_health(q, body, m):
    fm = brain.frontmatter(brain.read(brain.MASTER))
    return 200, {"ok": True, "server": mcp_server.SERVER, "master_context": {"version": fm.get("version"),
                 "last_updated": fm.get("last_updated")}, "auth": "bearer" if TOKEN else "loopback only"}, JSON


def h_tasks(q, body, m):
    return 200, [{"task": k, "description": v["desc"], "audience": v.get("audience"),
                  "needs_audience": bool(v.get("per_audience"))} for k, v in brain.TASKS.items()], JSON


def h_context(q, body, m):
    task, aud, fmt = m["task"], q.get("audience"), q.get("format", "json")
    if fmt not in ("json", "cat", "list"):
        raise BadRequest("format is json, cat, or list")
    if fmt != "json":
        return 200, brain.context_bundle(task, aud, fmt), MARKDOWN if fmt == "cat" else "text/plain; charset=utf-8"
    out = json.loads(brain.context_bundle(task, aud, "json"))
    if q.get("include_text", "").lower() in ("1", "true", "yes"):
        out["text"] = brain.context_bundle(task, aud, "cat")
    return 200, out, JSON


def h_lint(q, body, m):
    if not isinstance(body, dict) or not isinstance(body.get("text"), str):
        raise BadRequest('send {"text": "...", "audience": "merchants" or "implementers"}')
    aud = body.get("audience")
    if aud not in (None, *AUDIENCES):
        raise BadRequest("audience is merchants or implementers")
    findings = brain.lint_text(body["text"], aud)
    errs = sum(1 for f in findings if f["severity"] == "error")
    return 200, {"errors": errs, "warnings": len(findings) - errs, "findings": findings}, JSON


def h_lookup(q, body, m):
    if m["kind"] not in LOOKUP_KINDS:
        raise BadRequest("kind is " + ", ".join(LOOKUP_KINDS))
    if not q.get("q"):
        raise BadRequest("q is required")
    return 200, brain.lookup(m["kind"], q["q"]), JSON


def h_search(q, body, m):
    if not q.get("q"):
        raise BadRequest("q is required")
    try:
        limit = max(1, min(int(q.get("limit", 30)), 200))
    except ValueError:
        raise BadRequest("limit is an integer")
    return 200, brain.search(q["q"], limit), JSON


def h_file(q, body, m):
    rel = mcp_server.safe_rel(q.get("path", ""))  # ValueError, a 404, outside the brain or not a text file
    text = brain.read(rel)
    return 200, {"path": rel, "layer": brain.layer_of(rel), "sha256": brain.sha256(text), "text": text}, JSON


def h_metrics(q, body, m):
    aud = q.get("audience")
    return 200, [r for r in brain.metric_rows() if not aud or r["audience"] == aud], JSON


def h_tripwires(q, body, m):
    return 200, brain.tripwire_rows(), JSON


def h_portable(q, body, m):
    return 200, brain.read("adapters/portable-control-layer.md"), MARKDOWN


HANDLERS = {"health": h_health, "tasks": h_tasks, "context": h_context, "lint": h_lint, "lookup": h_lookup,
            "search": h_search, "file": h_file, "metrics": h_metrics, "tripwires": h_tripwires, "portable": h_portable}


# ================================================================ OpenAPI, generated into adapters/http/

def _param(name, where="query", required=False, desc="", schema=None):
    return {"name": name, "in": where, "required": required, "description": desc, "schema": schema or {"type": "string"}}


def _ok(desc, kind="object", ctype="application/json"):
    schema = {"type": kind} if ctype == "application/json" else {"type": "string"}
    return {"200": {"description": desc, "content": {ctype: {"schema": schema}}}}


def openapi_spec(base_url=DEFAULT_URL):
    """The REST door, in OpenAPI 3.1. Import it into a custom GPT as an Action, or into n8n, Dify, or Flowise."""
    fm = brain.frontmatter(brain.read(brain.MASTER))
    audience = _param("audience", desc="merchants or implementers, never blended", schema={"type": "string", "enum": AUDIENCES})
    paths = {
        "/health": {"get": {"operationId": "getHealth", "summary": "Server and master context version. No token needed.",
                            "security": [], "responses": _ok("Health")}},
        "/v1/tasks": {"get": {"operationId": "listTasks", "summary": "The tasks in the load policy, and which audience each one takes.",
                              "responses": _ok("Tasks", "array")}},
        "/v1/context/{task}": {"get": {
            "operationId": "getContext",
            "summary": "The exact brain files to load for a task, in order. Call this before writing anything customer-facing, with include_text=true for their full text.",
            "parameters": [_param("task", "path", True, "A task from listTasks", {"type": "string", "enum": sorted(brain.TASKS)}),
                           audience,
                           _param("format", desc="json, the default, or cat for one Markdown document", schema={"type": "string", "enum": ["json", "cat", "list"]}),
                           _param("include_text", desc="With format json, add the concatenated text", schema={"type": "boolean"})],
            "responses": _ok("The load set: paths, hashes, a token estimate, and optionally the text")}},
        "/v1/lint": {"post": {
            "operationId": "lintDraft",
            "summary": "Check a draft against the brain's rules. Fix every error, using the replacement each finding names, before returning the draft.",
            "requestBody": {"required": True, "content": {"application/json": {"schema": {
                "type": "object", "required": ["text"],
                "properties": {"text": {"type": "string"}, "audience": {"type": "string", "enum": AUDIENCES}}}}}},
            "responses": _ok("Error and warning counts, and every finding with its rule and fix")}},
        "/v1/lookup/{kind}": {"get": {
            "operationId": "lookupLedger",
            "summary": "Query a ledger: a feature's status flag, a forbidden claim and what to say instead, a glossary term, a decision by ID such as D25, or a metric against its target.",
            "parameters": [_param("kind", "path", True, schema={"type": "string", "enum": LOOKUP_KINDS}),
                           _param("q", required=True, desc="Words or an ID")],
            "responses": _ok("Matching ledger items", "array")}},
        "/v1/search": {"get": {"operationId": "searchBrain", "summary": "Case-insensitive search across the brain.",
                               "parameters": [_param("q", required=True), _param("limit", schema={"type": "integer", "default": 30})],
                               "responses": _ok("Path, line, and text of each hit", "array")}},
        "/v1/file": {"get": {"operationId": "readFile", "summary": "Read one brain file by its repository path, for example rules/do-not-say.md.",
                             "parameters": [_param("path", required=True)],
                             "responses": _ok("The file's path, layer, hash, and text")}},
        "/v1/metrics": {"get": {"operationId": "getMetrics", "summary": "Every KPI computed from the event log, against its target and review date.",
                                "parameters": [audience], "responses": _ok("Metric rows", "array")}},
        "/v1/tripwires": {"get": {"operationId": "getTripwires", "summary": "Every decision's reopen condition. FIRED means the decision should be reopened.",
                                  "responses": _ok("Tripwire rows", "array")}},
        "/v1/portable": {"get": {"operationId": "getPortableControlLayer", "summary": "The dated paste-in control layer for a model with no file access.",
                                 "responses": _ok("Markdown", ctype="text/markdown")}},
    }
    return {"openapi": "3.1.0",
            "info": {"title": "Pico GTM Brain", "version": str(fm.get("version", "1.0")),
                     "description": "The Pico go-to-market brain, read only. Load the context for a task before writing, lint every draft, and treat the lookups as the source of truth. Pico is pre-launch: there are no customers, reviews, or results, and nothing may be invented."},
            "servers": [{"url": base_url, "description": "Replace with the URL where tools/http_server.py runs"}],
            "paths": paths,
            "components": {"schemas": {}, "securitySchemes": {"bearerAuth": {"type": "http", "scheme": "bearer"}}},
            "security": [{"bearerAuth": []}]}


def dispatch_spec():
    """The write door for tools that only make HTTP calls: GitHub's repository_dispatch, read by ingest-event."""
    payload = {
        "type": "object", "required": ["type", "source"],
        "properties": {
            "type": {"type": "string", "description": "For brain-signal, one of " + ", ".join(brain.SIGNAL_TYPES) +
                     ". For brain-event, one of " + ", ".join(sorted(brain.EVENT_TYPES)) + "."},
            "source": {"type": "string", "description": "Where it came from, for example founding call, App Store review, or Partner Dashboard"},
            "verbatim": {"type": "string", "description": "brain-signal only: the exact words, never paraphrased"},
            "context": {"type": "string", "description": "brain-signal only: who, where, and what was happening"},
            "disposition": {"type": "string", "description": "brain-signal only: NOISE (the default), WATCH (n/N), PATCH, or AMEND"},
            "tags": {"type": "array", "items": {"type": "string"}, "description": "Tripwire tags, for example handoff-request, theme-issue, gcc-inbound, attribution-dispute"},
            "audience": {"type": "string", "enum": ["merchants", "implementers", "both"], "description": "brain-event only"},
            "data": {"type": "object", "description": "brain-event only: the facts. A KPI value uses type metric.observed with data {metric, value, period}, for example {\"metric\": \"m.listing_to_install\", \"value\": 0.031}"},
            "refs": {"type": "object", "description": "brain-event only: related ids by kind, for example {\"experiments\": [\"EXP-001\"], \"decisions\": [\"D33\"]}"},
            "ts": {"type": "string", "description": "brain-event only: when it happened, ISO 8601 in UTC. Defaults to now"},
        }}
    return {"openapi": "3.1.0",
            "info": {"title": "Pico GTM Brain, log a signal or an event", "version": "1",
                     "description": "Writes to the brain through GitHub's repository_dispatch API. The ingest-event workflow validates the payload against schemas/, appends it to ops/signal-log.md or innovation/events/, refreshes the ledger, and commits. Authenticate with a fine-grained GitHub token for this one repository with Contents read and write."},
            "servers": [{"url": "https://api.github.com"}],
            "paths": {f"/repos/{REPO}/dispatches": {"post": {
                "operationId": "logToBrain",
                "summary": "Log what a person said (brain-signal) or what happened (brain-event). Never estimate a value.",
                "requestBody": {"required": True, "content": {"application/json": {"schema": {
                    "type": "object", "required": ["event_type", "client_payload"],
                    "properties": {"event_type": {"type": "string", "enum": ["brain-signal", "brain-event"]},
                                   "client_payload": payload}}}}},
                "responses": {"204": {"description": "Accepted. The workflow commits the entry a minute or two later."}}}}},
            "components": {"schemas": {}, "securitySchemes": {"githubToken": {"type": "http", "scheme": "bearer"}}},
            "security": [{"githubToken": []}]}


# ================================================================ the server

def redact(line):
    return re.sub(r"/mcp/[^\s/?]+", "/mcp/[redacted]", line)


class Handler(BaseHTTPRequestHandler):
    server_version = "pico-gtm-brain/1.0"
    protocol_version = "HTTP/1.1"

    def log_message(self, fmt, *args):
        sys.stderr.write(f"{self.address_string()} {redact(fmt % args)}\n")

    def send(self, status, payload=b"", ctype=JSON, headers=None):
        if isinstance(payload, (dict, list)):
            payload = json.dumps(payload, indent=2, ensure_ascii=False)
        body = payload.encode("utf-8") if isinstance(payload, str) else payload
        self.send_response(status)
        if body:
            self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.send_header("X-Content-Type-Options", "nosniff")
        for k, v in (headers or {}).items():
            self.send_header(k, v)
        self.end_headers()
        if body and self.command != "HEAD":
            self.wfile.write(body)

    def body_json(self):
        n = int(self.headers.get("Content-Length") or 0)
        if n > MAX_BODY:
            raise BadRequest(f"body over {MAX_BODY} bytes")
        raw = self.rfile.read(n) if n else b""
        try:
            return json.loads(raw.decode("utf-8")) if raw else None
        except (UnicodeDecodeError, json.JSONDecodeError) as e:
            raise BadRequest(f"body is not JSON: {e}")

    def origin_ok(self):
        origin = self.headers.get("Origin")
        return bool(TOKEN) or not origin or bool(LOCAL_ORIGIN.match(origin))

    def authorized(self, p):
        if not TOKEN or p in OPEN_PATHS:
            return True
        auth = self.headers.get("Authorization", "")
        if auth[:7].lower() == "bearer " and hmac.compare_digest(auth[7:].strip().encode(), TOKEN.encode()):
            return True
        m = re.fullmatch(r"/mcp/([^/]+)", p)
        return bool(m) and hmac.compare_digest(unquote(m.group(1)).encode(), TOKEN.encode())

    def base_url(self):
        proto = self.headers.get("X-Forwarded-Proto", "http").split(",")[0].strip()
        host = self.headers.get("X-Forwarded-Host") or self.headers.get("Host") or DEFAULT_URL.split("//")[1]
        return f"{proto}://{host}"

    def route(self, method):
        url = urlsplit(self.path)
        p = url.path.rstrip("/") or "/"
        q = {k: v[-1] for k, v in parse_qs(url.query).items()}
        if not self.origin_ok():
            return self.send(403, {"error": "this origin may not call a server without a token"})
        if not self.authorized(p):
            return self.send(401, {"error": "missing or wrong bearer token"}, headers={"WWW-Authenticate": "Bearer"})
        try:
            if p == "/mcp" or p.startswith("/mcp/"):
                if method != "POST":
                    return self.send(405, {"error": "POST JSON-RPC messages here. This server sends no event stream."},
                                     headers={"Allow": "POST"})
                return self.mcp()
            if p == "/openapi.json" and method == "GET":
                return self.send(200, openapi_spec(self.base_url()))
            allowed = []
            for verb, pattern, name in ROUTES:
                m = re.fullmatch(pattern, p)
                if m:
                    if verb != method:
                        allowed.append(verb)
                        continue
                    body = self.body_json() if method == "POST" else None
                    status, payload, ctype = HANDLERS[name](q, body, m.groupdict())
                    return self.send(status, payload, ctype)
            if allowed:
                return self.send(405, {"error": f"use {', '.join(allowed)}"}, headers={"Allow": ", ".join(allowed)})
            return self.send(404, {"error": "no such route", "see": "/openapi.json"})
        except BadRequest as e:
            return self.send(413 if "bytes" in str(e) else 400, {"error": str(e)})
        except SystemExit as e:  # the load policy refuses, for example a blended audience
            return self.send(400, {"error": str(e)})
        except ValueError as e:
            return self.send(404, {"error": str(e)})
        except Exception as e:  # one bad call never takes the server down
            return self.send(500, {"error": f"{type(e).__name__}: {e}"})

    def mcp(self):
        try:
            msg = self.body_json()
        except BadRequest as e:
            return self.send(400, {"jsonrpc": "2.0", "id": None, "error": {"code": -32700, "message": str(e)}})
        if isinstance(msg, list):
            out = [r for r in (mcp_server.respond(x, readonly=True) for x in msg) if r is not None]
        else:
            out = mcp_server.respond(msg, readonly=True)
        return self.send(202) if not out else self.send(200, out)

    def do_GET(self):
        self.route("GET")

    def do_HEAD(self):
        self.route("GET")

    def do_POST(self):
        self.route("POST")

    def do_DELETE(self):
        self.route("DELETE")

    def do_PUT(self):
        self.route("PUT")


def is_loopback(host):
    if host == "localhost":
        return True
    try:
        return ipaddress.ip_address(host).is_loopback
    except ValueError:
        return False


def make_server(host="127.0.0.1", port=8765):
    if not TOKEN and not is_loopback(host):
        raise SystemExit(f"refusing to serve on {host} without PICO_BRAIN_TOKEN. Set a token, or bind to 127.0.0.1.")
    srv = ThreadingHTTPServer((host, port), Handler)
    srv.daemon_threads = True
    return srv


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--host", default=os.environ.get("PICO_BRAIN_HOST", "127.0.0.1"))
    ap.add_argument("--port", type=int, default=int(os.environ.get("PORT") or os.environ.get("PICO_BRAIN_PORT") or 8765))
    a = ap.parse_args(argv)
    srv = make_server(a.host, a.port)
    host, port = srv.server_address[:2]
    print(f"pico-gtm-brain on http://{host}:{port}  REST /v1, OpenAPI /openapi.json, MCP /mcp, "
          f"auth: {'bearer token' if TOKEN else 'none, loopback only'}, read only", file=sys.stderr)
    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        srv.server_close()


if __name__ == "__main__":
    main()
