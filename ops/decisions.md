# Decision log

What was decided and why, so settled strategy is not relitigated. Newest at the top. Decision IDs (D1 to D56) are stable identifiers from the GTM build on 2026-11-03: cite them in commits, signals, and experiments. Every entry carries its reopen trigger, which `innovation/tripwires.json` encodes so the accounting layer can flag it automatically.

Types: **Decision** is a call Pico controls. **Researched** is a sourced fact. **Assumption** is a planning number nobody publishes, never used in customer copy, measured where it says.

---

## 2026-11 This repository is the go-to-market source of truth (DECIDED)
**IDs:** B1. Decided 2026-11-04.
The PicoGTMBrain repository holds the governed go-to-market for both audiences. Strategy, claims, status, and voice are changed here first, in the order ledger, master context, decision log, copy. `CLAUDE.md` wins if the routers disagree.
The GTM build produced dashboards, a walkthrough, and a Google folder. Those are deliverables. This repo is the operating system that keeps them true.
**What this does not change:** any decision below, any price, any target, any channel.
**Downstream:** the Google folder documents and the walkthrough are regenerated from this repo's ledgers when a ledger changes. Owner: founder.
**Reopen when:** never.

## 2026-11 Launch calendar and build list (DECIDED)
**IDs:** D56 and the launch calendar. Decided 2026-11-03.
Week 1 starts Monday 2026-11-09. Build order: inventory webhook (week 1), sync failure email (2), first insight email and weekly summary (4), partner ledger, payout run, and proof capture point (6), monthly usage summary (8), the words against the catalog check (10). The founding cohort opens 2026-12-01, after Cyber Monday. Day 60 review in week 12, day 90 review in week 13.
Each item is the touch-point for one funnel stage, sequenced so sync works before installs and partner tooling before the partner page.
**What this does not change:** prices, the partner terms, the channels.
**Reopen when:** an item slips by more than two weeks. The founder and engineer move the next block's scope.

## 2026-11 Planning bands where trackers are silent (DECIDED)
**IDs:** D53, D54, D55. Decided 2026-11-03.
Merchant Level 1: 100 or more products, 10,000 to 100,000 monthly sessions, 1 to 10 people, about $150,000 to $3 million a year. Level 2: 250 or more products, 100,000 to 1 million sessions, 10 to 50 people. 2% of sessions start a conversation (Assumption). Implementer Level 1: 1 to 5 people, under $250,000, 2 to 10 client stores. Level 2: 6 to 50 people, $1 million to $20 million, 10 to 100 client stores (Assumption).
Catalog cutoffs are researched (StoreLeads, 2026: 28.2% of stores sell 100 or more products). Sessions decide the band, because order values differ.
**What this does not change:** any customer copy. Bands never appear in copy.
**Reopen when:** the founding cohort's intake answers and first 30 days of conversations, and the first 30 session applications.

## 2026-11 Legal and platform conduct (DECIDED)
**IDs:** D47 to D52. Decided 2026-11-03.
A US private mailbox in Pico's name is the postal address on every commercial email from week 1. Cold email goes to US recipients only in the first 90 days, then UK companies and LLPs only, never UK sole traders, never cold to the EU. Sessions found on a platform are paid on that platform, and no partner invitation goes inside Upwork or Fiverr. Counsel reviews the partner terms in week 5. Permission forms and a terms clause are ready in week 2. Invoice-paid implementers sign a session agreement and give a W-9 or W-8BEN.
CAN-SPAM needs a postal address and an opt-out. PECR treats sole traders as individuals. Fiverr bars steering off the platform, and Upwork's term covers payments for 24 months.
**What this does not change:** the fee, the shares, the channel mix.
**Reopen when:** counsel advises otherwise, or either platform changes its terms.

## 2026-11 Listing, reviews, targets, and feedback cadence (DECIDED)
**IDs:** D42 to D46. Decided 2026-11-03.
The listing is "Pico AI Shopping Assistant" in the Chat category, search terms AI shopping assistant, product finder, product discovery. Screenshots lead with the Shopper Words Test, then cards, then Analytics, then the plan page. Reviews are asked for only after the merchant has opened Analytics and made one fix, replies within 2 business days, no incentives. Merchant and implementer 90-day targets are in `innovation/metrics.json`. Founding merchants get a monthly 30-minute call, partners a quarterly call and a digest after each batch of 10 sessions.
Merchants compare chat apps first, and the first reviews set the listing's tone.
**What this does not change:** the conversation definition or any price.
**Reopen when:** listing visit to install falls below 2% at day 30, or call attendance falls below half.

## 2026-11 Partner program terms and operations (DECIDED)
**IDs:** D35, D36, and D38 to D41. Decided 2026-11-03.
25% of each referred store's subscription charges for 24 months, 30% for lead partners at 5 active paying stores, 10% managed share, one share per store, no cash bounty. Payouts monthly on the 15th for charges Shopify paid out the prior month, $50 minimum carried forward, PayPal or bank transfer. Attribution by deal registration on the myshopify domain, merchant-confirmed, valid 90 days. Referral traffic is routed setup requests, never a promised volume. No separate agency price. The partner page goes live in week 6.
Above the 20% floor that Gorgias and Shopify set. A recurring share pays only while the store pays.
**What this does not change:** merchant prices, and Shopify Billing charging each store.
**Reopen when:** 12 months in, partner-referred stores pass 25% of paying stores, 2 attribution disputes in a quarter, or 50 routed requests a month.

## 2026-11 Paid sessions, interviews, and the session cohort (DECIDED)
**IDs:** D33, D34, D37. Decided 2026-11-03.
$150 for a fixed scope of up to 90 minutes: sandbox, install on a development or permissioned client store, the Shopper Words Test, timed setup, feedback form. Pico pays platform fees. Optional $75 interview for 30 minutes. 30 sessions in 60 days from week 1: Upwork 15, Fiverr 5, email 6, LinkedIn 4.
About $100 an hour, inside the research incentive range for engineers and above the roughly $100 gig for installing an AI chat app.
**What this does not change:** the partner terms.
**Reopen when:** fewer than 10 qualified applicants per Upwork post (raise to $200), fewer than half accept the interview, or day 30 completion rates by channel.

## 2026-11 The 90-day budget and the runway gate (DECIDED)
**IDs:** D31, D32. Decided 2026-11-03.
$9,000 over 90 days, capped at $3,000 a month: sessions $4,984, interviews $1,215, ScoreApp and Sales Navigator $477, sending domain and US mailbox $180, counsel $1,000, held back $1,144. Spend is released in 30-day blocks, each needing 6 months of company runway after it. If a block fails, paid sessions pause and outreach continues on email, LinkedIn, and the scorecard.
**What this does not change:** company burn, which sits outside the plan.
**Reopen when:** each 30-day block, and the day 90 review.

## 2026-11 The founding cohort (DECIDED)
**IDs:** D30. Decided 2026-11-03.
20 US stores, 50% off any paid plan for 6 billing periods through a Shopify Billing subscription discount, a monthly feedback call, a direct line to the founder, roadmap input. A written case study request at day 60. Opens 2026-12-01 and closes at 20 stores or 90 days after the listing goes live.
**What this does not change:** list prices.
**Reopen when:** it fills before day 60: open a second cohort of 20.

## 2026-11 Pricing structure (DECIDED)
**IDs:** D26 to D29. Decided 2026-11-03.
Yearly plans give two months free: Growth $490, Pro $990, Scale $2,990. Scale is $299 a month for 6,000 conversations with an onboarding call, and custom plans above it at about $0.05 a conversation. Model cost ceiling $0.02 a conversation (Assumption), which puts gross margin before other costs at 76% on Growth and 60% on Pro and Scale. Month 6 target mix: Free 60% of active installs, paying stores 70% Growth, 22% Pro, 8% Scale.
**What this does not change:** Free, Growth, and Pro monthly prices.
**Reopen when:** fewer than 10% choose yearly by month 6, 3 stores request a custom plan, measured model cost exceeds the ceiling in the first 30 days of logs, or the month 6 mix review.

## 2026-11 What a conversation is, and what happens at the quota (DECIDED)
**IDs:** D24, D25. Decided 2026-11-03.
A conversation is a chat thread with at least one AI reply, counted once per shopper and device per 24 hours, fair use 50 AI replies. At the quota: alerts at 80% and 100%, open conversations finish, paid plans get 10% grace at no charge, then the launcher pauses until the next cycle or an upgrade. No overage charge, ever.
Billing surprise is the category's most frequent complaint class, so a capped quota becomes a positioning line once it ships.
**What this does not change:** the plan prices.
**Reopen when:** 3 support tickets about the definition in a month, or pauses drive more than 20% of uninstall reasons.

## 2026-11 One value metric, development stores, and the workspace trigger (DECIDED)
**IDs:** D21, D22, D23. Decided 2026-11-03.
Every feature is on every plan, and plans differ only in conversations a month. Paid plans are free for testing on partners' development stores. The multi-store workspace is built when 10 partners each have 3 or more active paying stores, and until then a partner takes the admin role on each store.
**What this does not change:** one store per plan.
**Reopen when:** a feature needs gating to protect margin, or the workspace trigger fires.

## 2026-11 Product claims: themes, headless, speed, stock, catalog text (DECIDED)
**IDs:** D16 to D20. Decided 2026-11-03.
Theme claims cover Online Store themes through the theme app embed, tested on Dawn and Horizon before launch. Headless is not claimed. Speed budget 10 Lighthouse points on Dawn, measured in week 1 and published, never "no impact". Stock copy is "Stock as of your last catalog sync" until the inventory webhook ships. No claim that Pico translates catalog text.
**What this does not change:** the install path or the checklist.
**Reopen when:** a theme issue appears in 2 sessions, a Hydrogen store passes a session, the speed test fails the budget, or the webhook ships.

## 2026-11 Launch scope: handoff, orders, channels, integrations (DECIDED)
**IDs:** D12 to D15. Decided 2026-11-03.
Human handoff is not built or claimed. Order, return, and policy answers are out of scope by design. WhatsApp and Instagram wait for the GCC. The first integration is a GA4 event export, built with revenue attribution after the founding cohort.
Positioning against chat apps rests on not trying to answer everything.
**What this does not change:** the shopper widget's shipped capabilities.
**Reopen when:** 5 of 20 founding stores ask for handoff or order answers, or 2 uninstall reasons cite them in a month, or the GCC opens, or the founding cohort closes.

## 2026-11 Geography: USA first, the GCC on a trigger (DECIDED)
**IDs:** D11, owner decision 3. Decided 2026-11-03.
Global, USA first. The GCC opens when the US founding cohort is full and at least 5 GCC stores have asked for Pico in one quarter. Until then GCC material is reference only.
**What this does not change:** Arabic right to left as a shipped feature line.
**Reopen when:** the trigger fires: size the GCC and review messaging channels.

## 2026-11 Two standalone go-to-markets, slates stand, Shopware deferred (DECIDED)
**IDs:** D9, D10, owner decisions 5 and 8. Decided 2026-11-03.
Merchants and implementers each get a standalone go-to-market. Both competitor slates stand as built. Shopware 6 and custom stores wait for a deferred third run, and EGP prices appear in no merchant or implementer asset.
**What this does not change:** Shopware 6 and the custom catalog API as shipped product.
**Reopen when:** a slate slot fails its page-loaded check, or the third run starts.

## 2026-11 Operating basis and pre-launch state (DECIDED)
**IDs:** D5 to D8. Decided 2026-11-03.
An Egypt-based team selling in USD worldwide (Researched). Founder-led, two people (Assumption). No channel tried with results, and no installs, stores, payers, or rating recorded (Researched).
**What this does not change:** anything customer-facing. The team basis sizes timeframes only.
**Reopen when:** the team grows, the listing goes live, or the first 30 days of results arrive.

## 2026-11 Open proof, never invented proof (DECIDED)
**IDs:** D4, owner decision 2. Decided 2026-11-03.
The customer proof log is empty and closed. Every proof slot carries open proof: an invitation to check a claim now, naming what and where. A case study enters only with exact wording, a source, and recorded permission from everyone it names.
**What this does not change:** the narrowed claims, which still govern every line.
**Reopen when:** the first case study has recorded permission: it replaces the open proof line in its drill.

## 2026-11 Website and listing (DECIDED)
**IDs:** D1, D2, D3. Decided 2026-11-03.
Website: picofinds.com. The listing is submitted in week 1 as "Pico AI Shopping Assistant", live target week 3, buffer to week 6. Until it is live, every merchant call to action is "Connect your store". The site is aligned with the US-first plan before the first implementer email: Shopify and English first, Shopware on its own page, three broad lines replaced, new headline "An AI shopping assistant for Shopify that answers from your own catalog."
**What this does not change:** implementer sessions, which run on development stores and need no approved listing.
**Reopen when:** the listing is approved: every call to action switches to the listing.

---

## Open, owned elsewhere
- **Approve the six examples in `examples/` as voice references.** Owner: founder. Until approved they are proposed gold standards, five built only from copy-bank lines and the sync failure email written as the brain's live test on 2026-11-05.
- **Tone anchors.** Two brands whose voice is right for Pico, two that are wrong. Owner: founder.
- **Which AI tools the team runs.** Doors ship for 19 tools with their own file, for agents that read `AGENTS.md` such as Zed, Jules, and Amp, for MCP and HTTP clients, and for chat windows, rendered from one source, so a stale door fails CI instead of drifting. Prune the ones nobody uses from `RULE_DOORS` and `COMMAND_TOOLS` in `tools/brain.py`. Owner: founder.
- **Company runway and burn.** Outside the plan, read by the runway gate (D32). Owner: founder as CFO.
- **Counsel's review** of the partner terms, the session brief, and the platform conduct rules, week 5 (D50).
- **Shopware 6 connection wording.** The source says "Admin API access keys, optional sales channel key" in one place and "Admin API and Store API" in another. A status question for the third run.
- **Corroboration thresholds and ledger owners,** set to defaults in `ops/review-cadence.md` on 2026-11-04. Confirm or change.
