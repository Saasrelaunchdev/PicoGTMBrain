# Review cadence

Who reviews what, how often, and when a file is considered stale. Defaults agreed 2026-11-04, to be confirmed by the founder. Owners are roles: on a two-person team the founder holds most of them.

## Rituals

| Ritual | Frequency | Owner | Work |
|---|---|---|---|
| Signal triage | Weekly, Monday | Founder | Disposition every new signal, increment WATCH counters, execute PATCHes, run `python3 tools/brain.py tripwires` |
| Metrics pull | Weekly, Monday | Engineer | Add `metric.observed` events for every KPI in `innovation/metrics.json` that has data, then `python3 tools/brain.py ledger` |
| Ledger sweep | Monthly, first Monday | Founder and engineer | Read all four `rules/` files against reality, update `last_reviewed`, expire stale WATCH items |
| Snapshot | Monthly until launch day 90, then quarterly | Founder | `python3 tools/brain.py snapshot <label>`, fill every section, end in what it changed |
| Experiment review | At each experiment's end date | Founder | Close the experiment in `innovation/experiments.json` with result, learning, and decision |
| Master context version | On any AMEND, and quarterly | Founder | Bump version, refresh `status_notes`, verify sections against the ledgers |
| Brain audit | Monthly, and in CI on every push | Engineer | `python3 tools/brain.py audit`, then produce one live asset using only the brain |
| Adapter check | With the ledger sweep | Engineer | Regenerate the portable control layer with `python3 tools/brain.py build`, run the conformance prompts |

The launch calendar sets fixed review points: day 30 after the listing goes live (listing and activation targets), day 60 (week 12, conversion and both cohorts), day 90 (week 13, budget and the next block).

## Ledger ownership and staleness

| File | Owner | Stale after |
|---|---|---|
| `rules/feature-status.md` | Engineer | 14 days during launch, then 30 |
| `rules/do-not-say.md` | Founder | 60 days |
| `rules/glossary.md` | Founder | 90 days |
| `rules/writing-rules.md` | Founder | 180 days |
| `context/Pico_GTM_Master_Context.md` | Founder | 60 days |
| `adapters/portable-control-layer.md` | Engineer | Regenerated on any ledger change, never older than the newest ledger |
| `innovation/metrics.json` | Engineer | 7 days without a metrics pull after launch |

`feature-status.md` goes stale fastest during the launch build, because the build list ships something every two weeks.

## Authority
- A PATCH can be made by anyone producing work, human or agent.
- An AMEND to any `rules/` file needs the founder's approval in the pull request.
- A change to positioning, ICP, pricing, the partner terms, or the channel mix needs the founder and a dated entry in `ops/decisions.md`.
- A legal or platform rule change (D47 to D52) needs counsel's note recorded in the decision entry.
