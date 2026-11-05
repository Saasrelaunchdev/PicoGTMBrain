# Pico GTM Brain, Copilot instructions

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

GitHub Copilot: this applies to customer-facing strings in code, docs, prompts, and release notes too. The prompt files are in `.github/prompts/`, and `.vscode/mcp.json` mounts the MCP server in agent mode.

<!-- Generated from adapters/door.md by `python3 tools/brain.py build`. Edit the source, never this file. -->

<!-- gtm-brain:begin -->
## Go-to-Market Brain

This project keeps its go-to-market as files, not as tribal knowledge.

For marketing, sales, positioning, messaging, or any customer-facing copy, read
`.claude/skills/go-to-market-brain/SKILL.md` first and follow its procedure. It covers three modes: building a
governed context repository from source material, updating one from a market signal, and
producing an asset against one that exists.

When this project holds a built brain, load its entry file and its `rules/` layer before
suggesting copy. Three rules override any suggestion you would otherwise make: a capability
that is not shipped is never described in the present tense, a number or customer name that
is not in the brain is never written, and every draft passes the brain's `ops/QA-checklist.md`
before it is offered.
<!-- gtm-brain:end -->
