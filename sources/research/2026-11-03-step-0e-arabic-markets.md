# Step 0.E: Arabic-speaking markets

**Date checked:** 2026-11-03. **Prompt:** `../RESEARCH-PROMPTS.md` Step 0.E. **Extends:** `2026-11-03-step-0-first-pass.md` Section 6. **Feeds:** open decision 3 (target geography) in `../GTM-BRIEF.md` Section 4.

**Method and limits.** Web search only, because this session's network policy blocks page loads. Regional sources were preferred where the index had them. Two trackers measure different things and are never combined: **StoreLeads** counts live Shopify stores it detects, and **wmtips** reports the share of detected ecommerce websites by platform. Marks: `VENDOR` for a company selling one of the options, `SELF-REPORTED` for user-submitted data, `2ND` for secondary coverage. Agencies are reported as counts, not names.

---

## 1. Ecommerce platform share, by country

### 1a. Live Shopify stores, StoreLeads

| Country | Live Shopify stores | Year-over-year | Page date | Source |
|---|---|---|---|---|
| United Arab Emirates | 26,986. Dubai alone 16,116 to 16,549 | Up 15%, 2026 Q3 | 2026 | [StoreLeads AE](https://storeleads.app/reports/shopify/AE/top-stores) |
| Egypt | 16,122 | **Up 63%, 2026 Q3** | 2026-10-16 | [StoreLeads EG](https://storeleads.app/reports/shopify/EG/top-stores) |
| Morocco | 10,539 | Growth figure dated 2026 Q1 | 2026 | [StoreLeads MA](https://storeleads.app/reports/shopify/MA/top-stores) |
| Saudi Arabia | 4,480 headline, 4,517 in its own 2026 Q3 chart | | 2026-10-09 | [StoreLeads SA](https://storeleads.app/reports/shopify/SA/top-stores) |
| Kuwait | 3,790 | Up 13%, 2026 Q3 | 2026 | [StoreLeads KW](https://storeleads.app/reports/shopify/KW/top-stores) |
| Qatar | 2,265 | Up 30%, 2026 Q3 | 2026 | [StoreLeads QA](https://storeleads.app/reports/shopify/QA/top-stores) |
| Bahrain | No national total. City pages sum to at least 367: Manama 282, Riffa 65, Janabiyah 11, Hamala 9 | | 2024-12 to 2026-03 | `2026-11-03-tbd-resolution-research.md` Section 6 |
| Oman | No national total. Area pages sum to at least 471: Muscat Governorate 413, Al Batinah North 30, Dhofar 28. 11 on Plus | | 2026 | Same |
| Jordan | Not found | | | Outside the GCC, context only (`../DECISIONS.md` D11) |

**`DERIVED`:** the six countries found sum to about 64,000 detected live Shopify stores (same tracker, page dates within a few months of each other). Many of these, especially in the UAE, run English storefronts, so this is the ceiling of the Shopify footprint in the region, not a count of Arabic storefronts. Stores with an Arabic storefront language: no tracker publishes storefront language, so this is not sized. Storefront language is asked at intake instead (`../DECISIONS.md` D53).

### 1b. Share of detected ecommerce websites, wmtips

| Country | Leader | Shopify | Others | Source |
|---|---|---|---|---|
| Egypt | WooCommerce 47.2% | **37.4%** | Magento 2.2% | [wmtips EG](https://www.wmtips.com/technologies/e-commerce/country/eg/) |
| Saudi Arabia | WooCommerce 36.8% | **13.5%** | Zid 16.4% | [wmtips SA](https://www.wmtips.com/technologies/e-commerce/country/sa/) |
| United Arab Emirates | WooCommerce first, share not visible in the index | `?` | 56 platforms detected | [wmtips AE](https://www.wmtips.com/technologies/e-commerce/country/ae/) |
| Morocco | WooCommerce about 61.6% | `?` | YouCan share not found | [wmtips MA](https://www.wmtips.com/technologies/e-commerce/country/ma) |
| Kuwait | Page exists, figures not visible | `?` | | [wmtips KW](https://www.wmtips.com/technologies/e-commerce/country/kw/) |
| Global, for reference | WooCommerce 34.9% | 21.1% | Based on 3,861,081 websites, 2026-10-13 | [wmtips global](https://www.wmtips.com/technologies/e-commerce/) |

### 1c. Saudi Arabia by store count, a third method

AfterShip counts Salla at 19,640 stores, 44.11% of stores it tracks, and Zid at 12.55% ([AfterShip](https://www.aftership.com/ecommerce/statistics/regions/sa)). Salla says it powers over 68,000 active merchants, per a comparison article (`VENDOR`, unverified). **Saudi Arabia is a Salla, Zid, and WooCommerce market. Shopify is a minority there by every method found.**

### 1d. Local builders

ExpandCart claims 20,000+ merchants in Egypt (first pass, [MENAbytes](https://www.menabytes.com/expandcart-series-a/)). YouCan, EasyOrders, and Wuilt shares: not found. Egypt is context only, outside the GCC (`../DECISIONS.md` D11).

**What 1a to 1d mean for Pico.** The Shopify footprint in the region concentrates in the **UAE (about 27,000 stores) and Egypt (about 16,000, growing fastest)**, then Morocco. Saudi Arabia is large in ecommerce but small on Shopify. Pico reaches Salla and Zid stores only through its custom catalog API, which is development work and a Run 3 kind of motion.

---

## 2. Arabic AI shopping assistants and chat products

### 2a. On Shopify (full detail in `2026-11-03-step-0a-direct-competitors.md` Section 6)

| Product | Arabic claim | Shape |
|---|---|---|
| Luma | Arabic, English, Franco-Arabic | Support bot, widget plus Instagram, human dashboard. Free plan |
| shamz.ai | "Gulf Arabic", auto-detects Arabic or English | WhatsApp and Instagram front desk, $170 or up to $299 |
| Jaweb | Arabic among many | WhatsApp including voice notes |
| Sobot | Lists Arabic | Live chat with real-time translation |
| AI SmartTalk | Lists Arabic | Trained on products, voice input |
| Algoshop | Not explicit | Sales chatbot with WhatsApp and Instagram |
| Shoply AI | Lists Arabic and Hebrew | Product expert plus search |
| Verifast | Names Arabic | Chat, helpdesk, WhatsApp |

### 2b. On Salla, Zid, and others

| Product | Platform | What it says | Source |
|---|---|---|---|
| **Salla AI Finder** | Salla, native | Smart search for Arabic queries: understands Arabic, corrects typos, recommends by behavior. Installed from the Salla App Store. **The platform ships its own Arabic discovery tool** | [Salla Help](https://help.salla.sa/en/article/ai-finder-smart-search/na3m06sl43i9bnonmgohyoas) |
| Alfinder | Salla | AI search, recommendations, an assistant, analytics. Claims Gulf, Egyptian, and Levantine dialects (`VENDOR`) | [alfinder.ai](https://alfinder.ai/en/solutions/salla) |
| Thikaa | Salla | Chatbot answering on WhatsApp (`VENDOR`) | [Thikaa](https://thikaa.com/blog/salla-chatbot-integration?lang=en) |
| Swiftli | Salla listing | ChatGPT-based product search indexing Salla stores in Arabic and English | [brandfetch](https://brandfetch.com/swiftli.app.md) |
| Mando AI, Nano AI, Zoe | Salla and Zid | Arabic-first, mostly WhatsApp-led (first pass) | [Mando](https://mando.cx/solutions/e-commerce/salla), [Nano AI](https://www.nano-ai.net/en/services/salla-zid-whatsapp-ai), [Zoe](https://zoe-agent.com/salla-store-owners-whatsapp-ai/) |
| LetsBot, ChatMaxima | Salla, Zid | WhatsApp bots for Saudi stores (`VENDOR`) | [LetsBot](https://letsbot.net/en/salla.html), [ChatMaxima](https://chatmaxima.com/integrations/zid-whatsapp-integration/) |
| Zid WhatsApp | Zid, native | Connects WhatsApp Business to Zid and merges conversations | [Zid](https://zid.sa/en/solutions/zid-whatsapp/) |
| Assistli, ATMET | Shopify and others, Gulf and Levant | Arabic AI chat (first pass) | [Assistli](https://www.assistli.ai/ai-chatbot-for-ecommerce), [ATMET](https://atmet.app/en/blog/shopify-whatsapp-arabic) |
| **Meta Business AI** (business agent) | WhatsApp, Instagram, Messenger | Answers questions, recommends from the business's catalog, books, hands off to humans. Launched globally after about two years of testing in India and Mexico, gated by account and market eligibility (`2ND`) | [DEV Community](https://dev.to/creeta/meta-business-ai-went-global-gated-rollout-paid-plans-tbd-16j0), [YourStory](https://yourstory.com/ai-story/mark-zuckerberg-ai-agents-whatsapp-business-ai-essentials) |

**Dialect claims.** Alfinder (Gulf, Egyptian, Levantine), shamz.ai (Gulf), and Luma (Franco-Arabic) are the only explicit dialect claims found. All are vendor claims. Pico states no dialect handling, and the brief's narrowing already bans "understands every Arabic dialect".

---

## 3. Do the big global options support Arabic today

Checked against each vendor's own documentation where the index had it.

| Vendor | Arabic | Source | Mark |
|---|---|---|---|
| Shopify Inbox agent | **Replies in the customer's language.** The Inbox listing's roughly 21 interface languages do not include Arabic. Right to left in the chat widget not documented | [Help: Inbox agent](https://help.shopify.com/en/manual/inbox/assigning-your-ai-staff-member), [listing](https://apps.shopify.com/inbox) | Vendor docs |
| Klaviyo Customer Agent | 113 languages per the product page. Arabic not confirmed by name in the index | [Klaviyo](https://www.klaviyo.com/solutions/ai/customer-agent) | Vendor docs |
| Intercom Fin | **Yes, Arabic (Modern)** listed among languages Fin answers in. Translates answers into the customer's language | [Intercom Help](https://www.intercom.com/help/en/articles/8322387-set-up-fin-ai-agent-s-multilingual-support) | Vendor docs |
| Tidio Lyro | **Yes, Arabic (Modern)** among 48 languages, auto-detected | [Tidio Help](https://help.tidio.com/hc/en-us/articles/12643043611036-Lyro-Multilanguage-support) | Vendor docs |
| Gorgias AI Agent | 80+ languages per a competitor's comparison. Arabic not confirmed | [Zipchat](https://www.zipchat.ai/blog/customer-service-software-comparison) | `VENDOR` (competitor) |
| Rep AI | **No.** English and Spanish only, more in development, per Rep AI's own pages | [hellorep.ai](https://www.hellorep.ai/blog/best-shopify-product-recommendation-apps) | Vendor docs |
| Manifest AI | Not found | | Treated as no Arabic claim. Manifest AI is on the watchlist, not the slate |
| Zipchat | "Speaks any language", no list | [Zipchat](https://www.zipchat.ai/how-it-works) | `VENDOR` |

**Reading it.** Arabic text replies are available from Fin, Lyro, probably Klaviyo, and from the Inbox agent's language-following behavior. **What none of these documents is right to left product cards, a language switcher in the widget, or separate merchant copy per language.** Those are Pico's stated features. They are describable as what Pico does. "The Arabic assistant" or "the only one that speaks Arabic" is not supportable.

---

## 4. How shoppers in these countries ask product questions

No 2025 or 2026 survey measured pre-purchase contact by channel (site chat, WhatsApp, Instagram DM, phone) for these countries. The closest data:

| Market | Finding | Source | Mark |
|---|---|---|---|
| UAE | 79% use social media to research brands or products, 59% bought through social media in the past year | [Business of Apps on RetailX](https://www.businessofapps.com/news/shopping-on-social-apps-is-on-the-rise-in-the-uae/) | `2ND` |
| Saudi Arabia | 83% of electronics shoppers and 79% of quick-service restaurant customers say they buy through social platforms. Snapchat, Publicis Media, and NRG, about 600 respondents per category, August 2025 | [Arabian Business](https://www.arabianbusiness.com/gcc/saudi-arabia/snapchat-study-saudis-rely-on-social-media-to-shop) | `2ND`, platform-sponsored |
| Middle East | 82% look for reviews before buying a product found on social media. PwC Voice of the Consumer 2024 | [PwC](https://pwc.com/m1/en/publications/documents/2024/voice-of-the-Consumer-empowered.pdf) | Consultancy survey |
| Egypt | Not found | | Context only, outside the GCC (D11) |
| WhatsApp specifically | Not quantified. Its centrality is inferred from the number of WhatsApp-first tools (Section 2), Zid's native WhatsApp integration, and Meta's Business AI rollout | | Inference |

**What it means.** On-site chat competes with WhatsApp and Instagram DMs as the place a shopper in these markets asks for a product. That is why C7 (WhatsApp and other channels) is a candidate. It stays not built, per open decision 6, closed later on 2026-11-03 as out of scope until the GCC opens (`../DECISIONS.md` D14), and copy must not imply it.

---

## 5. Shopify Partner Directory agencies in these countries

Counts only, per the run rule.

| Measure | Finding | Source |
|---|---|---|
| Egypt location page | One indexed view of the Partner Directory filtered to Egypt showed **33 partners**, in Cairo, Maadi, and other cities. Tier split not visible | [Partner Directory, Egypt](https://www.shopify.com/eg/partners/directory) |
| UAE, Saudi Arabia, Qatar | No aggregate count found. Three partner profiles seen (one Plus tier in Dubai, one Select tier in Dubai, one serving Egypt, Saudi Arabia, the UAE, and Qatar) list Arabic as a working language and **Arabic right to left development as a service** | Partner Directory profiles, not named |
| By tier and country | Not loadable through the search index. Counted from the directory's filters when the GCC opens (D11) | |

**What it means for Run 2.** Gulf agencies already sell Arabic right to left builds as a service line. An app whose widget renders Arabic right to left is something those agencies can install without custom work. That is a Run 2 hypothesis to test in 0.F and 0.G, not a finding yet.

---

## 6. Payment rails, and how App Store billing works for these merchants

| Topic | Finding | Source |
|---|---|---|
| **How Shopify bills app charges** | App prices are set in USD. Merchants billed in a supported local currency are charged the converted amount. Local-currency estimates appear for 14 currencies (AUD, CAD, CHF, CZK, DKK, EUR, GBP, INR, JPY, NOK, PLN, RON, SEK, SGD), **none of them AED, SAR, EGP, KWD, QAR, JOD, or MAD**. Merchants billed in USD from outside the US may hit card restrictions on foreign transactions. Shopify suggests asking the bank to enable international transactions and using a credit card | [Shopify dev changelog](https://shopify.dev/changelog/posts/estimated-local-currency-prices), [Help: payment methods for bills](https://help.shopify.com/en/manual/your-account/manage-billing/paying-your-bills/making-payments/payment-methods-for-bills), [App billing](https://shopify.dev/docs/apps/launch/billing) |
| **Egypt card limits** | Banks eased foreign-currency card limits bank by bank after the March 2024 devaluation. The central bank recommended removing credit card spending limits (reported January 2025). One bank raised its international cap to $10,000 in August 2025. No 2026 source confirms a full nationwide removal | `2ND`: [african-markets](https://www.african-markets.com/en/news/north-africa/egypt/egypts-central-bank-lifts-foreign-currency-spending-limit-on-credit-cards), [Gulf News](https://gulfnews.com/business/egyptians-can-splurge-abroad-again-as-banks-ease-card-curbs-1.2025008), [CairoScene](https://cairoscene.com/Buzz/CBE-Removes-Restrictions-on-Foreign-Currency-Spending-on-Credit-Cards) |
| **Pico's own rails** | Shopify App Store installs bill through Shopify Billing in USD. InstaPay with EGP applies only to Shopware and custom stores in Egypt, per the source | `source/` |
| Saudi Arabia local methods | mada and STC Pay lead digital adoption. Cash on delivery estimates range from 13% to about 75% of transactions depending on source and year. No reliable 2026 figure | `2ND`, `VENDOR`: [eGrow](https://www.egrow.com/en/blog/saudi-arabia-cod-ecommerce-guide-2026), [Arab News](https://www.arabnews.pk/node/2176401) |
| Egypt local methods | One payments handbook lists cash on delivery 40%, Fawry 24%, international cards 15%, eWallets 8%, undated. Other sources put cash on delivery at 57% to 80%. No InstaPay share found | `VENDOR`: [dLocal](https://dlocal.com/payment-processors-middle-east-africa/egypt-payment-methods-processors-ecommerce-market/) |
| Kuwait, Qatar, Jordan, Morocco | Not researched in depth. Out of scope until the GCC opens (D11) | |

**What it means.** For an Egyptian Shopify merchant, paying Pico means a USD card charge on the Shopify bill. That works when the merchant's bank allows it, and it is the blocker `../SKILL-ADAPTATION.md` Phase 7 names: "whether the buyer can pay". InstaPay does not help App Store installs.

---

## 7. Shopify Payments, Markets, and AI features by country

| Item | Finding | Source |
|---|---|---|
| Shopify Payments | Cached copies of Shopify's supported-countries page conflict. One recent copy lists about 50 countries **including the UAE**. Secondary sources say Saudi Arabia and Egypt are not supported. Verify on the live page | [Shopify Help](https://help.shopify.com/en/manual/payments/shopify-payments/supported-countries), `2ND`: [ecosire](https://ecosire.com/blog/shopify-payment-gateways-by-country-2026) |
| Right to left on Shopify | Improved support for Arabic, Urdu, and Hebrew in the admin and storefronts, including checkout, customer accounts, and the Horizon themes. Translate & Adapt auto-translates Arabic | 0.C row 7 |
| Inbox agent | No country restriction found in the Help Center. Plan and customer-account requirements apply everywhere | 0.C row 1 |
| Agentic Storefronts | Baseline is selling to US buyers. A store in these countries qualifies only for its US sales | 0.C row 4 |
| Shopify Markets | Not checked country by country. Checked when the GCC opens (D11) | |

---

## What this means for open decision 3 (target geography)

**The proposed default holds:** English-speaking Shopify stores worldwide as Run 1's primary segment, Arabic-speaking stores as a named secondary segment. The evidence does not justify reversing it. Saudi Arabia, the largest Arabic ecommerce market by spend, is mostly on Salla, Zid, and WooCommerce, which Pico reaches only through custom API work.

**A refinement offered to the owner, closed later on 2026-11-03 and not applied:** the owner set the secondary market as the GCC, which excludes Egypt, and `../DECISIONS.md` D11 opens it on a stated trigger, with the UAE as the reference market. The refinement as offered: name the secondary segment by country, **UAE and Egypt Shopify stores first**. They are the two largest Shopify bases in the region by StoreLeads count (about 27,000 and 16,000), and Egypt grew 63% in a year. Egypt also matches Pico's inferred origin (open decision 3's own note), which matters for founder-led selling. Two cautions travel with it: Egyptian merchants pay App Store charges by USD card, and in both markets shoppers ask on WhatsApp and Instagram, where Pico is not (C7).

**What competition looks like in that segment.** Not empty. Small Arabic-first Shopify apps, mostly support-first and WhatsApp-led. Global vendors whose agents answer in Arabic (Fin, Lyro, the Inbox agent). On Salla, a native Arabic discovery tool. On WhatsApp, Meta's own business agent. Pico's describable difference is the combination in its widget, right to left cards with a language switcher and per-language merchant copy, not Arabic as such.
