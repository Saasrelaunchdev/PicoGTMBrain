# Step 0.A: Direct competitors, AI shopping assistants and AI sales agents on the Shopify App Store

**Date checked:** 2026-11-03. **Prompt:** `../RESEARCH-PROMPTS.md` Step 0.A. **Extends:** `2026-11-03-step-0-first-pass.md` Section 2, which verified existence only.

## How this was researched, and what it cannot show

- **Network limit.** This session's network policy allows package registries only. Direct page loads of apps.shopify.com, vendor sites, G2, and Reddit all failed (proxy 403 and DNS denial, 2026-11-03). Every App Store fact below was read through the web search index of the listing page, on 2026-11-03. The listing page itself was not loaded.
- **Provenance codes used in every table.**
  - `IDX` the Shopify App Store listing, read through the search index on 2026-11-03.
  - `VEN` the vendor's own website or help center, read through the search index on 2026-11-03.
  - `3P` a third party, named.
  - `CLAIM` a vendor or reviewer outcome claim. Recorded as a claim, never as a finding.
- **Index snapshots disagree.** The index holds listing snapshots from different dates, so review counts and prices often differ by snapshot. Where two differ, both are given. Where a summary was wrong once, it was caught: one summary reported "CZ Shopping AI Assistant, 4.7 from 1,264 reviews", and a direct query on that listing showed 1 review. Treat every single-snapshot number as approximate until a page load confirms it.
- **What could not be done without page loads.** Sorting each search term's results by review count, reading the "Built for Shopify" badge reliably, reading the date of the most recent review, and reading each listing's language list. These are marked `?` and passed to Step 1.1 and Step 2.1, which need page access.
- **Search terms run** (all 17 from the prompt, some combined in one query, each against apps.shopify.com): AI shopping assistant; AI sales assistant and AI sales agent; AI shopping agent; AI chatbot; ChatGPT chatbot; AI chat; AI concierge, virtual shopping assistant, and product finder; product recommendation chat and gift finder; conversational search and AI search assistant; multilingual chatbot; Arabic chatbot; AI live chat. Plus the Chat, Helpdesk, and Support category pages and Shopify's curated "AI Shopping Assistants" collection.

---

## 1. What the sweep found

1. **The shelf is crowded and long-tailed.** The App Store's Chat category alone lists about 1,055 apps (`IDX`, [category page](https://apps.shopify.com/categories/store-management-support-chat/all)). This sweep found 90+ distinct shopper-facing AI chat listings. Most have fewer than 20 reviews. Shopify also curates an "AI Shopping Assistants" collection, which held 17 apps in the indexed snapshot ([collection](https://apps.shopify.com/collections/ai-shopping-assistants)).
2. **Review volume sits with support-first chat apps, not with pure shopping assistants.** Shopify Inbox (about 5,810 reviews), Chatty (about 1,900), and Tidio (about 1,355) lead by a wide margin. The apps that call themselves shopping assistants and nothing else have small review bases: Dialog 38, iAdvize 30, Shoply AI about 25, Alhena 6. A merchant looking for "AI chat" meets the support-plus-sales apps first.
3. **Catalog grounding, product cards, and add to cart are table stakes.** Dozens of listings, including apps with zero reviews, describe answers from the synced catalog, product cards, and add to cart from chat. Tidio's help center says Lyro skips out-of-stock items ([Tidio Help](https://help.tidio.com/hc/en-us/articles/15960742181148-Product-Recommendations-for-Shopify), `VEN`). This confirms the brief's Section 5 narrowing: "Built around your synced catalog" is a description, not a differentiator.
4. **Billing units vary more than prices do.** Per AI conversation, per AI reply, per monthly visitor, per resolution, flat tiers, per session, per query, and commission on AI-attributed sales all appear (Section 5). Only a few vendors publish a definition of the unit.
5. **Pico's closest pricing analog is Chatty, not Manifest AI.** Chatty bills per AI conversation, and its free plan includes 50 AI conversations a month, the same allowance as Pico's Free plan. Manifest AI's paid prices were not visible in any indexed snapshot, so the first pass's note that Manifest is "closest to Pico's price band" is not confirmed (Section 3).
6. **Language coverage is uneven, and it is a live axis.** Rep AI's own pages say English and Spanish only ([hellorep.ai](https://www.hellorep.ai/blog/best-shopify-product-recommendation-apps), `VEN`). Tidio's Lyro lists 48 languages including Modern Arabic ([Tidio Help](https://help.tidio.com/hc/en-us/articles/12643043611036-Lyro-Multilanguage-support), `VEN`). Klaviyo's Customer Agent now lists 113 languages (see 0.B). A cluster of Arabic-first chat apps has appeared on Shopify (Section 6).
7. **One notable exit.** Big Sur AI Sales Agent was removed from the App Store on 2026-05-15 according to StoreLeads ([StoreLeads](https://storeleads.app/reports/shopify/app/bigsurai), `3P`). A cached listing says it is not currently available. Drop it from the active set.
8. **Name check.** No App Store listing named "Pico" appeared (`IDX`, 2026-11-03). The nearest is "Piko ‑ Pickup Reminder" by Excelcore Development, an unrelated pickup reminder app ([listing](https://apps.shopify.com/pickup-reminder)). A web search found no AI shopping product called Pico, only a Google AI developer competition project named PICO aimed at sellers ([ai.google.dev](https://ai.google.dev/competition/projects/pico)). Low collision risk in this category, worth a trademark check before launch.

---

## 2. The 20 most-reviewed direct competitors

Scope: apps whose main job, or one of two equal jobs, is shopper-facing AI chat that recommends products. Support-first helpdesks that added a shopping role are in Section 2b and in `2026-11-03-step-0b-indirect-competitors.md`. All rows `IDX` unless marked. Prices in USD per month as indexed on 2026-11-03.

| # | App, developer | Listing | Rating (reviews) | Billing unit | Plans as indexed | Shopping job seen | Other jobs | Language notes |
|---|---|---|---|---|---|---|---|---|
| 1 | Chatty AI Chatbot & Live Chat | [apps.shopify.com/chatty](https://apps.shopify.com/chatty) | 4.9 (1,898 to 1,900) | Per AI conversation | Free: 50 AI conversations a month, renewing, 200 trained products, 1 seat, unlimited human chats. Basic $19.99 for 100. Pro $68.99 for 500. Plus $199 for 1,000. Overage $0.40 per AI conversation, spend limit default $1,000 ([Chatty blog](https://chatty.net/blog/ai-chatbot-pricing/), `VEN`). Older pages list $19.99, $49.99, $199.99 per user, superseded | Recommendations, upsells, Shopify discounts, checkout links, cart recovery | Live chat, helpdesk, inbox | `?` |
| 2 | SmartBot: Leading AI Chatbot | [apps.shopify.com/smartbot](https://apps.shopify.com/smartbot) | 4.7 (461) | `?` | Free tier of 300 AI chats, lifetime. Listing says "Unlimited AI Chat" | Recommendations and upsells, per reviewers | Service | `?` |
| 3 | Qubify: AI Sales Chat & Upsell | [apps.shopify.com/qubify-ai-chatbot-live-chat](https://apps.shopify.com/qubify-ai-chatbot-live-chat) | 4.9 (388) in one snapshot, 0.0 (0) in another. Unresolved | Conversations | Free plan with 75 conversations a month | Recommendations, upsells | Order tracking | `?` |
| 4 | Zipchat AI Chatbot & Live Chat | [apps.shopify.com/zipchat](https://apps.shopify.com/zipchat) | 4.9 (200 to 209) | **Per AI reply** | Pricing page: Starter $80 monthly or $64 a month billed annually for 750 replies, about 300 conversations. Pro $240, Scale $480, Scale Plus $960 (annual). Unlimited from $2,100. 250 extra replies $49. 7 day trial, 30 day money-back. No free plan on the pricing page, although listing snippets say "free plan" ([zipchat.ai/pricing](https://www.zipchat.ai/pricing), `VEN`). Older $49 Starter figures are superseded | Recommendations, sales | Support, WhatsApp and other channels | `?` |
| 5 | Blabbe: AI Shopping Assistant | [apps.shopify.com/blabbe-ai-assistant](https://apps.shopify.com/blabbe-ai-assistant) | 4.8 (175) | Interactions | Free tier with 100 AI interactions a month | Guided conversation, real-time recommendations | | `?` |
| 6 | Wizybot AI CRM & Chatbot, Wizybot Inc | [apps.shopify.com/wizybot](https://apps.shopify.com/wizybot) | 4.5 to 4.7 (167 to 168) | Messages and flat tiers | Free with 30 AI messages. Basic $149.99 with WhatsApp. Personalized $400, custom. Partner page says "From $69.99". Conflict | Pre-purchase answers, cart recovery | CRM, live chat, WhatsApp, Instagram, Messenger, Telegram | `?` |
| 7 | Verifast AI Chatbot & Helpdesk | [apps.shopify.com/verifast-sales-assistant](https://apps.shopify.com/verifast-sales-assistant) | 4.9 (144) | Chats or conversations | Listing: Free up to 200 chats a month. Starter $99 or $990 a year for 1,000 chats, extra chat $0.05, 7 day trial. Vendor page: $79 for 500, $159 for 2,000, $239 for 5,000, Enterprise custom ([verifast.ai/pricing](https://verifast.ai/pricing), `VEN`). Conflict | Recommendations, cart recovery | Helpdesk, WhatsApp, Instagram, email | Claims 125, 100+, and 40+ languages on different pages. Arabic named on the support page |
| 8 | Rep AI: AI Agent & Live Chat, Rep AI Technologies Inc. | [apps.shopify.com/rep-ai-sales-associate](https://apps.shopify.com/rep-ai-sales-associate) | 4.5 (125), 4.7 (107), 4.6 (118) in three snapshots | **Per visitor** | Free: 100 visitors a month, up to 100 products. Starter $104, Basic $209, Standard $368. Annual saves 20%. 14 day trial. $12 per extra 1,000 visitors | Proactive chat to hesitating shoppers, recommendations, one-click add to cart, discounts, checkout without leaving chat ([hellorep.ai](https://www.hellorep.ai/blog/best-shopify-product-recommendation-apps), `VEN`) | Returns, live chat, ticket deflection | **English and Spanish only**, more in development, per vendor pages (`VEN`) |
| 9 | VanChat AI Chatbot & Live Chat | [apps.shopify.com/vanchat](https://apps.shopify.com/vanchat) | 4.9 (91 to 123) | Monthly visitors | Free with all features. Starter $19 or $190 a year, $49, Pro $99. 7 day trial. Unlimited products and replies | Sales chat, product-page knowledge | Live chat, support | Multilingual replies, per reviewers |
| 10 | Buddy AI: Agentic Commerce, Buddify | [apps.shopify.com/buddify-ai-discount-negotiator](https://apps.shopify.com/buddify-ai-discount-negotiator) | 4.8 (71 to 87) | **Flat fee plus commission** | $49 plus 3.5% commission on AI-generated sales. $79 plus 1.5%. $199 with 0%. 7 day trial | Sales agent, discount negotiation, conversion agent | Support agent | `?` |
| 11 | Manifest AI Chatbot & Agents | [apps.shopify.com/manifest-ai-shopping-assistant](https://apps.shopify.com/manifest-ai-shopping-assistant) | 4.3 to 4.4 (61 to 62) | `?` | Free to install. "Minimum 30-day free trial. Month-to-month and long-term agreements available after free trial." Paid prices not visible | Recommendations, quiz, cart and checkout recovery, lead collection | Dedicated AI expert on top tier | `?` |
| 12 | Dialog ‑ AI Shopping Assistant | [apps.shopify.com/dialog-ai-sales-assistant](https://apps.shopify.com/dialog-ai-sales-assistant) | 5.0 (38) | **Monthly unique visitors** after a free tier | Free: 200 conversations a month on a basic model. Starter $249 to 25,000 visitors, Standard $399 to 50,000, Scale $799 to 100,000. 14 day trial ([askdialog.com](https://www.askdialog.com/resources/best-ai-shopping-assistant-shopify), `VEN`) | Agent described as "inspired by Rufus", recommendations | Also on SFCC, BigCommerce, PrestaShop (first pass) | `?` |
| 13 | iAdvize: AI Shopping Assistant | [apps.shopify.com/iadvize](https://apps.shopify.com/iadvize), [second listing](https://apps.shopify.com/iadvize-ai-copilot) | 5.0 (30) and 5.0 (17) | `?` | Free plan, 30 day trial. Paid $290 to $1,330 | Recommendations on product pages, listing pages, and search. Listing positions it as built to sell rather than support | | `?` |
| 14 | Shoply AI Search & AI Chatbot | [apps.shopify.com/shopping-assistant-by-shoplyai](https://apps.shopify.com/shopping-assistant-by-shoplyai) | 4.9 (23 to 26) | Replies | Free with 50 replies a month. Paid from $29.99, or $49.99 in another snapshot. Conflict | Product expert plus search | Support | Lists Arabic, Hebrew, Vietnamese among languages. Listing cites a June 2025 "Best of Built for Shopify" recognition |
| 15 | Juphy: AI Chatbot & ChatGPT, Juphy, Inc. | [apps.shopify.com/juphy](https://apps.shopify.com/juphy) | 4.6 to 4.9 (37 to 39) | `?` | From $49 | Product search, sales | Support, after-hours cover | `?` |
| 16 | Chatifai AI Chatbot & Support | [apps.shopify.com/chatifai](https://apps.shopify.com/chatifai) | 4.5 (28). One snippet says 406, unresolved | `?` | Free tier, paid from $39 | Sales, product answers | Order tracking, handoff | English, German, Dutch, Spanish, French, Italian, Japanese, Korean |
| 17 | Hivebee AI | [apps.shopify.com/hivebee](https://apps.shopify.com/hivebee) | (13) | AI searches | Free with 100 AI searches a month. $49 tier includes multilingual | Natural language search, chat widget | | Multilingual on the $49 tier |
| 18 | Octocom AI Chatbot & Live Chat, Octocom LTD | [apps.shopify.com/ai-support](https://apps.shopify.com/ai-support) | 4.9 (10) | Conversations | Listing: Basic $200 for 350 conversations, extra blocks $15, 14 day trial. Vendor site: Basic $100 for up to 199, Advanced $200 ([octocom.ai/pricing](https://www.octocom.ai/pricing), `VEN`). Conflict | Sales and upsell | Support across chat, email, WhatsApp, Instagram, SMS | Claims 80 to 100+ languages (first pass) |
| 19 | Chaterimo | [apps.shopify.com/chaterimo](https://apps.shopify.com/chaterimo) | 3.4 (7) | `?` | `?` | Sales chat with a choice of GPT, Claude, Gemini, or Grok | Support. One review notes no live agent takeover | `?` |
| 20 | Alhena: AI Shopping Concierge, Alhena AI | [apps.shopify.com/gleen-ai](https://apps.shopify.com/gleen-ai) | 5.0 (6) | **Per conversation** | Free: 25 conversations a month. $239, $599, $1,199. 14 day trial. Overage $1.20 per conversation. A comparison page puts the $239 tier at 200 conversations. Alhena's own blog posts give other figures ($199 annual, 50 or 200 free credits), which conflict | Discovery, recommendations, upsells | Support automation, handoff, order and returns agents. Also WooCommerce, Magento, BigCommerce, SFCC | `?` |

**Near the cut line:** Humind 5.0 (6) from $49 with a trial ([listing](https://apps.shopify.com/humind-ai-shopping-assistant)), Selli 5.0 (3) from $19.90 ([listing](https://apps.shopify.com/ai-sales-assistant)), Ochatbot 5.0 (4) with a free plan for 1,000 monthly visitors and a "Built for Shopify" mention in the index ([listing](https://apps.shopify.com/ochatbot-by-ometrics)), ShopAI Assistant 5.0 (2), Karley 5.0 (1), CZ Shopping AI Assistant 5.0 (1) at $20 by Corezene Technology ([listing](https://apps.shopify.com/cz-advance-chatbot)).

### 2b. Same shelf, support-first, profiled in 0.B and 0.C

A merchant browsing the Chat category sees these next to the apps above, so their review gravity matters to Phase 2 even though their main job is support.

| App | Listing | Rating (reviews), `IDX` | Free entry |
|---|---|---|---|
| Shopify Inbox | [apps.shopify.com/inbox](https://apps.shopify.com/inbox) | 4.6 (5,810 to 5,813). Tagline: "An AI sales associate that knows your customers" | Free |
| Tidio: AI Chatbot & Live Chat | [apps.shopify.com/tidio-chat](https://apps.shopify.com/tidio-chat) | 4.8 (1,355 to 1,356) | Free plan, 50 Lyro conversations once per account |
| Redo | Helpdesk category | 4.9 (839) | Free to install |
| Gorgias: AI Helpdesk & Chat | [apps.shopify.com/helpdesk](https://apps.shopify.com/helpdesk) | 4.3 (709), about 10% one-star | Free trial |
| Moose AI Chatbot & Live Chat, Vegahub Technology | [apps.shopify.com/moosedesk](https://apps.shopify.com/moosedesk) | 5.0 (453 to 490) | Free plan. $19, $49, $249 |
| Willdesk: Live Chat & AI Chatbot, Channelwill | [apps.shopify.com/self-faq](https://apps.shopify.com/self-faq) | 4.7 (377 to 383) | Free with 20 conversations |
| Commslayer: AI Helpdesk & Chat | [apps.shopify.com/commslayer](https://apps.shopify.com/commslayer) | 4.9 (238) | Free plan. $39, $99 |
| Fin AI Agent & Intercom | [apps.shopify.com/fin](https://apps.shopify.com/fin) | 3.7 (18): 9 five-star, 5 four-star, 4 one-star. Latest review 2026-08-19, one star | Free trial, then $0.99 per outcome |
| Smartsupp Live Chat & Chatbots (Mira AI) | [apps.shopify.com/smartsupp-chat](https://apps.shopify.com/smartsupp-chat) | 2.3 (4) | Trial |

---

## 3. Pricing closest to Pico

Pico's public plans, from the source: Free covers 50 conversations a month, Growth covers 600 for $49, Pro covers 2,000 for $99, one store per plan. What counts as one conversation was decided later on 2026-11-03: a chat thread with at least one AI reply, once per shopper and device per 24 hours (`../DECISIONS.md` D24).

| Vendor | Unit | Free entry | Paid entry | Effective price per unit at the paid entry tier | Source |
|---|---|---|---|---|---|
| **Pico** | Conversation, as defined in D24 | 50 a month | Growth $49 for 600, Pro $99 for 2,000 | about $0.08 (Growth), about $0.05 (Pro) | `source/` |
| Chatty | AI conversation | 50 a month, renewing | $19.99 for 100, $68.99 for 500, $199 for 1,000 | about $0.20, $0.14, $0.20. Overage $0.40 | [Chatty](https://chatty.net/blog/ai-chatbot-pricing/) `VEN` |
| Verifast | Chat | 200 a month | $99 for 1,000 (listing), $79 for 500 (vendor page) | about $0.10 or $0.16. Extra chat $0.05 | `IDX`, [Verifast](https://verifast.ai/pricing) `VEN` |
| Smartsupp Mira AI | AI conversation | Trial only | From €16 for 100, up to 5,000 | about €0.16 | [Smartsupp](https://www.smartsupp.com/pricing/) `VEN` |
| Zipchat | AI reply | None on pricing page | $80 monthly, or $64 annual, for 750 replies, about 300 conversations | about $0.11 per reply, about $0.27 per conversation by the vendor's own equivalence | [Zipchat](https://www.zipchat.ai/pricing) `VEN` |
| Tidio Lyro | AI conversation, defined as any conversation with at least one AI reply | 50, once per account | Add-on tiers of 50 to 1,000 | about $0.58 to $0.65 on annual billing, $0.50 on the homepage. Conflict | [Tidio](https://www.tidio.com/blog/chatbot-pricing/) `VEN` |
| Octocom | Conversation | "Start free" on vendor site | $200 for 350 (listing) or $100 for 199 (site) | about $0.57 or $0.50 | `IDX`, [Octocom](https://www.octocom.ai/pricing) `VEN` |
| Commslayer | Conversation, extras | Free plan | $39, $99 | Extra conversation $0.15 | [Commslayer](https://www.commslayer.com/pricing) `VEN` |
| Alhena | Conversation | 25 a month | $239, reported as 200 conversations | about $1.20. Overage $1.20 | `IDX` |
| Fin for Ecommerce | Resolution | Trial | 50 outcomes a month minimum | $0.99 | [Intercom Help](https://www.intercom.com/help/en/articles/14997821-fin-for-ecommerce-explained) `VEN` |
| Gorgias AI Agent | Automated interaction | Trial | Bundled into helpdesk plans | $0.90 annual, $1.00 monthly, $1.50 overage | [Gorgias](https://www.gorgias.com/pricing) `VEN` |
| Dialog | Free conversations, then monthly visitors | 200 conversations | $249 for up to 25,000 visitors | Not per conversation. Dialog's own example: $399 whether shoppers hold 500 or 5,000 conversations | [Dialog](https://www.askdialog.com/resources/best-ai-shopping-assistant-shopify) `VEN` |
| VanChat | Monthly visitors | Free with all features | $19, $49, $99 | Not per conversation | `IDX` |
| Rep AI | Monthly visitors | 100 visitors | $104 | Not per conversation. $12 per extra 1,000 visitors | `IDX` |
| Small apps in the $0 to $49 band | Various | Dori 200 conversations, ShopGenie 100 conversations, Qubify 75, Hivebee 100 searches, SuperBot 200, Blabbe 100 interactions, CartPilot 50 | Concierge $49, Humind $49, Shoppi $49, Juphy $49, K AI Search $19, Seekr $19 | | `IDX` |

**What this table can and cannot support.**

- **Can support, internally:** Pico Pro's price per conversation (about $0.05) sits at or below every per-conversation or per-chat vendor sampled. Pico Growth (about $0.08) is level with Verifast's vendor-page Growth tier ($159 for 2,000, about $0.08) and below the rest. That is a Phase 9 input.
- **Cannot support, in customer copy:** any "cheaper than" claim. Units are not like-for-like (conversation, AI conversation, reply, resolution, visitor), Pico's own unit is undefined, and most of these products include support automation and live chat that Pico does not. Section 5 of the brief already bans named comparisons without a sourced, dated Phase 2 finding. A pricing-model contrast also needs a page-loaded check of the competitor's pricing page, which this session could not do.
- **Pattern worth keeping:** Pico, Chatty, and CartPilot use a 50-conversation free allowance. Pico's Free plan is not distinctive. The 14 day Growth trial with no card, and the sandbox store, have more company in trials than in sandboxes. Nothing sampled offered a sandbox store with a sample catalog.

---

## 4. Feature presence, partial

The flags the prompt asks for, filled only where a source states them. `Y` stated, `N` stated as absent, `?` not found. Step 1.1 completes this table for the watchlist.

| | Add to cart in chat | Checkout in chat or link | Human handoff or live chat | Order status | Returns or policy answers | Proactive prompts | WhatsApp or other channels | Unmet-demand report (zero results, not found) | Revenue attribution | Arabic |
|---|---|---|---|---|---|---|---|---|---|---|
| **Pico** | Y | N (store checkout) | N, C5 not built | N, C6 not built | N, C6 not built | N, C12 not built | N, C7 not built | **Y** | N, C1 not built | **Y, right to left** |
| Chatty | ? | Y, checkout links | Y | ? | ? | Y, cart recovery | Y (first pass) | ? | ? | ? |
| Rep AI | Y | Y | Y | ? | Y, returns | Y | ? | ? | Y, 3 hour same-session window, AI-assisted only | N, English and Spanish |
| Zipchat | ? | ? | Y | ? | ? | ? | Y | ? | ? | ? |
| Dialog | ? | ? | ? | ? | ? | ? | ? | ? | Reports into GA4 (first pass) | ? |
| Manifest AI | Y (first pass) | Checkout recovery | ? | ? | ? | ? | ? | ? | ? | ? |
| Alhena | ? | ? | Y | Y | Y | ? | ? | ? | ? | ? |
| Wizybot | ? | ? | Y | ? | ? | Cart recovery | Y | ? | ? | ? |
| Verifast | ? | ? | Y | Y | ? | Cart recovery | Y | ? | ? | Named |
| Tidio Lyro | ? | ? | Y | Y, Lyro Actions | ? | ? | Y | ? | ? | Y, Modern Arabic among 48 |
| ShopGenie | Y | ? | ? | Y | Y | ? | ? | **Y, "products shoppers looked for but couldn't find"** | ? | ? |
| Seekr (search) | n/a | n/a | n/a | n/a | n/a | n/a | n/a | **Y, searches that returned no products** | ? | ? |

**Watch item for Phase 1.** Pico's zero result and weak click report is listed in the source as a possible differentiator. At least two small apps, ShopGenie ([listing](https://apps.shopify.com/shop-genie-1)) and Seekr ([listing](https://apps.shopify.com/seekr)), describe a similar report (`IDX`). Step 1.1 should also check Shopify's own search analytics before Phase 1 scores this row (see 0.C).

---

## 5. Billing models in the direct set

| Model | Vendors seen | Buyer risk |
|---|---|---|
| Per AI conversation | Chatty, Alhena, Tidio Lyro, Octocom, Smartsupp Mira, Klaviyo Customer Agent (see 0.B), Pico | Needs a published definition of one conversation. Tidio publishes one: a conversation with at least one AI reply |
| Per AI reply | Zipchat | Long conversations cost more, which the shopper controls |
| Per monthly visitor | Rep AI, Dialog (after the free tier), VanChat, Debales ($100 for 10,000 visitors, [listing](https://apps.shopify.com/debales-ai-chatbot)), Ochatbot | Cost follows traffic whether or not anyone chats. Dialog presents this as predictability |
| Per resolution or outcome | Fin ($0.99), Gorgias ($0.90 to $1.50), Yuma (about $1.20) | Cost follows success, but the vendor defines success |
| Flat fee plus commission on AI-attributed sales | Buddy AI (3.5% or 1.5% or 0%), ChatPilot ($19 plus 2.5%, [listing](https://apps.shopify.com/chat-pilot)), Gimmie AI (commission only, [listing](https://apps.shopify.com/gimmie)) | Needs attribution the merchant trusts. The Closer advertises "0% commission" against this model ([listing](https://apps.shopify.com/the-closer-ai)) |
| Per session or per query | Supportify ($0.60 per session after 50 free, [listing](https://apps.shopify.com/supportify-1)), N3 Smart Search ($0.12 per AI query, capped at $12, [listing](https://apps.shopify.com/ai-search-chatbot)) | Small caps make these cheap but limited |
| Flat tiers | Moose, Willdesk, Commslayer, most long-tail apps | Predictable, usually capped by features |

---

## 6. Arabic-first and multilingual direct apps on Shopify

Feeds 0.E. All `IDX` on 2026-11-03.

| App | Listing | What it says | Price as indexed |
|---|---|---|---|
| Luma | [apps.shopify.com/luma](https://apps.shopify.com/luma) | Support chatbot in Arabic, English, and Franco-Arabic. Storefront widget and Instagram DMs. Product questions, order tracking. Escalates to a human dashboard. A reviewer reports setup in about 15 minutes | Free plan, paid `?` |
| shamz.ai | [apps.shopify.com/shamz-ai](https://apps.shopify.com/shamz-ai) | "Gulf Arabic AI Front Desk on WhatsApp & Instagram." Detects Arabic or English automatically, live agent handoff, product search, order tracking, bookings | $170 in one snapshot, free to $299 in another. Conflict |
| Jaweb AI Chatbot & Live Chat | [apps.shopify.com/jawebchatbot](https://apps.shopify.com/jawebchatbot) | Arabic and many languages, WhatsApp including voice notes, order tracking | `?` |
| Sobot AI Agents & Live Chat | [apps.shopify.com/sobot](https://apps.shopify.com/sobot) | Lists Arabic, live chat, real-time translation | `?` |
| AI SmartTalk | [apps.shopify.com/aismarttalk](https://apps.shopify.com/aismarttalk) | Lists Arabic, voice input in 20+ languages, trained on products | `?` |
| Algoshop AI Chatbot & Live Chat | [apps.shopify.com/algoshop-ai-sales-chatbot](https://apps.shopify.com/algoshop-ai-sales-chatbot) | Sales chatbot, inbox, order tracking, WhatsApp and Instagram | `?` |
| Shoply AI | See row 14 | Lists Arabic and Hebrew | Free, then $29.99 or $49.99 |
| Verifast | See row 7 | Arabic named on the support page | Free 200 chats |
| Chizy: AI Chatbot & Live Chat | [apps.shopify.com/chizy-ai-chatbot](https://apps.shopify.com/chizy-ai-chatbot) | Claims 100+ languages, Arabic not confirmed | "Unlimited AI chat" |
| ChatMate | [apps.shopify.com/chatmate](https://apps.shopify.com/chatmate) | 16 languages, real-time translation. 0 reviews | `?` |
| Helpy AI | [apps.shopify.com/helpy-v2](https://apps.shopify.com/helpy-v2) | Claims "7,000+ languages", `CLAIM` | `?` |
| RTL tooling, not chat | [RTL Tools](https://apps.shopify.com/rtl-rtl-hebrew), [Sense Apps](https://apps.shopify.com/partners/sense-apps), [Arabify notifications](https://apps.shopify.com/arabic-notifications) | Right to left layout and Arabic notifications for Shopify themes | RTL Tools $5 with a trial |

**What it means for the narrowed claims.** Arabic support on Shopify is not empty ground. It is a cluster of small apps, mostly support-first and WhatsApp-led, plus global vendors that list Arabic among dozens of languages. The brief's narrowing holds: "Arabic replies display right to left, with a language switcher and separate merchant copy per language" is a description Pico can make. "The Arabic AI shopping assistant" is not. None of the listings above was read for right to left product cards specifically, so whether any of them renders RTL product cards is `?`.

---

## 7. Long-tail register

Every other shopper-facing AI chat listing the sweep found. `IDX`, 2026-11-03. Ratings shown only where the index gave them.

| App | Listing | Price as indexed | What it says |
|---|---|---|---|
| AI Chatbot: Shopping Assistant (SetuBridge) | [ai-shopping-assistant-chat-bot](https://apps.shopify.com/ai-shopping-assistant-chat-bot) | Free tier with "unlimited chats" | Catalog and store knowledge, product finder with budget filter, add to cart, checkout link, order tracking, live agent handoff |
| AI Shopping Agent & Support | [ai-shopping-agent](https://apps.shopify.com/ai-shopping-agent) | `?` | Discover, compare, instant answers |
| AI Shopping Agent | [mr-ai-shopping-agent](https://apps.shopify.com/mr-ai-shopping-agent) | Free to $299 | Shop by photo, cart building, order tracking, policy answers, 11 languages |
| ShopBrain | [shopbrain](https://apps.shopify.com/shopbrain) | `?` | Product search, recommendations, add to cart |
| ShopGenie: AI Search & Support | [shop-genie-1](https://apps.shopify.com/shop-genie-1) | Free with 100 conversations | Variant picking, add to cart, shipping and returns answers, order tracking, dashboard of top searches and products not found |
| AI Shopping Assistant, RVS Media | [rvs-personal-assistant](https://apps.shopify.com/rvs-personal-assistant) | From $9.99, trial. No reviews | Chat recommendations |
| SearchMind AI Shop Assistant | [searchmind-ai](https://apps.shopify.com/searchmind-ai) | Free, paid from $20 | Answers from the catalog |
| Future Chat AI Assistant | [future-chat](https://apps.shopify.com/future-chat) | `?` | Visual search, virtual try-on, upsells |
| Sigma ‑ AI Shopping Assistant | [sigma-agent](https://apps.shopify.com/sigma-agent) | `?` | Launched January 2026, no reviews |
| ShopAgent | [shopagent-ai](https://apps.shopify.com/shopagent-ai) | `?` | AI chatbot |
| Shopchat: AI Search Assistant | [shopchat](https://apps.shopify.com/shopchat) | From $14.99. Listing about three years old | GPT-4 search widget |
| Easy AI Shopping Assistant | [easy-ai-shopping-assistant](https://apps.shopify.com/easy-ai-shopping-assistant) | `?` | |
| N3 Smart Search AI | [ai-search-chatbot](https://apps.shopify.com/ai-search-chatbot) | $9.99 plus $0.12 per AI query, capped at $12 | Search chatbot |
| ShopAI Assistant | [shopai-assistant](https://apps.shopify.com/shopai-assistant) | `?`, 5.0 (2) | Search, checkout, live chat, leads |
| Karley | [karley-ai-shopping-assistant](https://apps.shopify.com/karley-ai-shopping-assistant) | `?`, 5.0 (1) | Tagline claims more conversions, `CLAIM` |
| Humind | [humind-ai-shopping-assistant](https://apps.shopify.com/humind-ai-shopping-assistant) | From $49, trial, 5.0 (6) | Shopping experience and upsells |
| Selli | [ai-sales-assistant](https://apps.shopify.com/ai-sales-assistant) | From $19.90, 5.0 (3) | GPT assistant tied to inventory |
| Shopilot | [shopilot](https://apps.shopify.com/shopilot) | Free, paid from $4.99 | Recommendations, guide to checkout |
| Debales AI Agent for Sales and Support | [debales-ai-chatbot](https://apps.shopify.com/debales-ai-chatbot) | $100 for up to 10,000 visitors, 7 day trial | Sales and support |
| XInfer.AI | [xinfer-ai](https://apps.shopify.com/xinfer-ai) | From $39, phone add-on $30 | Chat, voice, phone, SMS |
| Sellivo | [sellivo-ai-sales-autopilot](https://apps.shopify.com/sellivo-ai-sales-autopilot) | From $10 | WhatsApp and web chat, cart recovery, returns |
| Recomaze | [recomaze-ai](https://apps.shopify.com/recomaze-ai) | From $399 | Sales agent plus AI answer engine visibility |
| ChatPilot | [chat-pilot](https://apps.shopify.com/chat-pilot) | $19 plus 2.5% commission, 5.0 (7) | Sales chat and upsell |
| The Closer | [the-closer-ai](https://apps.shopify.com/the-closer-ai) | $79.99, 14 day trial, "0% commission" | Proactive, add to cart in chat |
| Claros | [claros](https://apps.shopify.com/claros) | `?` | Sales agent |
| CartPilot ‑ AI Sales Agent | [cartpilot](https://apps.shopify.com/cartpilot) | Free with 50 conversations, paid from $39 | Voice and text, compare, add to cart, coupons, order tracking |
| CartPilot AI | [cartpilot-ai](https://apps.shopify.com/cartpilot-ai) | `?` | Search to checkout |
| K AI Search Shopping Assistant | [agentic-store](https://apps.shopify.com/agentic-store) | From $19 | Search and assistant "for your agentic storefronts", add to cart |
| Talkom | [talkom-ai](https://apps.shopify.com/talkom-ai) | `?` | Recommendations, add to cart |
| Rynex | [rynex](https://apps.shopify.com/rynex) | `?` | Questions to carts |
| Shopique | [shopique-ai](https://apps.shopify.com/shopique-ai) | `?` | Add to cart from chat |
| Chatonbo | [chatonbo](https://apps.shopify.com/chatonbo) | `?` | Sells from the catalog, live chat |
| Qubly | [qubly](https://apps.shopify.com/qubly) | `?` | Vector search and reranking |
| EmbedAI | [embedai](https://apps.shopify.com/embedai) | `?` | Custom GPT support |
| Chatbot ‑ Smart AI Assistant | [smart-ai-chat](https://apps.shopify.com/smart-ai-chat) | `?` | Support |
| Neurobloom | [neurobloom-chatbot-chatgpt](https://apps.shopify.com/neurobloom-chatbot-chatgpt) | `?` | Voice, memory |
| Site Chat | [site-chat-shop-extension](https://apps.shopify.com/site-chat-shop-extension) | From $19, no reviews | Q&A-trained bot |
| Concierge: AI Sales Associate | [concierge-2](https://apps.shopify.com/concierge-2) | Free, paid from $49 | Text, voice, or photo input, add to cart |
| ShopGPT | [shopgpt-2](https://apps.shopify.com/shopgpt-2) | `?` | SMS concierge that refers to checkout |
| Angle | [angle](https://apps.shopify.com/angle) | $39 or $99 in different snapshots. Listing about 669 days old | Product finder and FAQ |
| Shopkeeper | [shopkeeper-2](https://apps.shopify.com/shopkeeper-2) | $19 | Voice-first |
| Refina | [refina](https://apps.shopify.com/refina) | From $9 | Shows reasons for each pick on the product page |
| Dori | [dori](https://apps.shopify.com/dori) | Free with 200 conversations | Discovery, comparison, add to cart, gift guidance |
| Gimmie AI | [gimmie](https://apps.shopify.com/gimmie) | Free install, commission on influenced sales | Catalog shopping assistant, in the curated collection |
| AE: AI Chatbot Sales & Support | [ai-chatbot-sales-support](https://apps.shopify.com/ai-chatbot-sales-support) | `?` | Comparison, gift finder, add to cart, orders |
| GiftX | [giftx-ai-shopping-assistant](https://apps.shopify.com/giftx-ai-shopping-assistant) | `?` | Quiz-style chat, view or add to cart |
| Smart Product Finder AI | [smart-product-finder](https://apps.shopify.com/smart-product-finder) | `?` | Questions to matches |
| Perla | [perla-ai-shopping-assistant](https://apps.shopify.com/perla-ai-shopping-assistant) | `?` | Natural language search, attribute filters |
| Shoppi | [shoppi-ai](https://apps.shopify.com/shoppi-ai) | $49, 14 day trial | Text, voice, image search plus chat |
| Trieve | [trieve](https://apps.shopify.com/trieve) | `?` | Guided discovery to checkout |
| Wantly ‑ AI Sales Assistant | [wantly-chat](https://apps.shopify.com/wantly-chat) | Free plan, no reviews | Recommendations, upsells, support |
| Juphy, SuperBot, Chatkit, Ernest, Asks, ChatPal, Pooch, BestChat, AI Support Chatbot & Whatsapp, Smart AI Chatbot & Live Chat, CSS AI Sales Chatbot, Commerce AI, AI Sales Helper Chat, Repli AI | [juphy](https://apps.shopify.com/juphy), [superbot-ai](https://apps.shopify.com/superbot-ai), [chatkit-1](https://apps.shopify.com/chatkit-1), [ernest](https://apps.shopify.com/ernest), [asks-app](https://apps.shopify.com/asks-app), [chatpal](https://apps.shopify.com/chatpal), [pooch-app](https://apps.shopify.com/pooch-app), [bestchat](https://apps.shopify.com/bestchat), [ai-support-agent-chatbot](https://apps.shopify.com/ai-support-agent-chatbot), [smart-chatbot-ai-assistant](https://apps.shopify.com/smart-chatbot-ai-assistant), [ai-sales-bot](https://apps.shopify.com/ai-sales-bot), [arena](https://apps.shopify.com/arena), [ai-helper](https://apps.shopify.com/ai-helper), [repli-ai](https://apps.shopify.com/repli-ai) | SuperBot free with 200 conversations. Others `?` | General AI chat for sales and support. ChatPal covers storefront, WhatsApp, Instagram, Telegram |

**Excluded on review:** "Chats: ChatGPT AI Chatbot" ([chatgpt-1](https://apps.shopify.com/chatgpt-1)) is a merchant-side workspace, not shopper-facing. "Manifest Multi‑Chat Messenger" is by a different developer and is not Manifest AI.

---

## 8. Off-App-Store direct competitors

| Vendor | Where | Status and model | Note |
|---|---|---|---|
| Envive | [envive.ai](https://www.envive.ai/) | No public pricing, demo-led, aimed at larger brands, per a September 2026 guide ([Macha](https://www.getmacha.com/blog/envive-complete-guide), `3P`). Formerly Spiffy AI, Seattle. Raised $15M | Homepage names brand customers. `CLAIM`: "3x avg conversion lift" for engaged visitors. `CLAIM` via CB Insights: 11.5% conversion increase and $5.35M annualized incremental revenue at one brand ([CB Insights](https://www.cbinsights.com/company/spiffy-2)) |
| Big Sur AI | [StoreLeads](https://storeleads.app/reports/shopify/app/bigsurai) | Removed from the App Store 2026-05-15. A competitor's blog calls it "sunsetting" ([Milly Software](https://millysoftware.com/blog/bigsur-ai-alternative-migration-guide)) | Exited. Not a slate or watchlist candidate |
| Enterprise discovery vendors with shopping agents | Constructor, Bloomreach, Algolia, and others | See 0.B category 8 | |

---

## 9. Outcome claims seen in the direct set, recorded as claims

| Vendor | Claim, as worded or summarized by the index | Where |
|---|---|---|
| Gorgias | "62% uplift in conversion rate" for brands using Shopping Assistant. Arc'teryx conversion rate up 75%. A jewelry retailer's average order value up 32% | [Gorgias blog](https://www.gorgias.com/blog/guide-shoppers-to-checkout), [Arc'teryx story](https://www.gorgias.com/customers/arcteryx) |
| Envive | "3x avg conversion lift" for engaged visitors | [envive.ai](https://www.envive.ai/) |
| Wizybot | Answers 96% of inquiries | [wizybot.com](https://www.wizybot.com/en/) |
| Smartsupp | 70% of inquiries resolved by Mira AI, 25% more chat-driven sales | [Smartsupp](https://www.smartsupp.com/mira-ai-shopping-assistant/) |
| Verifast | Automates 90% of tickets | [verifast.ai](https://verifast.ai/support) |
| Rep AI | One App Store reviewer credits it with 12% of sales assisted. Vendor case study on chat-influenced revenue at HigherDOSE | [Rep AI reviews](https://apps.shopify.com/rep-ai-sales-associate/reviews), [case study](https://www.hellorep.ai/case-studies/nearly-half-of-higherdoses-website-visitors-chat-with-ai-heres-how-its-driving-sales) |
| Manifest AI, Dialog, Karley | Taglines promise higher or boosted conversions | Listings in Section 2 and 7 |

**How the category measures.** Rep AI publishes an attribution method: a sale counts only if the AI helped during the session, inside a 3 hour same-session window, and greetings or human requests are filtered out (`VEN`). Dialog reports into GA4 (first pass). Gorgias and Envive publish lift figures without a method visible in the index. No vendor in this sweep described a holdout test. Pico measures none of these outcomes, so none of this is a template for Pico copy. It is evidence for brief Section 5 and for candidate C9 (holdout measurement).
