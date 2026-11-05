<!-- build: xlsx -->
# Run 1, Dashboard 7: Customer Journey Funnel, Shopify merchants

Step 7.1 of gtm-builder v3.1 for the primary market, USA first, with the three Shopify specifics from `SKILL-ADAPTATION.md` Phase 7: stage 2 happens on the App Store and in AI assistants, stage 4 holds an activation sub-funnel (Activation sheet), and stage 7 is a monthly subscription that ends with an uninstall. Built on 2026-11-03.

KPI targets are set in the Targets sheet (`DECISIONS.md` D44), each with the date it is reviewed. Targets are goals, not results. Quotes in the mindset column are illustrative personas, not quotes from real merchants. Function labels follow the skill, read for a self-serve motion: "Product" means the product does the selling.

## Sheet: Journey

| Funnel Stage | Buyer Mindset & Trigger | Key Questions They Ask | Pico Touch-points & Assets (channel) | Internal Goal / KPI | State After Stage (Desired Outcome) | Function |
|---|---|---|---|---|---|---|
| 1. Problem Awareness | "Shoppers keep emailing to ask which one fits. I answer the same questions every day." Trigger: repeat pre-purchase questions, a new product line, peak season prep | • Why do shoppers leave without finding what they wanted? • What are they asking for in words my catalog doesn't use? • Would an AI shopping assistant help a store like mine? | • Shopper Words Test (content and search) • Store Findability Scorecard, the lead magnet (content and search) • Catalog and search guides (content and search) • Answers in AI assistants for category questions (content and search) | • Scorecard completions • Words Test runs • Organic visits to guides | The merchant sees that shoppers describe products in their own words, and wants to know which of those words their catalog misses | Marketing |
| 2. Solution Discovery | "There are dozens of AI chat apps. Which ones actually help shoppers choose?" Trigger: a Shopify announcement, a roundup, an agency mention | • Which apps answer from my own catalog? • What do reviews say about billing and support? • Is the free Inbox agent enough for me? | • App Store listing: screenshots of product cards and the Analytics page, category placement (App Store) • Comparison and alternative pages, every fact sourced and dated (content and search) • Sandbox store link (product-led) | • Listing views • Listing to install rate • Sandbox visits | Pico is on the shortlist, and the merchant has tried the sandbox | Marketing |
| 3. Vendor Evaluation | "Will it tell shoppers something wrong, break my theme, or surprise me with a bill?" Trigger: a shortlist of two or three apps | • Does it only recommend what I sell? • What counts as a conversation, and what happens at the quota? • Will it work with my theme? | • Sandbox store (product-led) • Plan page with every quota, the definition of a conversation, and what happens at the quota (App Store, site, D24, D25) • "What Pico does not do" list (site) • Technical one-pager for their developer (site) | • Sandbox session to install rate • Plan page to install rate | The merchant installs and starts the 14 day Growth trial with no card | Product (self-serve) |
| 4. Trial/Purchase Decision | "Let me see it on my own store before I pay." Trigger: the install | • How long will setup take? • Is the widget actually live? • Is Growth worth it when the trial ends? | • Four-step checklist in the dashboard (product-led) • Trial emails: setup, first conversations, trial ending (product-led) • In-dashboard prompts (product-led) • Setup skill for their developer's coding agent (product-led) | • Each activation step, see the Activation sheet • Time from install to widget seen • Trial to paid rate | The widget is live on the published theme, the first conversations are recorded, and a plan is chosen | Product / CS |
| 5. Value Realization | "Shoppers are using it. What are they asking for?" Trigger: the first week of conversations | • Which requests found nothing? • What should I fix in the catalog first? • Is product click-through moving? | • Analytics page: funnel, zero result and weak click phrases (product) • Overview, 30 days against the prior 30 (product) • Weekly summary email, live in week 4 (product-led, D56) • Proof capture point at value realization, live in week 6 (product, D56) | • Weekly dashboard visits • Zero result phrases reviewed • Catalog fixes made from the report, logged in the monthly founding-cohort call (D46) | The merchant makes a catalog or description fix from what shoppers asked | CS |
| 6. Expansion & Advocacy | "We hit the quota. Is Pro worth it? Should I tell our agency?" Trigger: the quota meter, a good month | • What happens when we pass the quota? • Can I add another store? • Who else should know about this? | • Quota meter and upgrade prompt (product) • App Store review request after value realization, within Shopify's review rules (App Store) • Case study invitation, with permission (email) • Referral to the implementer program (Run 2) | • Free to Growth and Growth to Pro upgrades • Review rate • Proof rows entered under the intake rule | An upgrade, a review, or a proof row with recorded permission | CS / Marketing |
| 7. Renewal & Loyalty | "Is this still worth it this month?" Trigger: each monthly charge, a theme change | • Would I miss it if I uninstalled? • Did the theme change switch it off? | • Monthly usage summary, live in week 8 (email, D56) • Embed check after a theme change (product) • Cancel flow with a reason and the optional 50% retention offer for two billing periods (product) | • Monthly uninstall rate • Uninstall reasons • Share of installs with the embed active | The merchant keeps paying, or leaves a reason that shapes the product | CS / Product |

## Sheet: Activation

### Stage 4, the activation sub-funnel

A store that never enables the embed has installed Pico and never used it. Each step has its own drop-off question and a target, reviewed after the first 50 installs (D44).

| Step | What happens | Drop-off question | What Pico can see | Intervention |
|---|---|---|---|---|
| 1. Install | The merchant adds Pico from the App Store | Did they finish installing, or leave at the permissions screen? | Install event | A setup email with the checklist |
| 2. Authorize | OAuth authorization, tokens stored encrypted | Did the person installing have the rights to authorize? | Checklist step state | The checklist explains who needs store access |
| 3. Enable the theme embed | The merchant switches on the Pico Assistant app embed. Shopify app embeds are off by default after install and stay active only on the theme where they were enabled | Was the embed switched on, and on the live theme? | Checklist step state, and whether the widget has been seen | An in-dashboard prompt that links to the theme editor. Help from their implementer (Run 2) |
| 4. Sync the catalog | Catalog sync, with product and variant counts and the sync log | Did the sync finish? Did any job fail? | Sync log, last successful sync | Retry from the Catalog page. An email when a sync fails, live in week 2 (D56) |
| 5. Confirm the widget was seen | The checklist confirms a storefront visitor saw the widget | Has anyone seen it yet? | Widget seen event | A prompt to preview the storefront |
| 6. First conversation | A shopper asks the assistant something | Are shoppers opening it? | Conversation count on the Overview | Suggested reply chips and the greeting, set per language |
| 7. Plan and quota | The 14 day Growth trial ends, then Free covers 50 conversations a month, or the merchant pays for Growth or Pro through Shopify Billing | Will the quota run out mid-month? Can the buyer pay by card in USD? | Quota meter | An upgrade prompt at 80% of the quota. At 100%, open conversations finish, paid plans get a 10% grace allowance, then the launcher pauses. Never an overage charge (D25) |

### Step targets

Shares of installs, for the first 90 days after the listing goes live (D44).

| Step | Target | Measured in |
|---|---|---|
| 2. Authorize | 95% of installs | Checklist step state |
| 3. Enable the theme embed | 70% of installs within 24 hours, on the live theme | Checklist step state |
| 4. Sync the catalog | 90% of installs within 24 hours | Sync log |
| 5. Confirm the widget was seen | 65% of installs within 24 hours. Median time from install under 20 minutes | Widget seen event |
| 6. First conversation | 50% of installs within 7 days | Overview |
| 7. Plan and quota | 15% of installs on a paid plan by day 30 | Shopify Billing |

## Sheet: Insights

### Critical Success Factors

| # | Factor |
|---|---|
| 1 | The theme embed is switched on, on the live theme, and stays on after theme changes |
| 2 | The first value moment arrives inside the trial: the merchant opens the zero result phrases and recognizes a fix to make |
| 3 | The quota and the definition of a conversation are clear before the first charge, because billing surprise is the most frequent complaint class in the category (Dashboard 2, Reviews_2.7) |
| 4 | The App Store listing earns installs before any review exists, through the sandbox link, screenshots of cards and the Analytics page, and a plain list of what Pico does not do |

### Primary Journey Blockers

| # | Blocker |
|---|---|
| 1 | The theme embed left off. Shopify app embeds are off by default after install and active only on the theme where they were enabled |
| 2 | The Free quota of 50 conversations running out mid-month. Decided: alerts at 80% and 100%, then a pause with no charge, and an upgrade that applies at once (D25) |
| 3 | Whether the buyer can pay. Shopify Billing handles payment for App Store installs, charged in USD. InstaPay does not apply to App Store installs |
| 4 | The free Inbox agent as the default comparison, while Pico has no reviews yet |

### Acceleration Opportunities

| # | Opportunity |
|---|---|
| 1 | Start evaluation from the merchant's own words: the Shopper Words Test and the Findability Scorecard lead into the sandbox |
| 2 | Implementers from Run 2 install Pico for client stores, which takes the embed step off the merchant |
| 3 | A proof capture point at value realization, for example the first fall in a store's zero result rate on requests after a catalog fix, recorded with permission |
| 4 | An embed check after every theme change, and an upgrade prompt before the quota runs out |

## Sheet: Targets

### KPI targets, first 90 days after the listing goes live

Decided on 2026-11-03 (`DECISIONS.md` D44). The listing is planned live in week 3 and the founding cohort opens on 2026-12-01. Benchmarks are named where one exists. Where none was found, the target is a decision reviewed early.

| Stage | KPI | Target | Basis | Measured in | Review |
|---|---|---|---|---|---|
| 1. Problem Awareness | Scorecard completions that open the sandbox | 25% | Decision | ScoreApp and site analytics | Day 30 |
| 2. Solution Discovery | Listing visit to install | 3% | No benchmark found | Partner Dashboard listing analytics | Day 30 |
| 3. Vendor Evaluation | Sandbox visit to install | 10% | Decision | Site analytics and install events | Day 30 |
| 4. Trial/Purchase Decision | Widget seen within 24 hours of install | 65% | Shopify ships app embeds switched off, so this is the step to watch | Widget seen event | After 50 installs |
| 4. Trial/Purchase Decision | Median time from install to widget seen | Under 20 minutes | The four-step checklist | Checklist events | After 50 installs |
| 4. Trial/Purchase Decision | Trial to paid by day 30 | 15% of installs | 15% to 20% median reported for Shopify apps (practitioner post) | Shopify Billing | Day 60 |
| 5. Value Realization | Catalog fixes made from the report | 3 per founding store in 60 days | Decision | Monthly founding-cohort call (D46) | Day 60 |
| 6. Expansion & Advocacy | Unincentivized App Store reviews | 10 by day 90 | Decision. Asked only after a fix (D43) | App Store | Day 90 |
| 6. Expansion & Advocacy | Founding stores | 20 by day 60 | D30 | Cohort list | Day 60 |
| 7. Renewal & Loyalty | Monthly uninstall rate | Under 15% of active installs | No benchmark found | Partner Dashboard | Monthly |
| 7. Renewal & Loyalty | Installs with the embed still active after a theme change | 90% | Decision | Embed check | Monthly |
