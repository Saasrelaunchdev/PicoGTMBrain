# Pico GTM: the decision log

Every open decision and every unknown-value placeholder in this build, resolved on 2026-11-03 at the owner's request. Each line names the role that owns it, the call, the reason, and the measurement that reopens it. Research behind the calls is in `research/2026-11-03-tbd-resolution-research.md`.

## How to read it

Three kinds of resolution, labelled everywhere they are used:

| Label | Meaning | Example |
|---|---|---|
| **Decision** | A call Pico controls: a price, a rule, a scope, a date. True once Pico does it | Growth costs $490 a year |
| **Researched** | A fact found and sourced, with the date checked | 28.2% of Shopify stores sell 100 or more products (StoreLeads) |
| **Assumption** | A planning number nobody publishes. It is used for sizing and budgets, never in customer copy, and each one names where it gets measured | 2% of sessions start a conversation |

**What did not change.** No testimonial, customer, install count, rating, review, quote, or outcome was created. Customer proof still enters only under the intake rule in `GTM-BRIEF.md` Section 5. The narrowed claims still govern copy, Shopify is still never disparaged, and every vendor fact still carries a URL and a date. Owners are roles. On a founding team one person holds several.

**Two placeholder strings stay on purpose,** both in text this build does not own: one in the vendored skill file, `.claude/skills/gtm-builder/SKILL.md`, which is the skill's own instruction, and one in the owner's source document, `source/2026-11-02-pico-core-features-overview.md`, which is never edited.

## The eight open decisions from the brief

| # | Brief decision | Closed by |
|---|---|---|
| 1 | Website and App Store listing | D1, D2, D3 |
| 2 | The proof set | Owner, then D4 |
| 3 | Target geography | Owner: global, USA first. D11 for the GCC |
| 4 | The Run 2 offer | Owner outline, then D33 to D41 |
| 5 | Shopware 6 | Owner: deferred. D9 |
| 6 | Status of C5 to C8 | D12 to D15 |
| 7 | Pricing gaps | D24 to D29 |
| 8 | The slates | Owner. D10 |

---

## CEO: scope, identity, and sequence

| ID | Decision | Type | Why | Reopen when |
|---|---|---|---|---|
| D1 | **Website: picofinds.com** | Researched | The live site's footer gives us@picofinds.com, and the project is named PicoFinds (owner's screenshots, 2026-11-03) | Never, unless the domain changes |
| D2 | **App Store listing: not live on 2026-11-03. Submit in week 1 as "Pico AI Shopping Assistant", plan for it live in week 3, with a buffer to week 6.** Until it is live, every merchant call to action is the site's own "Connect your store" button on picofinds.com. Run 2's paid sessions start in week 1 on development stores, which need no approved listing | Decision | No listing was found in the App Store index. Shopify staff quote 5 to 10 business days for review, and 2026 forum reports run to 30 days. The full name separates Pico from "Piko ‑ Pickup Reminder" | The listing is approved: every call to action switches to the listing |
| D3 | **Align the website with the US-first plan before the first Run 2 email.** Lead with Shopify and English. Arabic stays a feature line. Shopware moves to the existing "For Shopware merchants" page. The region selector defaults to the visitor's country. Three lines are replaced: "only recommends what is in stock" becomes "Shows stock on every card, and keeps out-of-stock items out of the cart." "Checks live stock" becomes "Stock as of your last catalog sync." "Never invents stock, prices, or capabilities" becomes "Product cards show names, prices, and stock from your synced catalog." New headline: "An AI shopping assistant for Shopify that answers from your own catalog." | Decision | The site leads with Shopware, Arabic, and Egypt, and three of its lines are broader than the source supports. The first review that shows an out-of-stock card could quote the homepage | A US visitor test shows the new hero underperforms |
| D4 | **Proof fields are filled with open proof, never invented proof.** In both runs, each copy drill's Social Proof headline becomes an Open Proof headline: an invitation to check the claim now, in the sandbox, on the plan page, or in Shopify's own documentation. Each Supporting Proof Point names a checkable artifact and where to check it. The customer proof set stays empty until the intake rule admits a row | Decision | The owner closed the proof set, then asked for every field to be filled. Open proof fills the field with something true that the reader can verify in under a minute | The first case study clears the intake rule: it replaces the open proof line in its drill |
| D5 | **Operating base: an Egypt-based team selling in USD worldwide, USA first** | Researched | The source's EGP and InstaPay billing rail, and the site's default region, Egypt, with Egypt first in its footer | Never for the GTM. Only the postal address (D47) and the payout entity depend on it |
| D6 | **Team planning basis: founder-led, two people.** The founder is CEO and runs go-to-market, partnerships, and content. One engineer runs product and setup support. Design and video are contracted by the asset | Assumption | The source names no team. Every asset timeframe in both libraries is sized to this basis | The team is larger: timeframes shrink, nothing else changes |
| D7 | **Channels tried: none with recorded results, pre-launch** | Researched | No listing found, and the source records no customer or channel result. The brief asks for this exact answer when nothing has been tried | The first 30 days of results replace it |
| D8 | **Installs, active stores, paying stores, rating: none recorded, pre-launch** | Researched | Same evidence as D7 | The listing goes live |
| D9 | **Shopware 6 and custom stores stay in a deferred Run 3. EGP prices appear in no Run 1 or Run 2 asset**, and the site's Egypt pricing stays as the owner published it | Decision | Owner decision 5. Shopify installs bill in USD through Shopify Billing, so EGP has no role in either run | Run 3 starts |
| D10 | **Both slates stand as built** | Decision | Owner decision 8 | A slot fails its page-loaded check |
| D11 | **The GCC opens when the US founding cohort is full and at least 5 GCC stores have asked for Pico in one quarter.** Until then GCC sheets stay for reference, and their unfilled counts are out of scope | Decision | Owner: the GCC is for later. A trigger makes "later" a date someone can see coming | The trigger fires: run Step 0.E again and size the GCC |

## CPO and CTO: product scope and what copy may say

| ID | Decision | Type | Why | Reopen when |
|---|---|---|---|---|
| D12 | **C5, human handoff: not built, not claimed, not in launch scope.** Copy: "Pico answers product questions. Keep your help desk for orders and people." | Decision | The source is silent, so it is treated as absent. Merchants already run Inbox or a help desk | 5 of the 20 founding stores ask for it, or it appears in 2 uninstall reasons in one month |
| D13 | **C6, order status, returns, and policy answers: out of scope by design.** Pico is a pre-purchase assistant, and copy says so | Decision | Positioning against chat apps rests on not trying to answer everything (Dashboard 3) | The same trigger as D12 |
| D14 | **C7, WhatsApp and Instagram: not in scope** | Decision | They matter most in the GCC, which is for later | The GCC opens (D11) |
| D15 | **C8, marketing integrations: not in launch scope. The first one is a GA4 event export, built with revenue attribution (C1)** after the founding cohort | Decision | Both need the same event model, and neither is a launch blocker | The founding cohort closes |
| D16 | **Themes: claims cover Online Store themes through the theme app embed. Pre-launch tests on Dawn and Horizon, Shopify's free reference themes.** Rendering issues found in paid sessions are fixed and listed on the technical one-pager | Decision | Shopify documents app embeds on vintage and Online Store 2.0 themes (Step 0.F). Whether Pico renders cleanly on each theme is tested, not assumed | A theme issue appears in 2 sessions |
| D17 | **Headless (Hydrogen): no theme embed, so not claimed.** The catalog syncs through the normal Shopify install, and a developer places the custom-store widget script in the Hydrogen layout. Untested | Decision | Theme app embeds do not reach Hydrogen storefronts. StoreLeads detects Hydrogen on 901 US stores | One Hydrogen store passes a paid session: the one-pager adds it |
| D18 | **Speed budget: no more than 10 Lighthouse performance points**, measured on Dawn with and without Pico in week 1, with the measured number published on the technical one-pager. Copy never says "no impact" | Decision | Built for Shopify requirement 2.2.1 sets the same 10-point line | The test fails the budget: the widget is fixed before launch |
| D19 | **Stock wording: "Stock as of your last catalog sync" in every asset.** Subscribing to Shopify's inventory webhook is a launch requirement for engineering. "Updated by webhook on Shopify" enters copy only once it ships | Decision | The source names webhooks for Shopify but not their coverage of stock | The webhook ships |
| D20 | **Catalog text: product cards show names and prices as synced. Replies follow the shopper's language. No claim that Pico translates catalog text** | Decision | The source states the widget text languages, not catalog translation | Catalog translation is built |
| D21 | **Every feature is on every plan. Plans differ only in conversations a month**, and Scale adds a 30-minute onboarding call | Decision | One value metric keeps the plan page simple, and the Free plan shows the whole product, including Analytics | A feature needs gating to protect margin (D28) |
| D22 | **C11, development stores: paid plans free for testing on partners' development stores**, switched on at launch in Shopify App Pricing | Decision | A billing setting, cheap to deliver (Step 0.G), and the floor every partner program sets | Never |
| D23 | **C3, the multi-store workspace: built when 10 partners each have 3 or more active paying stores.** Until then a partner takes the existing admin role on each client store's Pico account | Decision | Role-based access already exists. A workspace before demand is cost before evidence | The trigger fires |
| D56 | **The launch build list, by week.** Week 1: the inventory webhook subscription (D19). Week 2: an email when a catalog sync fails. Week 4, before the founding cohort opens: the first insight email in a store's first week, then a weekly summary. Week 6: the partner ledger and payout run, and the proof capture point, which records the first fall in a store's zero result rate after a catalog fix and asks for permission while it is fresh. Week 8: the monthly usage summary. Week 10: the words against the catalog check, a public page where a merchant tests phrases against their store's own search. The partner portal waits for 25 partners (D36) | Decision | Each item is small, and each is named in a dashboard as the touch-point for one stage. Sequencing follows the calendar: sync and webhook before installs, merchant emails before the cohort, partner tooling before the partner page | An item slips by more than two weeks: the CFO and CPO move the next block's scope |

## CFO: prices, costs, and cash

| ID | Decision | Type | Why | Reopen when |
|---|---|---|---|---|
| D24 | **One conversation is a chat thread that gets at least one AI reply. Messages from the same shopper on the same device within 24 hours belong to the same conversation.** Fair use: a conversation includes up to 50 AI replies | Decision | Close to Tidio's published definition, easy to explain, and it matches Pico's session memory on one device. Published on the plan page and the listing | Support tickets about the definition reach 3 in a month |
| D25 | **At the quota: alerts at 80% and 100%, in the dashboard and by email. Open conversations finish. Paid plans get a 10% grace allowance at no charge. Then the launcher pauses until the next cycle or an upgrade. No overage charge, ever.** Upgrades apply at once through Shopify Billing | Decision | Billing surprise is the most frequent complaint class in the category. A visible, capped quota turns it into a positioning line: "No surprise charges. Pico pauses before it bills you more." | Pauses drive more than 20% of uninstall reasons |
| D26 | **Yearly prices: two months free.** Growth $490 a year, Pro $990, Scale $2,990 | Decision | 16.7% off, the most common annual offer, beside a 16% to 17% average (ProfitWell, Vendr). Shopify Billing supports annual plans | Fewer than 10% of paying stores choose yearly by month 6 |
| D27 | **A fourth tier fills the anchor slot: Scale, $299 a month, 6,000 conversations, one store, with an onboarding call.** Above Scale, a custom plan at Scale's unit price, about $0.05 a conversation, set up through Shopify Billing on request | Decision | The anchor was empty, and a store past 2,000 conversations had nowhere to go. Scale keeps Pro's unit price because model cost grows with every conversation (D28) | 3 stores request a custom plan |
| D28 | **Model cost ceiling: $0.02 a conversation on average.** Planning basis: 4 AI replies of about 3,000 input and 250 output tokens each, about $0.017 at $1 and $5 per million tokens for a small, fast model. Gross margin before other costs at the ceiling: Growth 76%, Pro 60%, Scale 60% | Assumption | Tokens per shopping conversation are published nowhere. A ceiling turns the unknown into a rule engineering can hold | Measured cost in the first 30 days of logs. Above the ceiling, the model or prompt changes before any price does |
| D29 | **Target mix at month 6: Free is 60% of active installs. Of paying stores, Growth 70%, Pro 22%, Scale 8%** | Decision | Free is where every trial lands, so it carries most installs. Growth is the hero | Month 6 review |
| D30 | **The founding cohort: 20 US stores. 50% off any paid plan for the first 6 billing periods, through a Shopify Billing subscription discount. A monthly 30-minute feedback call, a direct line to the founder, and roadmap input.** A written case study request at day 60, under the intake rule. It closes at 20 stores or 90 days after the listing goes live, whichever comes first | Decision | Small enough to onboard by hand, large enough to see a pattern. List revenue given up: about $2,940 if all 20 choose Growth, $5,940 if all choose Pro. That is revenue, not cash | It fills before day 60: open a second cohort of 20 |
| D31 | **The 90-day GTM cash budget: $9,000, capped at $3,000 a month.** Itemized in the budget table below | Decision | Funds the full Run 2 cohort and the Run 1 tools, with about 13% held back | Day 90 review |
| D32 | **Runway gate: spend is released in 30-day blocks. Each block needs at least 6 months of company runway after it.** If a block fails the gate, paid sessions pause and Run 2 continues on email, LinkedIn, and the scorecard | Decision | The source states neither burn nor runway, so the plan carries its own stop rule rather than an assumed balance | Each block |
| D33 | **The paid session: $150 for a fixed scope of up to 90 minutes**: the sandbox, an install on a development store or, with the merchant's permission, a client store, the Shopper Words Test, a timed setup, and the feedback form. Pico pays the platform fees. Paid within 7 days of the completed form by invoice, or by milestone release on Upwork, or order completion on Fiverr | Decision | About $100 an hour: inside the $100 to $150 research incentive range for engineers, above the $33 global median freelance rate, inside the US mid-level $62 to $100 range, and above the roughly $100 gig for installing an AI chat app | Fewer than 10 qualified applicants per Upwork post: raise to $200 |
| D34 | **The interview: $75 for 30 minutes**, optional, booked after the session. A second milestone on Upwork, a separate order on Fiverr | Decision | $150 an hour equivalent, at the top of the research incentive range, because it asks for opinion rather than work | Fewer than half of session participants accept |
| D35 | **Partner share: 25% of each referred store's subscription charges for 24 months from its first paid charge. Lead partners earn 30%. A 10% managed share pays on stores the partner manages but did not refer. One share per store. No cash bounty** | Decision | Above the 20% floor that Gorgias and Shopify set, because the owner's brief is to win implementers from the tools they use. A recurring share pays only while the store pays. A bounty would pay for installs that churn. At Growth, a referred store still returns about 51% of its price after model cost and the share | 12 months in, or when partner-referred stores pass 25% of paying stores |
| D36 | **Payouts: monthly, on the 15th, for subscription charges Shopify paid out to Pico in the prior month. A $50 minimum, carried forward. By PayPal or bank transfer.** Partners met on Upwork are paid through Upwork for the first 24 months of that relationship. Tax forms are collected before the first payout | Decision | Pico pays out of money it has received, and Shopify pays app developers with a $25 minimum and holds a first payout for 30 days | 25 partners: move from a ledger to a partner platform |

### The 90-day budget (D31)

| Line | Amount | Basis |
|---|---|---|
| 15 paid sessions on Upwork | $2,655 | $150 plus an 8% marketplace fee and up to $14.99 per contract, about $177 each |
| 5 paid sessions on Fiverr | $809 | $150 plus 5.5% and $3.50, about $162 each |
| 10 paid sessions by invoice | $1,520 | $150 plus about $2 in transfer cost |
| 15 interviews | $1,215 | $75 plus fees, about $81 each |
| ScoreApp Starter, 3 months | $117 | $39 a month (Toolradar, 2026-11-03) |
| LinkedIn Sales Navigator Core, 3 months | $360 | $119.99 a month (2026-11-03) |
| Email sending domain and inboxes | $90 | Allocation |
| US private mailbox for the CAN-SPAM address | $90 | Allocation |
| Counsel review of the partner terms | $1,000 | Allocation |
| Held back | $1,144 | Remainder |
| **Total** | **$9,000** | **$3,000 a month cap** |

## CRO and partnerships: how the program runs

| ID | Decision | Type | Why | Reopen when |
|---|---|---|---|---|
| D37 | **The session cohort: 30 paid sessions in 60 days, from week 1.** Upwork 15, Fiverr 5, email 6, LinkedIn 4 | Decision | Upwork brings applicants to a posted job. Fiverr starts from an existing gig. Email and LinkedIn reach agencies that do not sell on marketplaces | Day 30: shift sessions toward the channel with the best completion rate |
| D38 | **Attribution by deal registration: the partner registers the client store's myshopify domain before the install, the merchant confirms by email, and the first valid registration holds for 90 days.** Checked against install and charge records in the Partner Dashboard | Decision | Works without tracking links, and the merchant's confirmation prevents claims on stores the partner never touched | Disputes reach 2 in a quarter |
| D39 | **Referral traffic: merchants who ask Pico for setup help, through "Book a tailored demo" or support, are offered a listed partner, in rotation and by country. Partners see the count each month. No volume is promised** | Decision | Traffic cannot be promised before Pico has merchants to refer, so the mechanism is promised instead | 50 routed requests a month: add matching by speciality |
| D40 | **Tiers and standing. Partner: an accepted application, open to anyone who completed a session or runs at least one active client store. Directory listing on picofinds.com/partners after the first active paying store. Lead partner: 5 active paying stores, referred or managed. Good standing: at least one active paying store in the last 12 months, no platform rule breach, no incentivized reviews, and copy that uses the narrowed claims.** Shares already earned continue to term unless the partner is removed for a breach. The partner page goes live in week 6 | Decision | Thresholds a solo freelancer can reach, with a top tier an agency would show as a credential | 12 months in |
| D41 | **No separate agency price. Each client store pays its own plan through Shopify Billing. The agency workspace is free to partners (D23)** | Decision | App Store apps cannot bill off-platform, so a multi-store price billed to the agency is not available. The partner earns through the share instead | Shopify permits cross-store billing |

## CMO: listing, reviews, and targets

| ID | Decision | Type | Why | Reopen when |
|---|---|---|---|---|
| D42 | **Listing: "Pico AI Shopping Assistant", in the Chat category where the slate's direct substitutes list. Search terms: AI shopping assistant, product finder, product discovery. Screenshots lead with the Shopper Words Test, then product cards, then the Analytics page, then the plan page with the quota. The partner program's line: "Paid to test it. Credited when it works."** | Decision | Merchants compare chat apps first. The Analytics page is the lead (Dashboard 2) | Listing visit to install falls below 2% at day 30 |
| D43 | **Reviews: ask only after the merchant has opened Analytics and made one fix. Reply to every review within 2 business days. No incentives** | Decision | Shopify's review rules, and the first reviews will set the listing's tone | Never |
| D44 | **Run 1 targets for the first 90 days after the listing goes live:** listing visit to install 3%. Widget seen within 24 hours of install 65%. Median install to widget seen under 20 minutes. A first conversation within 7 days on 50% of installs. Trial to paid by day 30 at 15% of installs. Monthly uninstall rate under 15%. 3 catalog fixes per founding store in 60 days. 10 unincentivized reviews by day 90. 20 founding stores by day 60 | Decision | Trial to paid sits at the 15% to 20% median reported for Shopify apps. No benchmark was found for listing conversion or uninstalls, so those are set as targets and reviewed early | Day 30 for listing and activation, day 60 for conversion |
| D45 | **Run 2 targets for the first 90 days:** cold email reply rate 5%. LinkedIn acceptance 30% and replies from 15% of accepted. 15 hires from 3 Upwork posts. 5 Fiverr orders. 30 sessions completed by day 60. Median setup time under 30 minutes. 15 interviews. 3 case study permissions recorded from both sides. 10 implementers installing on a second client store. 15 partner sign-ups | Decision | A paid offer should beat the 3.43% cold email average. The rest follow from the 30-session cohort | Day 30 |
| D46 | **Feedback cadence: founding merchants, a monthly 30-minute call. Partners, a quarterly call and a findings digest after each batch of 10 sessions** | Decision | Monthly matches the billing cycle, and quarterly matches how agencies review their stack | Attendance falls below half |

## COO and legal: rules before anything is sent

| ID | Decision | Type | Why | Reopen when |
|---|---|---|---|---|
| D47 | **The CAN-SPAM postal address: a US private mailbox registered with a commercial mail receiving agency in Pico's name, on every commercial email from week 1** | Decision | The FTC rule accepts a registered private mailbox, and a US address suits US recipients | Pico opens a US office |
| D48 | **Cold email goes to US recipients only in the first 90 days.** After that, UK recipients only at companies and LLPs, with sender identity and an opt-out. Never to UK sole traders or ordinary partnerships, and never cold to the EU. UK freelancers and EU implementers are reached on LinkedIn, Upwork, and Fiverr | Decision | PECR treats sole traders as individuals. Germany requires prior consent even between businesses. The US needs only CAN-SPAM | Counsel advises otherwise |
| D49 | **Platform conduct.** Sessions found on a platform are paid on that platform. No partner invitation, link, or contact request goes inside Upwork or Fiverr: implementers met there find the program on Pico's public page. An implementer met on Upwork who joins is paid through Upwork for the first 24 months of that relationship, with no conversion fee | Decision | Fiverr bars steering off the platform. Upwork's term covers payments for 24 months, and its conversion fee costs more than paying through Upwork | Either platform changes its terms |
| D50 | **Counsel reviews the partner terms, the session brief, and the platform conduct rules in week 5, before the partner page goes live in week 6** | Decision | Budgeted at $1,000 in D31 | Never skipped |
| D51 | **Week 2: a permission clause in the terms of service, a case study permission form for merchants, and a matching form for implementers**, ready before the first paying merchant | Decision | The brief's proof capture rules need them before anyone asks | Never |
| D52 | **Implementers paid by invoice sign a one-page session agreement and give a W-9 or W-8BEN before the first payment** | Decision | Standard for paying contractors from the US | Never |

## Market sizing: planning bands where trackers are silent

| ID | Decision | Type | Why | Reopen when |
|---|---|---|---|---|
| D53 | **Run 1 ICP bands. Level 1: 100 or more products, 10,000 to 100,000 monthly sessions, 1 to 10 people, annual online sales of about $150,000 to $3 million. Level 2: 250 or more products, 100,000 to 1 million monthly sessions, 10 to 50 people plus an agency or developer, about $1.5 million to $30 million.** The sales bands overlap because order values differ by store, so sessions are the band that decides. Storefront languages are asked at intake, not sized | Decision on researched and assumed inputs | Catalog cutoffs are researched: 28.2% of Shopify stores sell 100 or more products, 16.5% sell 250 or more (StoreLeads, 2026). Sales bands are `DERIVED` from the session bands, Littledata's 1.4% conversion rate, and an order value range of $90 to $180 | The founding cohort's intake answers |
| D54 | **2% of sessions start a conversation**, so Free fits about 2,500 monthly sessions, Growth about 30,000, Pro about 100,000, and Scale about 300,000 | Assumption | Inside the 1% to 5% that vendors report for floating widgets | The founding cohort's first 30 days |
| D55 | **Run 2 ICP bands. Level 1, freelancers and small studios: 1 to 5 people, under $250,000 a year, 2 to 10 active client stores. Level 2, agencies: 6 to 50 people, $1 million to $20 million a year, 10 to 100 active client stores.** Asked in the session application form | Assumption | No source publishes implementer revenue or client store counts. Fiverr shows 40,000+ Shopify gig results, Upwork publishes no headcount, and the Partner Directory holds about 3,754 partners (secondary) | The first 30 applications |

---

## The launch calendar

Week 1 starts Monday 2026-11-09. Black Friday is 2026-11-27 and Cyber Monday 2026-11-30, when US stores freeze theme changes, so the founding cohort opens on 2026-12-01.

| Week | Starts | What happens | Decisions |
|---|---|---|---|
| 1 | 2026-11-09 | Site aligned. Listing submitted. Speed test on Dawn. Inventory webhook live. US mailbox registered. First Upwork post, first emails and LinkedIn messages | D2, D3, D18, D19, D37, D47, D56 |
| 2 | 2026-11-16 | First paid sessions on development stores. Terms clause and permission forms ready. Sync failure email live. Both scorecards tested with five implementers and five of their client merchants | D33, D51, D56 |
| 3 | 2026-11-23 | Listing live target. Merchant scorecard live on ScoreApp. Thanksgiving week: outreach pauses from Wednesday | D2 |
| 4 | 2026-11-30 | First insight email and weekly summary live. Founding cohort opens on 2026-12-01 | D30, D56 |
| 5 | 2026-12-07 | Counsel review of the partner terms | D50 |
| 6 | 2026-12-14 | Partner ledger, payout run, and proof capture point live. Partner page live at picofinds.com/partners, with the implementer scorecard. Invitations to session participants met by email and LinkedIn. Upwork and Fiverr participants find the page on their own | D35 to D40, D49, D56 |
| 8 | 2026-12-28 | Monthly usage summary live | D56 |
| 9 | 2027-01-04 | 30 sessions complete. First case study permission requests | D37, D45 |
| 10 | 2027-01-11 | The words against the catalog check goes live as a public page | D56 |
| 12 | 2027-01-25 | Day 60 review of the founding cohort and both target sets | D44, D45 |
| 13 | 2027-02-01 | Day 90 review. The CFO releases the next block, or not | D31, D32 |
