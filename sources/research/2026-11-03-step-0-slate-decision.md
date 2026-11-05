# Step 0 result: slates confirmed or swapped, watchlists, and the landscape index

**Date:** 2026-11-03. **Decides:** open decision 8 in `../GTM-BRIEF.md`. Accepted by the owner on 2026-11-03, who asked for every dashboard to be built on it (`../DECISIONS.md` D10). **Reads from:** the eight Step 0 files in this folder, `2026-11-03-step-0a` to `2026-11-03-step-0h`.

**Selection rule, from the brief.** A competitor earns a slot only if the buyer actually evaluates it. Evaluation evidence used here, in order of weight: detected installs (StoreLeads), App Store review volume, presence on the same App Store shelf or in Shopify's curated collection, presence in implementer stacks (Run 2), and closeness of billing unit and price.

**Evidence limit.** Every App Store and vendor fact was read through the web search index, because this session's network policy blocked page loads. Before Phase 2's Step 2.1 and Step 2.7, each slate competitor's listing, pricing page, and reviews need a page-loaded check.

---

## Run 1, Shopify merchants

| Slot | Brief proposed | Decision | Reason | Evidence |
|---|---|---|---|---|
| 1. Closest direct substitute | Manifest AI | **Swapped to Chatty AI Chatbot & Live Chat** | Chatty bills per AI conversation with a free plan of 50 AI conversations a month, the same unit and the same free allowance as Pico, and sells itself as an AI sales agent with recommendations, upsells, and checkout links. It has about 1,900 reviews and about 9,000 detected installs. Manifest AI has about 61 reviews and about 330 installs, and its paid prices were not visible in any snapshot, so the brief's reason for it ("flat paid tiers in Pico's price band") could not be confirmed. The brief's own swap note pointed to Zipchat on the assumption that Zipchat bills per conversation. It bills per AI reply, so the per-conversation analog is Chatty | 0.A rows 1, 4, 11 and Section 3. [Chatty pricing](https://chatty.net/blog/ai-chatbot-pricing/), [StoreLeads Chatty](https://storeleads.app/reports/shopify/app/chatty), [Zipchat pricing](https://www.zipchat.ai/pricing) |
| 2. Free or low-cost alternative | Shopify Inbox with the AI sales associate | **Confirmed, and stronger than the brief states** | Free, about 358,000 detected installs and about 5,810 reviews. Since the Fall '26 Edition (2026-10-28) the Inbox agent gives personalized recommendations and can start checkout from the chat. It personalizes with Shop sign-in. It needs new customer accounts | 0.C row 1. [Fall '26](https://www.shopify.com/news/fall-26-edition-merchant), [Help: Inbox agent](https://help.shopify.com/en/manual/inbox/assigning-your-ai-staff-member) |
| 3. Where they solve it today | Shopify Search & Discovery | **Confirmed, with two fact changes** | Native and free. Semantic search is no longer English only per Shopify's changelog. Search & Discovery already reports "Searches with no results" and "Searches with no clicks". For ICP Level 2, the store's existing search app (Boost, Smart Product Filter & Search, or Searchanise, about 50,000 detected installs together) is the variant to name in Phase 3, and all three are on the watchlist | 0.C rows 2 and 2a, 0.B category 2 |
| 4. Better-known adjacent option | Tidio with Lyro | **Confirmed** | The most-installed third-party chat app after Inbox (about 27,500 installs, about 1,356 reviews). Lyro recommends from Shopify product data, skips out-of-stock items, bills per AI conversation, and answers in 48 languages including Modern Arabic, so it tests Pico's language angle directly. Gorgias stays the Level 2 swap and is on the watchlist. Rep AI stays on the watchlist: about 1,000 installs and English and Spanish only | 0.B category 1. [Tidio Help: recommendations](https://help.tidio.com/hc/en-us/articles/15960742181148-Product-Recommendations-for-Shopify), [Tidio Help: languages](https://help.tidio.com/hc/en-us/articles/12643043611036-Lyro-Multilanguage-support), [StoreLeads Tidio](https://storeleads.app/reports/shopify/app/tidio-chat) |
| 5. Build it or hire it | Both halves | **Confirmed, both halves, now with cost bands** | Build: Shopify's Storefront Catalog MCP on UCP, Cart and Order MCP, WebMCP, and the AI Toolkit. Freelance offers $30 to $1,000 across 18 listings sampled, agency builds $8,000 to $90,000 per agency guides (vendor-sourced). Hire: US median $21.53 an hour (BLS, May 2025), UK floor £12.71 an hour (from 2026-04-01), offshore outsourced $6 to $16 an hour (vendor-sourced) | 0.D |
| 6. Institutional option | Agentic Storefronts and UCP | **Confirmed, widened** | Now one part of Shopify's agentic stack: Agentic Storefronts (ChatGPT, Copilot, AI Mode, Gemini, Meta), the catalog MCP servers on UCP, WebMCP on every Liquid and Hydrogen storefront, Shop.md, and the agentic knowledge base. Profile it in Phase 2 as "Shopify's agentic commerce stack". Never position against it | 0.C rows 3 to 5b |

### Run 1 watchlist, 22 names, for Step 1.1 feature presence

| Group | Names | Change from the brief, with reason |
|---|---|---|
| AI shopping assistants and AI sales chat | Rep AI, Zipchat AI, Dialog, Alhena AI, Wizybot, **Manifest AI**, **Verifast**, **Moose AI Chatbot & Live Chat**, **Luma** | **Manifest AI** moved down from slot 1. **Verifast** replaces Octocom: 144 reviews against 10, Arabic named, up 195% in installs. **Moose** replaces Wantly: about 8,100 installs and up 463%, against Wantly's zero reviews. **Luma** added so the watchlist includes one Arabic-first Shopify app for the Arabic right to left row |
| Support platforms with a shopping role | Gorgias Shopping Assistant, Intercom Fin for Ecommerce, Klaviyo Customer Agent | Unchanged. Chatty left this list for slot 1 |
| Search and discovery | Fast Simon, Boost AI Search & Filter, Searchanise, Doofinder, **Smart Product Filter & Search** | **Smart Product Filter & Search** added: the most-reviewed search app (about 2,394 reviews) with about 16,400 installs |
| Recommendations, quizzes, video, messaging | Rebuy, Octane AI, RevenueHunt, Tolstoy, Zoko | Unchanged |
| Platform agents to monitor, not scored | Microsoft Brand Agents (via Clarity), Google Business Agent, Meta Business AI on WhatsApp | New. Brand agents offered by platforms the merchant already uses. Not Shopify apps, so not scored in Step 1.1 |

---

## Run 2, Shopify implementers

| Slot | Brief proposed | Decision | Reason | Evidence |
|---|---|---|---|---|
| 1. Closest direct substitute with an agency program | Gorgias Shopping Assistant and the Gorgias agency program | **Confirmed** | Gorgias appears on 13 of 26 sampled agency stack pages, and agencies display Gorgias tiers as credentials. The agency program pays 20% for 2 to 3 years, with a 15% bounty at Elite (help center, 2026-01-22). The brief's swap condition (Rep AI's program being what agencies join) did not hold: Rep AI appeared on none of the 26 pages | 0.F Section 2, 0.G Section 2a. [Gorgias help](https://helpcenter.gorgias.com/en-US/agency-partner-program-81969) |
| 2. Free alternative | Shopify Inbox AI sales associate | **Confirmed** | Shopify's own developer docs tell merchants who want AI chat on the store without code to use the Inbox agent | 0.C row 5a. [shopify.dev WebMCP](https://shopify.dev/docs/api/web-mcp) |
| 3. Where they solve it today | The standard discovery stack, to be named | **Named: Rebuy plus Shopify Search & Discovery** | Rebuy is the only discovery app on more than three sampled agency pages (7 of 26, plus a blog mention). No dedicated search app appeared on any of the 26. Search is left to Shopify's native app, with Nosto at the enterprise end (3 of 26). Rebuy has about 15,200 installs, up 24.7%, and pays agencies a 5% managed share for active work regardless of who referred the brand | 0.F Section 2, 0.G Section 2b. [Rebuy 2026 update](https://help.rebuyengine.com/en/articles/13690188-rebuy-partner-program-updates-2026) |
| 4. Better-known adjacent option | Klaviyo Customer Agent | **Confirmed** | Klaviyo is on 17 of 26 sampled agency pages, the most of any app. Customer Agent now lists 113 languages, answers on web chat, email, SMS, and WhatsApp, and starts at $50 a month for 75 conversations. It arrives inside K:Partners, a relationship agencies already have | 0.B category 1, 0.F Section 2, 0.G |
| 5. Build it | Custom build on UCP or Storefront MCP with the AI Toolkit | **Confirmed** | The old Storefront MCP catalog and cart tools were removed. The build path is now the Storefront Catalog MCP on UCP. Freelancers already sell builds ($30 to $1,000) and installation of existing AI chat apps (about $100) | 0.D Section 1 |
| 6. Institutional option | Shopify Partner Program and Partner Directory | **Confirmed, widened** | Shopify pays 20% of a referred merchant's subscription, $2,500 per Plus referral, and since 2026-08-10 a launch partner share of 20% of subscription plus 0.1% of eligible online GMV for 4 years. That sets what agencies expect from any app program | 0.G Section 1 |

### Run 2 watchlist, 13 names

| Name | Why it is here |
|---|---|
| Rep AI Partner Program | 10% for 12 months up to 25% for life at Elite, with a 15% client discount. The most generous top tier among AI chat vendors |
| **Zipchat agency program** (new) | Lets agencies manage client stores **under their own brand at their own pricing**, the only resale model found |
| Tidio Agency Partner Program | Up to 25% for up to 3 years, and up to $27,000 per referral on the same page |
| Intercom Solution Partner Program | Rates unpublished. Fin supports several Shopify stores in one workspace |
| Octane AI partners | 20% for the life of the account, PartnerStack |
| Fast Simon partners | Expanding agency network in the US and Australia, Plus partner |
| **Nosto** (new) | The discovery vendor at the Plus end of agency stacks (3 of 26) |
| **Recharge, Okendo, LoyaltyLion** (new) | Program benchmarks from the apps agencies list most: billable hours plus share (Recharge), 20% (Okendo), 10% plus 10% client discount (LoyaltyLion) |
| Voiceflow, Chatbase | Build-with-a-builder alternatives |
| Freelance AI chatbot gigs on Upwork, Fiverr, and Storetasker | The build and install market, as a segment, not named |

**Removed from the Run 2 watchlist:** Rebuy and Klaviyo partner programs (now inside slots 3 and 4). Boost and Searchanise: no dedicated search app appeared on any of the 26 sampled agency stack pages, and no partner program was found for either. They stay on the Run 1 watchlist.

---

## The landscape, indexed

Everything found, by file. The slate and watchlist are drawn from these.

| Tier | Where |
|---|---|
| 90+ shopper-facing AI chat listings, top 20 by reviews, pricing closest to Pico, billing models, Arabic apps, long tail, off-store direct vendors, outcome claims | `2026-11-03-step-0a-direct-competitors.md` |
| Indirect: support platforms, search, recommendations, quizzes, video, messaging, builders, enterprise. Install leaders by category | `2026-11-03-step-0b-indirect-competitors.md` |
| Shopify's own tools and AI shopping off the store | `2026-11-03-step-0c-shopify-native-and-offsite.md` |
| Build, hire, do nothing, with cost bands | `2026-11-03-step-0d-build-hire-nothing.md` |
| Arabic-speaking markets | `2026-11-03-step-0e-arabic-markets.md` |
| Implementer segments, agency stack analysis, communities, events | `2026-11-03-step-0f-implementer-landscape.md` |
| Partner programs and Shopify's own partner and billing terms | `2026-11-03-step-0g-partner-programs.md` |
| Sizing by tracker, country, Plus, category, installs, search benchmarks | `2026-11-03-step-0h-market-sizing.md` |
| First pass, existence only | `2026-11-03-step-0-first-pass.md` |

---

## Facts that changed in the brief, and where

| Brief location | Old | New | Source file |
|---|---|---|---|
| Section 2, Run 1 slot 1 | Manifest AI | Chatty, with reason | This file |
| Section 2, Run 1 slot 1 swap note | Zipchat "if per-conversation pricing" | Zipchat bills per AI reply | 0.A |
| Section 2, Run 1 slot 3 | "Semantic search covers eligible English stores" | More languages than English per Shopify's changelog, plus native no-results and no-clicks reports | 0.C |
| Section 2, Run 2 slot 3 | To be named after 0.F | Rebuy plus Shopify Search & Discovery | 0.F |
| Section 2, watchlists | As proposed | As above | This file |
| Section 3, feature 11 | Stated, possible differentiator per source | Shopify's native search analytics already show search-bar zero results. Pico's report covers conversational requests | 0.C |
| Section 3, feature 16 | Theme embed | App embeds are off by default after install and active only on the theme where enabled, per Shopify | 0.F Section 5 |
| Section 3, candidate C11 | Program element | Buildable as a billing setting with Shopify App Pricing "free for testing" | 0.G Section 1 |
| Section 4, decision 3 | Default only | Default holds. Refinement offered: UAE and Egypt first in the Arabic segment | 0.E |
| Section 4, decision 7 | Pricing gaps | Adds Shopify's revenue share (0% to $1M lifetime, 15% above) and Tidio's published conversation definition as a benchmark | 0.G, 0.A |
| Section 5, narrowing drill | Several counter-examples | Updated with Step 0 evidence | 0.A to 0.E |
| Section 5, banned list | | Adds any claim that Shopify's tools lack Arabic or right to left | 0.C |
