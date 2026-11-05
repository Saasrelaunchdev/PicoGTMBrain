## What changed

<!-- One line. Name the ledger, file, or asset. -->

## Type
- [ ] PATCH: copy only, no ledger change
- [ ] AMEND: a ledger, a position, or a rule changed
- [ ] Activity: signals, events, snapshots, or experiment updates
- [ ] Tooling: `tools/`, `schemas/`, adapters, or CI

## AMEND checklist, all five or none
- [ ] The `rules/` ledger updated first, with `last_reviewed`
- [ ] The master context section updated, `version` and `last_updated` bumped
- [ ] A dated `ops/decisions.md` entry with what this does not change, downstream owners, and the reopen trigger
- [ ] Old phrasing searched for and fixed in the copy bank, templates, examples, and references
- [ ] `python3 tools/brain.py build` run and the generated files committed

## Checks
- [ ] `python3 tools/brain.py audit` passes
- [ ] `python3 -m unittest discover -s tools/tests` passes
