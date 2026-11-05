"""Unit tests for the brain CLI, the tool doors, the MCP server, and the HTTP server. Standard library only.

    python3 -m unittest discover -s tools/tests -v
"""
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

TOOLS = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(TOOLS))
import brain  # noqa: E402


class Lint(unittest.TestCase):
    def rules(self, text):
        return {f["rule"] for f in brain.lint_text(text) if f["severity"] == "error"}

    def test_catches_outcome_and_proof_claims(self):
        r = self.rules("Pico increases sales. Trusted by brands, 4.9 stars.")
        self.assertIn("claims.do-not-say", r)
        self.assertIn("claims.outcome", r)

    def test_catches_status_and_mechanics(self):
        r = self.rules("It uses semantic search " + brain.EM_DASH + " and checks live stock.")
        self.assertIn("status.unshipped", r)
        self.assertIn("mechanics.em-dash", r)

    def test_catches_banned_words_and_comparisons(self):
        r = self.rules("Leverage Pico, smarter than Shopify search.")
        self.assertIn("mechanics.banned-word", r)
        self.assertIn("claims.comparison", r)

    def test_platform_rule(self):
        r = self.rules("Upwork job: install Pico. Afterwards, join our partner program at picofinds.com/partners.")
        self.assertIn("channel.platform", r)

    def test_clean_copy_passes(self):
        text = "Product cards show names, prices, and stock from your synced catalog. Open the sandbox store."
        self.assertEqual(self.rules(text), set())

    def test_examples_are_clean(self):
        for p in (brain.ROOT / "examples").glob("*.md"):
            body = brain.example_body(str(p.relative_to(brain.ROOT)))
            self.assertEqual(self.rules(body), set(), p.name)


class Ledgers(unittest.TestCase):
    def test_exports_parse(self):
        self.assertGreater(len(brain.export_features()["items"]), 30)
        flags = {i["status"] for i in brain.export_features()["items"]}
        self.assertTrue(flags <= set(brain.STATUS_FLAGS))
        self.assertGreater(len(brain.export_claims()["items"]), 20)
        ids = {i for d in brain.export_decisions()["items"] for i in d["ids"]}
        for d in ("D4", "D25", "D33", "D35", "D56"):
            self.assertIn(d, ids)

    def test_every_decision_id_resolves(self):
        ids = [i for d in brain.export_decisions()["items"] for i in d["ids"]]
        self.assertEqual(sorted(set(ids) - {"B1"}, key=lambda x: int(x[1:])), [f"D{n}" for n in range(1, 57)])
        self.assertIn("Legal", brain.lookup("decision", "D48")[0]["title"])  # inside "D47 to D52"

    def test_exports_match_schema(self):
        sch = brain.schema("export")
        for kind, fn in brain.EXPORTS.items():
            self.assertEqual(brain.validate(fn(), sch), [], kind)

    def test_innovation_files_validate(self):
        self.assertEqual(brain.validate_all(), [])

    def test_generated_files_current(self):
        stale = [rel for rel, text in brain.generated().items() if brain.read(rel) != text]
        self.assertEqual(stale, [], "run python3 tools/brain.py build")


class ContextLayer(unittest.TestCase):
    def test_load_sets_resolve(self):
        for task, spec in brain.TASKS.items():
            aud = spec.get("audience") or ("merchants" if spec.get("per_audience") else None)
            _, files = brain.load_set(task, aud)
            self.assertTrue(files, task)
            for f in files:
                self.assertTrue((brain.ROOT / f).exists(), f)

    def test_audiences_never_blend(self):
        with self.assertRaises(SystemExit):
            brain.load_set("cold-email", "merchants")
        with self.assertRaises(SystemExit):
            brain.load_set("copy", None)


class Accounting(unittest.TestCase):
    def test_metrics_and_tripwires(self):
        ev = [{"id": "evt_000000000001", "ts": "2026-12-01T00:00:00Z", "type": "metric.observed", "audience": "implementers",
               "source": "test", "data": {"metric": "i.upwork_applicants_per_post", "value": 6}}]
        rows = {r["id"]: r for r in brain.metric_rows(ev)}
        self.assertEqual(rows["i.upwork_applicants_per_post"]["status"], "below target")
        fired = {t["id"]: t["status"] for t in brain.tripwire_rows(ev)}
        self.assertEqual(fired["TW-D33"], "FIRED")
        self.assertEqual(fired["TW-D42"], "no data")

    def test_counts_and_ratios(self):
        mk = lambda i, t, d: {"id": f"evt_{i:012d}", "ts": "2026-11-20T00:00:00Z", "type": t, "audience": "implementers", "source": "t", "data": d}
        ev = [mk(1, "session.completed", {"channel": "upwork", "setup_minutes": 22}),
              mk(2, "session.completed", {"channel": "fiverr", "setup_minutes": 40}),
              mk(3, "interview.completed", {})]
        rows = {r["id"]: r for r in brain.metric_rows(ev)}
        self.assertEqual(rows["i.sessions_completed"]["value"], 2)
        self.assertEqual(rows["i.upwork_hires"]["value"], 1)
        self.assertEqual(rows["i.interview_acceptance"]["value"], 0.5)
        self.assertEqual(rows["i.median_setup_minutes"]["value"], 31)

    def test_event_schema_rejects_bad_events(self):
        bad = {"id": "nope", "ts": "yesterday", "type": "Bad Type", "audience": "everyone", "source": "", "data": {}}
        self.assertGreaterEqual(len(brain.validate(bad, brain.schema("event"))), 4)


class Mcp(unittest.TestCase):
    def session(self, *reqs):
        lines = "\n".join(json.dumps(r) for r in reqs) + "\n"
        out = subprocess.run([sys.executable, str(TOOLS / "mcp_server.py")], input=lines, capture_output=True,
                             text=True, env={"PICO_BRAIN_READONLY": "1", "PATH": "/usr/bin:/bin"}, timeout=60)
        return [json.loads(x) for x in out.stdout.splitlines() if x.strip()]

    def test_handshake_and_calls(self):
        res = self.session(
            {"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {"protocolVersion": "2025-06-18"}},
            {"jsonrpc": "2.0", "method": "notifications/initialized"},
            {"jsonrpc": "2.0", "id": 2, "method": "tools/list"},
            {"jsonrpc": "2.0", "id": 3, "method": "tools/call", "params": {"name": "brain_lint", "arguments": {"text": "Pico boosts conversion."}}},
            {"jsonrpc": "2.0", "id": 4, "method": "resources/read", "params": {"uri": "brain:///rules/glossary.md"}},
            {"jsonrpc": "2.0", "id": 5, "method": "tools/call", "params": {"name": "brain_read", "arguments": {"path": "../../etc/passwd"}}})
        by = {r["id"]: r for r in res}
        self.assertEqual(by[1]["result"]["protocolVersion"], "2025-06-18")
        names = {t["name"] for t in by[2]["result"]["tools"]}
        self.assertIn("brain_load_set", names)
        self.assertNotIn("brain_log_event", names)  # read-only mode hides writes
        self.assertGreater(json.loads(by[3]["result"]["content"][0]["text"])["errors"], 0)
        self.assertIn("Glossary", by[4]["result"]["contents"][0]["text"])
        self.assertTrue(by[5]["result"]["isError"])


class Doors(unittest.TestCase):
    def test_rule_doors_point_at_the_brain(self):
        outs = brain.door_outputs()
        for rel, *_ in brain.RULE_DOORS:
            for must in ("AGENTS.md", "rules/do-not-say.md", "rules/feature-status.md", "tools/brain.py lint"):
                self.assertIn(must, outs[rel], rel)

    def test_every_command_reaches_every_tool(self):
        outs = brain.door_outputs()
        names = [c["name"] for c in brain.claude_commands()]
        self.assertGreaterEqual(len(names), 7)
        for tool, spec in brain.COMMAND_TOOLS.items():
            for n in names:
                text = outs[spec["path"].format(n=n)]
                if spec["args"] != "$ARGUMENTS":
                    self.assertNotIn("$ARGUMENTS", text, f"{tool} {n}")
                self.assertNotIn("`/amend`", text, f"{tool} {n} points at another tool's command")

    def test_gemini_commands_are_valid_toml(self):
        try:
            import tomllib
        except ImportError:
            self.skipTest("tomllib needs Python 3.11")
        for rel, text in brain.door_outputs().items():
            if rel.endswith(".toml"):
                doc = tomllib.loads(text)
                self.assertTrue(doc["description"] and doc["prompt"], rel)

    def test_installer_blocks_survive_a_build(self):
        outs = brain.door_outputs()
        for rel in ("GEMINI.md", ".github/copilot-instructions.md"):
            self.assertIn(brain.BLOCK_BEGIN, outs[rel])
            self.assertIn("<!-- gtm-brain:end -->", outs[rel])

    def test_specs_are_valid_json_with_operation_ids(self):
        import http_server
        for spec in (http_server.openapi_spec(), http_server.dispatch_spec()):
            self.assertEqual(spec["openapi"], "3.1.0")
            ops = [op for item in spec["paths"].values() for op in item.values()]
            self.assertTrue(ops)
            for op in ops:
                self.assertRegex(op["operationId"], r"^[a-zA-Z]+$")


class Http(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        import threading
        import urllib.request
        import http_server
        cls.hs = http_server
        http_server.Handler.log_message = lambda *a: None  # keep test output clean
        cls.srv = http_server.make_server("127.0.0.1", 0)
        cls.base = f"http://127.0.0.1:{cls.srv.server_address[1]}"
        cls.opener = urllib.request.build_opener(urllib.request.ProxyHandler({}))  # never route loopback via a proxy
        threading.Thread(target=cls.srv.serve_forever, daemon=True).start()

    @classmethod
    def tearDownClass(cls):
        cls.srv.shutdown()
        cls.srv.server_close()

    def call(self, method, route, body=None, headers=None):
        import urllib.error
        import urllib.request
        data = json.dumps(body).encode() if body is not None else None
        req = urllib.request.Request(self.base + route, data=data, method=method,
                                     headers={"Content-Type": "application/json", **(headers or {})})
        try:
            with self.opener.open(req, timeout=30) as r:
                status, raw, ctype = r.status, r.read(), r.headers.get("Content-Type", "")
        except urllib.error.HTTPError as e:
            status, raw, ctype = e.code, e.read(), e.headers.get("Content-Type", "")
        if raw and "json" in ctype:
            return status, json.loads(raw)
        return status, raw.decode("utf-8")

    def test_rest_routes(self):
        self.assertEqual(self.call("GET", "/health")[0], 200)
        status, tasks = self.call("GET", "/v1/tasks")
        self.assertEqual((status, len(tasks)), (200, len(brain.TASKS)))
        status, ctx = self.call("GET", "/v1/context/cold-email?include_text=true")
        self.assertEqual(status, 200)
        self.assertIn("rules/do-not-say.md", [f["path"] for f in ctx["files"]])
        self.assertIn("===== rules/do-not-say.md =====", ctx["text"])
        self.assertEqual(self.call("GET", "/v1/context/cold-email?audience=merchants")[0], 400)  # never blended
        status, lint = self.call("POST", "/v1/lint", {"text": "Pico boosts conversion."})
        self.assertGreater(lint["errors"], 0)
        self.assertTrue(self.call("GET", "/v1/lookup/decision?q=D24")[1])
        self.assertEqual(self.call("GET", "/v1/file?path=../../etc/passwd")[0], 404)
        self.assertEqual(self.call("GET", "/v1/file?path=rules/glossary.md")[1]["layer"], "control")
        self.assertIn("portable control layer", self.call("GET", "/v1/portable")[1])
        self.assertEqual(self.call("GET", "/v1/lint")[0], 405)
        self.assertEqual(self.call("GET", "/nope")[0], 404)

    def test_every_documented_route_is_served(self):
        for route, item in self.hs.openapi_spec()["paths"].items():
            for method, op in item.items():
                url = route.replace("{task}", "session").replace("{kind}", "decision")
                url += "?q=D24&path=CLAUDE.md" if method == "get" else ""
                status, _ = self.call(method.upper(), url, {"text": "x"} if method == "post" else None)
                self.assertEqual(status, 200, f"{method} {route}")

    def test_remote_mcp_is_read_only(self):
        rpc = lambda i, m, p=None: {"jsonrpc": "2.0", "id": i, "method": m, "params": p or {}}
        status, init = self.call("POST", "/mcp", rpc(1, "initialize", {"protocolVersion": "2025-06-18"}))
        self.assertEqual((status, init["result"]["protocolVersion"]), (200, "2025-06-18"))
        self.assertEqual(self.call("POST", "/mcp", {"jsonrpc": "2.0", "method": "notifications/initialized"})[0], 202)
        names = {t["name"] for t in self.call("POST", "/mcp", rpc(2, "tools/list"))[1]["result"]["tools"]}
        self.assertIn("brain_lint", names)
        self.assertNotIn("brain_log_event", names)
        res = self.call("POST", "/mcp", rpc(3, "tools/call", {"name": "brain_log_event", "arguments": {
            "type": "milestone", "data": {}, "source": "test"}}))[1]["result"]
        self.assertTrue(res["isError"])
        self.assertEqual(self.call("GET", "/mcp")[0], 405)

    def test_token_guards_everything_but_health(self):
        self.hs.TOKEN = "s3cret-token"
        try:
            self.assertEqual(self.call("GET", "/health")[0], 200)
            self.assertEqual(self.call("GET", "/v1/tasks")[0], 401)
            self.assertEqual(self.call("GET", "/v1/tasks", headers={"Authorization": "Bearer wrong"})[0], 401)
            self.assertEqual(self.call("GET", "/v1/tasks", headers={"Authorization": "Bearer s3cret-token"})[0], 200)
            init = {"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {}}
            self.assertEqual(self.call("POST", "/mcp/s3cret-token", init)[0], 200)
            self.assertEqual(self.call("POST", "/mcp/guess", init)[0], 401)
        finally:
            self.hs.TOKEN = ""

    def test_refuses_a_public_interface_without_a_token(self):
        with self.assertRaises(SystemExit):
            self.hs.make_server("0.0.0.0", 0)

    def test_cross_site_origin_rejected_without_a_token(self):
        self.assertEqual(self.call("GET", "/v1/tasks", headers={"Origin": "https://evil.example"})[0], 403)
        self.assertEqual(self.call("GET", "/v1/tasks", headers={"Origin": "http://localhost:3000"})[0], 200)


if __name__ == "__main__":
    unittest.main()
