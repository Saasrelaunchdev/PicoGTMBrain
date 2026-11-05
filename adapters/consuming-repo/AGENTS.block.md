<!-- pico-gtm-brain:begin -->
## Pico go-to-market

The Pico go-to-market lives at `gtm-brain/`, a git submodule of PicoGTMBrain. It is the source of truth for positioning, messaging, claims, status, and voice. Do not restate strategy from memory when the brain settles it.

Before any customer-facing text, including dashboard strings, emails, listing copy, docs, and release notes, in this order:

1. `gtm-brain/AGENTS.md`, the router.
2. `gtm-brain/rules/feature-status.md`
3. `gtm-brain/rules/do-not-say.md`
4. `gtm-brain/rules/writing-rules.md`

Pick the audience before writing. Merchants and implementers are never blended.

Run `python3 gtm-brain/tools/brain.py lint <file>` on every changed string file and fix every error. When a change ships a capability, update `gtm-brain/rules/feature-status.md` in the same pull request, before the copy.
<!-- pico-gtm-brain:end -->
