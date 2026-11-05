<!-- build: xlsx -->
# Run 1, Dashboard 9: Pricing and Packaging, Shopify merchants

Steps 9.1 to 9.3 of gtm-builder v3.1, run as a **review of Pico's existing public tiers, not a rebuild** (`SKILL-ADAPTATION.md` Phase 9). Built on 2026-11-03.

Rules applied: Pico's prices come from the source: Free 50 conversations a month, Growth 600 for $49, Pro 2,000 for $99, monthly or yearly, one store per plan. Yearly prices, the definition of a conversation, behavior at the quota, and a fourth tier were decided on 2026-11-03 (`DECISIONS.md` D24 to D29). Every input about Pico's effect is left for the merchant to fill in, because revenue attribution is not measured. Worked examples use labelled example inputs, never Pico results. Competitor prices were read through the web search index on 2026-11-03 from vendor pages, so each one is rechecked on its own page, with the date, before any use outside this workbook. `DERIVED` marks arithmetic done here. Nothing in this workbook is customer-facing copy, except the Calculator, which is built to be filled in by the merchant.

## Sheet: Value_Metric

### Step 9.1: denominators this category actually uses

| Denominator | Who bills this way, 2026-11-03 | Correlation to Value | Scalability | Ease of Measurement | Score (1-10) |
|---|---|---|---|---|---|
| Per conversation (Pico's metric) | Pico, Chatty, Tidio Lyro, Alhena, Verifast (per chat), Commslayer | High. A conversation is the moment a shopper asks for help, which is what Pico does | Grows with traffic and with shoppers' use of the assistant, in quota tiers | Easy, now that it is defined (D24): a thread with at least one AI reply, counted once per shopper and device per 24 hours. Tidio's published definition is close: at least one reply from the AI agent | 8 |
| Per visitor or session | Rep AI, Dialog, VanChat (monthly visitors). Supportify (sessions) | Low to medium. The merchant pays for traffic whether shoppers use the assistant or not | High, follows traffic | Easy, but bot traffic and session rules invite disputes | 5 |
| Per resolution or outcome | Intercom Fin ($0.99), Gorgias AI Agent ($0.90 to $1.50), Yuma (about $1.20) | High in principle, but the vendor defines success, and a shopper browsing is not a ticket to resolve | Medium | Hard for Pico, which does not measure outcomes (candidate C1) | 3 |
| Per AI reply | Zipchat | Low to medium. Long conversations cost more, and the shopper controls the length | High | Easy | 4 |
| Commission on AI-attributed sales | Buddy AI, ChatPilot, Gimmie AI | High only if the merchant trusts the attribution | High | Not possible for Pico without attribution, and sales claims are banned | 2 |
| Per store, flat tier | Shopify's free native tools, many flat-fee apps | Low. Same price at any level of use | Low | Very easy | 5 |
| Per seat | Richpanel (per seat), seat limits on some free plans | Low. Value lives in shopper conversations, not merchant logins | Low for small stores | Easy | 2 |
| Per capability (feature-gated tiers) | Common across the category | Medium as a secondary lever | Medium | Easy | 4 |

### Recommendation

| Element | Recommendation |
|---|---|
| Primary Value Metric | **Per conversation, which holds.** It matches what Pico does and measures, it matches the unit Chatty and Tidio Lyro use, and the merchant can watch it on the quota meter |
| Secondary Usage Metric | **Stores per plan.** Each plan connects one store today. A second store means a second plan. A multi-store plan is the obvious expansion, decided in Run 2 |
| Rationale | Per visitor charges for traffic that never asks. Per resolution and commission need outcome measurement Pico does not have, and would invite claims Pico cannot support. Per conversation is the closest unit to the value, provided the definition is published |
| Definition of one conversation | **Decided (D24):** a chat thread that gets at least one AI reply. Messages from the same shopper on the same device within 24 hours belong to the same conversation. Fair use: up to 50 AI replies per conversation. It goes on the plan page and the listing |
| Behavior at the quota | **Decided (D25):** alerts at 80% and 100%, in the dashboard and by email. Open conversations finish. Paid plans get a 10% grace allowance at no charge, then the launcher pauses until the next cycle or an upgrade, which applies at once. No overage charge, ever. Billing surprise is the most frequent complaint class in the category (Dashboard 2), so this is also a positioning line: "No surprise charges. Pico pauses before it bills you more." |

### Price per conversation, internal comparison

`DERIVED` from each vendor's published plan, dated 2026-11-03. Internal only: features differ widely, and a named comparison goes into copy only after a page-loaded recheck.

| Offer | Plan | Price per month | Included | Price per unit | Unit | Source |
|---|---|---|---|---|---|---|
| Pico | Growth | $49 | 600 conversations | About $0.08 | Conversation | Source document |
| Pico | Pro | $99 | 2,000 conversations | About $0.05 | Conversation | Source document |
| Pico | Scale | $299 | 6,000 conversations | About $0.05 | Conversation | `DECISIONS.md` D27 |
| Chatty | Basic, Pro, Plus | $19.99, $68.99, $199 | 100, 500, 1,000 AI conversations | About $0.20, $0.14, $0.20. Overage $0.40 | AI conversation | [Chatty](https://chatty.net/blog/ai-chatbot-pricing/) |
| Tidio Lyro | Add-on | Tiers of 50 to 1,000 conversations | | About $0.50 to $0.65, sources conflict | AI conversation | [Tidio](https://www.tidio.com/blog/chatbot-pricing/) |
| Verifast | Starter (listing) or vendor tiers | $99, or $79 to $239 | 1,000 chats, or 500 to 5,000 | About $0.10, or $0.16 to $0.05 | Chat | Listing, [Verifast](https://verifast.ai/pricing) |
| Zipchat | Starter | $80 monthly | 750 AI replies, about 300 conversations by the vendor's own equivalence | About $0.11 per reply, $0.27 per conversation | AI reply | [Zipchat](https://www.zipchat.ai/pricing) |
| Intercom Fin for Ecommerce | Per outcome | 50 outcomes a month minimum | | $0.99 | Resolution | [Intercom Help](https://www.intercom.com/help/en/articles/14997821-fin-for-ecommerce-explained) |
| Shopify Inbox agent | Free | Free | | Free | | [Shopify Help](https://help.shopify.com/en/manual/inbox/assigning-your-ai-staff-member) |

## Sheet: Tiers

### Step 9.2: the existing tiers on the Decoy, Hero, Anchor structure

The skill's share ranges are its framework defaults, shown for reference. Pico's target shares are set for month 6 (D29): Free as a share of active installs, the paid plans as shares of paying stores.

| Plan | Price | Conversations a month (primary metric) | Stores (secondary metric) | Position | Skill framework share | Pico target share |
|---|---|---|---|---|---|---|
| Free | $0 | 50 | 1 | Entry. Where every trial lands after 14 days, so it works as the entry tier, not a decoy | 10-20% | 60% of active installs |
| Growth | $49 a month, or $490 a year (D26) | 600 | 1 | Hero | 60-80% | 70% of paying stores |
| Pro | $99 a month, or $990 a year (D26) | 2,000 | 1 | Hero+ | 10-20% | 22% of paying stores |
| Scale | $299 a month, or $2,990 a year (D27) | 6,000 | 1, with a 30-minute onboarding call | Anchor, added 2026-11-03 | 5-10% | 8% of paying stores |
| Above Scale | A custom plan at Scale's unit price, about $0.05 a conversation, set up through Shopify Billing on request (D27) | By request | 1 | Off the plan page | | |

### Findings

| # | Finding |
|---|---|
| 1 | **The anchor slot was empty, and Scale now fills it** (D27). Before, nothing made Pro look moderate, and a store past 2,000 conversations had nowhere to go. Scale keeps Pro's unit price, about $0.05, because model cost grows with every conversation (D28). A separate agency price is not available under Shopify Billing, so Run 2 pays partners through a share instead (D41) |
| 2 | Growth to Pro is 2.0 times the price for 3.3 times the conversations (`DERIVED`), a clear reason to upgrade once a store passes 600 |
| 3 | Pico's price per conversation sits below every per-conversation vendor sampled (Value_Metric sheet). Internal input only, not a copy line until rechecked |
| 4 | Shopify's revenue share is 0% on the first $1M of lifetime app revenue and 15% above it, so net price equals list price until then ([Shopify changelog](https://shopify.dev/changelog/update-to-shopifys-app-developer-revenue-share)) |
| 5 | App charges are set in USD. Shopify shows local-currency estimates for 14 currencies, none of them a GCC currency. Relevant only when the GCC is opened |
| 6 | Yearly plans give two months free, 16.7% off, beside a 16% to 17% SaaS average (ProfitWell, Vendr, both secondary). Shopify Billing supports annual plans (D26) |
| 7 | At the model cost ceiling of $0.02 a conversation, gross margin before other costs is 76% on Growth and 60% on Pro and Scale (`DERIVED`, D28). Free costs about $1 a month per store in model use |

### Expansion levers

| # | Lever | How a customer upgrades |
|---|---|---|
| 1 | Conversation quota | Free to Growth to Pro to Scale as conversations grow, prompted at 80% of the quota, before it runs out (D25) |
| 2 | Stores | One store per plan. Each store pays its own plan through Shopify Billing. An agency workspace across stores comes when 10 partners each have 3 or more active stores (D23, D41) |
| 3 | Billing period | Yearly plans with two months free: Growth $490, Pro $990, Scale $2,990 (D26) |
| 4 | Capability by tier | None by design. Every feature is on every plan, and plans differ only in conversations a month (D21) |

## Sheet: ROI_Anchors

### Anchor 1: cost of the problem

Built on the store's own zero result searches, which Shopify's free Search & Discovery reports for the search bar, and on time spent answering questions by hand. Industry zero-result rates are not used: Step 0.H found every one secondhand.

| Problem Scenario | Cost Without Solution | Annual Subscription Cost | ROI Multiple |
|---|---|---|---|
| Shoppers ask for products in words the catalog doesn't use, and find nothing | The merchant's own figure: monthly searches with no results, times the share who would have bought, times average order margin, all from the merchant's own numbers. Worked example, example inputs only: 100 searches × 10% × $30 = $300 a month | Growth $490 a year, or $588 at the monthly price (`DERIVED`) | The merchant's own: yearly cost without, divided by $490, in the Calculator sheet. No multiple is stated for Pico, because revenue is not measured |
| The owner answers the same pre-purchase questions by hand | The merchant's own figure: hours a week, times the cost of an hour. Reference rate: US customer service representatives, median $21.53 an hour (BLS, May 2025). Worked example, example inputs only: 3 hours a week is about $280 a month (`DERIVED`) | Growth $490 a year, or $588 at the monthly price | The merchant's own, in the Calculator sheet. Not stated for Pico, which does not replace a person |

### Anchor 2: alternative comparison

The strongest anchor. `DERIVED` arithmetic on sourced prices. **Not like for like:** Pico covers product discovery requests. Staffed chat and support suites also answer orders, returns, and policy questions, which Pico does not.

| Alternative | Their Cost | Our Cost | Savings % |
|---|---|---|---|
| A US customer service representative answering "which product is right for me" | $21.53 an hour (BLS median, May 2025) | Growth $49 a month equals about 2.3 hours at that rate. Pro $99 equals about 4.6 hours (`DERIVED`) | Not a percentage: the honest comparison is hours of a person against a conversation quota (`research/2026-11-03-step-0d-build-hire-nothing.md`). Pico does not replace an agent |
| Offshore outsourced chat | $6 to $16 an hour (vendor-sourced range) | Growth $49 a month equals about 3.1 to 8.2 hours at those rates (`DERIVED`) | Not a percentage, same reason |
| Chatty at 600 AI conversations a month | About $109 a month: Pro $68.99 for 500, plus 100 at $0.40 (`DERIVED` from Chatty's pricing post) | Growth $49 a month | About 55% (`DERIVED`). Chatty also includes live chat, a helpdesk, and channels. Recheck before any use |
| Chatty at 2,000 AI conversations a month | About $599 a month: Plus $199 for 1,000, plus 1,000 at $0.40 (`DERIVED`) | Pro $99 a month | About 83% (`DERIVED`). Same caveats |
| Custom build | Freelance $30 to $1,000, agency $8,000 to $90,000 one-off (agency guides, vendor-sourced). Plus model use, about $144 a year at 600 conversations a month and $0.02 each, and upkeep at 15% to 20% of the build a year, both planning assumptions (D28) | Growth $490 a year | `DERIVED`: a freelance build under about $300 costs less in year 1. An $8,000 agency build costs about 16 times Growth's yearly price before upkeep |
| Shopify Inbox agent | Free | Growth $49 a month | **None. Pico costs more than the free native agent.** The case rests on what the merchant learns (VP 2), not on price |
| Do nothing beyond what the store has | $0 direct. The indirect cost is Anchor 1, in the merchant's own numbers | Free plan $0, then Growth $49 a month or $490 a year | Not a saving. Doing nothing costs nothing directly, so the case rests on Anchor 1 |

### Anchor 3: breakeven

Written as arithmetic the merchant completes. The example margin of $30 is an example input, labelled, never a Pico result.

| Plan | Annual Cost | Value Needed to Break Even | Typical Customer Value | Payback Period |
|---|---|---|---|---|
| Growth | $490 a year, or $588 at the monthly price | Extra orders a month equal to $49 divided by the merchant's average order margin. At an example $30 margin, 1.6, so 2 orders a month (`DERIVED`) | Not stated. Revenue is not measured (C1), so no typical value is claimed | Inside the first month if the extra orders reach the breakeven count. No payback period is claimed for Pico |
| Pro | $990 a year, or $1,188 at the monthly price | $99 divided by the margin. At an example $30 margin, 3.3, so 4 orders a month (`DERIVED`) | Not stated, as above | As above |
| Scale | $2,990 a year, or $3,588 at the monthly price | $299 divided by the margin. At an example $30 margin, 10 orders a month (`DERIVED`) | Not stated, as above | As above |

### "One order pays for X years" calculator

| One Order's Margin | Plan | Years of Subscription Covered |
|---|---|---|
| The merchant's own margin. Example input: $30 | Growth | Margin divided by $490 at the yearly price. In the example, about 22 days of Growth |
| The merchant's own margin. Example input: $30 | Pro | Margin divided by $990 at the yearly price. In the example, about 11 days of Pro |

**Message, as a sum the merchant completes:** "One order with $[your margin] of margin covers [your margin ÷ $588] years of Growth." Never stated as a result Pico produced.

## Sheet: Calculator

Yellow cells are for the merchant. Nothing is pre-filled except Pico's public plan prices. Results are the merchant's own estimate, never a Pico result.

<!-- calculator -->
| Key | Item | Value | Note |
|---|---|---|---|
| margin | Your average order margin, $ | [input] | Margin, not order value |
| growth_price | Growth, price per month, $ | 49 | Public plan price |
| pro_price | Pro, price per month, $ | 99 | Public plan price |
| scale_price | Scale, price per month, $ | 299 | Public plan price from 2026-11-03 (D27) |
| zero_searches | Your searches with no results, per month | [input] | From Shopify's own Search & Discovery analytics |
| buy_share | Share of those shoppers you think would buy if they found the product | [input] | Your estimate, as a decimal between 0 and 1 |
| hours_week | Hours a week spent answering pre-purchase questions | [input] | Your estimate |
| hour_cost | Cost of one of those hours, $ | [input] | Reference: US median $21.53, BLS, May 2025 |
| breakeven_growth | Extra orders a month for Growth to break even | `=IF(AND(ISNUMBER({margin}),{margin}>0),{growth_price}/{margin},"enter your margin")` | Growth price divided by your margin |
| breakeven_pro | Extra orders a month for Pro to break even | `=IF(AND(ISNUMBER({margin}),{margin}>0),{pro_price}/{margin},"enter your margin")` | Pro price divided by your margin |
| breakeven_scale | Extra orders a month for Scale to break even | `=IF(AND(ISNUMBER({margin}),{margin}>0),{scale_price}/{margin},"enter your margin")` | Scale price divided by your margin |
| years_growth | Years of Growth covered by one order's margin | `=IF(ISNUMBER({margin}),{margin}/({growth_price}*12),"enter your margin")` | At the monthly price |
| years_pro | Years of Pro covered by one order's margin | `=IF(ISNUMBER({margin}),{margin}/({pro_price}*12),"enter your margin")` | At the monthly price |
| at_stake | Margin at stake each month in searches with no results | `=IF(AND(ISNUMBER({zero_searches}),ISNUMBER({buy_share}),ISNUMBER({margin})),{zero_searches}*{buy_share}*{margin},"enter the three inputs")` | Your estimate, not a Pico result |
| manual_cost | Monthly cost of answering questions by hand | `=IF(AND(ISNUMBER({hours_week}),ISNUMBER({hour_cost})),{hours_week}*{hour_cost}*52/12,"enter hours and cost")` | Your estimate |
