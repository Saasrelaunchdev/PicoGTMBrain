Run the weekly loop:

1. `python3 tools/brain.py tripwires`. Report anything FIRED, with its decision and action.
2. `python3 tools/brain.py metrics`. Report every KPI below target or missed at review.
3. Read the signals added since last week in `ops/signal-log.md`. Increment or expire WATCH items, execute PATCHes, and list AMENDs for the founder.
4. Close or start experiments in `innovation/experiments.json`.
5. `python3 tools/brain.py ledger`, then summarize what changed, and say plainly what did not.

<!-- Generated from .claude/commands/weekly-review.md by `python3 tools/brain.py build`. Edit the source, never this file. -->
