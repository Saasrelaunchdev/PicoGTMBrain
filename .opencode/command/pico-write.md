---
description: Produce one Pico GTM asset inside the guardrails
---

Produce this asset for Pico: $ARGUMENTS

1. Name the task and the audience. Tasks: `python3 tools/brain.py context --help`. Never blend merchants and implementers.
2. Run `python3 tools/brain.py context <task> --audience <audience> --format cat` and read everything it prints.
3. Draft from the template, using `ops/copy-bank.md` lines verbatim where they fit. Open proof only.
4. Save the draft, run `python3 tools/brain.py lint <file>`, and fix every error.
5. Walk `ops/QA-checklist.md`. Return the asset, then the audience, stage, template used, every capability with its status flag, any claim you narrowed, and anything the brain could not supply.

<!-- Generated from .claude/commands/write.md by `python3 tools/brain.py build`. Edit the source, never this file. -->
