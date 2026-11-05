#!/usr/bin/env python3
"""The Pico GTM Brain command line. Python 3.9+, standard library only.

The brain is Markdown first. This tool is the machine interface on top of it:

  context    print the exact load set for a task, as paths, concatenated text, or JSON
  lint       check a draft against the control layer (claims, status, channels, mechanics)
  lookup     query the ledgers: feature, claim, term, decision, metric
  search     grep the brain
  signal     append a market signal to ops/signal-log.md and mirror it as an event
  event      append an activity to the innovation event log
  metrics    compute every KPI from the event log against its target
  tripwires  evaluate every decision's machine-checkable reopen condition
  ledger     regenerate innovation/LEDGER.md
  snapshot   scaffold a dated snapshot pre-filled with current metrics
  export     regenerate data/*.json from the Markdown ledgers
  build      export, bundle (llms-full.txt and the portable control layer), ledger, every tool door
             (rendered from adapters/door.md and .claude/commands/), and the HTTP specs
  check      fail if any generated file is stale (used in CI)
  validate   validate the innovation JSON files and the event log against schemas/
  audit      run the vendored go-to-market-brain audit on the brain, plus this repo's checks

Run `python3 tools/brain.py <command> --help` for options.
"""
import argparse
import datetime as dt
import hashlib
import json
import re
import shutil
import statistics
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
VENDORED_AUDIT = ROOT / ".claude" / "skills" / "go-to-market-brain" / "scripts" / "audit_brain.py"
MASTER = "context/Pico_GTM_Master_Context.md"
RULES = ["rules/glossary.md", "rules/feature-status.md", "rules/do-not-say.md", "rules/writing-rules.md"]
EM_DASH = chr(0x2014)
EN_DASH = chr(0x2013)
BANNED = ["leverage", "unlock", "seamless", "robust", "streamline", "cutting-edge", "empower"]
SLOP = ["elevate", "revolutionize", "game-changing", "best-in-class", "world-class", "supercharge", "turbocharge",
        "harness", "delve", "tapestry", "realm", "testament", "foster", "facilitate", "utilize", "myriad",
        "plethora", "pivotal"]
SIGNAL_TYPES = ["OBJECTION", "LANGUAGE", "PROOF", "STATUS", "COMPETITIVE", "SEGMENT", "CHANNEL", "LOSS", "RISK"]
EVENT_TYPES = {"metric.observed", "signal.logged", "install", "activation.step", "conversation.first", "plan.changed",
               "uninstall", "review.received", "cohort.joined", "session.offered", "session.completed",
               "interview.completed", "case_study.permission", "partner.signed", "payout.made", "asset.shipped",
               "experiment.started", "experiment.closed", "decision.made", "decision.reopened", "milestone"}
STATUS_FLAGS = ["SHIPPED", "PARTIAL", "IN BUILD", "ROADMAP", "OUT"]


# ================================================================ files

def path(rel):
    return ROOT / rel


def read(rel):
    return path(rel).read_text(encoding="utf-8")


def write(rel, text):
    p = path(rel)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text, encoding="utf-8")


def load_json(rel):
    return json.loads(read(rel))


def dumps(obj):
    return json.dumps(obj, indent=2, ensure_ascii=False) + "\n"


def sha256(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


DATE_LINE = re.compile(r"(?:last_reviewed|last_updated)\s*:\s*(\d{4}-\d{2}-\d{2})")


def file_date(rel):
    m = DATE_LINE.search(read(rel))
    return m.group(1) if m else None


def frontmatter(text):
    out = {}
    if text.startswith("---"):
        end = text.find("\n---", 3)
        for line in text[3:end].splitlines():
            if ":" in line:
                k, v = line.split(":", 1)
                out[k.strip()] = v.strip()
    return out


def plain(s):
    s = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r"\1", s)
    return s.replace("**", "").replace("`", "").strip()


def md_tables(text):
    """Yield (heading, header, rows) for every pipe table, with the nearest ## or ### heading above it."""
    lines = text.splitlines()
    heading, i = "", 0
    while i < len(lines):
        ln = lines[i].strip()
        if ln.startswith("#"):
            heading = ln.lstrip("#").strip()
        if ln.startswith("|") and i + 1 < len(lines) and re.match(r"^\|[\s:|-]+\|$", lines[i + 1].strip()):
            header = [c.strip() for c in ln.strip("|").split("|")]
            rows, i = [], i + 2
            while i < len(lines) and lines[i].strip().startswith("|"):
                rows.append([c.strip() for c in lines[i].strip().strip("|").split("|")])
                i += 1
            yield heading, header, rows
            continue
        i += 1


def sections(text, level=2):
    """Split Markdown into (heading, body) pairs at the given heading level."""
    marker = "#" * level + " "
    out, head, buf = [], None, []
    for ln in text.splitlines():
        if ln.startswith(marker):
            if head is not None:
                out.append((head, "\n".join(buf).strip()))
            head, buf = ln[len(marker):].strip(), []
        elif head is not None:
            buf.append(ln)
    if head is not None:
        out.append((head, "\n".join(buf).strip()))
    return out


# ================================================================ JSON Schema, the subset these schemas use

def _is(v, t):
    return {"object": isinstance(v, dict), "array": isinstance(v, list), "string": isinstance(v, str),
            "integer": isinstance(v, int) and not isinstance(v, bool),
            "number": isinstance(v, (int, float)) and not isinstance(v, bool),
            "boolean": isinstance(v, bool), "null": v is None}[t]


def validate(inst, schema, where="$"):
    errs = []
    t = schema.get("type")
    if t:
        types = t if isinstance(t, list) else [t]
        if not any(_is(inst, x) for x in types):
            return [f"{where}: expected {'/'.join(types)}, got {type(inst).__name__}"]
    if "enum" in schema and inst not in schema["enum"]:
        errs.append(f"{where}: {inst!r} not one of {schema['enum']}")
    if isinstance(inst, str):
        if "pattern" in schema and not re.search(schema["pattern"], inst):
            errs.append(f"{where}: {inst!r} does not match {schema['pattern']}")
        if len(inst) < schema.get("minLength", 0):
            errs.append(f"{where}: shorter than {schema['minLength']}")
    if _is(inst, "number"):
        if "minimum" in schema and inst < schema["minimum"]:
            errs.append(f"{where}: below minimum {schema['minimum']}")
        if "maximum" in schema and inst > schema["maximum"]:
            errs.append(f"{where}: above maximum {schema['maximum']}")
    if isinstance(inst, dict):
        for k in schema.get("required", []):
            if k not in inst:
                errs.append(f"{where}: missing required {k!r}")
        props = schema.get("properties", {})
        for k, v in inst.items():
            if k in props:
                errs += validate(v, props[k], f"{where}.{k}")
            elif schema.get("additionalProperties") is False:
                errs.append(f"{where}: unexpected property {k!r}")
    if isinstance(inst, list) and "items" in schema:
        for n, item in enumerate(inst):
            errs += validate(item, schema["items"], f"{where}[{n}]")
    return errs


def schema(name):
    return load_json(f"schemas/{name}.schema.json")


# ================================================================ exports: Markdown ledgers to data/*.json

def export_features():
    text = read("rules/feature-status.md")
    items, area = [], ""
    flag_re = re.compile(r"(?:^|(?<=\.)\s+)([^.:]+?):\s*(SHIPPED|PARTIAL|IN BUILD|ROADMAP|OUT)\b([^.]*)")
    for ln in text.splitlines():
        if ln.startswith("## "):
            area = ln[3:].strip()
        elif ln.startswith("- ") and area not in ("Demo rule",):
            body = plain(ln[2:])
            for m in flag_re.finditer(body):
                note = m.group(3).strip(" ,.")
                items.append({"area": area, "capability": m.group(1).strip(), "status": m.group(2),
                              "note": note.lstrip("(").rstrip(")") if note else ""})
    return envelope("features", ["rules/feature-status.md"], file_date("rules/feature-status.md"), items)


def export_claims():
    text = read("rules/do-not-say.md")
    items = []
    for heading, header, rows in md_tables(text):
        if header[:1] == ["Do not say"]:
            for r in rows:
                items.append({"scope": heading, "do_not_say": plain(r[0]), "say_instead": plain(r[1]),
                              "phrases": [p.strip().rstrip(".") for p in re.findall(r'"([^"]{3,})"', r[0])]})
    for m in re.finditer(r"^- \*\*(.+?)\*\*\s*(.*)$", text, re.M):
        body = m.group(2)
        ce = re.search(r"Counter-example:\s*(.+?)(?=Safe form:|$)", body)
        sf = re.search(r"Safe form:\s*(.+)$", body)
        items.append({"scope": "Claims that need scoping", "do_not_say": plain(m.group(1)),
                      "counter_example": plain(ce.group(1)) if ce else "",
                      "say_instead": plain(sf.group(1)) if sf else plain(body),
                      "phrases": [p.strip().rstrip(".") for p in re.findall(r'"([^"]{3,})"', m.group(1))]})
    return envelope("claims", ["rules/do-not-say.md"], file_date("rules/do-not-say.md"), items)


def export_glossary():
    items = []
    for heading, header, rows in md_tables(read("rules/glossary.md")):
        for r in rows:
            items.append({"section": heading, "term": plain(r[0]), "rule": plain(r[1]) if len(r) > 1 else ""})
    return envelope("glossary", ["rules/glossary.md"], file_date("rules/glossary.md"), items)


def decision_ids(line):
    """Every ID on an IDs line, with ranges such as "D47 to D52" expanded."""
    spans = re.sub(r"\b([DB])(\d{1,3}) to \1(\d{1,3})\b",
                   lambda m: ", ".join(f"{m.group(1)}{n}" for n in range(int(m.group(2)), int(m.group(3)) + 1)), line)
    return re.findall(r"\b[DB]\d{1,3}\b", spans)


def export_decisions():
    text = read("ops/decisions.md")
    items = []
    for head, body in sections(text, 2):
        m = re.match(r"(\d{4}-\d{2})\s+(.+?)\s+\((DECIDED|OPEN)\)$", head)
        if not m:
            continue

        def field(name):
            fm = re.search(r"\*\*" + re.escape(name) + r":\*\*\s*(.+)", body)
            return plain(fm.group(1)) if fm else ""
        ids_line = field("IDs")
        decided = re.search(r"Decided (\d{4}-\d{2}-\d{2})", ids_line)
        verdict = [plain(ln) for ln in body.splitlines() if ln.strip() and not ln.startswith("**")]
        items.append({"month": m.group(1), "title": m.group(2), "status": m.group(3),
                      "ids": decision_ids(ids_line),
                      "decided": decided.group(1) if decided else None,
                      "verdict": verdict[0] if verdict else "", "rationale": " ".join(verdict[1:]),
                      "does_not_change": field("What this does not change"), "downstream": field("Downstream"),
                      "reopen_when": field("Reopen when")})
    opened = [plain(ln[2:]) for ln in dict(sections(text, 2)).get("Open, owned elsewhere", "").splitlines()
              if ln.startswith("- ")]
    for o in opened:
        items.append({"month": None, "title": o.split(".")[0], "status": "OPEN", "ids": [], "decided": None,
                      "verdict": o, "rationale": "", "does_not_change": "", "downstream": "", "reopen_when": ""})
    dates = [i["decided"] for i in items if i["decided"]]
    return envelope("decisions", ["ops/decisions.md"], max(dates) if dates else None, items)


SIGNAL_HEAD = re.compile(r"^### (\d{4}-\d{2}-\d{2}) \| ([A-Z]+) \| (.+)$")


def parse_signals():
    text = read("ops/signal-log.md")
    out, cur = [], None
    for ln in text.splitlines():
        m = SIGNAL_HEAD.match(ln)
        if m:
            cur = {"date": m.group(1), "type": m.group(2), "source": m.group(3).strip(), "verbatim": "",
                   "context": "", "disposition": "", "routed_to": "", "tags": []}
            out.append(cur)
            continue
        if cur is None:
            continue
        for key, name in (("verbatim", "Verbatim"), ("context", "Context"), ("disposition", "Disposition"),
                          ("routed_to", "Routed to"), ("tags", "Tags")):
            fm = re.match(r"^\*\*" + name + r":\*\*\s*(.*)$", ln)
            if fm:
                val = fm.group(1).strip()
                if key == "tags":
                    cur[key] = [t.strip() for t in val.split(",") if t.strip()]
                else:
                    cur[key] = plain(val).strip('"') if key == "verbatim" else plain(val)
    return out


def export_signals():
    sigs = parse_signals()
    return envelope("signals", ["ops/signal-log.md"], max((s["date"] for s in sigs), default=None), sigs)


def export_copy_bank():
    items = []
    for head, body in sections(read("ops/copy-bank.md"), 2):
        for ln in body.splitlines():
            if not ln.startswith("- "):
                continue
            raw = ln[2:]
            status = "IN BUILD" if "[IN BUILD" in raw else "APPROVED"
            quotes = re.findall(r'"([^"]+)"', raw)
            items.append({"section": head, "status": status, "line": quotes[0] if quotes else plain(raw),
                          "note": plain(re.sub(r'"[^"]+"', "", raw)).strip(" :.") if quotes else ""})
    return envelope("copy-bank", ["ops/copy-bank.md"], frontmatter(read(MASTER)).get("last_updated"), items)


LAYERS = [("router", ["CLAUDE.md", "AGENTS.md", "GEMINI.md", "llms.txt"]), ("source-of-truth", ["context/"]),
          ("control", ["rules/", "ops/QA-checklist.md"]), ("reference", ["reference/"]),
          ("execution", ["templates/", "examples/", "prompts/", "pages/"]),
          ("state", ["ops/", "snapshots/"]), ("innovation", ["innovation/"]), ("machine", ["data/", "schemas/", "tools/"]),
          ("machine", ["Dockerfile", ".dockerignore", ".gitattributes", "Makefile"]),
          ("adapter", ["adapters/", ".cursor/", ".windsurf/", ".github/", ".vscode/", ".gemini/", ".mcp.json",
                       ".claude/commands/", ".claude/settings.json", ".clinerules/", ".roo/", ".continue/", ".kiro/",
                       ".amazonq/", ".junie/", ".aiassistant/", ".trae/", ".openhands/", ".opencode/", ".goosehints",
                       ".aider.conf.yml", "llms-full.txt"])]


def layer_of(rel):
    for name, prefixes in LAYERS:
        if any(rel == p or rel.startswith(p) for p in prefixes):
            return name
    return "other"


def brain_files():
    skip = {".git", "node_modules", "__pycache__", ".venv"}
    for p in sorted(ROOT.rglob("*")):
        r = p.relative_to(ROOT)
        if p.is_file() and not (set(r.parts) & skip) and not str(r).startswith(".claude/skills/"):
            yield str(r)


GENERATED = ("llms-full.txt", "adapters/portable-control-layer.md", "innovation/LEDGER.md")


def generated_paths():
    return set(GENERATED) | set(door_outputs())


def export_manifest():
    fm = frontmatter(read(MASTER))
    files = []
    gen = generated_paths()
    for rel in sorted(set(brain_files()) | gen):  # generated paths count before their first build writes them
        if rel.startswith(("sources/", "data/", "innovation/events/")) or rel.endswith((".pyc",)):
            continue
        if rel in gen:
            files.append({"path": rel, "layer": layer_of(rel), "generated": True})
            continue
        text = path(rel).read_text(encoding="utf-8", errors="replace")
        files.append({"path": rel, "layer": layer_of(rel), "bytes": len(text.encode("utf-8")), "sha256": sha256(text)})
    items = [{"version": fm.get("version"), "last_updated": fm.get("last_updated"), "status_notes": fm.get("status_notes"),
              "load_policy": {k: v["desc"] for k, v in TASKS.items()}, "files": files}]
    return envelope("manifest", [MASTER, "llms.txt"], fm.get("last_updated"), items)


def envelope(kind, sources, as_of, items):
    return {"$schema": "../schemas/export.schema.json", "kind": kind, "generated_from": sources,
            "as_of": as_of or "1970-01-01", "items": items}


EXPORTS = {"features": export_features, "claims": export_claims, "glossary": export_glossary,
           "decisions": export_decisions, "signals": export_signals, "copy-bank": export_copy_bank}


def data(kind):
    """Read a data export, regenerating it in memory if the file is missing."""
    p = path(f"data/{kind}.json")
    return json.loads(p.read_text(encoding="utf-8")) if p.exists() else EXPORTS[kind]()


# ================================================================ the context layer: load policy as code

CONTROL = ["CLAUDE.md"] + RULES
COPY = CONTROL + ["ops/copy-bank.md", "ops/QA-checklist.md"]
AUD = {
    "merchants": ["reference/value-proposition-merchants.md", "reference/icp-personas-merchants.md",
                  "reference/customer-journey-merchants.md", "reference/app-store-engine.md"],
    "implementers": ["reference/value-proposition-implementers.md", "reference/icp-personas-implementers.md",
                     "reference/customer-journey-implementers.md", "reference/outreach-engine.md"],
}
TASKS = {
    "session": {"desc": "Any session: the router only", "files": ["CLAUDE.md"]},
    "copy": {"desc": "Any customer-facing writing for one audience", "files": COPY, "per_audience": True},
    "app-store-listing": {"desc": "Shopify App Store listing", "audience": "merchants", "files": COPY + [
        "reference/app-store-engine.md", "reference/value-proposition-merchants.md", "templates/app-store-listing.md",
        "examples/app-store-listing.md"]},
    "landing-page": {"desc": "A landing page for one audience", "files": COPY + ["templates/landing-page.md",
                     "reference/objection-handling.md"], "per_audience": True},
    "seo-article": {"desc": "Catalog guide or comparison page", "audience": "merchants", "files": COPY + [
        "reference/app-store-engine.md", "reference/competitive-analysis-merchants.md", "templates/seo-article.md"]},
    "lifecycle-email": {"desc": "Merchant lifecycle email", "audience": "merchants", "files": COPY + [
        "reference/customer-journey-merchants.md", "templates/lifecycle-email.md", "examples/first-insight-email.md",
        "examples/sync-failure-email.md"]},
    "review-reply": {"desc": "App Store review reply", "audience": "merchants", "files": COPY + [
        "templates/review-reply.md", "reference/objection-handling.md"]},
    "cold-email": {"desc": "Cold email to US implementers", "audience": "implementers", "files": COPY + [
        "reference/outreach-engine.md", "reference/value-proposition-implementers.md", "templates/cold-email.md",
        "examples/cold-email-paid-session.md"]},
    "linkedin": {"desc": "LinkedIn note, message, or founder post", "audience": "implementers", "files": COPY + [
        "reference/outreach-engine.md", "templates/linkedin-message.md", "examples/linkedin-founder-post.md"]},
    "job-post": {"desc": "Upwork job post or Fiverr brief", "audience": "implementers", "files": COPY + [
        "reference/outreach-engine.md", "templates/marketplace-job-post.md", "examples/upwork-job-post.md"]},
    "partner-page": {"desc": "Partner page or invitation (from week 6)", "audience": "implementers", "files": COPY + [
        "reference/partner-program.md", "templates/landing-page.md"]},
    "case-study": {"desc": "Case study, gated by the proof log", "files": COPY + ["templates/case-study.md"],
                   "per_audience": True},
    "one-pager": {"desc": "Technical one-pager or decision summary", "files": COPY + ["templates/one-pager.md"],
                  "per_audience": True},
    "sales-call": {"desc": "Call prep for a prospect or partner", "files": CONTROL + [
        "reference/objection-handling.md", "reference/competitor-battlecards.md"], "per_audience": True},
    "strategy": {"desc": "A strategy question", "files": ["CLAUDE.md", MASTER, "ops/decisions.md",
                 "reference/positioning-verdict.md"]},
    "pricing": {"desc": "Plans, quota, partner economics", "files": CONTROL + ["reference/pricing-and-packaging.md",
                "reference/partner-program.md", "ops/decisions.md"]},
    "signal": {"desc": "Ingest a signal from the market", "files": ["CLAUDE.md", "ops/signal-log.md",
               "ops/decisions.md", "rules/glossary.md", "reference/innovation-accounting.md"]},
    "experiment": {"desc": "Plan, run, or close an experiment", "files": ["CLAUDE.md",
                   "reference/innovation-accounting.md", "innovation/metrics.json", "innovation/hypotheses.json",
                   "innovation/experiments.json", "innovation/LEDGER.md"]},
    "snapshot": {"desc": "Take a periodic snapshot", "files": ["CLAUDE.md", "innovation/LEDGER.md",
                 "rules/feature-status.md", "ops/signal-log.md"]},
    "investor-update": {"desc": "Investor or advisor update", "files": ["CLAUDE.md", MASTER,
                        "reference/market-sizing.md", "reference/launch-plan.md", "innovation/LEDGER.md"]},
    "amend": {"desc": "Change a ledger, a position, or a rule", "files": [MASTER] + RULES + [
              "ops/decisions.md", "ops/copy-bank.md", "ops/review-cadence.md"]},
}


def load_set(task, audience=None):
    if task not in TASKS:
        raise SystemExit(f"unknown task {task!r}. Tasks: {', '.join(TASKS)}")
    spec = TASKS[task]
    fixed = spec.get("audience")
    if fixed and audience and audience != fixed:
        raise SystemExit(f"{task} is for {fixed} only. Audiences are never blended.")
    aud = fixed or audience
    files = list(spec["files"])
    if spec.get("per_audience"):
        if not aud:
            raise SystemExit(f"{task} needs --audience merchants or --audience implementers")
        files += AUD[aud]
    if task == "snapshot":
        snaps = sorted(path("snapshots").glob("*.md"))
        if snaps:
            files.append(str(snaps[-1].relative_to(ROOT)))
    seen, out = set(), []
    for f in files:
        if f not in seen and path(f).exists():
            seen.add(f)
            out.append(f)
    return aud, out


def context_bundle(task, audience=None, fmt="list"):
    aud, files = load_set(task, audience)
    if fmt == "list":
        return "\n".join(files) + "\n"
    if fmt == "json":
        recs = [{"path": f, "bytes": path(f).stat().st_size, "sha256": sha256(read(f))} for f in files]
        total = sum(r["bytes"] for r in recs)
        return dumps({"task": task, "audience": aud, "description": TASKS[task]["desc"], "files": recs,
                      "bytes": total, "tokens_estimate": total // 4})
    parts = [f"<!-- Pico GTM Brain context: task={task} audience={aud or 'n/a'} files={len(files)} -->"]
    for f in files:
        parts.append(f"\n\n===== {f} =====\n\n{read(f).strip()}")
    return "\n".join(parts) + "\n"


# ================================================================ lint: the control layer as checks

NEGATION = re.compile(r"\b(no|not|never|without|isn't|doesn't|does not|don't|cannot|can't|coming soon|roadmap|out of scope)\b", re.I)
STATUS_PHRASES = [
    (r"semantic search|vector search|understands what shoppers mean", "OUT/ROADMAP: there is no semantic or vector search", "error"),
    (r"checkout (?:in|inside) (?:the )?chat|buy right in the chat", "OUT: Pico adds to the store's own cart, checkout stays in the store", "error"),
    (r"live stock|real[- ]time (?:inventory|stock)|checks live stock", "Stock is as of the last catalog sync", "error"),
    (r"revenue attribution|attributed revenue|orders influenced", "ROADMAP: revenue attribution is not measured", "warn"),
    (r"human handoff|hand(?:s)? off to (?:your|a) (?:team|agent|human)|live chat", "OUT: no human handoff or live chat", "error"),
    (r"order status|returns? questions|policy answers", "OUT by design: Pico is a pre-purchase assistant", "warn"),
    (r"whatsapp|instagram dm", "OUT until the GCC opens", "warn"),
    (r"white[- ]label", "OUT: no white label or resale", "error"),
    (r"multi-store|agency workspace|one login for (?:all|every)", "ROADMAP: the workspace is built when 10 partners each have 3 active stores", "warn"),
    (r"partner portal|tier badge|certif(?:ied|ication)", "ROADMAP or OUT: check rules/feature-status.md", "warn"),
    (r"pauses before it bills|no overage|never charges? overage|80% and 100%", "IN BUILD: quota alerts and pause ship before this line can", "warn"),
    (r"\$490|\$990|\$2,990|yearly plan|annual plan", "IN BUILD: yearly prices", "warn"),
    (r"\bscale plan\b|\$299", "IN BUILD: the Scale tier", "warn"),
    (r"25% of each referred|partner program|picofinds\.com/partners", "IN BUILD until week 6: the partner page", "warn"),
    (r"ga4|klaviyo integration", "ROADMAP: marketing integrations", "warn"),
    (r"no impact on (?:speed|performance)|zero impact|won't slow", "OUT: speed is measured and published, never claimed as none", "error"),
    (r"headless|hydrogen", "OUT: headless is not claimed", "warn"),
    (r"translat(?:es|ed|ion of) (?:your )?catalog", "OUT: catalog text is shown as synced", "error"),
]
OUTCOME = [
    (r"\b(?:increase[sd]?|boost(?:s|ed)?|grow(?:s|th)?|lift(?:s|ed)?|double[sd]?|drive[sn]?)\b[^.\n]{0,40}\b(?:sales|revenue|conversions?|aov|order value)\b", "Outcome claim: Pico does not measure revenue or conversion"),
    (r"\bpays? for itself\b|\broi\b", "Outcome claim: no ROI is stated for Pico. Leave the merchant's inputs blank"),
    (r"\d+(?:\.\d+)?\s?%\s+(?:more|higher|increase|lift|boost|uplift)", "Invented lift figure"),
    (r"\btrusted by\b|\bloved by\b|\bjoin \d", "Social proof claim: the proof log is empty"),
    (r"\b\d(?:\.\d)?\s?(?:stars?|★)", "Rating claim: there are no reviews yet"),
]
DISPARAGE = [
    (r"(?:smarter|better|faster|cheaper)\s+than\s+(?:shopify|the inbox|search & discovery|chatty|tidio|gorgias|klaviyo|rebuy|rep ai|zipchat)", "Named comparison: not without a sourced, dated finding"),
    (r"shopify(?:'s)?\s+(?:search|inbox|tools?|agent)\s+(?:is|are)\s+(?:broken|bad|weak|limited|useless)", "Disparages Shopify: describe what Pico does instead"),
    (r"(?:your|the) store is losing sales", "Insults the merchant's setup"),
]
SUPERLATIVE = (r"\bthe only\b|\bonly (?:assistant|app|tool|platform|one|vendor)\b|\bthe first (?:ai|assistant|app|tool|platform)\b|"
               r"\bbest\b|\bno other\b|\bguarantee[ds]?\b|\bunlimited\b|\bfree forever\b|\b100%")
MENTION = re.compile(r"\b(?:never|not|no|don't|do not|instead of|avoid|banned|forbidden)\b", re.I)


def lint_text(text, audience=None):
    findings = []
    claims = data("claims")["items"]
    phrases = []
    for c in claims:
        for p in c.get("phrases", []):
            if len(p) >= 8:
                phrases.append((p, c.get("say_instead", "")))
    lower_all = text.lower()
    for n, line in enumerate(text.splitlines(), 1):
        low = line.lower()

        def add(sev, rule, msg, col=0, fix=""):
            findings.append({"line": n, "col": col + 1, "severity": sev, "rule": rule, "message": msg, "fix": fix})
        if EM_DASH in line:
            add("error", "mechanics.em-dash", "Em dash. Use a comma or restructure", line.index(EM_DASH))
        if EN_DASH in line and not re.search(r"\d\s?" + EN_DASH + r"\s?\d", line):
            add("warn", "mechanics.en-dash", "En dash used as punctuation", line.index(EN_DASH))
        for w in BANNED:
            m = re.search(r"\b" + re.escape(w) + r"\w*", line, re.I)
            if m:
                add("error", "mechanics.banned-word", f"Banned word: {m.group(0)}", m.start())
        for w in SLOP:
            m = re.search(r"\b" + re.escape(w) + r"\w*", line, re.I)
            if m:
                add("warn", "mechanics.slop-word", f"Slop word: {m.group(0)}", m.start())
        for p, fix in phrases:
            i = low.find(p.lower())
            if i >= 0:
                quoted = line[max(0, i - 1):i] in ('"', "'") or MENTION.search(line[:i])
                add("warn" if quoted else "error", "claims.do-not-say",
                    f'{"Mentions" if quoted else "Forbidden claim:"} "{p}"', i, fix)
        for rx, msg in OUTCOME:
            m = re.search(rx, line, re.I)
            if m and not NEGATION.search(line):
                add("error", "claims.outcome", msg, m.start())
        for rx, msg in DISPARAGE:
            m = re.search(rx, line, re.I)
            if m:
                add("error", "claims.comparison", msg, m.start())
        for rx, msg, sev in STATUS_PHRASES:
            m = re.search(rx, line, re.I)
            if m and not NEGATION.search(line):
                add(sev, "status.unshipped", f"{m.group(0)}: {msg}", m.start(), "See rules/feature-status.md")
        m = re.search(SUPERLATIVE, line, re.I)
        if m:
            add("warn", "claims.superlative", f"Superlative {m.group(0)!r}: check rules/do-not-say.md scoping", m.start())
        m = re.search(r"\b(\d[\d,]*\+?)\s+(?:merchants|stores|customers|brands|installs|reviews|users)\b", line, re.I)
        if m and not re.search(r"cohort|founding|sample|example|planning|frame|tracker|storeleads|\bof\b \d", low):
            add("warn", "claims.count", f"Count claim {m.group(0)!r}: Pico has no installs or customers to cite", m.start())
    if ("upwork" in lower_all or "fiverr" in lower_all) and re.search(
            r"partner program|picofinds\.com/partners|your email|e-?mail me|whatsapp me|off (?:the )?platform", lower_all):
        findings.append({"line": 0, "col": 0, "severity": "error", "rule": "channel.platform",
                         "message": "Upwork or Fiverr copy mentions the partner program, an outside contact, or moving off the platform",
                         "fix": "Keep marketplace copy to the paid session. Implementers find the partner page on their own"})
    if re.search(r"\b(?:arabic|gcc|saudi|uae|dubai|middle east)\b", lower_all) and not re.search(r"right to left", lower_all):
        findings.append({"line": 0, "col": 0, "severity": "warn", "rule": "channel.gcc",
                         "message": "GCC or Arabic-market copy: out of scope until the GCC trigger fires", "fix": "reference/gcc-later.md"})
    if audience is None and re.search(r"\byour (?:shoppers|catalog|store's)\b", lower_all) and re.search(
            r"\b(?:store you work on|your client|your clients)\b", lower_all):
        findings.append({"line": 0, "col": 0, "severity": "warn", "rule": "audience.blend",
                         "message": "Mentions merchants and implementers: pick one audience per asset", "fix": ""})
    return findings


def format_findings(findings, name):
    out = []
    for f in findings:
        loc = f"{name}:{f['line']}:{f['col']}" if f["line"] else name
        fix = f"  ->  {f['fix']}" if f.get("fix") else ""
        out.append(f"{loc}: {f['severity']}: [{f['rule']}] {f['message']}{fix}")
    return "\n".join(out)


# ================================================================ events: the append-only activity log

def now_ts():
    return dt.datetime.now(dt.timezone.utc).replace(microsecond=0).strftime("%Y-%m-%dT%H:%M:%SZ")


def event_id(ts, etype, data_):
    return "evt_" + hashlib.sha1(f"{ts}|{etype}|{json.dumps(data_, sort_keys=True)}".encode()).hexdigest()[:12]


def load_events(strict=False):
    events = []
    sch = schema("event")
    for f in sorted(path("innovation/events").glob("*.jsonl")):
        for n, line in enumerate(f.read_text(encoding="utf-8").splitlines(), 1):
            if not line.strip():
                continue
            ev = json.loads(line)
            errs = validate(ev, sch)
            if errs and strict:
                raise SystemExit(f"{f.name}:{n}: " + "; ".join(errs))
            events.append(ev)
    events.sort(key=lambda e: e["ts"])
    return events


def append_event(etype, audience="both", data_=None, source="brain.py", refs=None, tags=None, ts=None, actor=None):
    data_ = data_ or {}
    ts = ts or now_ts()
    ev = {"id": event_id(ts, etype, data_), "ts": ts, "type": etype, "audience": audience, "source": source, "data": data_}
    if actor:
        ev["actor"] = actor
    if refs:
        ev["refs"] = refs
    if tags:
        ev["tags"] = tags
    errs = validate(ev, schema("event"))
    if errs:
        raise SystemExit("event rejected: " + "; ".join(errs))
    target = path(f"innovation/events/{ts[:7]}.jsonl")
    target.parent.mkdir(parents=True, exist_ok=True)
    existing = target.read_text(encoding="utf-8") if target.exists() else ""
    if f'"id": "{ev["id"]}"' in existing:
        return ev, False
    with target.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(ev, ensure_ascii=False) + "\n")
    return ev, True


def add_signal(stype, source, verbatim, context="", disposition="NOISE", routed="none", tags=None, date=None):
    stype = stype.upper()
    if stype not in SIGNAL_TYPES:
        raise SystemExit(f"type must be one of {', '.join(SIGNAL_TYPES)}")
    date = date or dt.date.today().isoformat()
    tags = tags or []
    rec = {"date": date, "type": stype, "source": source, "verbatim": verbatim, "context": context,
           "disposition": disposition, "routed_to": routed, "tags": tags}
    errs = validate(rec, schema("signal"))
    if errs:
        raise SystemExit("signal rejected: " + "; ".join(errs))
    entry = [f"### {date} | {stype} | {source}", f'**Verbatim:** "{verbatim}"', f"**Context:** {context or 'none recorded'}",
             f"**Disposition:** {disposition}", f"**Routed to:** {routed}"]
    if tags:
        entry.append(f"**Tags:** {', '.join(tags)}")
    text = read("ops/signal-log.md")
    marker = "## Entries"
    head, _, tail = text.partition(marker)
    first = re.search(r"^### \d{4}-\d{2}-\d{2}", tail, re.M)
    block = "\n".join(entry) + "\n\n"
    tail = tail[:first.start()] + block + tail[first.start():] if first else tail.rstrip() + "\n\n" + block
    write("ops/signal-log.md", head + marker + tail)
    ev, _ = append_event("signal.logged", "both", {"type": stype, "source": source, "verbatim": verbatim,
                         "disposition": disposition, "routed_to": routed}, source="ops/signal-log.md", tags=tags,
                         ts=f"{date}T12:00:00Z" if date != dt.date.today().isoformat() else None)
    return rec, ev


# ================================================================ metrics, hypotheses, tripwires

def _match(ev, etype, where=None):
    if ev["type"] != etype:
        return False
    return all(ev.get("data", {}).get(k) == v for k, v in (where or {}).items())


def compute(metric, events):
    c = metric["compute"]
    kind = c["type"]
    if kind == "observed":
        obs = [e for e in events if e["type"] == "metric.observed" and e["data"].get("metric") == metric["id"]]
        if not obs:
            return None, 0, None
        last = obs[-1]
        return last["data"].get("value"), len(obs), last["ts"]
    if kind == "count":
        hits = [e for e in events if _match(e, c["event"], c.get("where"))]
        return len(hits), len(hits), hits[-1]["ts"] if hits else None
    if kind == "ratio":
        num = [e for e in events if _match(e, c["numerator"]["event"], c["numerator"].get("where"))]
        den = [e for e in events if _match(e, c["denominator"]["event"], c["denominator"].get("where"))]
        if not den:
            return None, 0, None
        return round(len(num) / len(den), 4), len(den), den[-1]["ts"]
    if kind == "median":
        vals = [e["data"][c["field"]] for e in events if _match(e, c["event"], c.get("where")) and c["field"] in e["data"]]
        if not vals:
            return None, 0, None
        return statistics.median(vals), len(vals), None
    raise ValueError(kind)


OPS = {">=": lambda a, b: a >= b, ">": lambda a, b: a > b, "<=": lambda a, b: a <= b, "<": lambda a, b: a < b,
       "==": lambda a, b: a == b}


def review_date(review, anchors):
    if not review:
        return None
    if "anchor" in review:
        base = anchors.get(review["anchor"])
        if not base:
            return f"{review['anchor']} + {review.get('days', 0)} days (anchor not set)"
        return (dt.date.fromisoformat(base) + dt.timedelta(days=review.get("days", 0))).isoformat()
    if "every_days" in review:
        return f"every {review['every_days']} days"
    if "after_events" in review:
        return f"after {review['after_events']} {review['event']} events"
    if "per" in review:
        return f"per {review['per']}"
    return None


def metric_rows(events=None, today=None):
    events = load_events() if events is None else events
    reg = load_json("innovation/metrics.json")
    today = today or dt.date.today()
    rows = []
    for m in reg["north_stars"] + reg["metrics"]:
        value, n, last = compute(m, events)
        rd = review_date(m.get("review"), reg["anchors"])
        if value is None or (n == 0 and m["compute"]["type"] in ("count", "ratio", "median")):
            status = "no data"
        elif "target" in m:
            met = OPS[m["comparator"]](value, m["target"])
            status = "met" if met else "below target"
            if not met and rd and re.match(r"\d{4}-\d{2}-\d{2}$", rd) and dt.date.fromisoformat(rd) <= today:
                status = "missed at review"
        else:
            status = "tracking"
        rows.append({"id": m["id"], "audience": m["audience"], "stage": m.get("stage"), "name": m["name"],
                     "target": m.get("target"), "comparator": m.get("comparator"), "unit": m.get("unit"),
                     "value": value, "evidence": n, "last": last, "review": rd, "status": status,
                     "decision": m.get("decision")})
    return rows


def eval_condition(cond, events, metrics, today):
    if "all" in cond:
        vals = [eval_condition(c, events, metrics, today) for c in cond["all"]]
        return False if False in vals else (None if None in vals else True)
    if "any" in cond:
        vals = [eval_condition(c, events, metrics, today) for c in cond["any"]]
        return True if True in vals else (None if None in vals else False)
    op, value = OPS[cond["op"]], cond["value"]
    if "metric" in cond:
        v = metrics.get(cond["metric"])
        return None if v is None else op(v, value)
    window = cond.get("signals") or cond.get("events")
    since = today - dt.timedelta(days=window.get("window_days", 36500))
    if "signals" in cond:
        hits = [e for e in events if e["type"] == "signal.logged" and window["tag"] in e.get("tags", [])
                and dt.date.fromisoformat(e["ts"][:10]) >= since]
    else:
        hits = [e for e in events if _match(e, window["type"], window.get("where"))
                and dt.date.fromisoformat(e["ts"][:10]) >= since]
    return op(len(hits), value)


def tripwire_rows(events=None, today=None):
    events = load_events() if events is None else events
    today = today or dt.date.today()
    metrics = {r["id"]: r["value"] for r in metric_rows(events, today)}
    out = []
    for t in load_json("innovation/tripwires.json")["tripwires"]:
        res = eval_condition(t["when"], events, metrics, today)
        out.append({**t, "status": {True: "FIRED", False: "armed", None: "no data"}[res]})
    return out


def hypothesis_rows(rows):
    by_id = {r["id"]: r for r in rows}
    out = []
    for h in load_json("innovation/hypotheses.json")["hypotheses"]:
        r = by_id.get(h["metric"], {})
        status = h["status"]
        if status == "untested" and r.get("value") is not None:
            status = "testing"
        out.append({**h, "derived_status": status, "metric_value": r.get("value"), "metric_status": r.get("status")})
    return out


# ================================================================ generated documents

def fmt_value(v, unit):
    if v is None:
        return "no data"
    if unit == "ratio":
        return f"{v * 100:.1f}%"
    if unit == "usd":
        return f"${v:.3f}"
    return f"{v:g}"


def fmt_target(r):
    if r["target"] is None:
        return ""
    return f"{r['comparator']} {fmt_value(r['target'], r['unit'])}"


def render_ledger(events=None):
    events = load_events() if events is None else events
    reg = load_json("innovation/metrics.json")
    as_of = max([reg["last_reviewed"]] + [e["ts"][:10] for e in events])
    today = dt.date.fromisoformat(as_of)
    rows = metric_rows(events, today)
    sig = parse_signals()
    disp = {}
    for s in sig:
        key = s["disposition"].split(" ")[0] or "UNSET"
        disp[key] = disp.get(key, 0) + 1
    exps = load_json("innovation/experiments.json")["experiments"]
    hyps = hypothesis_rows(rows)
    tws = tripwire_rows(events, today)
    L = ["# Innovation accounting ledger", "",
         "Generated by `python3 tools/brain.py ledger` from `innovation/*.json`, `ops/signal-log.md`, and the event log. Do not edit by hand: change the inputs and regenerate.", "",
         f"As of {as_of}. Events logged: {len(events)}. Signals: {len(sig)} ({', '.join(f'{k} {v}' for k, v in sorted(disp.items()))}).", ""]
    anchors = reg["anchors"]
    phase_m = "pre-launch" if not anchors.get("listing_live") else "baseline"
    sessions = next((r["value"] for r in rows if r["id"] == "i.sessions_completed"), 0) or 0
    phase_i = "pre-launch" if sessions == 0 else ("baseline" if sessions < 10 else "tune")
    L += ["## Learning milestones", "",
          "| Audience | Milestone | Why |", "|---|---|---|",
          f"| Merchants | {phase_m} | Listing live: {anchors.get('listing_live') or 'not yet'}. Founding cohort opens {anchors.get('cohort_open')} |",
          f"| Implementers | {phase_i} | Week 1 starts {anchors.get('week1')}. Sessions completed: {sessions} of 30 |", ""]
    for aud, title in (("merchants", "Merchants"), ("implementers", "Implementers")):
        L += [f"## {title}: funnel metrics", "", "| Stage | Metric | Target | Current | Evidence | Review | Status |",
              "|---|---|---|---|---|---|---|"]
        for r in rows:
            if r["audience"] == aud:
                L.append(f"| {r['stage'] or 'north star'} | {r['name']} (`{r['id']}`) | {fmt_target(r)} | "
                         f"{fmt_value(r['value'], r['unit'])} | {r['evidence']} | {r['review'] or ''} | {r['status']} |")
        L.append("")
    L += ["## Hypotheses", "", "| ID | Statement | Metric | Status |", "|---|---|---|---|"]
    for h in hyps:
        L.append(f"| {h['id']} | {h['statement']} | `{h['metric']}`: {h['metric_status']} | {h['derived_status']} |")
    L += ["", "## Experiments", "", "| ID | Experiment | Window | Budget | Status | Learning |", "|---|---|---|---|---|---|"]
    for x in exps:
        start = x.get("start") or review_date(x.get("start_anchor"), anchors) or "not scheduled"
        end = x.get("end") or review_date(x.get("end_anchor"), anchors) or "open"
        L.append(f"| {x['id']} | {x['name']} | {start} to {end} | ${x['budget_usd']:,.0f} | {x['status']} | {x['learning'] or 'pending'} |")
    L += ["", "## Tripwires: decision reopen conditions", "", "| ID | Decision | Trigger | Status | Action |", "|---|---|---|---|---|"]
    for t in tws:
        L.append(f"| {t['id']} | {t['decision']} | {t['name']} | {t['status']} | {t['action']} |")
    closed = [x for x in exps if x["status"] == "closed"]
    reopened = [e for e in events if e["type"] == "decision.reopened"]
    routed = sum(v for k, v in disp.items() if k in ("PATCH", "AMEND"))
    L += ["", "## Learning velocity", "",
          f"- Experiments closed: {len(closed)} of {len(exps)}.",
          f"- Hypotheses validated: {sum(1 for h in hyps if h['derived_status'] == 'validated')}, invalidated: {sum(1 for h in hyps if h['derived_status'] == 'invalidated')}, testing: {sum(1 for h in hyps if h['derived_status'] == 'testing')}, untested: {sum(1 for h in hyps if h['derived_status'] == 'untested')}.",
          f"- Decisions reopened by evidence: {len(reopened)}. Tripwires fired now: {sum(1 for t in tws if t['status'] == 'FIRED')}.",
          f"- Signals routed into the brain (PATCH or AMEND): {routed} of {len(sig)}.", "",
          "## Recent events", "", "| When | Type | Audience | Summary |", "|---|---|---|---|"]
    for e in events[-15:][::-1]:
        d = e.get("data", {})
        summ = d.get("name") or d.get("metric") or d.get("source") or d.get("note") or ", ".join(f"{k}={v}" for k, v in list(d.items())[:2])
        L.append(f"| {e['ts'][:10]} | {e['type']} | {e['audience']} | {str(summ)[:90]} |")
    return "\n".join(L) + "\n"


def render_llms_full():
    fm = frontmatter(read(MASTER))
    order = ["CLAUDE.md", MASTER] + RULES + ["ops/QA-checklist.md", "ops/copy-bank.md", "ops/decisions.md"]
    order += sorted(str(p.relative_to(ROOT)) for p in path("reference").glob("*.md"))
    order += ["prompts/common-tasks.md"]
    out = [f"# Pico GTM Brain, full text", "",
           f"Every governing and reference file of the brain in one document, for tools that ingest a single file: Claude Projects, custom GPT knowledge, Gemini Gems, NotebookLM, retrieval pipelines. Generated by `python3 tools/brain.py build` from master context version {fm.get('version')}, last updated {fm.get('last_updated')}. The repository is authoritative. Regenerate after any ledger change.", "",
           "## Files", ""] + [f"- {f}" for f in order]
    for f in order:
        out += ["", "", f"===== {f} =====", "", read(f).strip()]
    return "\n".join(out) + "\n"


def _status_list(features, flags):
    return [f"{i['capability']} ({i['area']})" for i in features if i["status"] in flags]


def render_portable():
    feats = export_features()["items"]
    claims = export_claims()["items"]
    dates = [file_date(r) for r in RULES] + [frontmatter(read(MASTER)).get("last_updated")]
    stamp = max(d for d in dates if d)
    hard = [c for c in claims if c["scope"] in ("Hard bans", "Implementer bans")]
    L = ["# Pico GTM, portable control layer", "",
         f"Generated {stamp} from the PicoGTMBrain ledgers by `python3 tools/brain.py build`. It carries content, so it decays: regenerate after any ledger change, and never use a copy older than the newest `last_reviewed` date in `rules/`.", "",
         "Paste everything below the line into any model with no access to the repository: ChatGPT or a custom GPT, Claude.ai Projects, Gemini or a Gem, Grok, Perplexity, or an API system prompt.", "", "---", "",
         "You write for Pico, an AI shopping assistant for Shopify stores. Shoppers describe what they want in plain language, and Pico replies with product cards drawn from the store's own synced catalog. The merchant sees what shoppers asked for, including the requests that found nothing. Pico is pre-launch: there are no installs, reviews, customers, or results yet.", "",
         "**Audiences. Pick one before writing. Never blend them.**",
         "- Merchants, US Shopify stores whose shoppers need help choosing. Promise: shoppers find products from your catalog by asking in their own words, and you see what they asked for. Pillars: shoppers ask in their own words, see what your shoppers asked for, a low-risk start.",
         "- Implementers, the agencies, developers, and freelancers who set up Shopify stores. Promise: we pay you to try Pico on a store you work on, and we credit your work when your client agrees. Pillars: set up without touching theme code, show your client what shoppers ask, get paid to shape it.", "",
         "**Positioning.** Merchants: Pico shows merchants what their shoppers ask for, and answers shoppers with products drawn from the store's own synced catalog. Implementers: Pico pays implementers for a first session on a store they work on, and, with the client's permission, credits their work in the case study that follows. Short form: \"Paid to test it. Credited when it works.\"", "",
         "**Words we use.** Pico (never Pico AI as a bare name). Pico AI Shopping Assistant (the App Store listing). Conversation (a thread with at least one AI reply, counted once per shopper and device per 24 hours). Synced catalog (stock is as of the last sync). Zero result phrases and weak click phrases (requests to the assistant, never search-bar terms). Implementer (agencies, developers, and freelancers). Never: chatbot, semantic search, live stock, checkout in chat, Pico Partner Program before week 6.", "",
         "**Status. Never write an unshipped capability in the present tense.**",
         "- Shipped: " + "; ".join(_status_list(feats, ["SHIPPED"])[:24]) + ".",
         "- In build, say \"coming soon\" or leave out: " + "; ".join(_status_list(feats, ["IN BUILD", "PARTIAL"])) + ".",
         "- Roadmap, never a launch claim: " + "; ".join(_status_list(feats, ["ROADMAP"])) + ".",
         "- Out of scope, never claimed: " + "; ".join(_status_list(feats, ["OUT"])) + ".", "",
         "**Proof points, the closed set.** None. There is no customer proof. Use open proof, an invitation to check something now: the sandbox store in picofinds.com's top menu, the View link on every card, the setup skill file, Shopify's own documentation on app embeds. Anything that reads as a customer result is fabrication.", "",
         "**Do not say.** Left is forbidden, right is what to write instead.", "", "| Do not say | Say instead |", "|---|---|"]
    for c in hard:
        L.append(f"| {c['do_not_say']} | {c['say_instead']} |")
    L += ["", "**Channels.** In: the Shopify App Store, content and search including AI answer engines, the product-led lifecycle, cold email to US implementers, LinkedIn messages sent by hand, Upwork and Fiverr job posts for paid sessions. Out: paid ads, cold outbound to store owners, GCC or Arabic-market assets, LinkedIn automation or ads, any partner pitch inside Upwork or Fiverr, cold email to UK sole traders or the EU. If asked for a channel that is out, say it is out of scope for this go-to-market and offer the nearest channel that is in.", "",
          "**How it is written.** Plain, exact, a little dry. Short paragraphs, one to three sentences. Specific numbers, named pages, and checkable facts over adjectives. Prices with units: \"$49 a month for 600 conversations\". Partner terms quoted exactly: 25% of each referred store's subscription for 24 months, 30% for lead partners, 10% managed share. One call to action per asset.", "",
          "Banned words: " + ", ".join(BANNED) + ". No em dashes. One idea per sentence. Front-load the point. Write to one reader in the second person. Cut any sentence that would still read correctly with a competitor's name swapped in. Never disparage Shopify or its tools, and never compare Pico with a named competitor.", "",
          "**Before you return anything.** Check the draft against the status list, the proof rule, and the do-not-say table. Fix what breaks. Then name, in one line, the rule the draft came closest to breaking.", "",
          "**When you are unsure.** Ask, or write [NEEDS BRAIN] and keep going. Never fill a gap with an invention."]
    return "\n".join(L) + "\n"


# ================================================================ doors: one source, every tool
#
# Every tool's rule file is rendered from adapters/door.md, and every tool's slash commands from
# .claude/commands/*.md, so a door can never drift on its own: `check` fails in CI if one does.

DOOR_SOURCE = "adapters/door.md"
COMMANDS_DIR = ".claude/commands"
BLOCK_BEGIN = "<!-- gtm-brain:begin -->"
MCP_HINT = "with the command `python3 tools/mcp_server.py` run from this repository's root"

# (path, header, the line for that tool, keep the installer's marked block)
RULE_DOORS = [
    (".cursor/rules/pico-gtm-brain.mdc",
     "---\ndescription: The Pico go-to-market brain. Applies to every task in this repository.\nglobs:\nalwaysApply: true\n---\n",
     "Cursor: `.cursor/mcp.json` mounts the MCP server, and the slash commands are in `.cursor/commands/`.", False),
    (".windsurf/rules/pico-gtm-brain.md",
     "---\ntrigger: always_on\ndescription: The Pico go-to-market brain. Positioning, messaging, claims, competitive work, and any customer-facing copy.\n---\n",
     f"Windsurf: the workflows are in `.windsurf/workflows/`. Add the MCP server in Windsurf's MCP settings {MCP_HINT}.", False),
    (".github/copilot-instructions.md", "# Pico GTM Brain, Copilot instructions\n",
     "GitHub Copilot: this applies to customer-facing strings in code, docs, prompts, and release notes too. The prompt files are in `.github/prompts/`, and `.vscode/mcp.json` mounts the MCP server in agent mode.", True),
    ("GEMINI.md", "# Pico GTM Brain, Gemini CLI entry point\n",
     "Gemini CLI: `.gemini/settings.json` mounts the MCP server and loads `AGENTS.md`, and the slash commands are in `.gemini/commands/pico/`.", True),
    (".clinerules/pico-gtm-brain.md", "# Pico GTM Brain\n", f"Cline: add the MCP server in Cline's MCP settings {MCP_HINT}.", False),
    (".roo/rules/pico-gtm-brain.md", "# Pico GTM Brain\n", f"Roo Code: add the MCP server in Roo's MCP settings {MCP_HINT}.", False),
    (".continue/rules/pico-gtm-brain.md", "---\nname: Pico GTM Brain\nalwaysApply: true\n---\n",
     f"Continue: add the MCP server to your Continue configuration {MCP_HINT}.", False),
    (".kiro/steering/pico-gtm-brain.md", "---\ninclusion: always\n---\n\n# Pico GTM Brain\n",
     f"Kiro: add the MCP server in Kiro's MCP configuration {MCP_HINT}.", False),
    (".amazonq/rules/pico-gtm-brain.md", "# Pico GTM Brain\n",
     f"Amazon Q Developer: add the MCP server in Q's MCP configuration {MCP_HINT}.", False),
    (".junie/guidelines.md", "# Pico GTM Brain, guidelines for Junie\n",
     f"JetBrains Junie: add the MCP server in the IDE's MCP settings {MCP_HINT}.", False),
    (".aiassistant/rules/pico-gtm-brain.md", "# Pico GTM Brain\n",
     "JetBrains AI Assistant: set this rule's type to Always in the AI Assistant rules settings.", False),
    (".trae/rules/project_rules.md", "# Pico GTM Brain\n", f"Trae: add the MCP server in Trae's MCP settings {MCP_HINT}.", False),
    (".openhands/microagents/repo.md", "# Pico GTM Brain\n",
     "OpenHands: every `python3 tools/brain.py` command runs in the sandbox with Python 3.9 or newer and no packages.", False),
    (".goosehints", "Pico GTM Brain\n", f"Goose: add the MCP server as a stdio extension {MCP_HINT}.", False),
]
AIDER_READ = ["AGENTS.md"] + RULES + ["ops/QA-checklist.md"]

# How each tool names, invokes, and passes arguments to a slash command
COMMAND_TOOLS = {
    "cursor": {"path": ".cursor/commands/pico-{n}.md", "invoke": "/pico-{n}", "args": "<the text after this command>"},
    "windsurf": {"path": ".windsurf/workflows/pico-{n}.md", "invoke": "/pico-{n}", "args": "<the text after this command>",
                 "front": ["description"]},
    "copilot": {"path": ".github/prompts/pico-{n}.prompt.md", "invoke": "/pico-{n}", "args": "${{input:request:{hint}}}",
                "front": ["description"]},
    "opencode": {"path": ".opencode/command/pico-{n}.md", "invoke": "/pico-{n}", "args": "$ARGUMENTS",
                 "front": ["description"]},
    "codex": {"path": "adapters/codex/prompts/pico-{n}.md", "invoke": "/prompts:pico-{n}", "args": "$ARGUMENTS",
              "front": ["description", "argument-hint"], "preamble": "Work from the root of the PicoGTMBrain checkout."},
    "gemini": {"path": ".gemini/commands/pico/{n}.toml", "invoke": "/pico:{n}", "args": "{{{{args}}}}", "toml": True},
}


def gen_note(src):
    return f"Generated from {src} by `python3 tools/brain.py build`. Edit the source, never this file."


def door_body():
    return re.sub(r"<!--.*?-->\s*", "", read(DOOR_SOURCE), flags=re.S).strip()


def render_rule_door(rel, head, tool_line, keep_block):
    plain_text = not rel.endswith((".md", ".mdc"))
    note = gen_note(DOOR_SOURCE) if plain_text else f"<!-- {gen_note(DOOR_SOURCE)} -->"
    out = "\n".join([head.rstrip("\n"), "", door_body(), "", tool_line, "", note]) + "\n"
    if keep_block and path(rel).exists():
        text = read(rel)
        if BLOCK_BEGIN in text:
            out += "\n" + text[text.index(BLOCK_BEGIN):].rstrip("\n") + "\n"
    return out


def claude_commands():
    cmds = []
    for p in sorted(path(COMMANDS_DIR).glob("*.md")):
        text = p.read_text(encoding="utf-8")
        fm = frontmatter(text)
        body = re.sub(r"\A---\n.*?\n---\n", "", text, flags=re.S).strip()
        cmds.append({"name": p.stem, "src": f"{COMMANDS_DIR}/{p.name}", "description": fm.get("description", ""),
                     "hint": fm.get("argument-hint", ""), "body": body})
    return cmds


def toml_basic(s, multiline=False):
    s = s.replace("\\", "\\\\")
    if multiline:
        return '"""\n' + s.replace('"""', '\\"\\"\\"') + '\n"""'
    return '"' + s.replace('"', '\\"').replace("\n", "\\n") + '"'


def render_command(tool, cmd, names):
    spec = COMMAND_TOOLS[tool]
    hint = re.sub(r"[<>{}]", "", cmd["hint"]).strip() or "the request"
    body = cmd["body"].replace("$ARGUMENTS", spec["args"].format(hint=hint))
    for n in names:  # point cross-references at this tool's own command names
        body = body.replace(f"`/{n}`", f"`{spec['invoke'].format(n=n)}`")
    if spec.get("preamble"):
        body = spec["preamble"] + "\n\n" + body
    if spec.get("toml"):
        return "\n".join([f"# {gen_note(cmd['src'])}", f"description = {toml_basic(cmd['description'])}",
                          f"prompt = {toml_basic(body, multiline=True)}"]) + "\n"
    front = ""
    if spec.get("front"):
        fields = {"description": cmd["description"], "argument-hint": cmd["hint"]}
        lines = [f"{k}: {fields[k]}" for k in spec["front"] if fields.get(k)]
        front = "---\n" + "\n".join(lines) + "\n---\n\n" if lines else ""
    return front + body + f"\n\n<!-- {gen_note(cmd['src'])} -->\n"


def door_outputs():
    """Every tool door and the HTTP specs, rendered from their single sources."""
    out = {rel: render_rule_door(rel, head, line, keep) for rel, head, line, keep in RULE_DOORS}
    out[".aider.conf.yml"] = "\n".join([f"# {gen_note('tools/brain.py (AIDER_READ)')}",
                                        "# Aider loads these files read-only into every chat.", "read:"] +
                                       [f"  - {f}" for f in AIDER_READ]) + "\n"
    cmds = claude_commands()
    names = [c["name"] for c in cmds]
    for tool, spec in COMMAND_TOOLS.items():
        for c in cmds:
            out[spec["path"].format(n=c["name"])] = render_command(tool, c, names)
    here = str(Path(__file__).resolve().parent)
    if here not in sys.path:
        sys.path.insert(0, here)
    import http_server  # lazy, because the HTTP door imports this module
    out["adapters/http/openapi.json"] = dumps(http_server.openapi_spec())
    out["adapters/http/github-dispatch.openapi.json"] = dumps(http_server.dispatch_spec())
    return out


def generated():
    """Every generated file and its expected content."""
    out = {f"data/{k}.json": dumps(fn()) for k, fn in EXPORTS.items()}
    out["data/manifest.json"] = dumps(export_manifest())
    out["llms-full.txt"] = render_llms_full()
    out["adapters/portable-control-layer.md"] = render_portable()
    out["innovation/LEDGER.md"] = render_ledger()
    out.update(door_outputs())
    return out


# ================================================================ commands

def cmd_context(a):
    sys.stdout.write(context_bundle(a.task, a.audience, a.format))


def cmd_lint(a):
    text = sys.stdin.read() if a.file == "-" else Path(a.file).read_text(encoding="utf-8")
    findings = lint_text(text, a.audience)
    if a.json:
        print(dumps(findings), end="")
    else:
        if findings:
            print(format_findings(findings, a.file))
        errs = sum(1 for f in findings if f["severity"] == "error")
        print(f"{errs} error(s), {len(findings) - errs} warning(s).")
    return 1 if any(f["severity"] == "error" for f in findings) else 0


def lookup(kind, query):
    q = query.lower()
    if kind == "decision":
        return [d for d in data("decisions")["items"] if query.upper() in d["ids"] or q in d["title"].lower()]
    if kind == "metric":
        return [r for r in metric_rows() if q in r["id"].lower() or q in r["name"].lower()]
    src = {"feature": ("features", ["capability", "area", "note"]), "claim": ("claims", ["do_not_say", "say_instead"]),
           "term": ("glossary", ["term", "rule"])}
    if kind not in src:
        raise SystemExit("kind must be feature, claim, term, decision, or metric")
    name, fields = src[kind]
    return [i for i in data(name)["items"] if any(q in str(i.get(f, "")).lower() for f in fields)]


def cmd_lookup(a):
    print(dumps(lookup(a.kind, a.query)), end="")


def search(query, limit=50):
    rx = re.compile(re.escape(query), re.I)
    hits = []
    doors = set(door_outputs())  # rendered copies of adapters/door.md and .claude/commands/, searched at the source
    for rel in brain_files():
        if not rel.endswith((".md", ".txt", ".mdc", ".json")) or rel.startswith(("data/", "llms-full")) or rel in doors:
            continue
        for n, line in enumerate(read(rel).splitlines(), 1):
            if rx.search(line):
                hits.append({"path": rel, "line": n, "text": line.strip()[:240]})
                if len(hits) >= limit:
                    return hits
    return hits


def cmd_search(a):
    for h in search(a.query, a.limit):
        print(f"{h['path']}:{h['line']}: {h['text']}")


def refresh():
    """Rewrite the generated files after a write, so the ledger and exports never lag the logs."""
    for rel, text in generated().items():
        if not path(rel).exists() or read(rel) != text:
            write(rel, text)


def cmd_signal(a):
    tags = [t.strip() for t in (a.tags or "").split(",") if t.strip()]
    rec, ev = add_signal(a.type, a.source, a.verbatim, a.context or "", a.disposition, a.routed, tags, a.date)
    refresh()
    print(f"logged {rec['type']} signal in ops/signal-log.md and event {ev['id']}, ledger refreshed")


def cmd_event(a):
    data_ = json.loads(a.data) if a.data else {}
    refs = {}
    for key in ("decisions", "hypotheses", "experiments", "metrics", "signals"):
        val = getattr(a, key)
        if val:
            refs[key] = [x.strip() for x in val.split(",") if x.strip()]
    if a.corrects:
        refs["corrects"] = a.corrects
    if a.type not in EVENT_TYPES:
        print(f"warning: {a.type!r} is not in the documented taxonomy (reference/innovation-accounting.md)", file=sys.stderr)
    tags = [t.strip() for t in (a.tags or "").split(",") if t.strip()]
    ev, new = append_event(a.type, a.audience, data_, a.source, refs or None, tags or None, a.ts, a.actor)
    refresh()
    print(("appended " if new else "already logged ") + ev["id"])


def cmd_observe(a):
    ev, new = append_event("metric.observed", a.audience, {"metric": a.metric, "value": float(a.value), "period": a.period or ""},
                           a.source, {"metrics": [a.metric]}, None, a.ts)
    refresh()
    print(("appended " if new else "already logged ") + ev["id"])


def cmd_metrics(a):
    rows = metric_rows()
    if a.json:
        print(dumps(rows), end="")
        return 0
    for r in rows:
        if a.audience and r["audience"] != a.audience:
            continue
        print(f"{r['id']:<34} {fmt_value(r['value'], r['unit']):>10}  target {fmt_target(r):<10}  {r['status']:<16} review {r['review'] or '-'}")
    return 0


def cmd_tripwires(a):
    rows = tripwire_rows()
    if a.json:
        print(dumps(rows), end="")
    else:
        for t in rows:
            print(f"{t['id']:<8} {t['decision']:<4} {t['status']:<8} {t['name']}: {t['action']}")
    return 3 if a.strict and any(t["status"] == "FIRED" for t in rows) else 0


def cmd_ledger(a):
    write("innovation/LEDGER.md", render_ledger())
    print("wrote innovation/LEDGER.md")


def cmd_snapshot(a):
    date = a.date or dt.date.today().isoformat()
    label = re.sub(r"[^a-z0-9-]+", "-", a.label.lower()).strip("-")
    rel = f"snapshots/{date}-{label}.md"
    if path(rel).exists():
        raise SystemExit(f"{rel} exists. Snapshots are never overwritten")
    rows = metric_rows()
    L = [f"# Snapshot, {date}, {a.label}", "", "A dated capture of external state. Never skip one because nothing changed: the record that nothing changed is the output.", "",
         "## 1. Funnel", "", "| Stage | Metric | Target | Current | Status |", "|---|---|---|---|---|"]
    for r in rows:
        if r["stage"]:
            L.append(f"| {r['audience']} {r['stage']} | {r['name']} | {fmt_target(r)} | {fmt_value(r['value'], r['unit'])} | {r['status']} |")
    L += ["", "## 2. Channels", "", "| Channel | Assigned role | Actual | Verdict |", "|---|---|---|---|",
          "| Shopify App Store | Merchant discovery and install | Fill in | Fill in |",
          "| Content and search | Merchant awareness | Fill in | Fill in |",
          "| Product-led lifecycle | Activation to paid | Fill in | Fill in |",
          "| Cold email | Implementer awareness | Fill in | Fill in |",
          "| LinkedIn by hand | Implementer awareness | Fill in | Fill in |",
          "| Upwork and Fiverr | Paid sessions | Fill in | Fill in |", "",
          "## 3. Segments", "", "Fill in: which ICP level is converting, and which named segment is not showing up.", "",
          "## 4. Wins and losses", "", "| Reason | Count | Won or lost | Signal type |", "|---|---|---|---|", "", "",
          "## 5. Competitive", "", "Fill in: launches, repositions, pricing changes. Recheck every claim in `rules/do-not-say.md` that names a competitor.", "",
          "## 6. Product and delivery status", "", "| Capability | Ledger says | Reality | Action |", "|---|---|---|---|"]
    for f in export_features()["items"]:
        if f["status"] == "IN BUILD":
            L.append(f"| {f['capability']} | IN BUILD | Fill in | Fill in |")
    L += ["", "## 7. What this changes", "", "Fill in: the AMENDs and PATCHes with owners, or the sentence \"No ledger change this period.\"", "",
          "**Ledgers reviewed this snapshot:** list them, and update `last_reviewed` on each."]
    write(rel, "\n".join(L) + "\n")
    print(f"wrote {rel}")


def cmd_export(a):
    for k, fn in EXPORTS.items():
        write(f"data/{k}.json", dumps(fn()))
    write("data/manifest.json", dumps(export_manifest()))
    print("wrote data/*.json")


def cmd_build(a):
    for rel, text in generated().items():
        write(rel, text)
    print("built data/*.json, llms-full.txt, adapters/portable-control-layer.md, innovation/LEDGER.md, "
          "every tool door, and adapters/http/*.json")


def cmd_check(a):
    stale = [rel for rel, text in generated().items() if not path(rel).exists() or read(rel) != text]
    for rel in stale:
        print(f"stale: {rel}")
    if stale:
        print("Run `python3 tools/brain.py build` and commit the result.")
        return 1
    print("generated files are current")
    return 0


def validate_all():
    errs = []
    for rel, sch in (("innovation/metrics.json", "metrics"), ("innovation/hypotheses.json", "hypotheses"),
                     ("innovation/experiments.json", "experiments"), ("innovation/tripwires.json", "tripwires")):
        errs += [f"{rel}: {e}" for e in validate(load_json(rel), schema(sch))]
    sch = schema("event")
    for f in sorted(path("innovation/events").glob("*.jsonl")):
        for n, line in enumerate(f.read_text(encoding="utf-8").splitlines(), 1):
            if line.strip():
                errs += [f"{f.relative_to(ROOT)}:{n}: {e}" for e in validate(json.loads(line), sch)]
    for s in parse_signals():
        errs += [f"ops/signal-log.md {s['date']}: {e}" for e in validate({k: v for k, v in s.items() if v or k in ('disposition',)}, schema("signal"))]
    mids = {m["id"] for m in load_json("innovation/metrics.json")["metrics"]}
    for h in load_json("innovation/hypotheses.json")["hypotheses"]:
        if h["metric"] not in mids:
            errs.append(f"innovation/hypotheses.json {h['id']}: unknown metric {h['metric']}")
    for rel in (".mcp.json", ".cursor/mcp.json", ".vscode/mcp.json", ".gemini/settings.json"):
        if path(rel).exists():
            try:
                load_json(rel)
            except json.JSONDecodeError as e:
                errs.append(f"{rel}: {e}")
    return errs


def cmd_validate(a):
    errs = validate_all()
    for e in errs:
        print(e)
    print(f"{len(errs)} schema error(s).")
    return 1 if errs else 0


def example_body(rel):
    """The asset itself: the text between the first two horizontal rules of an example file."""
    parts = re.split(r"^---\s*$", read(rel), flags=re.M)
    return parts[1] if len(parts) >= 3 else read(rel)


def cmd_audit(a):
    code = 0
    if not VENDORED_AUDIT.exists():
        print("vendored audit not found: install the skill with the installer in README.md")
        code = 1
    else:
        with tempfile.TemporaryDirectory() as tmp:
            mirror = Path(tmp) / "brain"
            shutil.copytree(ROOT, mirror, ignore=shutil.ignore_patterns(".git", "node_modules", "__pycache__", ".venv"))
            shutil.rmtree(mirror / ".claude" / "skills", ignore_errors=True)
            res = subprocess.run([sys.executable, str(VENDORED_AUDIT), str(mirror), "--max-age-days", str(a.max_age_days)],
                                 capture_output=True, text=True)
            print(res.stdout.replace(str(mirror), "PicoGTMBrain").rstrip())
            code = max(code, res.returncode)
    errs = validate_all()
    print(f"\nSchema validation: {len(errs)} error(s).")
    for e in errs:
        print(f"  [ERROR] {e}")
    stale = [rel for rel, text in generated().items() if not path(rel).exists() or read(rel) != text]
    print(f"Generated files: {'current' if not stale else 'stale: ' + ', '.join(stale)}")
    lint_errs = 0
    for rel in sorted(str(p.relative_to(ROOT)) for p in path("examples").glob("*.md")):
        found = [f for f in lint_text(example_body(rel)) if f["severity"] == "error"]
        lint_errs += len(found)
        for f in found:
            print(f"  [LINT] {rel}:{f['line']}: {f['message']}")
    print(f"Examples lint: {lint_errs} error(s).")
    return 1 if (code or errs or stale or lint_errs) else 0


def main(argv=None):
    p = argparse.ArgumentParser(prog="brain.py", description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("context", help="print the load set for a task")
    s.add_argument("task", choices=sorted(TASKS))
    s.add_argument("--audience", choices=["merchants", "implementers"])
    s.add_argument("--format", choices=["list", "cat", "json"], default="list")
    s.set_defaults(fn=cmd_context)
    s = sub.add_parser("lint", help="check a draft against the control layer")
    s.add_argument("file", help="a file, or - for stdin")
    s.add_argument("--audience", choices=["merchants", "implementers"])
    s.add_argument("--json", action="store_true")
    s.set_defaults(fn=cmd_lint)
    s = sub.add_parser("lookup", help="query a ledger")
    s.add_argument("kind", choices=["feature", "claim", "term", "decision", "metric"])
    s.add_argument("query")
    s.set_defaults(fn=cmd_lookup)
    s = sub.add_parser("search", help="grep the brain")
    s.add_argument("query")
    s.add_argument("--limit", type=int, default=50)
    s.set_defaults(fn=cmd_search)
    s = sub.add_parser("signal", help="log a market signal")
    s.add_argument("--type", required=True, choices=SIGNAL_TYPES + [t.lower() for t in SIGNAL_TYPES])
    s.add_argument("--source", required=True)
    s.add_argument("--verbatim", required=True)
    s.add_argument("--context")
    s.add_argument("--disposition", default="NOISE")
    s.add_argument("--routed", default="none")
    s.add_argument("--tags")
    s.add_argument("--date")
    s.set_defaults(fn=cmd_signal)
    s = sub.add_parser("event", help="append an activity to the event log")
    s.add_argument("type")
    s.add_argument("--audience", default="both", choices=["merchants", "implementers", "both"])
    s.add_argument("--data", help="JSON object")
    s.add_argument("--source", default="brain.py")
    s.add_argument("--actor")
    s.add_argument("--ts")
    s.add_argument("--tags")
    for key in ("decisions", "hypotheses", "experiments", "metrics", "signals"):
        s.add_argument(f"--{key}", help="comma-separated ids")
    s.add_argument("--corrects", help="id of the event this one corrects")
    s.set_defaults(fn=cmd_event)
    s = sub.add_parser("observe", help="record a metric value as a metric.observed event")
    s.add_argument("metric")
    s.add_argument("value")
    s.add_argument("--audience", default="both", choices=["merchants", "implementers", "both"])
    s.add_argument("--period")
    s.add_argument("--source", default="manual")
    s.add_argument("--ts")
    s.set_defaults(fn=cmd_observe)
    s = sub.add_parser("metrics", help="compute KPIs from the event log")
    s.add_argument("--audience", choices=["merchants", "implementers"])
    s.add_argument("--json", action="store_true")
    s.set_defaults(fn=cmd_metrics)
    s = sub.add_parser("tripwires", help="evaluate decision reopen conditions")
    s.add_argument("--json", action="store_true")
    s.add_argument("--strict", action="store_true", help="exit 3 if any tripwire fired")
    s.set_defaults(fn=cmd_tripwires)
    sub.add_parser("ledger", help="regenerate innovation/LEDGER.md").set_defaults(fn=cmd_ledger)
    s = sub.add_parser("snapshot", help="scaffold a dated snapshot")
    s.add_argument("label")
    s.add_argument("--date")
    s.set_defaults(fn=cmd_snapshot)
    sub.add_parser("export", help="regenerate data/*.json").set_defaults(fn=cmd_export)
    sub.add_parser("build", help="regenerate every generated file").set_defaults(fn=cmd_build)
    sub.add_parser("check", help="fail if a generated file is stale").set_defaults(fn=cmd_check)
    sub.add_parser("validate", help="validate JSON files against schemas/").set_defaults(fn=cmd_validate)
    s = sub.add_parser("audit", help="run the full audit")
    s.add_argument("--max-age-days", type=int, default=90)
    s.set_defaults(fn=cmd_audit)
    a = p.parse_args(argv)
    return a.fn(a) or 0


if __name__ == "__main__":
    try:
        import signal as _signal
        _signal.signal(_signal.SIGPIPE, _signal.SIG_DFL)
    except (AttributeError, ValueError):
        pass
    sys.exit(main())
