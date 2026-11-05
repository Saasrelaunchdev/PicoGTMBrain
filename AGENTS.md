# Pico GTM Brain, agent entry point

Cross-tool entry file. Codex, Cursor, Zed, Jules, opencode, Amp, and most newer agents read `AGENTS.md`, and Aider loads it through `.aider.conf.yml`, so this is the widest door into the brain. Kept identical in intent to `CLAUDE.md`. If the two differ, `CLAUDE.md` wins.

No file access, or a tool that reads neither file? Paste `adapters/portable-control-layer.md`. MCP client? Mount `tools/mcp_server.py`. HTTP only? `tools/http_server.py` serves REST and remote MCP, read only (see `README.md`).

## Start here
1. `context/Pico_GTM_Master_Context.md`, the full go-to-market for both audiences. Source of truth.
2. `rules/glossary.md`, canonical names.
3. `rules/feature-status.md`, shipped versus in build.
4. `rules/do-not-say.md`, forbidden claims and safe replacements.
5. `rules/writing-rules.md`, mechanics and channel discipline.
6. The channel engine: `reference/app-store-engine.md` for merchants, `reference/outreach-engine.md` for implementers.

Exact load set for any task: `python3 tools/brain.py context <task> --audience <a> --format cat`.

## Channel discipline
In: the Shopify App Store, content and search, the product-led lifecycle, cold email to US implementers, LinkedIn by hand, Upwork and Fiverr job posts. Out: paid ads, cold outbound to store owners, GCC or Arabic-market work, LinkedIn automation or ads, partner pitches inside Upwork or Fiverr, cold email to UK sole traders or the EU.

## Audiences, never blended
- Merchants: US Shopify stores whose shoppers need help choosing between similar or technical products.
- Implementers: agencies, developers, theme developers, and freelancers who set up Shopify stores.

## Non-negotiables
- No revenue, conversion, ROI, or lift claim. No invented proof: the proof log is empty, use open proof.
- No unshipped capability in the present tense. Check `rules/feature-status.md`.
- Stock as of the last catalog sync. No semantic search, no checkout in chat.
- Never disparage Shopify. No named competitor comparison in copy that customers see.
- No em dashes, no banned words.

## Before shipping
`python3 tools/brain.py lint <file>`, then `ops/QA-checklist.md`.

## Compounding
Market input: `ops/signal-log.md` via `python3 tools/brain.py signal`. Activity: `python3 tools/brain.py event`. Rule changes: ledger, master context, decision log, copy, then `python3 tools/brain.py build`. Weekly: `python3 tools/brain.py tripwires` and `python3 tools/brain.py ledger`.

Every other tool's rule file and slash commands are rendered from `adapters/door.md` and `.claude/commands/` by `python3 tools/brain.py build`. Edit the sources, never the rendered copies.

<!-- gtm-brain:begin -->
## Go-to-Market Brain

For any go-to-market work in this project, read `.claude/skills/go-to-market-brain/SKILL.md` first and follow
its procedure instead of improvising a method it already defines.

It routes to three modes:

- **BUILD**, turn source material (dashboards, decks, positioning docs) into a governed context repository.
- **UPDATE**, take a signal from a lead, customer, or competitor, or a periodic snapshot, triage it, and route it to the right ledger.
- **OPERATE**, produce, check, and ship an asset against a brain that already exists.

Open the reference file `SKILL.md` names for the mode you are in at the point you need it,
rather than reading the whole skill up front.

If this project already contains a built brain, load its entry file and its `rules/` layer
before writing anything customer-facing. Never describe an unshipped capability as live,
never invent a number or a customer, and run the brain's `ops/QA-checklist.md` against a
draft before returning it.

For copy rules alone, with no brain in play, read `.claude/skills/gtm-slop-filter/SKILL.md`.
<!-- gtm-brain:end -->
