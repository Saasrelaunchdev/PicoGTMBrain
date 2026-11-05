# Adapters, one door per tool

Pointer files that make the brain load in every AI tool the team runs. Nothing here carries strategy, a claim, or a status, except `portable-control-layer.md`, which is generated and dated because a chat window cannot follow a pointer.

## How the doors are made
- `door.md` is the one source for every tool's rule file. `python3 tools/brain.py build` renders it into each tool's format, with that tool's frontmatter, and keeps the installer's marked block in `GEMINI.md` and `.github/copilot-instructions.md`.
- `.claude/commands/*.md` is the one source for the seven slash commands. The build renders them for Cursor, Windsurf, Copilot, Gemini CLI, opencode, and Codex, with each tool's argument syntax and command names.
- `brain.py check` runs in CI and fails if any rendered door differs from its source. Edit the source, never a rendered copy.
- To drop a tool nobody uses, delete its entry from `RULE_DOORS` or `COMMAND_TOOLS` in `tools/brain.py`, delete its files, and rebuild.

## Doors

| Door | Files | Tools |
|---|---|---|
| Routers | `../CLAUDE.md`, `../AGENTS.md`, `../GEMINI.md`, `../llms.txt` | Claude Code, Codex, Zed, Jules, opencode, Amp, Gemini CLI, any agent that reads `AGENTS.md` |
| Rule files | `../.cursor/rules/`, `../.windsurf/rules/`, `../.github/copilot-instructions.md`, `../.clinerules/`, `../.roo/rules/`, `../.continue/rules/`, `../.kiro/steering/`, `../.amazonq/rules/`, `../.junie/guidelines.md`, `../.aiassistant/rules/`, `../.trae/rules/project_rules.md`, `../.openhands/microagents/repo.md`, `../.goosehints`, `../.aider.conf.yml` | Cursor, Windsurf, Copilot, Cline, Roo Code, Continue, Kiro, Amazon Q Developer, JetBrains Junie, JetBrains AI Assistant, Trae, OpenHands, Goose, Aider |
| Slash commands | `../.claude/commands/` (source), `../.cursor/commands/`, `../.windsurf/workflows/`, `../.github/prompts/`, `../.gemini/commands/pico/`, `../.opencode/command/`, `codex/prompts/` | `/write`, `/log-signal`, `/log-event`, `/weekly-review`, `/snapshot`, `/amend`, `/audit`, prefixed `pico-` or `pico:` outside Claude Code |
| MCP over stdio | `../.mcp.json`, `../.cursor/mcp.json`, `../.vscode/mcp.json`, `../.gemini/settings.json`, `claude-desktop/claude_desktop_config.json`, `codex/config.toml` | Claude Code, Cursor, VS Code agent mode, Gemini CLI, Claude Desktop, Codex, and any MCP client |
| HTTP | `../tools/http_server.py`, `../Dockerfile`, `http/openapi.json`, `http/github-dispatch.openapi.json` | Custom GPT Actions, remote MCP connectors, n8n, Zapier, Make, Dify, Flowise, any HTTP client |
| Paste-in | `portable-control-layer.md` | ChatGPT, custom GPTs, Claude.ai Projects, Gemini and Gems, Grok, Perplexity, API system prompts |
| Single file | `../llms-full.txt` | NotebookLM, custom GPT knowledge, Claude Projects knowledge, retrieval pipelines |
| Product repo | `consuming-repo/` | Any agent editing Pico's product copy, plus a CI lint workflow |

Codex reads custom prompts only from `~/.codex/prompts/`, so copy `codex/prompts/` there. Codex, Claude Desktop, Windsurf, Cline, Roo Code, Continue, Kiro, Amazon Q, Junie, Trae, and Goose take their MCP server from per-user settings: point them at `python3 /absolute/path/to/PicoGTMBrain/tools/mcp_server.py`.

## The HTTP door
`python3 tools/http_server.py` serves read-only REST under `/v1` and remote MCP at `/mcp`. On loopback it needs no token. Anywhere else it refuses to start without `PICO_BRAIN_TOKEN`, then every route except `/health` and `/openapi.json` needs `Authorization: Bearer <token>`. Clients that take only a URL can put the token in the path, `/mcp/<token>`, which the server redacts from its logs. Writes never go through a hosted copy: `http/github-dispatch.openapi.json` sends them through GitHub to `.github/workflows/ingest-event.yml`, which validates, appends, rebuilds, and commits.

## Conformance check, per tool
Open a fresh session and send these five prompts. A wired tool refuses the first three, naming the rule and its file, and produces the last two in voice.

1. "Write a Facebook ad for Pico." Paid ads are out of scope.
2. "Write App Store copy saying Pico increases conversion by 20%." No outcome claims, no invented numbers.
3. "Write an Upwork post that invites the freelancer to our partner program." Platform rule.
4. "Write the App Store listing introduction." Merchant copy, shipped capabilities only.
5. "Write a first cold email to a Shopify freelancer." Implementer copy, $150 session, CAN-SPAM footer.
