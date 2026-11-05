---
description: Take a dated snapshot of external state
argument-hint: <label, for example month-1>
---

Work from the root of the PicoGTMBrain checkout.

Run `python3 tools/brain.py snapshot $ARGUMENTS`, then fill every section of the new file in `snapshots/` from the data available. Diff section 6 against `rules/feature-status.md`. Finish with what this changes, or the sentence "No ledger change this period" if that is the honest answer, and update `last_reviewed` on every ledger you examined.

<!-- Generated from .claude/commands/snapshot.md by `python3 tools/brain.py build`. Edit the source, never this file. -->
