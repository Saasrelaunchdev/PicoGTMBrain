# Feature status ledger

Governs what can be promised. Update this file the moment status changes, before any copy follows.
Legend: SHIPPED (live now, present tense). PARTIAL (say what works today). IN BUILD (decided, unshipped: "coming soon", or omit). ROADMAP (vision, never a launch claim). OUT (out of scope by decision, never claimed).
last_reviewed: 2026-11-04
Source: the Pico Core Features Overview (2026-11-02) and the decision log. Week 1 starts 2026-11-09.

## Shopper widget
- Natural language requests, matched by keywords, synonyms, and price range: SHIPPED.
- Product cards with image, name, price, stock label, View link: SHIPPED.
- Add to cart from the card, in-stock variant picked, out-of-stock blocked: SHIPPED.
- One clarifying question for vague requests, suggested reply chips: SHIPPED.
- Product comparison inside a reply: SHIPPED. A comparison screen: ROADMAP.
- Replies in the shopper's language, switcher, Arabic right to left, widget text in 10 languages: SHIPPED. Translation of catalog text: OUT.
- Personalized welcome, session memory across a reload on one device: SHIPPED. Cross-device memory or order-history personalization: OUT.
- Semantic or vector search: ROADMAP. Proactive prompts on product pages: ROADMAP.

## Merchant dashboard
- Overview, 30 days against the prior 30, with sync health: SHIPPED. Revenue attribution: ROADMAP.
- Analytics: discovery funnel, top phrases, zero result and weak click phrases, product impressions: SHIPPED.
- Catalog sync on demand, retry, sync log, counts: SHIPPED.
- Assistant voice controls, tone guidelines up to 1,000 characters, preview: SHIPPED.
- Plan & Usage: quota meter, upgrade, cancel with a reason, 50% retention offer for two periods: SHIPPED.
- Quota alerts at 80% and 100%, 10% grace on paid plans, launcher pause, no overage: IN BUILD.
- Published conversation definition on the plan page and listing: IN BUILD.
- Roles: owner, admin, analyst, support: SHIPPED. Multi-store agency workspace: ROADMAP, built when 10 partners each have 3 or more active paying stores.
- Every feature on every plan: SHIPPED, and kept that way.

## Setup and platform
- Shopify OAuth install, theme app embed, four-step checklist: SHIPPED.
- Shopify App Store listing and Shopify Billing: IN BUILD. Submit week 1, live target week 3, buffer to week 6.
- Theme coverage: claimed through the theme app embed only. Tests on Dawn and Horizon: IN BUILD. Headless (Hydrogen): OUT, not claimed.
- Speed: measured Lighthouse difference on Dawn, budget 10 points, published on the technical one-pager: IN BUILD (week 1). "No impact": OUT.
- Inventory webhook subscription: IN BUILD (week 1). Until it ships, copy says "Stock as of your last catalog sync".
- Sandbox store, setup skill for Cursor, Claude Code, Codex, Antigravity: SHIPPED.
- Shopware 6 and custom catalog API: SHIPPED in the product, OUT of both go-to-markets (deferred third run).
- EGP pricing by InstaPay: SHIPPED for non-Shopify stores, OUT of both go-to-markets.

## Plans and billing
- Free 50, Growth $49 for 600, Pro $99 for 2,000, 14 day Growth trial with no card: SHIPPED.
- Yearly at two months free: $490, $990, $2,990: IN BUILD.
- Scale, $299 for 6,000 with an onboarding call, and custom plans above it: IN BUILD.
- Founding cohort discount, 50% for 6 billing periods by Shopify Billing subscription discount: IN BUILD (opens 2026-12-01).
- Paid plans free for testing on partners' development stores: IN BUILD (switched on at launch).

## Lifecycle build list
- Sync failure email: IN BUILD (week 2). First insight email and weekly summary: IN BUILD (week 4).
- Proof capture point at value realization: IN BUILD (week 6). Monthly usage summary: IN BUILD (week 8).
- Words against the catalog check, a public page: IN BUILD (week 10).

## Scope decisions
- Human handoff or live chat: OUT. Reopen if 5 of 20 founding stores ask, or 2 uninstall reasons in a month.
- Order status, returns, and policy answers: OUT by design. Pico is a pre-purchase assistant.
- WhatsApp and Instagram: OUT until the GCC opens.
- GA4 event export: ROADMAP, built with revenue attribution after the founding cohort. Klaviyo: ROADMAP.
- Holdout or A/B lift measurement: ROADMAP, the candidate that could answer lift claims honestly.

## Implementer program
- Paid Usability Sessions ($150) and interviews ($75): IN BUILD, posts from week 1, sessions from week 2.
- Case study permission forms and terms clause: IN BUILD (week 2).
- Partner page, 25% and 30% shares, 10% managed share, deal registration, payouts on the 15th: IN BUILD (week 6, after counsel review in week 5).
- Directory listing on picofinds.com/partners: IN BUILD, after a partner's first active paying store.
- Partner portal, tier badges, co-marketing, certification: ROADMAP. White label, cash bounties, client discounts at launch: OUT.

## Demo rule
Nothing marked IN BUILD, ROADMAP, or OUT may be screen-recorded, narrated, or shown as if a merchant could use it today. Label it on screen and in the script, or leave it out.
