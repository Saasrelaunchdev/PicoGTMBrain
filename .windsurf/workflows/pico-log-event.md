---
description: Record an activity in the innovation event log
---

Record this activity: <the text after this command>

Pick the event type from `reference/innovation-accounting.md`, fill `data` with the facts and their source, add `refs` to decisions, hypotheses, or experiments, and run `python3 tools/brain.py event <type> --audience <a> --data '<json>' --source '<where it came from>'`. A KPI value is `python3 tools/brain.py observe <metric-id> <value> --source ...`. Never estimate a value, and never edit a past event: append a correction with `--corrects <id>`.

<!-- Generated from .claude/commands/log-event.md by `python3 tools/brain.py build`. Edit the source, never this file. -->
