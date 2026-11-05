# Step 0.D: Build it, hire it, or do nothing

**Date checked:** 2026-11-03. **Prompt:** `../RESEARCH-PROMPTS.md` Step 0.D. **Extends:** `2026-11-03-step-0-first-pass.md` Section 4.

**Method and limits.** Web search only, because this session's network policy blocks page loads. Figures marked `VENDOR` come from a company that sells one of the options and has a stake in the answer. Figures marked `SELF-REPORTED` come from salary aggregators built on user submissions. Arithmetic done here is labeled `DERIVED` with its formula. No figure was invented to fill a gap. Gaps left here were resolved later on 2026-11-03 as decisions or labelled assumptions in `../DECISIONS.md`.

**The no-named-implementer rule.** Freelancers and agencies are Pico's Run 2 audience. Per the brief and the run rules, they are reported here as anonymized rows, counts, and price bands, never as a named list. Individual gig and agency URLs are held out of this file. The marketplace category pages and search terms below reproduce the sample.

---

## 1. Build it

### 1a. What a developer builds on, per Shopify's own docs

| Component | What it is | Source |
|---|---|---|
| **Storefront Catalog MCP**, now on UCP | Per-store endpoint at `https://{storedomain}/api/ucp/mcp` with search_catalog, lookup_catalog, and get_product. Shopify's docs say it is the server meant for building a storefront AI agent, scoped to one merchant's catalog. Calls carry an agent profile in the request metadata | [shopify.dev](https://shopify.dev/docs/agents/catalog/storefront-catalog), [changelog](https://shopify.dev/changelog/posts/storefront-catalog-mcp-now-implements-ucp) |
| **Cart MCP and Order MCP** | Build a cart and look up orders for an agent | [Build a cart](https://shopify.dev/docs/agents/get-started/build-a-cart), [Order MCP](https://shopify.dev/docs/agents/orders/order-mcp) |
| **WebMCP storefront tools** | Since Fall '26, tools on every Liquid and Hydrogen storefront for browser agents. Chromium origin trial only | [WebMCP](https://shopify.dev/docs/api/web-mcp) |
| **Shopify AI Toolkit** | Lets a coding agent build with Shopify's docs, API schemas, and code validation, and manage a store through the CLI. Supports Claude Code, Codex, Antigravity CLI, Cursor, Hermes through a plugin, and VS Code. Installs as a plugin, as skill files, or as the Dev MCP server. Needs Node.js 18+. Shopify recently merged its toolkit skills into one `shopify` skill and also ships a `ucp` skill | [AI Toolkit](https://shopify.dev/docs/apps/build/ai-toolkit), [changelog](https://shopify.dev/changelog/shopify-ai-toolkit-connect-your-ai-tools-to-the-shopify-platform), [skills consolidated](https://shopify.dev/changelog/posts/ai-toolkit-skills-have-been-consolidated) |
| **The retired starting point** | The old Storefront MCP catalog and cart tools on `/api/mcp` were removed, and Shopify's `shop-chat-agent` sample is deprecated. A build started from older tutorials needs migration first | [Migrate from Storefront MCP](https://shopify.dev/docs/apps/build/storefront-mcp/servers/storefront), [GitHub](https://github.com/Shopify/shop-chat-agent) |

**What still has to be built** on top of those rails, none of which Shopify supplies: the chat widget and theme embed, the prompt and reply logic, guardrails, language handling and right to left layout, conversation storage, analytics on what shoppers asked, and the merchant's controls for voice. That list is the same as Pico's stated feature set, which is why the build path and Pico's setup skill target the same developers.

### 1b. Freelance offers, 18 listings sampled on 2026-11-03

**Where:** Fiverr category and search pages ([chatgpt-chatbot](https://www.fiverr.com/gigs/chatgpt-chatbot), [ai-shopify](https://www.fiverr.com/gigs/ai-shopify), [shopify-ai](https://www.fiverr.com/gigs/shopify-ai), [ecommerce-chatbot](https://www.fiverr.com/gigs/ecommerce-chatbot), [shopping-bot](https://www.fiverr.com/gigs/shopping-bot), [chatbots for commerce](https://www.fiverr.com/categories/programming-tech/buy/chatbots/commerce-payment)) and Upwork's services catalog and job board. **Search terms:** "Shopify AI chatbot", "Shopify ChatGPT integration", "AI shopping assistant Shopify". Prices are as listed by the seller, in the listing's currency, read through the search index.

| # | Platform | What is offered | Price | Delivery | Included |
|---|---|---|---|---|---|
| F01 | Fiverr | AI product recommendation chatbot for an ecommerce store, works with Shopify | $30 | 3 days | LLM with retrieval. Base tier covers 50 products and 100 conversations a month |
| F02 | Fiverr | OpenAI chatbot for a Shopify store | $30 | 5 days | Order status and stock availability answers |
| F03 | Fiverr | ChatGPT chatbot for WordPress, Shopify, or Wix | $90 headline, $98.45 with fees | 1 day | 1 revision, small knowledge base |
| F04 | Fiverr | ChatGPT chatbot or website with WhatsApp | $90 | n/a | |
| F05 | Fiverr | Custom chatbot trained on the store's data | $100 | 3 days | |
| F06 | Fiverr | Ecommerce chatbot with ChatGPT and ManyChat | €100.97 | 3 days | 2 revisions |
| F07 | Fiverr | **Setup of an existing AI chat app** on a Shopify store, naming Tidio, VanChat, SmartBot, and Verifast | $100 to $109 | n/a | Install and configure, not a build |
| F08 | Fiverr | ChatGPT or Gemini chatbot integrated in a site or app | Starter $150, higher tiers $350 and $1,000 | 3 to 7 days | 2 revisions, source code |
| F09 | Fiverr | ChatGPT API integration with WordPress, Wix, or Shopify, or custom agents | $155 | n/a | |
| F10 | Fiverr | Shopify chatbot using ChatGPT and Voiceflow | $200 | 14 days | |
| F11 | Fiverr | Shopify chatbot integration, app, and API work | $250 | 5 days | |
| F12 | Fiverr | Store optimization for agentic commerce and AI shopping (adjacent, not a chatbot) | $230 | n/a | Audit for ChatGPT and Gemini visibility |
| U01 | Upwork | ChatGPT chatbot for Wix, WordPress, Shopify, WhatsApp | $50, $100, $200 tiers | 1 to 5 days | |
| U02 | Upwork | ChatGPT chatbot on WordPress, Wix, and Shopify | From $50 | n/a | |
| U03 | Upwork | Custom AI agents for ecommerce sales and support, works with Shopify | $250, $500, $900 | n/a | Customer questions, product recommendations |
| U04 | Upwork | OpenAI integration with Shopify and other platforms | $250, $400, $1,000 | n/a | |
| U05 | Upwork | Store-connected AI assistant for Shopify or WooCommerce with GA4 and Search Console | $990 fixed, a launch rate for the first 3 clients | n/a | |
| U06 | Upwork | Job post: custom GPTs working with Shopify and marketing tools | $15 to $35 an hour | Under 30 hours a week, 1 to 3 months | Buyer-posted rate |

**Bands.** Basic bots: $30 to $250, delivered in 1 to 14 days. Store-connected agents: $250 to $1,000. Hourly: $15 to $35 on the one job post sampled. **Three patterns worth keeping.** Most gigs are generic chatbots that work across WordPress, Wix, and Shopify, not Shopify catalog assistants. The cheapest gigs cap products and conversations, the same limits an app sells. And at least one freelancer sells the **installation of existing AI chat apps** as a service, which is direct evidence for Run 2 that implementers already earn from setting these apps up.

### 1c. Agencies and development firms that build custom assistants

Reported as ranges from published cost guides, not as named firms. Most of these pages are written by firms selling the build, or by SaaS vendors arguing against it.

| Who published it | Range published | Marked |
|---|---|---|
| Development agencies (4 guides sampled) | MVP from about $8,000. Typical custom ecommerce chatbot $15,000 to $80,000. Ecommerce shopping assistant $30,000 to $90,000. Enterprise above $50,000 | `VENDOR` (they sell the build) |
| SaaS vendors that sell the alternative | Zipchat: "Building an AI chatbot for ecommerce costs $150,000 to $400,000 in engineering and takes 6 to 12 months" ([Zipchat](https://www.zipchat.ai/blog/ai-chatbot-for-ecommerce-build-vs-buy)). InstantDM: custom build $77,000 to $168,000 in year one against platforms from $49 a month ([InstantDM](https://instantdm.com/blog/ai-chatbot-ecommerce-build-vs-buy)) | `VENDOR` (they sell the app) |

**Reading it.** The ranges cluster by who is speaking: agencies quote what they would charge, SaaS vendors quote what the merchant would lose. Neither is a benchmark. The freelance floor ($30 to $1,000) and the agency band ($8,000 to $90,000) are both real offers, aimed at different buyers.

### 1d. Ongoing costs after a custom build

| Cost | What is known | Source |
|---|---|---|
| LLM usage | Priced per million tokens. Anthropic Claude Haiku 5.5: $0.10 input, $0.50 output for prompts up to 100,000 tokens. Claude Sonnet 5.5: $2 input, $10 output. OpenAI's pricing page lists gpt-6-luna at $0.10 input and $0.50 output, and gpt-6.1-terra at $1.00 and $5.00. Batch and cache discounts apply | [Claude pricing](https://platform.claude.com/docs/en/about-claude/pricing), [OpenAI pricing](https://developers.openai.com/api/docs/pricing), both read 2026-11-03 |
| LLM cost per conversation | `DERIVED` formula only: (input tokens × input price + output tokens × output price) ÷ 1,000,000. No source sampled measured a shopping conversation. Planning assumption, set later on 2026-11-03: 4 AI replies of about 3,000 input and 250 output tokens, about $0.017 at $1 and $5 per million tokens, held under a $0.02 ceiling (`../DECISIONS.md` D28) | |
| Hosting | No sourced figure found for a small-store assistant. Treated as part of upkeep, below | |
| Maintenance | Vendors call it the hidden cost of building but publish no reliable percentage. Planning assumption: 15% to 20% of the build cost a year, the common software rule of thumb, labelled as an assumption wherever it is used | [Zipchat](https://www.zipchat.ai/blog/ai-chatbot-for-ecommerce-build-vs-buy) `VENDOR` |
| Platform drift | Shopify retired the `/api/mcp` catalog and cart tools, deprecated its sample agent, and stopped the Global Catalog REST API on 2026-11-02. A custom build inherits these migrations | 0.C, `SHOPIFY` |

---

## 2. Hire it

### 2a. Chat agent pay, in-house

| Country | Figure | Type | Source and date |
|---|---|---|---|
| United States | **Median $21.53 an hour** for customer service representatives, May 2025. 10th percentile $15.27, 90th percentile $30.57. Business support services median $17.68. Chat agents are not split out from SOC 43-4051 | Government statistic | [BLS Occupational Outlook Handbook](https://www.bls.gov/ooh/office-and-administrative-support/customer-service-representatives.htm), [OEWS May 2025](https://www.bls.gov/news.release/pdf/ocwage.pdf) |
| United Kingdom | **Legal floor £12.71 an hour** for workers 21 and over from 2026-04-01, up from £12.21 | Statutory minimum | [GOV.UK](https://www.gov.uk/government/news/national-living-wage-increases-to-1271-per-hour) |
| United Kingdom, market | Payscale employer averages of about £8.34 to £9.35 an hour sit below the current legal floor, so they predate it and are not used. One Indeed estimate of £13.15 an hour rests on 10 postings at one employer | `SELF-REPORTED`, stale | [Payscale](https://www.payscale.com/research/UK/Job=Customer_Service_Advisor/Salary/b098503d/London), [Indeed](https://uk.indeed.com/cmp/Everyone-Active/salaries/Customer-Service-Representative) |
| UAE | Customer service agent average AED 51,923 a year. Entry level AED 49,350, mid-career AED 75,143 | `SELF-REPORTED` | [Payscale UAE](https://www.payscale.com/research/AE/Job=Customer_Service_Agent/Salary) |
| Saudi Arabia | Customer service agent average SAR 36,000 a year. Early career SAR 48,000. Riyadh page SAR 27,250. Internally inconsistent | `SELF-REPORTED` | [Payscale Saudi Arabia](https://www.payscale.com/research/SA/Job=Customer_Service_Agent/Salary) |
| Egypt | Customer support category average EGP 15,696 a month gross. Customer service analyst range EGP 10,341 to 19,487 a month. Payscale CSR average EGP 62,287 a year. Private-sector minimum wage EGP 7,000 a month from 2025-03-01, per a summary of the National Wages Council decision | `SELF-REPORTED`, and a secondary summary for the minimum | [Paylab](https://www.paylab.com/eg/salaryinfo/customer-support/customer-service-analyst), [Payscale Egypt](https://www.payscale.com/research/EG/Job=Customer_Service_Representative_(CSR)/Salary), [Hivedesk](https://www.hivedesk.com/salary-guides/egypt) |

### 2b. Chat agent cost, outsourced

| Where | Figure | Marked | Source |
|---|---|---|---|
| Philippines, dedicated live chat agent | $6 to $14 per loaded agent hour in one guide, $8 to $15 in another | `VENDOR` | [Stealth Agents](https://stealthagents.com/research/us-vs-philippines-customer-support-cost-comparison-2026), [Stealth Agents](https://stealthagents.com/research/live-chat-outsourcing-cost-statistics) |
| Asia generally (India, Philippines, Pakistan) | $7 to $16 an hour per agent | `VENDOR` | [Crescendo](https://www.crescendo.ai/blog/outsourced-call-center-pricing-guide?ssrid=ssr) |
| US-based outsourced | $29.40 to $42 an hour per agent | `VENDOR` | [Crescendo](https://www.crescendo.ai/blog/outsourced-call-center-pricing-guide?ssrid=ssr) |
| Per chat, outsourced | $2.50 to $5.00 average. India $0.40 to $0.90 against $3.20 to $5.50 for a US team | `VENDOR` | [Stealth Agents](https://stealthagents.com/research/live-chat-outsourcing-cost-statistics) |
| First pass range | Roughly $6 to $42 an hour by region | `VENDOR` | [Ringly](https://www.ringly.io/blog/cost-to-outsource-customer-service-ecommerce) |
| UK, UAE, Saudi Arabia, Egypt outsourced | Not found | | Out of scope: the plan is US first, and the GCC opens later (`../DECISIONS.md` D11) |

### 2c. Coverage and response time

- **Coverage arithmetic.** `DERIVED`: 24 hours × 7 days = 168 staffed hours a week, which is 4.2 full-time agents at 40 hours each before breaks, leave, or overlap. A small store that wants evening and weekend cover is buying hours, not just a seat.
- **Response time benchmarks**, all from vendors or aggregators with differing definitions of "first response": Comm100's 2024 data shows a 23.6 second average queue wait and a 44.8 second average response. A 2026 study relayed by a vendor puts ecommerce chat first response at 1 minute 48 seconds. One aggregator cites a Zendesk 2026 survey in which 74% of consumers expect 24/7 service. `VENDOR`. Sources: [Stealth Agents](https://stealthagents.com/research/first-response-time-benchmarks-2026), [Velaro](https://v20.velaro.com/blog/live-chat-benchmarks-2026), [Ringly](https://www.ringly.io/blog/customer-service-response-time-statistics-2026).
- **No benchmark split by staffed hours was found** for small Shopify stores. The pricing anchors use the merchant's own hours instead.

---

## 3. Do nothing beyond what the store already has

Shopify's own guidance on findability without extra apps, per the Help Center on 2026-11-03:

| Lever | What Shopify says | Source |
|---|---|---|
| Filters | Search & Discovery filters on collection and search pages. Standard filters (availability, category, price, product type, tags, vendor) for all stores. Up to 25 filters. Collections with more than 5,000 products show no filters. The theme must support filtering. Metafield-based custom filters | [Help: filters](https://help.shopify.com/en/manual/online-store/storefront-search/search-and-discovery-filters), [Help: theme filters](https://help.shopify.com/en/manual/online-store/themes/customizing-themes/common-customizations/storefront-filters) |
| Product copy and tags | A clear product description tells customers what they are buying. Tags help customers find products through storefront search and build collections | [Help: product details](https://help.shopify.com/en/manual/products/details) |
| Synonyms | Synonym groups in Search & Discovery so product text matches shoppers' words | [Help: storefront search](https://help.shopify.com/en/manual/online-store/storefront-search) |
| Built-in search | Predictive search and typo tolerance by default. Semantic search for eligible stores (see 0.C) | [Help: search](https://help.shopify.com/en/manual/online-store/search-and-discovery/search) |
| Measuring the gap | "Searches with no results" and "Searches with no clicks" reports, with advice to adjust titles and descriptions | [Help: search analytics](https://help.shopify.com/en/manual/online-store/storefront-search/search-and-discovery-analytics) |
| Free chat | Inbox and the Inbox agent | 0.C |

**Reading it.** "Do nothing" on Shopify in 2026 is not nothing. It is native search with semantic understanding for eligible stores, filters, synonyms, a no-results report, and a free AI agent. Phase 3's status quo statement is about this bundle, and it must describe what Pico adds without saying what Shopify lacks.

---

## 4. Cost comparison

Everything sourced, nothing filled in. Monthly unless stated.

| Option | Up-front | Ongoing | Who carries the work | Source |
|---|---|---|---|---|
| Do nothing beyond native | $0 | $0 | Merchant tunes copy, tags, synonyms, filters | Section 3 |
| Shopify Inbox agent | $0 | $0 | Merchant turns it on. Needs new customer accounts | 0.C |
| Buy Pico | $0 | Free (50 conversations), $49 (600), $99 (2,000) | Merchant or implementer installs | `source/` |
| Buy a competitor | $0 | From $0 to several hundred dollars, by unit (see 0.A Section 3) | Merchant or implementer | 0.A |
| Freelance build | $30 to $1,000 | Model use about $0.02 a conversation, and upkeep at 15% to 20% of the build a year, both planning assumptions (D28) | Freelancer, then the merchant | Section 1b |
| Agency build | $8,000 to $90,000 per agency guides | Same as above | Agency retainer or merchant | Section 1c, `VENDOR` |
| Hire in-house chat staff | Hiring cost: SHRM 2025 average $5,475 per nonexecutive hire, median $1,200 (secondary, `2026-11-03-tbd-resolution-research.md`) | US median $21.53 an hour. UK floor £12.71 an hour. UAE, Saudi Arabia, and Egypt in Section 2a | Merchant manages staff | Section 2a |
| Hire outsourced chat | Setup: no published figure found, so the hourly and per-chat rates carry the comparison | $6 to $16 an hour offshore, $29.40 to $42 US-based, or $2.50 to $5.00 per chat | Outsourcer | Section 2b, `VENDOR` |

**What Phase 9 can and cannot take from this.** Anchor 2 in `../SKILL-ADAPTATION.md` (alternative comparison) can use the BLS median and the UK statutory floor with their dates, because they are not vendor figures. It cannot use the outsourced rates as anything but a range with the `VENDOR` mark. It cannot claim Pico replaces an agent, because Pico does not handle orders, returns, or handoff (C5, C6). The honest comparison is narrower: hours of a person answering "which product is right for me" against a conversation quota.
