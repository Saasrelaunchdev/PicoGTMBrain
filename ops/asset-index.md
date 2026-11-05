# Asset index

Where the source deliverables, product surfaces, live claims, and tool adapters live. An amendment consults this file to find everything that carries an old claim, so keep it current.

## Source deliverables (the manifest)

| Artifact | Type | What it settles | Dated | Location |
|---|---|---|---|---|
| Pico Core Features Overview | PDF, MD transcription | Every shipped capability and current limit | 2026-11-02 | `sources/extracted/pico-core-features-overview.md` |
| GTM discovery brief | MD | Archetype, slates, feature list, narrowed claims, proof rules | 2026-11-03 | `sources/extracted/gtm-brief.md` |
| Decision log, 56 entries | MD | Every price, rule, target, and date | 2026-11-03 | `sources/extracted/decisions-source.md`, distilled in `ops/decisions.md` |
| Product Feature Matrix x2 | MD, XLSX | Hero, differentiators, table stakes, demand drivers | 2026-11-03 | `sources/extracted/merchants/`, `sources/extracted/implementers/` |
| Competitive Market Analysis x2 | MD, XLSX | Slates, vectors, presence, potency, advantages | 2026-11-03 | same folders |
| Positioning summary and statements x2 | MD, DOCX | Where Pico leads, defensibility, three statements each | 2026-11-03 | same folders |
| ICP Dashboard and Buying Committee x2 | MD, XLSX | Levels, bands, personas, design partners | 2026-11-03 | same folders |
| Value Proposition x2 | MD, DOCX | Promise, pillars, nine copy drills each | 2026-11-03 | same folders |
| Customer Journey Funnel x2 | MD, XLSX | Seven stages, activation and engagement sub-funnels, targets | 2026-11-03 | same folders |
| Assets and Collaterals Library x2 | MD, XLSX | Three channels each, asset backlog, QA rules | 2026-11-03 | same folders |
| Pricing and Packaging x2 | MD, XLSX | Value metric, tiers, ROI anchors, calculators | 2026-11-03 | same folders |
| Lead magnet specs and scorecard briefs x2 | MD, XLSX, DOCX | Questions, scoring, tiers, emails | 2026-11-03 | same folders |
| GTM walkthrough deck outlines x2 | MD | The ten-slide story per audience | 2026-11-03 | same folders |
| Research pass, 18 files | MD | Every sourced fact with URL and date | 2026-11-03 | `sources/research/` |
| Founder walkthrough | HTML | Both go-to-markets in one offline page | 2026-11-04 | PicoFindsGTMBuild repo, `walkthrough/index.html` |
| Google folder, 24 documents | XLSX, DOCX | The house-format deliverables per audience | 2026-11-04 | PicoFindsGTMBuild repo, `google-folder/` |
| Flow transformations | Mermaid | Before and after flows for both audiences | 2026-11-04 | PicoFindsGTMBuild repo, `flow-transformation/` |

Raw binaries stay in the build repository: github.com/Saasrelaunchdev/PicoFindsGTMBuild. The Markdown here is the readable copy.

## Product and brand
- Product and site: picofinds.com. Contact: us@picofinds.com.
- Sandbox store: the Sandbox link in picofinds.com's top menu.
- Setup skill: downloadable from the dashboard's Integrations page.
- Brand palette: purple #8B6CE8 (logo), #6448D8 (accent), #13111B (dark surface), from the walkthrough design tokens.

## Live surfaces (every place a claim is published)
- picofinds.com homepage: three lines to replace before the first implementer email (D3). Last reviewed 2026-11-03.
- picofinds.com pricing section: add yearly prices, Scale, and the conversation definition when they ship.
- Shopify App Store listing: not live. Submission week 1.
- picofinds.com/partners: not live. Week 6.
- ScoreApp scorecards: not live. Merchant week 3, implementer week 6.
- Technical one-pager: not published. Needs the week 1 speed measurement.

## Tool adapters (where the guardrails load)

Every rule file below except the routers is rendered from `adapters/door.md`, and every slash command from `.claude/commands/`, by `python3 tools/brain.py build`. CI fails if one drifts, so an unused door costs nothing until it is pruned from `RULE_DOORS` or `COMMAND_TOOLS` in `tools/brain.py`.

| Adapter | Installed at | Tool |
|---|---|---|
| `CLAUDE.md` | repo root | Claude Code, Claude apps |
| `AGENTS.md` | repo root | Codex, Cursor, Zed, Jules, opencode, Amp, and most newer agents |
| `GEMINI.md` | repo root, rendered | Gemini CLI |
| `.cursor/rules/`, `.windsurf/rules/`, `.github/copilot-instructions.md` | repo, rendered | Cursor, Windsurf, GitHub Copilot |
| `.clinerules/`, `.roo/rules/`, `.continue/rules/`, `.kiro/steering/`, `.amazonq/rules/` | repo, rendered | Cline, Roo Code, Continue, Kiro, Amazon Q Developer |
| `.junie/guidelines.md`, `.aiassistant/rules/`, `.trae/rules/`, `.openhands/microagents/repo.md`, `.goosehints`, `.aider.conf.yml` | repo, rendered | JetBrains Junie, JetBrains AI Assistant, Trae, OpenHands, Goose, Aider |
| `.cursor/commands/`, `.windsurf/workflows/`, `.github/prompts/`, `.gemini/commands/pico/`, `.opencode/command/` | repo, rendered | The seven slash commands in each tool |
| `.mcp.json`, `.cursor/mcp.json`, `.vscode/mcp.json`, `.gemini/settings.json` | repo | MCP clients over stdio |
| `tools/http_server.py`, `Dockerfile`, `adapters/http/openapi.json` | wherever it is hosted | Custom GPT Actions, n8n, Zapier, Make, Dify, remote MCP connectors |
| `adapters/http/github-dispatch.openapi.json` | GitHub API | Writes from tools that only make HTTP calls, through the ingest workflow |
| `adapters/portable-control-layer.md` | generated, dated | ChatGPT, custom GPTs, Grok, Claude.ai Projects, any chat window |
| `adapters/consuming-repo/` | copy into the Pico product repo | Any agent editing product copy |
| `adapters/codex/` | copy to `~/.codex/` | Codex prompts and MCP config |

## Related engagements
- Counsel review of the partner terms: week 5, budgeted $1,000 (D50).
- ScoreApp setup for both scorecards. Sales Navigator for LinkedIn research, messages sent by hand.
- Pricing and legal questions not settled here: `ops/decisions.md`, "Open, owned elsewhere".

## What this repo distills
`context/Pico_GTM_Master_Context.md` is the single distilled source. When a source artifact changes, reflect it in the relevant `rules/` ledger, then the master context, then here.
