# Signal log

Raw market input, captured before judgment. Every signal from a merchant, implementer, prospect, reviewer, competitor, platform, or channel lands here first, whatever it turns out to mean. Newest at the top. Each entry is mirrored as a `signal.logged` event in `innovation/events/` by `python3 tools/brain.py signal`, which is how signals reach the innovation accounting layer.

**Keep the verbatim.** Do not paraphrase a merchant or implementer into house vocabulary. Their words, before we taught them ours, are the most valuable thing a signal carries.

## How to use this file

**Types:** OBJECTION, LANGUAGE, PROOF, STATUS, COMPETITIVE, SEGMENT, CHANNEL, LOSS, RISK.

**Dispositions:**
- `NOISE`, one instance, no pattern, no action. Logged and closed.
- `WATCH (n/N)`, a plausible pattern awaiting corroboration. Increment as instances arrive.
- `PATCH`, changes copy but not strategy. Route it, edit, done. No decision entry.
- `AMEND`, changes a ledger, a position, or a rule. Follow the amendment procedure and write an `ops/decisions.md` entry.

**Corroboration thresholds** (defaults agreed 2026-11-04, see `ops/review-cadence.md`):

| Signal class | Threshold to act |
|---|---|
| Opinion, preference, language, objection | 3 independent instances within 60 days |
| Verifiable fact: status, proof, competitive, risk | 1 verified instance, act immediately |
| Loss reason, uninstall reason | 2 instances, or 1 if the store was a founding cohort store |
| Channel performance | A full measurement cycle, never a single week |
| Decision reopen trigger | The exact threshold in the decision's "Reopen when" line |

Default disposition is NOISE. A brain that amends on every input has no memory.

Triage runs every Monday. A WATCH item that has not incremented in two cycles expires to NOISE, and the expiry is written here.

---

## Entries

Entries dated 2026-11-03 are the seed entries from the research pass, before launch: market evidence, not customer conversations, and already routed.

### 2026-11-05 | RISK | brain live test, lifecycle-email load set
**Verbatim:** "Drafting the sync failure email, the brain could not say what shoppers see while a sync has failed or only partly finished, whether the sync log shows the cause of a failure, or where a merchant goes after a retry fails."
**Context:** Live test of the brain on 2026-11-05. The email in examples/sync-failure-email.md writes around all three gaps. Its trigger ships in week 2.
**Disposition:** PATCH
**Routed to:** Engineer: answer the three in rules/feature-status.md before the week 2 trigger ships, then update templates/lifecycle-email.md and examples/sync-failure-email.md
**Tags:** live-test, sync-failure

### 2026-11-03 | STATUS | App Store search, picofinds.com
**Verbatim:** "No Pico listing found in the Shopify App Store index."
**Context:** Pre-launch. Affects every merchant call to action.
**Disposition:** AMEND
**Routed to:** `rules/feature-status.md` (listing IN BUILD), `ops/decisions.md` (D2), `ops/copy-bank.md` (CTA "Connect your store" until live)

### 2026-11-03 | RISK | picofinds.com homepage
**Verbatim:** "only recommends what is in stock", "Checks live stock", "Never invents stock, prices, or capabilities"
**Context:** Three site lines broader than the product supports. The first review showing an out-of-stock card could quote them.
**Disposition:** AMEND
**Routed to:** `rules/do-not-say.md` (hard bans with replacements), `ops/decisions.md` (D3)

### 2026-11-03 | LANGUAGE | Shopify App Store reviews across the merchant slate
**Verbatim:** Pricing or billing surprise was the most frequent complaint class, 16 or more reviews seen in indexed snippets.
**Context:** Merchants evaluating chat apps, stage 3.
**Disposition:** AMEND
**Routed to:** `ops/decisions.md` (D25 no overage), `ops/copy-bank.md` (pause line, tagged IN BUILD)

### 2026-11-03 | LANGUAGE | Shopify App Store review of the Inbox agent
**Verbatim:** A reviewer reported inaccurate product information and asked for visibility into where answers came from.
**Context:** One review. Supports positioning vector 4, answers traceable to the catalog.
**Disposition:** WATCH (1/3)
**Routed to:** none yet. Two more independent instances promote it to the value proposition

### 2026-11-03 | COMPETITIVE | Shopify Fall '26 Edition
**Verbatim:** The Inbox agent gives personalized recommendations, starts checkout from the chat, and reaches staff.
**Context:** The free native default every merchant weighs Pico against, on about 358,000 stores.
**Disposition:** AMEND
**Routed to:** `reference/competitor-battlecards.md`, `rules/do-not-say.md` (never disparage, never compare to Shopify tools)

### 2026-11-03 | COMPETITIVE | Shopify Search & Discovery documentation
**Verbatim:** "Searches with no results" and "Searches with no clicks" are reported for the search bar.
**Context:** Narrows Pico's insight claim to requests made to the assistant.
**Disposition:** AMEND
**Routed to:** `rules/glossary.md` (distinction), `rules/do-not-say.md` (scoping drill)

### 2026-11-03 | CHANNEL | Upwork and Fiverr terms of service
**Verbatim:** Upwork: payments for a relationship found there stay on Upwork for 24 months unless a conversion fee is paid. Fiverr: no off-platform payment, steering, or contact sharing.
**Context:** Shapes how a partnership can start with implementers met on marketplaces.
**Disposition:** AMEND
**Routed to:** `ops/decisions.md` (D49), `reference/outreach-engine.md`, `ops/QA-checklist.md`

### 2026-11-03 | SEGMENT | 26 sampled agency stack pages
**Verbatim:** No AI shopping assistant listed on any of the 26 pages. Klaviyo on 17, Gorgias on 13.
**Context:** Implementer Level 1 and Level 2. The status quo is offering nothing.
**Disposition:** PATCH
**Routed to:** `reference/positioning.md` (implementer statement 3)
