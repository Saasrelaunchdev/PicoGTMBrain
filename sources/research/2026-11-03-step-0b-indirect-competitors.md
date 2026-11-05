# Step 0.B: Indirect competitors, the same job done another way

**Date checked:** 2026-11-03. **Prompt:** `../RESEARCH-PROMPTS.md` Step 0.B. **Extends:** `2026-11-03-step-0-first-pass.md` Section 3.

**Method and limits.** Web search only, because this session's network policy blocks page loads. Provenance codes follow `2026-11-03-step-0a-direct-competitors.md`: `IDX` App Store listing via the search index, `VEN` vendor page via the search index, `3P` third party, `CLAIM` outcome claim. Install counts come from **StoreLeads**, a third-party tracker that detects a subset of installs from storefront code, so every count is a lower-bound estimate and StoreLeads' own pages give slightly different figures by snapshot. Both are shown where they differ. Never add StoreLeads counts to counts from another tracker.

---

## The answer the prompt asks for first: what a merchant most likely already has

Ranked by StoreLeads detected installs, 2026-11-03. These are the apps a merchant is most likely to see Pico as overlapping with.

| Category | Most likely already installed | StoreLeads installs (year-over-year) | Source |
|---|---|---|---|
| 1. Support with a shopping role | **Shopify Inbox** | 355,420 to 358,008 (down 5.7%) | [StoreLeads](https://storeleads.app/reports/shopify/app/inbox) |
| | **Tidio** | 27,499 to 27,707 (down 10.2%) | [StoreLeads](https://storeleads.app/reports/shopify/app/tidio-chat) |
| | **Gorgias** | 25,120 to 25,614 (up 13.7%) | [StoreLeads](https://storeleads.app/reports/shopify/app/helpdesk) |
| | Chatty | 8,968 (down 1.7%) | [StoreLeads](https://storeleads.app/reports/shopify/app/chatty) |
| | Klaviyo, for whom Customer Agent is an add-on | 431,041 to 458,365 for the email and SMS app | [StoreLeads](https://storeleads.app/reports/shopify) |
| 2. Search and discovery | **Shopify Search & Discovery** | Count not found. Free and native | [listing](https://apps.shopify.com/search-and-discovery) |
| | **Boost AI Search & Filter** | 20,487 (down 18.2%) | [StoreLeads](https://storeleads.app/reports/shopify/app/product-filter-search) |
| | **Smart Product Filter & Search** | 16,290 to 16,597 (down 19.2%) | [StoreLeads](https://storeleads.app/reports/shopify/app/product-filter-and-search) |
| | Searchanise | 12,606 to 12,808 (up 14.6%) | [StoreLeads](https://storeleads.app/reports/shopify/app/searchanise) |
| 3. Recommendations and upsell | **Rebuy** | 15,008 to 15,175 (up 24.7%) | [StoreLeads](https://storeleads.app/reports/shopify/app/rebuy) |
| | **LimeSpot** | 6,149 to 6,890 | [StoreLeads](https://storeleads.app/reports/shopify/app/limespot) |
| | Wiser | 3,746 (down 11.7%) | [StoreLeads](https://storeleads.app/reports/shopify/app/recommended-products-wiser) |
| 4. Quizzes | **RevenueHunt** | 12,070 | [StoreLeads](https://storeleads.app/reports/shopify/app/product-recommendation-quiz-revenuehunt) |
| | **Octane AI** | 4,286 to 4,328. Top category Beauty & Fitness, 39% of its stores | [StoreLeads](https://storeleads.app/reports/shopify/app/octane-ai-quiz-personalization) |
| 5. Shoppable video | **Tolstoy** | 9,503 to 9,597 | [StoreLeads](https://storeleads.app/reports/shopify/app/tolstoy) |
| 6. Messaging commerce | **Zoko**, **Interakt** | Installs not found. Review counts lead the WhatsApp apps sampled (Section 6) | `IDX` |
| 7. General chatbot builders | None dominant on Shopify | Installs not found | |
| 8. Enterprise discovery | Not installed by small stores. For Plus brands: Algolia, Bloomreach, Constructor, Athos (Searchspring and Klevu), Nosto | Contract-based | Section 8 |
| Direct, for scale | Zipchat 1,952 to 2,135 (up 100.4%). Rep AI 1,007 to 1,012 (up 3.9%). Wizybot 944 to 961. Dialog 379 (up 121.6%). Manifest AI 308 to 334 | | [StoreLeads ranking](https://storeleads.app/reports/shopify/most-installed-apps), app pages |

**Reading it.** The installed base for "help shoppers find the right product" sits overwhelmingly in free native Shopify tools and in search, recommendation, and quiz apps, not in AI shopping assistants. A merchant with Boost, Rebuy, and Inbox already installed is the normal case for an established store. The fastest-growing direct apps (Zipchat, Dialog) are still two orders of magnitude below Inbox. That supports the brief's slot logic: slots 2 and 3 (Inbox and native search) are what Pico is weighed against most often.

---

## 1. Support helpdesks and support AI agents that added a shopping role

| Vendor | Listing or site | Rating (reviews) | Pricing model and prices, as indexed 2026-11-03 | Shopping role | Who it says it serves |
|---|---|---|---|---|---|
| **Shopify Inbox** | [listing](https://apps.shopify.com/inbox) | 4.6 (5,810 to 5,813) | Free | See 0.C. Recommends products, starts checkout from chat, order lookups for signed-in shoppers | All Shopify merchants on Basic and up |
| **Tidio with Lyro** | [listing](https://apps.shopify.com/tidio-chat), [Lyro](https://www.tidio.com/ai-agent/) | 4.8 (1,355 to 1,356) | Helpdesk plans: Starter $29 monthly ($24.17 annual) with 100 conversations, Growth from $59 ($49.17 annual), Plus from $300 plus usage, Premium custom. Lyro is a separate per-conversation add-on, about $0.50 to $0.65 per conversation, with 50 free Lyro conversations once per account ([Tidio](https://www.tidio.com/blog/chatbot-pricing/), `VEN`) | Lyro recommends products from Shopify product data, skips out-of-stock items, and needs a paid Lyro package or the 7 day trial. Product content in custom theme blocks outside the Shopify product schema is not read ([Tidio Help](https://help.tidio.com/hc/en-us/articles/15960742181148-Product-Recommendations-for-Shopify)). A "Lyro Shopping Assistant" update improved recommendations ([Tidio updates](https://updates.tidio.com/en/lyro-ai-agent-more-effective-recommendations-by-lyro-shopping-assistant-7VoW1YdF)) | Small and mid-size online businesses. Lyro speaks 48 languages including Modern Arabic ([Tidio Help](https://help.tidio.com/hc/en-us/articles/12643043611036-Lyro-Multilanguage-support)) |
| **Gorgias Shopping Assistant** | [listing](https://apps.shopify.com/helpdesk), [pricing](https://www.gorgias.com/pricing) | 4.3 (709), about 10% one-star | Helpdesk plans plus AI Agent interactions at $0.90 annual or $1.00 monthly. Overage $1.50 per interaction on Support plus Shopping Assistant plans ([Gorgias](https://www.gorgias.com/blog/ai-agent-pricing), `VEN`) | Recommends similar, complementary, and popular products, with promote, exclude, and block controls. Adjusts to discovery, interested, and ready-to-buy stages. Can offer discounts ([Gorgias Help](https://helpcenter.gorgias.com/en-US/articles/ai-agent-and-automations-135134)). `CLAIM`: 62% conversion uplift | Ecommerce brands, mostly Shopify. Agency programs in 0.G |
| **Intercom Fin for Ecommerce** | [listing](https://apps.shopify.com/fin), [Help](https://www.intercom.com/help/en/articles/14997821-fin-for-ecommerce-explained) | 3.7 (18) | $0.99 per resolution, 50 resolutions a month minimum, spend caps. Product clicks, add to cart, and checkout starts carry no extra charge (`VEN`) | One agent for shopping help and support. Shopify only. Multi-store: several Shopify stores in one Intercom workspace (per a review reply) | Shopify brands with support teams. Launched 2026-05 (first pass) |
| **Klaviyo Customer Agent** | [Customer Agent](https://www.klaviyo.com/solutions/ai/customer-agent), [billing help](https://help.klaviyo.com/hc/en-us/articles/115000976672) | Not on the App Store as a separate app | Priced on shopper-initiated conversations resolved, from **$50 a month for up to 75 conversations**. A conversation becomes billable when the agent responds and 48 hours pass without a shopper reply. Minimum spend commitment, flexible overages on by default. The solutions page also shows 1,000 AI resolutions a month for $700. 50 free conversations to try (`VEN`) | Shopping assistant role on web chat, email, SMS, and WhatsApp. **113 languages per the product page**, which supersedes the earlier English-only note in the first pass. Full web chat function requires Shopify. Uses Shopify Markets for regional catalogs. Open APIs for headless storefronts | Klaviyo's base, which is most Shopify DTC brands |
| **Siena AI** | Per [Yuma](https://yuma.ai/compare-yuma/yuma-ai-vs-siena), a competitor | Not found | About $750 a month plus about $0.90 per automated conversation, sales-led (`3P`, competitor-sourced) | Sales AI role alongside support, actions on Shopify, Zendesk, Kustomer | Mid-market ecommerce |
| **Yuma AI** | [listing](https://apps.shopify.com/yuma) | Not found | "From $850/month". About $1.20 per resolution, escalations unbilled, 30 day trial (`IDX`, `VEN`) | Mainly support: 75+ Shopify actions, returns, subscriptions, order status | Mid-market ecommerce on Gorgias, Zendesk, and others |
| **Richpanel** | [listing](https://apps.shopify.com/customer-support), [site](https://www.richpanel.com/) | Not found | Listing "From $89", Pro Max $119. Vendor content: $99 per seat a month annual, plus about $0.20 per AI conversation with a $200 AI minimum. Conflict | Product recommendations on higher tiers | DTC support teams |
| **Willdesk** (Channelwill) | [listing](https://apps.shopify.com/self-faq) | 4.7 (377 to 383) | Free with 20 conversations, Basic $16.90, higher $89.90 plus overage. Listing about 2,500 days old | Product recommendations, emotion detection. Reviewers complain about undisclosed AI fees and weak variant handling | Small Shopify stores |
| **Moose AI Chatbot & Live Chat** (Vegahub Technology) | [listing](https://apps.shopify.com/moosedesk) | 5.0 (453 to 490) | Free plan, $19, $49, $249, 7 day trial | Learns from products, FAQs, and past Q&A. Product recommendations not described | Small and growing stores |
| **Commslayer** | [listing](https://apps.shopify.com/commslayer), [pricing](https://www.commslayer.com/pricing) | 4.9 (238) | Free plan, $39, $99, AI agent on every plan, extra conversations $0.15 | Product recommendations in the feature list | Shopify brands leaving Gorgias, per its own marketing |
| **Redo** | Helpdesk category | 4.9 (839) | Free to install | Returns and support first | Shopify brands |
| **Smartsupp with Mira AI** | [listing](https://apps.shopify.com/smartsupp-chat), [Mira](https://www.smartsupp.com/mira-ai-shopping-assistant/) | 2.3 (4) | Mira add-on from €16 a month for 100 AI conversations, up to 5,000 | Shopping assistant add-on to live chat. `CLAIM`: 70% of inquiries resolved, 25% more chat-driven sales | European SMB online stores |
| Others in the category | Re:amaze ([StoreLeads](https://storeleads.app/reports/shopify/app/reamaze)), eDesk ([listing](https://apps.shopify.com/helpdesk-app)), Chatway, Zendesk, Gladly, Kustomer | Not profiled | | Support-first | |

---

## 2. On-site search and discovery apps

| Vendor | Listing or site | Rating (reviews) | Pricing, as indexed | Conversational assistant? | StoreLeads installs |
|---|---|---|---|---|---|
| **Shopify Search & Discovery** | [listing](https://apps.shopify.com/search-and-discovery) | **2.6 (514)** | Free | Semantic search, filters, synonyms, boosts, recommendations, no-results and no-clicks reports. No assistant (see 0.C) | Not found |
| **Smart Product Filter & Search** | [StoreLeads](https://storeleads.app/reports/shopify/app/product-filter-and-search) | 4.9 (2,190 to 2,394) | Free plan | No. AI semantic search and filters | 16,290 to 16,597 |
| **Searchanise Search & Filter** | [listing](https://apps.shopify.com/searchanise) | 4.7 (1,149 to 1,265) | Free plan. $19, $39, $49 on the listing, up to $349 by catalog size. 14 day trial | Not found. AI relevance and voice search | 12,606 to 12,808 |
| **Boost AI Search & Filter** | [listing](https://apps.shopify.com/product-filter-search), [pricing](https://boostcommerce.net/platform/pricing) | 4.7 to 4.8 (1,500 to 1,635) | From $29, tiered by store GMV. Convert at $239 or $299 and Accelerate at $399 or $699 in different sources. 21 day trial. Reviewers complain of price rises | Not found | 20,487 |
| **Doofinder** | [listing](https://apps.shopify.com/doofinder) | 4.7 (762) | $61, $186, $436, 15 day trial. Billed on requests. Reviewers report search stopping at usage limits | Not found. Noted for multi-language, image, and voice search (first pass) | 3,311 to 3,355 |
| **Fast Simon AI Search & Filters** | [listing](https://apps.shopify.com/instant-search) | 4.8 (355) | Free for 100 sessions. $39.99 for 2,000 sessions, $114.99 for 10,000, $299.99 for 30,000. A reviewer says bot traffic inflates session billing | **Yes**, AI Shopping Agents, pricing not visible. `CLAIM`: AI shopper agents "lift product discovery conversion to 22%" ([press](https://www.fastsimon.com/press/fast-simon-analysis-shows-ai-shopper-agents-lift-product-discovery-conversion-to-22/)) | 1,984 to 1,989 |
| **Prefixbox AI Search & Filter** | Search and filters category | (59) | `?` | **Yes**, AI chat for discovery | Not found |
| **Athos Commerce** (Searchspring and Klevu, merged January 2025) | [Business Wire](https://www.businesswire.com/news/home/20250113743474/en/Klevu-Joins-Forces-with-Searchspring-to-form-Athos-Commerce) | Klevu app 4.9 (12). "Athos: Unified Discovery" 3.7 (18) | Searchspring about $799 a month and Klevu about $449 a month per one competitor blog. Klevu modules up to $1,647 a month per another. Quote-based | Reported: a conversational tool called Asklo, and conversational assistants in a June 2026 platform release. Not confirmed from Athos. Legacy platforms retire from 2027 | Not found |
| **Nosto** | [listing](https://apps.shopify.com/nosto-personalization-for-shopify) | 4.7 (61) | Quote-based | Search plus recommendations | Not found |
| Mid-size search apps | [XCloud](https://apps.shopify.com/cloudsearch) (480 to 1,070 reviews), [Rapid Search](https://apps.shopify.com/rapid-search) 4.9 (418), [AI Search & Product Filter SB](https://apps.shopify.com/ultimate-search-and-filter-1), [Motive](https://apps.shopify.com/motive-commerce-search) (conversational search on all plans), [Seekr](https://apps.shopify.com/seekr) ($19 tier has multi-turn conversational search and zero-result insight), [Celebros](https://apps.shopify.com/celebros-search), [Vespo](https://apps.shopify.com/vespo), [Coveo](https://apps.shopify.com/coveo) | | | Motive and Seekr describe conversational search | |

**What changes in this category.** Search apps are adding conversational layers (Fast Simon, Prefixbox, Motive, Seekr, Athos). A merchant who already pays Boost or Searchanise is the ICP Level 2 store in `../SKILL-ADAPTATION.md` Phase 4, and the brief's slot 3 swap note already anticipates naming them. Boost and Smart Product Filter lost about a fifth of detected installs year over year while Searchanise grew, which suggests churn inside the category rather than exit from it.

---

## 3. Product recommendation, upsell, and personalization apps

| Vendor | Listing | Rating (reviews) | Notes | StoreLeads installs |
|---|---|---|---|---|
| **Rebuy Personalization Engine** | [listing](https://apps.shopify.com/rebuy) | 4.7 (744) | AI recommendations on cart, checkout, and post-purchase. Deep DTC stack integrations and a tiered agency program (0.G) | 15,008 to 15,175, up 24.7% |
| **LimeSpot** | [listing](https://apps.shopify.com/limespot) | 4.6 (508) | Bundles, cross-sell, upsell at checkout. Recent negatives on pricing and service | 6,149 to 6,890 |
| **Wiser** | [listing](https://apps.shopify.com/recommended-products-wiser) | 4.9 (567) | One reviewer reports being charged a share of all site sales, not only attributed ones | 3,746, down 11.7% |
| **Glood** | [listing](https://apps.shopify.com/recommendation-kit) | 4.7 to 4.8 (110 to 123) | A reviewer reports an auto-positioned widget rendering when not called and raising cost | Not found |
| **Nosto** | [listing](https://apps.shopify.com/nosto-personalization-for-shopify) | 4.7 (61) | Recommendations and search, also on Shopware, Adobe, Salesforce, BigCommerce | Not found |
| Others in the first pass | Maestra, AiTrillion, Frequently Bought Together style apps | | Widget-based recommendations | |

**Overlap reading.** These apps recommend from behavior, on product, cart, and checkout pages. Pico recommends from what the shopper says. A merchant with Rebuy may still see Pico as overlap, so Phase 3's indirect statement has to name the difference in input (stated need versus browsing history), not claim better recommendations.

---

## 4. Product quiz and guided selling apps

| Vendor | Listing | Rating (reviews) | Pricing, as indexed | StoreLeads installs |
|---|---|---|---|---|
| **RevenueHunt** | [listing](https://apps.shopify.com/product-recommendation-quiz-revenuehunt) | 4.9 (about 400 to 460) | Free for 100 quiz responses a month. $39 for 500, Pro $99, Premium $199. The developer says Basic has been $39 since 2019 | 12,070 |
| **Octane AI** | [listing](https://apps.shopify.com/octane-ai-quiz-personalization) | Count not visible | $50 (two quizzes), $200 (unlimited quizzes and A/B tests), $500. 14 day trial. Phoenix, an AI quiz builder, launched 2026-10 (first pass) | 4,286 to 4,328. Beauty & Fitness is 39% of its stores |
| Quiz Kit, GiftX, AE gift finder | [Quiz Kit](https://apps.shopify.com/quiz-kit), [GiftX](https://apps.shopify.com/giftx-ai-shopping-assistant) | | Quiz-style AI chat is converging with assistants | |

**Overlap reading.** Quizzes are the guided-selling incumbent in categories where shoppers need help choosing, which are the same categories the brief's niche names. Octane's base skews to beauty and fitness. A quiz asks the merchant's questions in the merchant's order. A conversation lets the shopper start from their own words. That is the honest Phase 3 contrast, and it is a description, not a superiority claim.

---

## 5. Shoppable video with an AI layer

| Vendor | Listing | Rating (reviews) | Pricing, as indexed | StoreLeads installs |
|---|---|---|---|---|
| **Tolstoy** | [listing](https://apps.shopify.com/tolstoy) | 4.6 (284), other snapshots 4.7 to 4.8 | Free tier, then $19, $44, $195, plus viewer charges. A Tolstoy blog says there is no free plan, which conflicts | 9,503 to 9,597 |
| Videowise, Firework | Per Tolstoy's own comparison, a competitor | Not found | Videowise pricing scales with widget impressions. Firework's free tier caps views and uploads | Not found |

---

## 6. Messaging commerce with catalog-aware AI

| Vendor | Listing | Rating (reviews) | Pricing, as indexed | AI |
|---|---|---|---|---|
| **Zoko** | [listing](https://apps.shopify.com/whatsapp-button-chat) | 4.8 to 4.9 (319 to 467) | From $49.99, trial | AI bots as a paid add-on, $24.99 a month per bot on the top tier. Most consistently positive reviews in the group |
| **Interakt** | [Marketing](https://apps.shopify.com/interakt-marketing), [Sell on WhatsApp](https://apps.shopify.com/interakt-sales) | 4.3 (234), 20% one-star | From $21. Sell on WhatsApp has a free plan and Growth at $41 | Advanced chatbot on higher tiers |
| **WATI** | [listing](https://apps.shopify.com/wati-abandonedcart-recovery) | 3.7 (118) | From $69. AI at $30 per 1,000 credits, messages extra | AI WhatsApp chat |
| **AiSensy** | [listing](https://apps.shopify.com/aisensy-whatsapp-marketing) | 4.1 (57), 23% one-star | $1 one-time on the listing | Not clear |
| Klaviyo Customer Agent | See category 1 | | | Now answers on WhatsApp |
| Arabic WhatsApp-first vendors | See 0.E | | | Salla, Zid, and Shopify |

**Overlap reading.** Messaging apps on Shopify are bought mainly for cart recovery, order and cash-on-delivery confirmation, and broadcasts, with AI as an add-on. They are a substitute for on-site discovery mainly where shoppers ask on WhatsApp, which 0.E examines for Arabic-speaking markets.

---

## 7. General AI chatbot builders with a Shopify integration

| Vendor | Source | Pricing | Shopify fit |
|---|---|---|---|
| **Chatbase** | [Chatbase](https://www.chatbase.co/blog/shopify-chatbots), `VEN` | Hobby $32, Standard $120, Pro $400 on annual billing. Its own Shopify guide says the App Store version has a free plan with 50 credits, then $40, $150, $500 | Syncs product data, browsing and recommendations, order lookup, customer updates |
| **Voiceflow** | [Voiceflow](https://www.voiceflow.com/blog/ecommerce-chatbot), pricing per [Botpress](https://botpress.com/blog/voiceflow-review), a competitor | Free to $150 plus usage credits, $50 per extra editor. Credits cannot be topped up | Connects to Shopify for order data. Built by teams with a developer |
| **Botpress** | [Botpress](https://botpress.com/blog/chatbase-review) | Free, Plus $150. Conversation-based pricing from May 2026 per Chatbase, a competitor | Developer-oriented |
| **Jotform AI Chatbot** | [Jotform](https://agent.jotform.com/ai/chatbot/shopify/) (first pass) | Not checked | Generic agent with a Shopify page |
| **n8n 2-Way Sync** connector app | [listing](https://apps.shopify.com/streamline-connector-voiceflow) | $9, $19, $29. Voiceflow and Botpress supported only on $19 and $29 | Syncs Shopify product and inventory into Voiceflow or Botpress |
| Tars | [Tars](https://hellotars.com/ai-agents/shopping-assistant-ai-agent) | Not checked | Shopping assistant template for Shopify and WooCommerce |

**Overlap reading.** These are build-it tools with a head start. They matter most to Run 2, where an agency or freelancer chooses between a builder plus their own hours and an app like Pico. See 0.D.

---

## 8. Enterprise discovery platforms with conversational shopping agents

| Vendor | Source | What it offers | Pricing |
|---|---|---|---|
| **Bloomreach Loomi** | [Bloomreach release, 2026-06-24](https://bloomreach.com/en/news/2026/bloomreach-transforms-customer-conversation-into-ecommerce-insight-with-conversational-agent/), [first pass release](https://lasvegassun.com/news/2026/aug/05/bloomreach-launches-multi-agent-ask-me-anything-ca/) | Conversational shopping agent that turns searches into guided conversations and returns in-stock catalog results, a Shopify Loomi AI app (April 2026), and a multi-agent "Ask Me Anything" release (dated August 2026 in the first pass, October 2026 in one index summary) | Quote-based |
| **Algolia Agent Studio** | [destinationCRM, July 2026](https://www.destinationcrm.com/Articles/CRM-News/CRM-Across-the-Wire/Algolia-Updates-Agent-Studio-175891.aspx) | Build your own shopping agent on an Algolia index, with guardrails and cost controls. Shopify Commerce Pipeline indexing, March 2026 | Usage and contract |
| **Constructor** | [Constructor](https://constructor.com/solutions/ai-shopping-assistant) | AI shopping assistant with in-stock results and personalization. Described as not built for small catalogs | Custom enterprise |
| **Coveo** | [listing](https://apps.shopify.com/coveo) | AI search across commerce, support, and internal knowledge | One source puts contracts at $100,000+ a year |
| **Envive** | See 0.A Section 8 | Sales agent, search agent, content agent | Demo-led |
| **Athos Commerce** | See category 2 | Search with reported conversational tools | Quote-based |
| Salesforce, Adobe | Not profiled | Platform-native agents for brands on those platforms, outside Shopify | |

**Overlap reading.** These vendors define what a Plus brand expects from conversational discovery: in-stock, catalog-only answers, multi-constraint queries, and merchandising control. They also confirm the brief's narrowing that catalog grounding is table stakes. They are not Run 1 slate candidates for a pre-launch app at $49 to $99 a month, but they are the ceiling a Level 2 buyer compares against.

---

## Summary for the slate

1. **Slot 4 (better-known adjacent option) has three real candidates:** Tidio (27,500 installs, 1,356 reviews, Lyro in 48 languages including Arabic, per-conversation AI), Gorgias (25,100 installs, growing, Shopping Assistant, per-interaction AI), and Chatty (9,000 installs, 1,900 reviews, the closest pricing model to Pico). The slate decision file weighs them.
2. **Slot 3 (status quo) should name the incumbent search apps:** Shopify Search & Discovery plus Boost, Smart Product Filter & Search, or Searchanise, which together account for about 50,000 detected installs.
3. **Klaviyo Customer Agent is now multilingual and on WhatsApp,** at $50 a month entry. It belongs on the Run 1 watchlist and stays at slot 4 for Run 2.
4. **Recommendation and quiz apps are overlap, not substitutes,** for most stores. They stay on the watchlist for Step 1.1 feature presence: Rebuy, RevenueHunt, Octane AI.
