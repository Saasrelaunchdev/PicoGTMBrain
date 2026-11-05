# Pico GTM Brain, agent entry point

This repository is the Pico go-to-market: two standalone GTMs, one for Shopify merchants and one for the implementers who set up their stores. You are an AI agent working inside it. Read this file, then follow its pointers. Do not improvise strategy the brain already settles.

## Read before any customer-facing output
1. `context/Pico_GTM_Master_Context.md`, the full strategy for both audiences. Source of truth. Read Section 0 and `status_notes` first.
2. `rules/glossary.md`, the canonical names and the distinctions that must never blur.
3. `rules/feature-status.md`, shipped versus in build. Check every capability you mention.
4. `rules/do-not-say.md`, forbidden claims and their safe replacements.
5. `rules/writing-rules.md`, mechanics, tone, channel discipline, signature lines.

Shortcut: `python3 tools/brain.py context <task> --audience <a>` prints the exact load set for a task. The MCP server in `tools/mcp_server.py` exposes the same through `brain_load_set`.

## This GTM is self-serve and pre-launch
Merchants: Shopify App Store, content and search including AI answer engines, and the product-led lifecycle. Load `reference/app-store-engine.md` first. Implementers: cold email to US recipients, LinkedIn messages sent by hand, and Upwork and Fiverr job posts for paid usability sessions. Load `reference/outreach-engine.md` first.

Out, refuse and redirect: paid ads, cold outbound to store owners, GCC or Arabic-market assets, LinkedIn automation or ads, any partner pitch inside Upwork or Fiverr, cold email to UK sole traders or the EU.

## Pick the audience first
Two audiences with separate value propositions. Never blend them in one asset.
- **Merchants:** US Shopify stores whose shoppers need help choosing. `reference/value-proposition-merchants.md`.
- **Implementers:** agencies, developers, theme developers, and freelancers. `reference/value-proposition-implementers.md`.

## Non-negotiables
- No revenue, sales, conversion, ROI, or lift claim. Pico measures what shoppers asked, saw, clicked, and added to cart.
- No invented proof: no install, review, or merchant count, no testimonial, no named merchant. The proof log is empty. Use open proof.
- No unshipped capability in the present tense. IN BUILD gets "coming soon" in the same sentence.
- Stock is "as of your last catalog sync". No semantic search, no checkout in chat.
- Never disparage Shopify or its tools. No named competitor comparison in copy that customers see.
- Partner terms only as published, and only from week 6: 25% for 24 months, 30% for lead partners, 10% managed.
- No em dashes. None of the banned words in `rules/writing-rules.md`.

## Before you ship
Run `python3 tools/brain.py lint <file>`, then walk `ops/QA-checklist.md`. State the audience, stage, and every capability's status flag.

## When something changes
New market input goes to `ops/signal-log.md` first (`python3 tools/brain.py signal ...`). Activity goes to the event log (`python3 tools/brain.py event ...`). A rule change follows the amendment procedure: the `rules/` ledger, then the master context, then `ops/decisions.md`, then the copy, then `python3 tools/brain.py build`. Never the other way around.

For BUILD, UPDATE, or OPERATE method, the installed skill is at `.claude/skills/go-to-market-brain/SKILL.md`.
