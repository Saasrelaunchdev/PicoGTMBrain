# Innovation accounting: how activity becomes knowledge

Load when logging any activity, reading progress, closing an experiment, or deciding to pivot or persevere. Synthesized for this brain from the compounding loop, the 90-day targets (D44, D45), and the "reopen when" triggers in `ops/decisions.md`.

## The idea
Pico is pre-launch, so the only honest measure of progress is validated learning: which assumptions survived contact with real merchants and implementers, and how fast. Every activity (a session, an install, a review, a call note, a shipped asset) becomes an event. Events roll up into metrics. Metrics test hypotheses. Hypotheses close experiments. Experiments and tripwires reopen or confirm decisions. Decisions change ledgers, and ledgers improve every next asset. That chain is the snowball.

## The three milestones
1. **Baseline.** Measure where each funnel really is. Until day 30 after the listing is live, and until the first 10 paid sessions, every metric is a baseline, not a verdict.
2. **Tune.** Run experiments that move one metric at a time toward its target: listing screenshots, the activation checklist, the first email's opening line, the Upwork post's fee.
3. **Pivot or persevere.** At the day 60 and day 90 reviews, and whenever a tripwire fires, decide with the numbers in `innovation/LEDGER.md`. Write the decision in `ops/decisions.md`, including what it does not change.

## The objects (schemas in `schemas/`)

| Object | Lives in | Written by | Purpose |
|---|---|---|---|
| Event | `innovation/events/YYYY-MM.jsonl`, append only | `tools/brain.py event`, the MCP server, CI, webhooks | One activity, with time, type, audience, data, and references |
| Signal | `ops/signal-log.md`, mirrored as a `signal.logged` event | `tools/brain.py signal` | Raw market input awaiting triage |
| Metric | `innovation/metrics.json` | Edited by hand, reviewed monthly | A KPI: definition, target, comparator, review point, and how it is computed from events |
| Hypothesis | `innovation/hypotheses.json` | Edited by hand | A leap-of-faith assumption with its metric and its pass and fail thresholds |
| Experiment | `innovation/experiments.json` | Edited by hand, closed at its end date | A time-boxed test of a hypothesis, with budget, result, and learning |
| Tripwire | `innovation/tripwires.json` | Edited with the decision it guards | A machine-checkable "reopen when" condition for a decision |
| Ledger | `innovation/LEDGER.md`, generated | `tools/brain.py ledger` | The current state of all of the above, for humans and agents |

## Metric rules
- **Actionable:** every metric names the stage it measures and the decision it informs. No vanity counts like page views without a conversion.
- **Accessible:** every metric is defined in one sentence a merchant could follow.
- **Auditable:** every value traces to events with a source. No number enters the ledger without one.
- Cohorts beat totals. Compare founding stores by install week, and sessions by channel.

## The event taxonomy
`metric.observed`, `signal.logged`, `install`, `activation.step`, `conversation.first`, `plan.changed`, `uninstall`, `review.received`, `session.offered`, `session.completed`, `interview.completed`, `case_study.permission`, `partner.signed`, `payout.made`, `asset.shipped`, `experiment.started`, `experiment.closed`, `decision.made`, `decision.reopened`, `milestone`. Unknown types are allowed but warned, so the taxonomy can grow without breaking the log.

## How the snowball compounds
- Every signal is kept verbatim, so customer language accumulates in `ops/copy-bank.md`.
- Every closed experiment leaves a learning that later prompts can cite.
- Every tripwire check is a recorded "nothing changed" or a dated reopen, so decisions stay settled until evidence moves them.
- Every amendment improves every future asset, for every operator and every agent, without anyone being told.

## Weekly loop (Monday)
1. Pull metrics: add `metric.observed` events for each KPI with new data.
2. Triage signals in `ops/signal-log.md`.
3. Run `python3 tools/brain.py tripwires` and `python3 tools/brain.py ledger`.
4. Close or start experiments. Route any AMEND through the procedure.

## Never
Never backfill an event with an estimate. Never edit or delete a past event: append a correction with `refs` to the original. Never let a metric value reach copy: metrics are internal until they enter the proof log with permission.
