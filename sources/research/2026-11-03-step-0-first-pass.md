# Step 0 first pass, the Shopify competitive and implementer landscape

**Date:** 2026-11-03. **Method:** web search, run once across the categories in `../RESEARCH-PROMPTS.md` Step 0. **Status:** a head start for Step 0, not a substitute for it.

## Read this before using anything below

- **Existence is verified, nothing else is.** Every vendor here appeared in a search result with a working URL. Whether Pico's buyers actually evaluate it is not known, and that is the selection rule for the slate.
- **Most category content is written by vendors.** The roundups that rank AI shopping assistants are almost all published by a competitor in the list. Treat rankings, ratings, and price comparisons in them as marketing.
- **Prices are not recorded here, pricing models are.** Prices conflicted across sources for nearly every vendor. The pricing model (per conversation, per visitor, per resolution, flat tier) was consistent, and it is what Phase 9 needs first. Step 2.1 collects current prices from each vendor's own page, with the date.
- **Vendor outcome claims are recorded as claims.** They are evidence of how the category sells, never evidence of what any product does.
- **Individual agencies are not named.** They are the Run 2 audience. A named list of them is a prospect list, which belongs in a later sprint, not in strategy inputs. Directories and segments are named instead.

---

## 1. Shifts in the market since 2025 that change the strategy

Dated, because each one moves fast and each one changes a phase.

| Date | What happened | Why it matters to Pico | Source |
|---|---|---|---|
| 2024, extended June 2024 | Shopify's Search & Discovery app added semantic search for storefront search. Shopify's help page limits it to English storefronts with fewer than 200,000 products, on Shopify, Advanced, and Plus plans | The free native option already does meaning-based search for many English stores. Pico has no semantic vector search, so "smarter than Shopify search" is not a claim Pico can make | [Shopify Help](https://help.shopify.com/manual/online-store/search-and-discovery/search), [Shopify Changelog](https://changelog.shopify.com/posts/semantic-search-is-now-available-on-more-plans) |
| Summer 2025 | Shopify Knowledge Base, a free Shopify app, lets merchants edit the FAQs that AI shopping agents use when answering about the store | Shopify is building the merchant-side controls for off-site agents itself | [Shopify App Store](https://apps.shopify.com/shopify-knowledge-base), [Shopify Help](https://help.shopify.com/en/manual/promoting-marketing/knowledge-base) |
| 2025 to 2026 | Klaviyo launched Customer Agent with a shopping assistant role for Shopify brands. Its page says English only, with more languages in 2026 | The email platform in most Shopify stacks now ships an on-site agent. Language coverage is a live gap | [Klaviyo](https://www.klaviyo.com/solutions/ai/customer-agent/shopping-assistant) |
| 2026-01 | Shopify and Google announced the Universal Commerce Protocol (UCP), an open standard for agents to discover products, build carts, and check out | The rails for agent shopping are being set by the platform. Reported: Storefront MCP catalog and cart tools moved to a UCP endpoint, and Shopify's `shop-chat-agent` sample is deprecated | [Shopifreaks](https://www.shopifreaks.com/google-and-shopify-launch-universal-commerce-protocol/), [Craftshift, secondary](https://craftshift.com/?p=24004), [GitHub sample](https://github.com/Shopify/shop-chat-agent) |
| 2026-03 | OpenAI pulled back from Instant Checkout. Shopify said Agentic Storefronts would make products discoverable in ChatGPT and send checkout to the merchant's own store | Discovery is moving into AI assistants that are not on the store. Checkout stays with the merchant | [Modern Retail](https://www.modernretail.co/technology/shopify-says-purchases-are-coming-inside-chatgpt-through-agentic-storefronts-as-openai-retreats-on-instant-checkout/) |
| 2026-03-24 | Shopify Agentic Storefronts: merchants can sell to ChatGPT users, with Microsoft Copilot, AI Mode in Google Search, and the Gemini app named. Coverage disagrees on Perplexity | The status quo competitor is no longer "no AI". It is "Shopify already put my products in ChatGPT" | [Shopify News](https://shopify.com/news/agentic-commerce-momentum), [Practical Ecommerce](https://www.practicalecommerce.com/shopify-integrates-ai-product-discovery) |
| 2026-05 | Intercom launched Fin for Ecommerce, one agent for shopping help and support, built for Shopify merchants | Helpdesk incumbents now sell the shopping role inside the support seat a merchant already pays for | [Intercom](https://www.intercom.com/blog/announcing-fin-for-ecommerce/), [Shopify App Store](https://apps.shopify.com/fin) |
| 2026, Spring Edition | Shopify Inbox added an AI sales associate on the storefront that answers questions, suggests products, and handles order questions from catalog, inventory, and policy data. Inbox is free | **The most important line in this file.** Shopify now ships a free, native version of the core job. Every Pico argument has to survive "why not just turn on Inbox" | [Shopify News](https://www.shopify.com/news/spring-26-edition-merchant), [Qikify, secondary](https://qikify.com/blogs/all-articles/shopify-spring-edition) |
| 2026 | Shopify AI Toolkit wraps the Dev MCP server for Claude Code, Cursor, Codex, and other coding agents | Developers now install and build Shopify features through coding agents. Pico's downloadable setup skill fits this workflow, and Shopify's toolkit is also the "build it yourself" path | [Shopify.dev](https://shopify.dev/docs/apps/build/ai-toolkit) |
| 2026-06, 2026-08 | Bloomreach upgraded its Loomi conversational agent and launched a multi-agent "Ask Me Anything" | Enterprise discovery vendors describe in-stock, catalog-only answers too | [Las Vegas Sun, press release](https://lasvegassun.com/news/2026/aug/05/bloomreach-launches-multi-agent-ask-me-anything-ca/) |
| 2026-10 | Octane AI launched Phoenix, an AI quiz builder for Shopify | Guided selling through quizzes keeps moving toward conversation | [Business Wire via TT](https://via.tt.se/pressmeddelande/4610387/octane-ai-launches-phoenix-an-ai-quiz-builder-that-builds-checks-and-improves-quizzes-for-shopify-brands?lang=en) |

---

## 2. Direct competitors, AI shopping assistants and AI sales agents

Same promise as Pico: a shopper asks in their own words and gets products from the catalog.

| Vendor | Where found | What it is, per its listing or site | Pricing model | Note |
|---|---|---|---|---|
| Rep AI | [Shopify App Store](https://apps.shopify.com/rep-ai-sales-associate), [hellorep.ai affiliates](https://hellorep.ai/affiliates) | AI sales associate and live chat. Described as handling the shopping experience in chat, including checkout | Priced by site traffic or sessions | The most-cited name in 2026 roundups. One App Store reviewer called it not worth the monthly cost "for a basic LLM", per [eesel](https://www.eesel.ai/blog/rep-ai-review) |
| Manifest AI | [Shopify App Store](https://apps.shopify.com/manifest-ai-shopping-assistant) | ChatGPT-based shopping assistant trained on real-time product and inventory data, add to cart from chat | Free tier plus flat paid tiers | Closest to Pico's price band in the sources |
| Zipchat AI | [zipchat.ai](https://www.zipchat.ai/blog/best-shopify-chatbot-apps-2026) | Shopify chatbot for the storefront plus WhatsApp and other channels | Per conversation | Same value metric as Pico |
| Dialog | [Shopify App Store](https://apps.shopify.com/dialog-ai-sales-assistant), [askdialog.com](https://www.askdialog.com/resources/best-ai-shopping-assistant-shopify) | AI sales assistant that learns from catalog, documents, and blog. Also on Salesforce Commerce Cloud, BigCommerce, PrestaShop | Free Starter tier by conversations, paid tiers reported as visitor based | Reports into Google Analytics 4 |
| Alhena AI | [Shopify App Store](https://apps.shopify.com/gleen-ai), [alhena.ai](https://alhena.ai/blog/ai-agent-for-shopify/) | Shopping and support agents, including product expert, order, and returns agents. Voice option | Free plan on listing, higher tiers reported | Sits on top of helpdesks such as Gorgias and Gladly |
| Envive | [envive.ai](https://www.envive.ai/) | Sales agent, search agent, and SEO or GEO content agent for mid-market and enterprise brands | Not public | Raised a $15M Series A ([Digital Commerce 360](https://www.digitalcommerce360.com/2025/09/29/envive-ai-15-million-series-a-funding/)). Homepage claims a conversion lift for engaged visitors |
| Big Sur AI | [Shopify App Store](https://apps.shopify.com/bigsurai) | Conversational discovery, smart search, adaptive quiz, recommendations | Fixed fee or commission on driven sales | [StoreLeads](https://storeleads.app/reports/shopify/app/bigsurai) reports it was removed from the App Store on 2026-05-15. Status unclear |
| Wizybot | [Shopify App Store](https://apps.shopify.com/wizybot) | AI chatbot and CRM with WhatsApp, Instagram, and Messenger | Flat paid tiers | Larger review base than most |
| Octocom | [octocom.ai](https://www.octocom.ai/upselling) | Support and sales agent across chat, email, WhatsApp, Instagram, SMS. Claims 80 to 100+ languages | Not confirmed | Multilingual claims are directly relevant to Pico's |
| Chatty | [Analyzify listing](https://analyzify.com/shopify-apps/chatty-ai-chatbot-live-chat) | AI chatbot trained on catalog and FAQs, live chat, WhatsApp, Instagram | Free to install, flat tiers | Review complaints include irrelevant recommendations, per [eesel](https://www.eesel.ai/blog/chatty-review) |
| Wantly | [Shopify App Store](https://apps.shopify.com/wantly-chat) | Replaces standard storefront search with a conversational assistant, voice input, real-time inventory sync | Not confirmed | Positions directly against search |
| Smaller Shopify listings | [DBestChatBot](https://apps.shopify.com/dbestchatbot), [SetuBridge AI Shopping Assistant](https://apps.shopify.com/ai-shopping-assistant-chat-bot), [AI Shopping Agent & Support](https://apps.shopify.com/ai-shopping-agent), [AI Sales and Conversion Patrol](https://apps.shopify.com/ai-sales-patrol), [Selli](https://apps.shopify.com/ai-sales-assistant), [AE AI Chatbot](https://appnavigator.io/app/ai-chatbot-sales-support/) | Catalog-synced chat with product cards and add to cart | Mostly free plans plus flat tiers | Most have zero to a handful of reviews. Evidence that catalog grounding and add to cart are table stakes |
| Vendors publishing category roundups | [Dori](https://dori.tech/blog/best-ai-shopping-assistant-shopify-2026), [Talkbar](https://talkbar.ai/blog/shopify-ai-shopping-assistant), [Kovax](https://www.kovax.ai/blog/ai-shopping-assistants/), [Brink](https://trybrink.com/blog/seven-ai-shopping-assistants-shopify-2026-compared), [Nobi](https://www.nobi.ai/blog/best-ai-search-ecommerce-2026), [Shoply AI](https://www.shoplyai.ai/blog/shoply-vs-gorgias) | Each sells an assistant, search, or support agent | Varies | Their roundups are where many merchants first meet the category. Read them in Step 2.1 for how the category describes itself |

---

## 3. Indirect competitors, same job done another way

### 3a. Support platforms that added a shopping role

| Vendor | Where found | Shopping role | Pricing model |
|---|---|---|---|
| Shopify Inbox | [Shopify News](https://www.shopify.com/news/spring-26-edition-merchant) | AI sales associate on the storefront, see Section 1 | Free |
| Tidio with Lyro | [Shopify App Store](https://apps.shopify.com/tidio-chat), [tidio.com](https://www.tidio.com/shopify/) | Live chat plus Lyro AI agent, product recommendations from Shopify data and chosen metafields | Conversation bundles on top of plans |
| Gorgias Shopping Assistant | [eesel pricing analysis](https://www.eesel.ai/blog/gorgias-ai-agent-pricing-2025), [Gorgias partners](https://www.gorgias.com/partners) | Pre-purchase module alongside the support agent | Per resolution, on top of helpdesk plans |
| Intercom Fin for Ecommerce | [Intercom](https://www.intercom.com/blog/announcing-fin-for-ecommerce/) | One agent for shopping and support, built for Shopify | Per outcome on listing |
| Klaviyo Customer Agent | [Klaviyo](https://www.klaviyo.com/solutions/ai/customer-agent/shopping-assistant) | Shopping assistant role, web chat, SMS, email | Not confirmed |
| Siena AI, Yuma AI | [eesel comparison](https://www.eesel.ai/es/blog/siena-ai-vs-yuma-ai-comparativa), [Yuma](https://yuma.ai/compare-yuma/yuma-ai-vs-siena) | Ecommerce support agents with a sales AI role | Per conversation plus platform fee, sales-led |
| Richpanel, Willdesk | [Shero Commerce](https://sherocommerce.com/pages/shopify-siena-ai-integration), [Skailama roundup](https://www.skailama.com/blog/best-shopify-live-chat-apps) | Helpdesks with built-in AI | Flat tiers |

### 3b. On-site search and discovery

| Vendor | Where found | Relevance to Pico |
|---|---|---|
| Shopify Search & Discovery | [Shopify Help](https://help.shopify.com/manual/online-store/search-and-discovery/search) | Free, native, semantic search for eligible English stores. The status quo |
| Boost AI Search & Discovery | [Boost Commerce](https://boostcommerce.net/platform/boost-klevu) | Filters and search at scale, low cost |
| Searchanise | [Searchanise](https://searchanise.io/searchanise-vs-boost-commerce/) | Upgrade from default search, self-reported 16,000+ stores |
| Doofinder | [Doofinder](https://www.doofinder.com/en/blog/shopify-search-apps) | Noted for multi-language, image, and voice search |
| Klevu, now part of Athos Commerce with Searchspring | [Nobi, secondary](https://nobi.ai/blog/athos-commerce-alternatives-ecommerce) | Enterprise AI search |
| Fast Simon | [Fast Simon](https://fastsimon.com/technologies/ai-shopping-assistants/) | Search suite that includes an AI shopping agent at no extra SKU |
| Motive Commerce Search | [Motive](https://www.motive.co/blog/best-shopify-search-app) | Search app with AI features |
| Prefixbox | [Prefixbox](https://www.prefixbox.com/blog/shopify-semantic-search-frustration) | Publishes on the limits of Shopify semantic search |
| Coveo | [Shopify App Store](https://apps.shopify.com/coveo) | Enterprise AI search and discovery |
| Kimonix, Nimstrata | [Kimonix](https://www.kimonix.com/blog/best-shopify-search-discovery-apps), [Nimstrata](https://nimstrata.com/article/best-shopify-search-apps-2026) | Merchandising and search vendors publishing comparisons |
| Algolia, Constructor, Bloomreach | [RFP Wiki](https://www.rfp.wiki/retail-ecommerce/search-product-discovery/fast-simon/algolia), [Ringly on Constructor](https://www.ringly.io/blog/constructor-alternatives), [Bloomreach release](https://lasvegassun.com/news/2026/aug/05/bloomreach-launches-multi-agent-ask-me-anything-ca/) | Enterprise and developer-first. Algolia's Agent Studio lets teams build their own shopping agent on an Algolia index |

### 3c. Recommendations, upsell, and personalization

| Vendor | Where found | Relevance |
|---|---|---|
| Rebuy | [Rebuy partners](https://rebuyengine.com/partners) | Most-reviewed recommendations app per one comparison, deep DTC stack integrations, strong agency program |
| LimeSpot, Wiser, Glood, Nosto, Maestra, AiTrillion | [Wiser Review](https://wiserreview.com/blog/limespot-alternatives/), [Personalizer AI](https://personalizerai.com/blog/best-limespot-alternatives-for-shopify), [Wiser](https://www.getwiser.ai/blog/best-ai-shopify-search-and-discovery-apps/) | Widget-based recommendations. A merchant who has one may see conversational discovery as overlap |

### 3d. Quizzes and guided selling

| Vendor | Where found | Relevance |
|---|---|---|
| Octane AI | [Shopify App Store](https://apps.shopify.com/octane-ai-quiz-personalization) | Quiz builder, Phoenix AI builder launched 2026-10, tight Klaviyo sync |
| RevenueHunt | [Shopify App Store](https://apps.shopify.com/product-recommendation-quiz-revenuehunt), [comparison](https://revenuehunt.com/compare/octane-ai/) | Recommender quiz with a large review base |

### 3e. Video commerce with an AI layer

| Vendor | Where found | Relevance |
|---|---|---|
| Tolstoy | [Shopify App Store](https://apps.shopify.com/tolstoy), [comparison page](https://www.gotolstoy.com/tolstoy-vs-videowise) | Shoppable video with an AI shopping assistant |
| Videowise | [Videowise](https://videowise.com/app-comparisons/tolstoy-vs-reefly-which-shoppable-video-app-is-best) | Shoppable and live video stack |

### 3f. Messaging commerce

Most relevant for Arabic-speaking markets, where shoppers often ask on WhatsApp rather than on the site.

| Vendor | Where found | Relevance |
|---|---|---|
| Zoko | [Zoko](https://www.zoko.io/post/whatsapp-marketing-automation-ai-tools) | WhatsApp commerce for Shopify, AI agents, catalog sync |
| WATI | [WATI](https://www.wati.io/en/blog/best-ai-sales-agents-shopify/) | WhatsApp platform, Shopify app with an AI agent for FAQs and product help |
| Interakt | [Zoko comparison](https://www.zoko.io/post/interakt-vs-wati-comparison) | Budget WhatsApp option with catalog sharing |

### 3g. General AI chatbot builders

| Vendor | Where found | Relevance |
|---|---|---|
| Voiceflow | [Voiceflow](https://www.voiceflow.com/integrations/shopify) | Agent builder with a Shopify integration, catalog search |
| Chatbase | [Chatbase](https://www.chatbase.co/blog/best-whatsapp-chatbots-ecommerce) | Agent trained on business data, snippet deploy |
| Jotform AI Chatbot | [Jotform](https://agent.jotform.com/ai/chatbot/shopify/) | Generic AI chatbot with a Shopify page |

---

## 4. Build it or hire it

| Alternative | What it looks like | Evidence |
|---|---|---|
| Build on Shopify's agent rails | A developer wires an LLM to the store through UCP or the Storefront MCP, using Shopify's AI Toolkit in a coding agent | [Shopify AI Toolkit](https://shopify.dev/docs/apps/build/ai-toolkit), [deprecated sample](https://github.com/Shopify/shop-chat-agent) |
| Hire chat staff | In-house or outsourced live chat on Shopify Inbox or a helpdesk | Vendor-sourced estimates put outsourced chat at roughly $6 to $42 an hour by region ([Ringly, vendor](https://www.ringly.io/blog/cost-to-outsource-customer-service-ecommerce)). Use as a range to verify, not a benchmark |
| Hire a freelancer or agency to build a custom assistant | A paid project on a freelance marketplace or with a Shopify agency | [Storetasker](https://storetasker.com/), plus Upwork and Fiverr gig searches in Step 0.D |
| Do nothing | Default search, filters, collections, and better product copy | The most common competitor in most categories. Profile it in Phase 3's status quo statement |

---

## 5. The implementer landscape (Run 2 audience, not competitors)

| Segment | Where to find them | What the evidence says |
|---|---|---|
| Shopify Partner Directory agencies | Shopify Partner Directory | Five tiers, Registered, Select, Plus, Premier, Platinum. Published counts per tier conflict between sources ([mgroupweb](https://mgroupweb.com/blogs/shopify-partner-directory/), [Qualimero](https://qualimero.com/en/blog/shopify-partner)). Tiers describe track record, not fit |
| CRO agencies | 2026 roundups ([Ecommerce Fastlane](https://ecommercefastlane.com/top-shopify-cro-agencies-2026/), [Skailama](https://www.skailama.com/blog/top-10-shopify-cro-agency)) | A recurring set of 10 to 15 names, mostly self-ranked. They sell conversion work, so they will ask for the conversion data Pico does not measure |
| Freelance Shopify developers | [Storetasker](https://storetasker.com/), Upwork, Fiverr | Storetasker vets and matches experts rather than running bids |
| Theme developers and designers | Shopify Theme Store | Premium theme houses report tens of thousands of merchants per theme, one claims 60,000+ ([Martechvibe](https://martechvibe.com/article/wecommerce-acquires-assets-of-archetype-themes-inc)). A theme partner reaches more stores than an agency does |
| Developers working through coding agents | Shopify AI Toolkit users in Claude Code, Cursor, Codex | The audience Pico's setup skill already targets |
| Arabic-language and Gulf Shopify agencies | Partner Directory, filtered by UAE, Saudi Arabia, Egypt, and Arabic | Plus-tier partners in Dubai list Arabic and right to left localization as a service. Egypt-based results were thin |
| Communities | [Shopify .dev forum and Partner Slack](https://shopify.com/partners/blog/announcing-the-new-shopify-dev-community-forums), Shopify Devs Discord (third party), [Shopify Community](https://community.shopify.com/) | Shopify routes developer troubleshooting to the .dev forum and keeps Partner Slack for peer connection |

### Partner program benchmarks

What implementers already get from apps they recommend. Phase 9 of Run 2 reads this.

| Program | Structure found | Source |
|---|---|---|
| Shopify Partner Program | Revenue share on referred merchants, app revenue share terms by earnings band, Partner Directory listing | [Shopify Help](https://help.shopify.com/en/partners/how-to-earn) |
| Gorgias | Agency tiers Partner, Premier, Elite, plus a certified Services Partner track. Separate affiliate program with a top tier at 40% revenue share for 2 years at 100+ customers | [Gorgias docs](https://docs.gorgias.com/en-US/agency-partner-program-81969), [Gorgias affiliates](https://www.gorgias.com/affiliate-program) |
| Gorgias, partnership share | PartnerStack case study titled as partnerships driving 50% of Gorgias revenue | [PartnerStack](https://www.partnerstack.com/customers/gorgias) |
| Rebuy | Up to 20% revenue share, Bronze, Silver, Gold tiers, four ways to join, model changed 2026-01-01 | [Rebuy partners](https://rebuyengine.com/partners), [Rebuy 2026 update](https://help.rebuyengine.com/en/articles/13690188-rebuy-partner-program-updates-2026) |
| Klaviyo | Agency tiers with training requirements per tier, profit sharing, directory listing | [Klaviyo Academy](https://academy.klaviyo.com/en-us/courses/partner-program-fundamentals/lessons/differentiate-partner-program-tracks-and-tiers) |
| Rep AI | Affiliate program exists | [hellorep.ai](https://hellorep.ai/affiliates) |

---

## 6. Regional, Arabic-speaking markets

| Finding | Source |
|---|---|
| Arabic-first AI assistants exist for Salla and Zid, the Saudi platforms, mostly WhatsApp-led | [Mando AI](https://mando.cx/solutions/e-commerce/salla), [Nano AI](https://www.nano-ai.net/en/services/salla-zid-whatsapp-ai), [Zoe](https://zoe-agent.com/salla-store-owners-whatsapp-ai/) |
| Arabic AI chat products also target Shopify in the Gulf and Levant | [Assistli](https://www.assistli.ai/ai-chatbot-for-ecommerce), [ATMET](https://atmet.app/en/blog/shopify-whatsapp-arabic), [LetsBot](https://letsbot.net/en/blogs/ksa-e-commerce-chatbots-personalized-shopping-2026.html) |
| One tracker of detected sites puts WooCommerce at 47.2% and Shopify at 37.4% of ecommerce sites in Egypt in 2026 | [wmtips](https://www.wmtips.com/technologies/e-commerce/country/eg/) |
| Egypt has local store builders that compete with Shopify, for example ExpandCart, which claims 20,000+ merchants | [MENAbytes](https://www.menabytes.com/expandcart-series-a/) |

**What this means.** In Egypt and Saudi Arabia, a large share of stores are not on Shopify or Shopware, so Pico reaches them only through the custom catalog API. And InstaPay applies to Shopware and custom stores, not to Shopify App Store installs, which bill through Shopify Billing. Both facts shape the geography decision in `../GTM-BRIEF.md`.

---

## 7. Sizing data points, with their conflicts

| Measure | Range found | Why it conflicts | Source |
|---|---|---|---|
| Live Shopify stores | About 2.8M (StoreLeads, 2026-02) to about 6.9M (BuiltWith, 2026-02) | Different definitions of a live store | [ecomm.design](https://ecomm.design/how-many-shopify-stores-are-there/), [Style Factory](https://www.stylefactoryproductions.com/blog/key-shopify-statistics) |
| Shopify Plus stores | About 52K to 85K | Different trackers and dates | Same compilations |
| Shopify Partner Directory agencies by tier | Conflicting counts | Tiers change quarterly | [mgroupweb](https://mgroupweb.com/blogs/shopify-partner-directory/) |

**Rule for Phase 4.** Pick one source, state its method and date, and never mix figures from two trackers in one calculation. Shopify itself no longer publishes a store count.

---

## 8. Pricing models in the category

The finding Phase 9 needs first. Prices themselves are collected in Step 2.1.

| Model | Who uses it, per sources | Buyer risk the model creates |
|---|---|---|
| Per conversation | Pico, Zipchat, Tidio Lyro bundles, Dialog Starter | Cost follows engagement. Needs a clear definition of one conversation |
| Per visitor or session | Rep AI, Dialog paid tiers | Cost follows traffic whether or not shoppers use the assistant |
| Per resolution or outcome | Gorgias AI Agent, Intercom Fin | Cost follows success but can surprise. One analysis reports a five-figure overage for one brand |
| Flat tiers | Manifest AI, Wizybot, Chatty, Willdesk | Predictable, often capped by features |
| Commission on driven sales | Big Sur AI | Needs attribution the merchant trusts |
| Free and native | Shopify Inbox AI sales associate | Sets the price floor at zero |

## 9. How the category sells, recorded as claims

The category leads with conversion and revenue lift. Envive's homepage claims a conversion lift for engaged visitors. Big Sur AI's funding release reported higher conversion for engaged shoppers. Bloomreach cited one customer's conversion and revenue-per-visitor lift. None of these is independent, and Pico measures none of these outcomes. That gap is the governing sensitivity in `../GTM-BRIEF.md` Section 5.

---

## What this pass did not do

- No review analysis. That is Step 2.7.
- No verification of current prices or plan limits. That is Step 2.1.
- No full sweep of Shopify App Store categories and search terms. Step 0.A lists the terms.
- No check of whether buyers evaluate any of these. That is the operator's call when the slate is confirmed.
- No research of Shopware 6 beyond a scan. Shopware plugins found include an AI product advisor, Blackrobe AI Agent, Chatixy, and a UCP shopping assistant plugin, per the [Shopware Store](https://store.shopware.com/en/fel7054049764027m/ai-product-advisor-shopping-experience.html). That belongs to a later run.
