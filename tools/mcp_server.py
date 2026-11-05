#!/usr/bin/env python3
"""Pico GTM Brain as a Model Context Protocol server. Python 3.9+, standard library only.

Speaks MCP over stdio (newline-delimited JSON-RPC 2.0), so any MCP client can mount the brain:
Claude Code, Claude Desktop, Cursor, Windsurf, VS Code and Copilot agent mode, Codex CLI, Gemini CLI,
Zed, Cline, Continue, and agent frameworks with an MCP adapter. tools/http_server.py serves the same handler over
MCP Streamable HTTP for remote clients, always read only.

    python3 tools/mcp_server.py            # serve on stdio
    PICO_BRAIN_READONLY=1 python3 tools/mcp_server.py   # disable the two write tools

Resources: every brain file, as brain:///<path>.
Tools:     load sets, file reads, search, lint, ledger lookups, metrics, tripwires, and two writes:
           brain_log_signal and brain_log_event, which append to the signal log and the event log.
Prompts:   write-asset, log-signal, weekly-review, amend.
"""
import json
import os
import sys
import traceback
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import brain  # noqa: E402

SERVER = {"name": "pico-gtm-brain", "version": "1.0.0"}
PROTOCOLS = ["2025-06-18", "2025-03-26", "2024-11-05"]
READONLY = os.environ.get("PICO_BRAIN_READONLY") == "1"
READABLE = (".md", ".txt", ".mdc", ".json", ".jsonl")
WRITE_TOOLS = ("brain_log_signal", "brain_log_event")
AUDIENCE = {"type": "string", "enum": ["merchants", "implementers"]}


def _schema(props, required=()):
    return {"type": "object", "properties": props, "required": list(required), "additionalProperties": False}


TOOLS = [
    {"name": "brain_load_set", "description": "The files an agent must load for a task, in order, with their full text when include_text is true. Call this before writing anything customer-facing. Tasks: " + ", ".join(sorted(brain.TASKS)) + ".",
     "inputSchema": _schema({"task": {"type": "string", "enum": sorted(brain.TASKS)}, "audience": AUDIENCE,
                             "include_text": {"type": "boolean", "default": False}}, ["task"])},
    {"name": "brain_read", "description": "Read one brain file by its repository path, for example rules/do-not-say.md.",
     "inputSchema": _schema({"path": {"type": "string"}}, ["path"])},
    {"name": "brain_search", "description": "Case-insensitive search across the brain's Markdown and JSON. Returns path, line, and text.",
     "inputSchema": _schema({"query": {"type": "string"}, "limit": {"type": "integer", "default": 30}}, ["query"])},
    {"name": "brain_lint", "description": "Check draft copy against the control layer: banned words, em dashes, forbidden claims with their safe replacements, unshipped capabilities, outcome and proof claims, named comparisons, and channel rules. Run on every draft before returning it.",
     "inputSchema": _schema({"text": {"type": "string"}, "audience": AUDIENCE}, ["text"])},
    {"name": "brain_lookup", "description": "Query a ledger. kind: feature (status flags), claim (do-not-say with say-instead), term (glossary), decision (by ID such as D25 or by title words), metric (current value against target).",
     "inputSchema": _schema({"kind": {"type": "string", "enum": ["feature", "claim", "term", "decision", "metric"]},
                             "query": {"type": "string"}}, ["kind", "query"])},
    {"name": "brain_metrics", "description": "Every KPI computed from the innovation event log, against its target and review point.",
     "inputSchema": _schema({"audience": AUDIENCE})},
    {"name": "brain_tripwires", "description": "Evaluate every decision's machine-checkable reopen condition. FIRED means the decision should be reopened.",
     "inputSchema": _schema({})},
    {"name": "brain_log_signal", "description": "Append a market signal to ops/signal-log.md, verbatim, and mirror it as a signal.logged event. Default disposition NOISE. Use tags for tripwires, for example handoff-request, theme-issue, gcc-inbound.",
     "inputSchema": _schema({"type": {"type": "string", "enum": brain.SIGNAL_TYPES}, "source": {"type": "string"},
                             "verbatim": {"type": "string"}, "context": {"type": "string"},
                             "disposition": {"type": "string", "default": "NOISE"}, "routed_to": {"type": "string", "default": "none"},
                             "tags": {"type": "array", "items": {"type": "string"}}}, ["type", "source", "verbatim"])},
    {"name": "brain_log_event", "description": "Append one activity to the append-only innovation event log, validated against schemas/event.schema.json. Types include metric.observed, install, session.completed, review.received, partner.signed, asset.shipped, experiment.closed.",
     "inputSchema": _schema({"type": {"type": "string"}, "audience": {"type": "string", "enum": ["merchants", "implementers", "both"]},
                             "data": {"type": "object"}, "source": {"type": "string"}, "refs": {"type": "object"},
                             "tags": {"type": "array", "items": {"type": "string"}}}, ["type", "data", "source"])},
]

PROMPTS = [
    {"name": "write-asset", "description": "Produce one customer-facing asset inside the guardrails.",
     "arguments": [{"name": "task", "description": "A task from brain_load_set, for example cold-email", "required": True},
                   {"name": "audience", "description": "merchants or implementers", "required": False},
                   {"name": "brief", "description": "What the asset is for", "required": True}]},
    {"name": "log-signal", "description": "Turn a call note, review, or message into a triaged signal.",
     "arguments": [{"name": "note", "description": "The raw note, pasted", "required": True}]},
    {"name": "weekly-review", "description": "Run the Monday loop: tripwires, triage, metrics, ledger.", "arguments": []},
    {"name": "amend", "description": "Change a ledger through the full amendment procedure.",
     "arguments": [{"name": "change", "description": "What changed, with its evidence", "required": True}]},
]


def text_result(obj, is_error=False):
    body = obj if isinstance(obj, str) else json.dumps(obj, indent=2, ensure_ascii=False)
    return {"content": [{"type": "text", "text": body}], "isError": is_error}


def safe_rel(rel):
    p = (brain.ROOT / rel).resolve()
    if brain.ROOT not in p.parents or not p.is_file() or p.suffix not in READABLE or ".git" in p.parts:
        raise ValueError(f"not a readable brain file: {rel}")
    return str(p.relative_to(brain.ROOT))


def call_tool(name, args, readonly=None):
    readonly = READONLY if readonly is None else readonly
    if name == "brain_load_set":
        if args.get("include_text"):
            return text_result(brain.context_bundle(args["task"], args.get("audience"), "cat"))
        return text_result(json.loads(brain.context_bundle(args["task"], args.get("audience"), "json")))
    if name == "brain_read":
        return text_result(brain.read(safe_rel(args["path"])))
    if name == "brain_search":
        return text_result(brain.search(args["query"], int(args.get("limit", 30))))
    if name == "brain_lint":
        findings = brain.lint_text(args["text"], args.get("audience"))
        errs = sum(1 for f in findings if f["severity"] == "error")
        return text_result({"errors": errs, "warnings": len(findings) - errs, "findings": findings})
    if name == "brain_lookup":
        return text_result(brain.lookup(args["kind"], args["query"]))
    if name == "brain_metrics":
        rows = brain.metric_rows()
        aud = args.get("audience")
        return text_result([r for r in rows if not aud or r["audience"] == aud])
    if name == "brain_tripwires":
        return text_result(brain.tripwire_rows())
    if name in WRITE_TOOLS:
        if readonly:
            return text_result("This server is read only. Log signals and events with tools/brain.py, the stdio MCP server, "
                               "or the ingest-event workflow.", True)
        if name == "brain_log_signal":
            rec, ev = brain.add_signal(args["type"], args["source"], args["verbatim"], args.get("context", ""),
                                       args.get("disposition", "NOISE"), args.get("routed_to", "none"), args.get("tags"))
            brain.refresh()
            return text_result({"logged": rec, "event": ev["id"], "next": "Triage it in the weekly review, or now if it is a verifiable fact."})
        ev, new = brain.append_event(args["type"], args.get("audience", "both"), args.get("data", {}), args["source"],
                                     args.get("refs"), args.get("tags"))
        brain.refresh()
        return text_result({"event": ev, "appended": new})
    raise KeyError(name)


def get_prompt(name, args):
    if name == "write-asset":
        task, aud = args.get("task", "copy"), args.get("audience")
        _, files = brain.load_set(task, aud)
        msg = (f"You are producing a Pico go-to-market asset. Task: {task}. Audience: {aud or 'as the task fixes it'}. Brief: {args.get('brief', '')}\n\n"
               f"Load these brain files in order, with brain_read or brain_load_set: {', '.join(files)}.\n"
               "Use ops/copy-bank.md lines verbatim where they fit. Never write an unshipped capability in the present tense. "
               "Never invent a number, customer, review, or quote. Run brain_lint on the draft and fix every error, then walk ops/QA-checklist.md. "
               "Return the asset, then list every capability mentioned with its status flag, any claim you narrowed, and anything the brain could not supply.")
    elif name == "log-signal":
        msg = ("Log this market input as a signal. Keep the verbatim. Pick the type, set the disposition with the thresholds in ops/signal-log.md "
               "(default NOISE), add tags that match innovation/tripwires.json where relevant, call brain_log_signal, then call brain_tripwires "
               f"and say whether any decision should be reopened.\n\nNote:\n{args.get('note', '')}")
    elif name == "weekly-review":
        msg = ("Run the Monday review of the Pico brain: call brain_tripwires, then brain_metrics, read the newest entries in ops/signal-log.md, "
               "increment or expire WATCH items, list PATCHes to make now and AMENDs that need the founder, and say plainly what did not change.")
    elif name == "amend":
        msg = ("Follow the AMEND procedure for this change, in order: the rules/ ledger first with last_reviewed updated, then the master context with a "
               "version bump, then a dated ops/decisions.md entry with what this does not change and the downstream list, then search the copy bank "
               f"for the old phrasing, then run `python3 tools/brain.py build`. Change:\n{args.get('change', '')}")
    else:
        raise KeyError(name)
    return {"description": next(p["description"] for p in PROMPTS if p["name"] == name),
            "messages": [{"role": "user", "content": {"type": "text", "text": msg}}]}


def resources():
    out = []
    doors = set(brain.door_outputs())  # tool pointer files repeat one source, so list that source once
    for rel in brain.brain_files():
        if rel.endswith(READABLE) and not rel.startswith(("sources/",)) and rel not in doors:
            mime = "application/json" if rel.endswith((".json", ".jsonl")) else "text/markdown"
            out.append({"uri": f"brain:///{rel}", "name": rel, "mimeType": mime,
                        "description": f"{brain.layer_of(rel)} layer"})
    return out


def handle(req, readonly=None):
    readonly = READONLY if readonly is None else readonly
    method, params = req.get("method"), req.get("params") or {}
    if method == "initialize":
        asked = params.get("protocolVersion")
        return {"protocolVersion": asked if asked in PROTOCOLS else PROTOCOLS[0],
                "capabilities": {"tools": {"listChanged": False}, "resources": {"listChanged": False}, "prompts": {"listChanged": False}},
                "serverInfo": SERVER,
                "instructions": "The Pico go-to-market brain. Before customer-facing writing, call brain_load_set for the task, follow the files it names, and run brain_lint on the draft. Audiences are merchants and implementers, never blended."}
    if method == "ping":
        return {}
    if method == "tools/list":
        tools = [t for t in TOOLS if not (readonly and t["name"] in WRITE_TOOLS)]
        return {"tools": tools}
    if method == "tools/call":
        try:
            return call_tool(params.get("name"), params.get("arguments") or {}, readonly)
        except KeyError as e:
            raise LookupError(f"unknown tool {e}")
        except (ValueError, SystemExit) as e:
            return text_result(str(e), True)
    if method == "resources/list":
        return {"resources": resources()}
    if method == "resources/read":
        uri = params.get("uri", "")
        rel = safe_rel(uri.replace("brain:///", "", 1))
        mime = "application/json" if rel.endswith((".json", ".jsonl")) else "text/markdown"
        return {"contents": [{"uri": uri, "mimeType": mime, "text": brain.read(rel)}]}
    if method == "prompts/list":
        return {"prompts": PROMPTS}
    if method == "prompts/get":
        return get_prompt(params.get("name"), params.get("arguments") or {})
    raise LookupError(f"method not found: {method}")


def respond(req, readonly=None):
    """One JSON-RPC message in, one response out, or None for a notification. Shared by stdio and HTTP."""
    if not isinstance(req, dict) or "id" not in req:
        return None  # a notification, such as notifications/initialized
    resp = {"jsonrpc": "2.0", "id": req["id"]}
    try:
        resp["result"] = handle(req, readonly)
    except LookupError as e:
        resp["error"] = {"code": -32601, "message": str(e)}
    except Exception as e:  # never crash the session on one bad call
        resp["error"] = {"code": -32603, "message": f"{type(e).__name__}: {e}",
                         "data": traceback.format_exc(limit=3)}
    return resp


def serve(stdin=sys.stdin, stdout=sys.stdout):
    for line in stdin:
        line = line.strip()
        if not line:
            continue
        try:
            req = json.loads(line)
        except json.JSONDecodeError as e:
            stdout.write(json.dumps({"jsonrpc": "2.0", "id": None, "error": {"code": -32700, "message": str(e)}}) + "\n")
            stdout.flush()
            continue
        resp = respond(req)
        if resp is not None:
            stdout.write(json.dumps(resp, ensure_ascii=False) + "\n")
            stdout.flush()


if __name__ == "__main__":
    serve()
