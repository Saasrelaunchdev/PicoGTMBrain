# Pico GTM Brain

This repository is the Pico go-to-market brain, the source of truth for positioning, messaging, claims, status, and voice for two audiences. Load `AGENTS.md` first, then `rules/glossary.md`, `rules/feature-status.md`, `rules/do-not-say.md`, and `rules/writing-rules.md`. For merchant channel work load `reference/app-store-engine.md`, for implementer outreach `reference/outreach-engine.md`. If this file and `CLAUDE.md` differ, `CLAUDE.md` wins.

Pick the audience first, never blend them:
- Merchants: US Shopify stores whose shoppers need help choosing. `reference/value-proposition-merchants.md`.
- Implementers: agencies, developers, theme developers, and freelancers. `reference/value-proposition-implementers.md`.

Non-negotiables:
- No revenue, conversion, ROI, or lift claim. No invented proof: the proof log is empty, use open proof.
- No unshipped capability in the present tense: check `rules/feature-status.md`.
- Stock as of the last catalog sync. No semantic search, no checkout in chat.
- Never disparage Shopify. No named competitor comparison in copy that customers see.
- No em dashes, none of the banned words in `rules/writing-rules.md`.

The exact files for a task: `python3 tools/brain.py context <task> --audience <audience> --format cat`. Run `python3 tools/brain.py lint <file>` and walk `ops/QA-checklist.md` before returning a draft. New market input goes to `ops/signal-log.md` first, never straight into the copy. Generated files (`data/`, `llms-full.txt`, `adapters/portable-control-layer.md`, `innovation/LEDGER.md`, and every tool door) are rebuilt with `python3 tools/brain.py build`, never edited by hand.

JetBrains AI Assistant: set this rule's type to Always in the AI Assistant rules settings.

<!-- Generated from adapters/door.md by `python3 tools/brain.py build`. Edit the source, never this file. -->
