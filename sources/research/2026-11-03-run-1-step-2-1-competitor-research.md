# Run 1, Step 2.1: Competitor deep research, Shopify merchants

**Date checked:** 2026-11-03. **Prompt:** `../RESEARCH-PROMPTS.md` Step 2.1, Run 1. **Slate:** `../GTM-BRIEF.md` Section 2, Run 1. **Feeds:** `../run-1-merchants/02-competitive-market-analysis/`.

**Method and limits.** Web search only, because this session's network policy blocks page loads. Taglines are taken from page titles and listing headlines as indexed, and listing subtitles vary by snapshot, so variants are shown. Strengths and weaknesses come from `2026-11-03-run-1-step-2-7-review-analysis.md`. Outcome claims are quoted as claims. Pico's row comes from `../GTM-BRIEF.md` Section 1 and the owner's site screenshots, not from a crawl. Its strengths come from the source's documented capabilities and its weaknesses from the source's own current limits, since no reviews or customers exist.

---

## Pico (ours)

| Attribute | Finding |
|---|---|
| Website, App Store URL | picofinds.com (`../DECISIONS.md` D1). No App Store listing found, so not live on 2026-11-03, planned live in week 3 (D2) |
| Tagline, sub-tagline | The site today: "An AI shopping assistant for Shopware and Shopify that answers in English and Arabic, and only recommends what is in stock." and "Pico searches your real catalog, checks live stock, and gives shoppers a product card with a single add-to-cart tap." Both are replaced under D3 by "An AI shopping assistant for Shopify that answers from your own catalog." |
| Description | "An AI shopping assistant that lets shoppers describe what they want in plain language and returns real products from the merchant's own catalog." A storefront chat widget managed from a seven-page dashboard |
| Strengths, weaknesses | From the source, not from users. Strengths: the discovery analytics on conversational requests, the sandbox store with a sample catalog, the setup skill for coding agents, the right to left widget with a language switcher, and a visible quota. Weaknesses, the source's own current limits: no revenue attribution, no semantic search, one store per plan, no comparison screen, and no reviews yet |
| Who it serves, own words | "E-commerce merchants, and the agencies or developers who set up their stores" |
| Pricing, every plan | Free: 50 conversations a month. Growth: 600 for $49. Pro: 2,000 for $99. Monthly or yearly, yearly two months free: Growth $490, Pro $990 (D26). Scale, $299 for 6,000, added as the anchor (D27). 14 day Growth trial, no card. One store per plan |
| Billing unit | Conversation: a chat thread with at least one AI reply, once per shopper and device per 24 hours (D24) |
| Outcome claims | None |

## 1. Chatty AI Chatbot & Live Chat

| Attribute | Finding | Source |
|---|---|---|
| Website, App Store URL | [chatty.net](https://chatty.net/), [apps.shopify.com/chatty](https://apps.shopify.com/chatty), developer page [Chatty AI Sales Agent](https://apps.shopify.com/partners/so-good6) | |
| Tagline | "AI Sales Agent for Shopify Stores" (homepage title) | `VEN` |
| Sub-tagline | Listing headline, by snapshot: "AI chat, livechat & helpdesk: AI chatbot inbox for sales...", "AI Chat & sale: recommend products, answer FAQs, track orders", "Sell more: AI chatbot, livechat, inbox, help center & WhatsApp" | `IDX` |
| Description | An AI sales agent that answers from store data (product details, variants, prices, stock, FAQs, discounts, policies), recommends products and adds them to the cart, applies Shopify discounts, sends checkout links, recovers abandoned carts, tracks orders, and hands chats to a human team. One inbox for email, Instagram, Messenger, and WhatsApp, plus a help center and FAQ page | `VEN`, `IDX` |
| Strengths | Responsive support and setup help, recurring in reviews. Easy setup. Multi-language replies praised | Step 2.7 |
| Weaknesses | A charge after a trial on a reinstall. A bug that lost a day of requests, with a slow fix. "Needs daily attention" and a "$49" plan called poor value. One agent logged in at a time and no after-hours messaging (2024) | Step 2.7 |
| Who it serves, own words | Shopify stores, "eCommerce" | `VEN` |
| Pricing, every plan, 2026-11-03 | Free: 50 AI conversations a month, renewing, 200 trained products, 1 seat, unlimited human chats. Basic $19.99 for 100. Pro $68.99 for 500. Plus $199 for 1,000. $0.40 per extra AI conversation, spend limit defaulting to $1,000 with an alert. 7 day trial | [Chatty pricing post](https://chatty.net/blog/ai-chatbot-pricing/) `VEN` |
| Billing unit | AI conversation. Definition not found | |
| Outcome claims | "#1 AI Sales Agent for Shopify" (homepage). "92% answer accuracy" (Chatty blog) | `CLAIM` |

## 2. Shopify Inbox with the Inbox agent

| Attribute | Finding | Source |
|---|---|---|
| Website, App Store URL | [shopify.com/inbox](https://www.shopify.com/inbox), [apps.shopify.com/inbox](https://apps.shopify.com/inbox), [Help Center](https://help.shopify.com/en/manual/inbox) | |
| Tagline | "An AI sales associate that knows your customers" (listing headline) | `IDX` |
| Sub-tagline | Fall '26: shoppers "get personalized recommendations, start checkout from the chat, and reach staff" | [Fall '26](https://www.shopify.com/news/fall-26-edition-merchant) |
| Description | Shopify's free chat app with an opt-in AI agent on the storefront. Answers product, shipping, returns, sizing, and policy questions from the catalog, inventory, and policies in the admin. Suggests products, looks up orders for signed-in shoppers, applies discount codes at checkout, hands off to staff, and personalizes with Shop sign-in. Merchants set a persona for tone, wording, personality, and service style, and train it by rating conversations | 0.C, [Help: persona](https://help.shopify.com/en/manual/inbox/agent-persona) |
| Strengths | Free and native. Reviewers praise accurate, on-brand answers. Personalization with Shop sign-in, which no third-party app can match | Step 2.7, 0.C |
| Weaknesses | A reviewer disabled the agent after inaccurate product information caused a costly order issue and asked for source visibility. Another found no human handover. The agent report cannot pinpoint a conversation. A September 2026 redesign drew complaints about the chat start and navigation. No email, SMS, or WhatsApp. Legacy customer accounts are excluded | Step 2.7, 0.C |
| Who it serves, own words | Shopify merchants on Basic, Grow, Advanced, and Plus | 0.C |
| Pricing | Free | |
| Billing unit | None | |
| Outcome claims | "Customers signed-in with Shop convert up to 1.5x higher in Shopify Inbox chats" | `CLAIM`, [Fall '26](https://www.shopify.com/news/fall-26-edition-merchant) |

## 3. Shopify Search & Discovery

| Attribute | Finding | Source |
|---|---|---|
| Website, App Store URL | [Help: search](https://help.shopify.com/manual/online-store/search-and-discovery/search), [apps.shopify.com/search-and-discovery](https://apps.shopify.com/search-and-discovery) | |
| Tagline | "Customize your storefront search and discovery experience" | `IDX` |
| Sub-tagline | Not found | |
| Description | Shopify's free app for storefront filters, synonyms, boosts, product recommendations, semantic search for eligible stores, and search analytics, including "Searches with no results" and "Searches with no clicks" | 0.C |
| Strengths | Free and native. Semantic search in more languages than English. Merchants can see their own zero-result search terms | 0.C |
| Weaknesses | 2.6 stars from about 514 reviews, with 21% one-star, down from 4.3 in a 2022-era snapshot. October 2026 reviews: search returning "hundreds of unrelated products", synonyms removed without notice, an Availability filter that will not stay on, filter caps | Step 2.7 |
| Who it serves | Every merchant with an online store | |
| Pricing | Free | |
| Billing unit | None | |
| Outcome claims | None found | |

## 4. Tidio with Lyro

| Attribute | Finding | Source |
|---|---|---|
| Website, App Store URL | [tidio.com](https://www.tidio.com/), [Lyro](https://www.tidio.com/ai-agent/), [apps.shopify.com/tidio-chat](https://apps.shopify.com/tidio-chat) | |
| Tagline | "Build a service department that never sleeps" (customer service solutions page) | [Tidio](https://www.tidio.com/solutions/customer-service/) `VEN` |
| Sub-tagline | Listing headline, by snapshot: "Live chat, helpdesk and an AI chatbot that sells and...", "AI agent for sales and support. Live chat, email, social..." | `IDX` |
| Description | Live chat, a helpdesk, and Lyro, an AI agent that recommends products from Shopify product data, skips out-of-stock items, answers in 48 languages including Modern Arabic, runs Lyro Actions on orders, and lists questions it could not answer so the merchant can add answers | 0.B, Step 1.1 |
| Strengths | Easy setup. Lyro handles most questions, including product fit and specs, per reviewers | Step 2.7 |
| Weaknesses | Lyro conversation limits and counting disputes. A plan that needed other apps. Branding removal priced above the tool. Upsells and limits. Slow, email-only support and lost tickets. A widget that blocked checkout clicks in one theme. Reporting called inaccurate. Wrong order information in one case | Step 2.7 |
| Who it serves, own words | Small and medium businesses and ecommerce stores | `VEN` |
| Pricing, every plan, 2026-11-03 | Listing: free plan, live chat from $29 a month for 100 conversations, Lyro AI plan $39 a month for up to 200 Lyro conversations. Tidio's pricing post: Starter $29 monthly ($24.17 annual), Growth from $59 ($49.17 annual), Plus from $300 plus usage, Premium custom, Lyro add-on at about $0.50 to $0.65 per conversation, 50 free Lyro conversations once per account | `IDX`, [Tidio pricing post](https://www.tidio.com/blog/chatbot-pricing/) `VEN` |
| Billing unit | Conversation. Lyro: a customer interaction with at least one AI reply | `VEN` |
| Outcome claims | "#1 in G2's AI Agent Evaluations" (solutions page). A 75% average resolution rate (Tidio). A reviewer reports about 90% | `CLAIM` |

## 5. Build it or hire it

| Attribute | Finding | Source |
|---|---|---|
| Website | [Shopify AI Toolkit](https://shopify.dev/docs/apps/build/ai-toolkit), [Storefront Catalog MCP](https://shopify.dev/docs/agents/catalog/storefront-catalog) | |
| Tagline | Not a company. Shopify presents the toolkit as a way to connect AI tools to the Shopify platform | [Shopify changelog](https://shopify.dev/changelog/shopify-ai-toolkit-connect-your-ai-tools-to-the-shopify-platform) |
| Description | Build: a developer connects an LLM to the per-store Storefront Catalog MCP on UCP, the Cart and Order MCP, and WebMCP, then builds the widget, prompts, guardrails, languages, analytics, and controls. Hire: chat staff on Inbox or a helpdesk | 0.D |
| Strengths | Full control and custom behavior. A person can answer anything, including orders and returns | 0.D |
| Weaknesses | Build: ongoing model, hosting, and maintenance costs (planning basis in `../DECISIONS.md` D28: about $0.02 a conversation for the model, with upkeep assumed at 15% to 20% of the build a year), and Shopify migrations (the `/api/mcp` tools were removed, the Global Catalog REST API stopped on 2026-11-02). Hire: 168 staffed hours a week is 4.2 full-time agents | 0.D |
| Pricing | Freelance builds $30 to $1,000. Agency builds $8,000 to $90,000 per agency guides (`VENDOR`). US chat staff median $21.53 an hour (BLS, May 2025). UK floor £12.71 an hour from 2026-04-01. Offshore outsourced $6 to $16 an hour (`VENDOR`) | 0.D |
| Outcome claims | SaaS vendors claim builds cost $77,000 to $400,000 in year one | `CLAIM`, 0.D |

## 6. Shopify's agentic commerce stack

| Attribute | Finding | Source |
|---|---|---|
| Website | [Agentic Storefronts launch](https://www.shopify.com/news/winter-26-edition-agentic-storefronts), [Help](https://help.shopify.com/en/manual/online-sales-channels/agentic-storefronts) | |
| Tagline | "Sell your products everywhere AI conversations happen" | `SHOPIFY` |
| Description | Agentic Storefronts (ChatGPT, Copilot, AI Mode and Gemini, Meta), the catalog MCP servers on UCP, WebMCP on every Liquid and Hydrogen storefront, Shop.md for third-party agents, and a knowledge base the merchant publishes to agents | 0.C |
| Strengths | Reach into AI assistants by default for eligible stores, with no channel fees per Shopify's Help pages | 0.C |
| Weaknesses | A US-buyer baseline with conflicting country rules. The conversation happens off the store, where the merchant does not own it | 0.C |
| Who it serves | Shopify merchants selling to US buyers | 0.C |
| Pricing | No channel fees per Help pages. The supplemental terms reserve the right to charge fees on some channels | 0.C |
| Outcome claims | Microsoft: Copilot journeys "194% more likely" to end in a purchase when shopping intent is present | `CLAIM`, 0.C |
