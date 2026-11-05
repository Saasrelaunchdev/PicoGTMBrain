---
description: Take a dated snapshot of external state
argument-hint: <label, for example month-1>
---

Run `python3 tools/brain.py snapshot $ARGUMENTS`, then fill every section of the new file in `snapshots/` from the data available. Diff section 6 against `rules/feature-status.md`. Finish with what this changes, or the sentence "No ledger change this period" if that is the honest answer, and update `last_reviewed` on every ledger you examined.
