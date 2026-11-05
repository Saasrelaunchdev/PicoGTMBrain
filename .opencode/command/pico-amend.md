---
description: Change a ledger through the full amendment procedure
---

Amend the Pico brain for: $ARGUMENTS

All five steps, in order, or none:

1. Update the governing `rules/` ledger and its `last_reviewed` date.
2. Update the matching section of `context/Pico_GTM_Master_Context.md`, bump `version` and `last_updated`, and revise `status_notes` if what an agent may assume changed.
3. Add a dated entry at the top of `ops/decisions.md`: verdict, rationale with the evidence, what this does not change, downstream assets with owners, and the reopen trigger. Add or update its tripwire in `innovation/tripwires.json`.
4. Search `ops/copy-bank.md`, `templates/`, `examples/`, and `reference/` for the old phrasing and fix it.
5. Run `python3 tools/brain.py build` and `python3 tools/brain.py audit`, then add a `decision.made` event.

<!-- Generated from .claude/commands/amend.md by `python3 tools/brain.py build`. Edit the source, never this file. -->
