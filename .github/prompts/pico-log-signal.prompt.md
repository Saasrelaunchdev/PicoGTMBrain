---
description: Log a market signal verbatim and triage it
---

Log this in the Pico brain: ${input:request:paste the call note, review, message, or competitor move}

1. Keep the verbatim. Classify the type: OBJECTION, LANGUAGE, PROOF, STATUS, COMPETITIVE, SEGMENT, CHANNEL, LOSS, or RISK.
2. Assign a disposition with the thresholds in `ops/signal-log.md`. Default NOISE. Facts that are verified act now.
3. Add tags that match `innovation/tripwires.json` where they apply, for example handoff-request, theme-issue, gcc-inbound, custom-plan-request.
4. Run `python3 tools/brain.py signal --type ... --source ... --verbatim ... --context ... --disposition ... --tags ...`.
5. Run `python3 tools/brain.py tripwires`. If the signal is a PATCH or AMEND, list exactly which files change, and for an AMEND follow `/pico-amend`.

<!-- Generated from .claude/commands/log-signal.md by `python3 tools/brain.py build`. Edit the source, never this file. -->
