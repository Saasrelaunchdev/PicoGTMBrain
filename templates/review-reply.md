# Template, App Store review reply

Audience: merchants, and every merchant who reads the reply. Stage 6. Reply to every review within 2 business days. Never incentivize a review.

## Shape
1. **Thank them by store or name,** as shown on the review.
2. **Restate the specific point** in one sentence, their words where possible.
3. **The honest answer.** If it is a limit, name it: "Pico answers product questions, not order questions." If it is a bug, say what is being fixed and when, only if known.
4. **One next step.** Where to reach us: us@picofinds.com.

## For a critical review
- Never argue, never blame the merchant's theme or setup.
- Never name a competitor or describe what a Shopify tool lacks.
- If the review describes something wrong in an answer, state the stock and sync facts plainly: cards come from the synced catalog, stock as of the last sync.

## After replying
Log the review as a signal in `ops/signal-log.md` with the reviewer's words verbatim, and add a `review.received` event with the rating.

Guardrails: merchants only, no incentive, no outcome claims, `rules/do-not-say.md`, `ops/QA-checklist.md` before posting.
