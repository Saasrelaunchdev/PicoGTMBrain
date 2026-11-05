# Thin wrappers around tools/brain.py. Python 3.9+, no dependencies.
PY ?= python3

.PHONY: build check audit test lint metrics tripwires ledger mcp http docker ci

build:        ## regenerate data/, llms-full.txt, the portable layer, the ledger, every tool door, the HTTP specs
	$(PY) tools/brain.py build

check:        ## fail if any generated file is stale
	$(PY) tools/brain.py check

audit:        ## the vendored skill audit plus schema, freshness, and example checks
	$(PY) tools/brain.py audit

test:         ## unit tests for the CLI, the doors, the MCP server, and the HTTP server
	$(PY) -m unittest discover -s tools/tests -v

lint:         ## lint a draft: make lint FILE=draft.md
	$(PY) tools/brain.py lint $(FILE)

metrics:
	$(PY) tools/brain.py metrics

tripwires:
	$(PY) tools/brain.py tripwires

ledger:
	$(PY) tools/brain.py ledger

mcp:          ## serve the brain over MCP on stdio
	$(PY) tools/mcp_server.py

http:         ## serve REST and remote MCP on http://127.0.0.1:8765, read only
	$(PY) tools/http_server.py

docker:       ## build the read-only HTTP image
	docker build -t pico-gtm-brain .

ci: check audit test
