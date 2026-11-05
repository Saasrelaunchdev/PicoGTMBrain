# Pico, GTM Builder Discovery Brief

The filled discovery input for the `gtm-builder` skill. This is what the skill's REQUIRED INPUTS checklist asks for, answered.

Read `SKILL-ADAPTATION.md` before Phase 1. Pico is B2B SaaS, so the phases run as written in substance, but it sells self-serve through the Shopify App Store to two different audiences. Phase 2 sources, Phase 4 fields, the Phase 5 committee, Phase 8 channels, and Phase 9 framing each need a documented change.

**Global rule for the whole run,** updated 2026-11-03: every unknown in this build is resolved in `DECISIONS.md`, as a decision Pico controls, a researched fact with its source and date, or a labelled operating assumption with the point where it gets measured. Nothing is invented. The source names no customers, installs, reviews, revenue, or results, so Pico is treated as pre-launch: customer proof enters only under the intake rule in Section 5, and until then copy uses open proof, claims the reader can check now (D4).

**Source:** `source/2026-11-02-pico-core-features-overview.md`, the Pico Core Features Overview, a product document dated 2026-11-02, read in full on 2026-11-03. **Research:** `research/2026-11-03-step-0-first-pass.md`, a first pass of Step 0 run on 2026-11-03, then Step 0 run in full on 2026-11-03 (parts 0.A to 0.H, one file each in `research/`), with the slate result in `research/2026-11-03-step-0-slate-decision.md`. Every App Store and vendor fact in that research was read through the web search index, because the session's network policy blocked page loads. Slate facts need a page-loaded check before Steps 2.1 and 2.7.

## Classification

The four facts everything downstream reads from.

| | |
|---|---|
| Archetype | B2B SaaS. Specifically a platform app: a storefront AI shopping assistant sold to ecommerce merchants through the Shopify App Store. Pico sells software to stores. It is not itself an ecommerce or DTC business, so do not apply the ecommerce archetype |
| Audiences | Two standalone go-to-markets now, a third deferred. **Run 1:** Shopify merchants, the store owners and ecommerce teams who install and pay. Global, **USA first**, with the GCC shown as a secondary market for later. **Run 2:** Shopify implementers, a full go-to-market of its own: agencies of every kind (build, Plus, CRO), Shopify developers, theme developers and designers, and freelancers, who install, recommend, or resell apps for merchants. **Deferred Run 3:** Shopware 6 merchants and agencies, plus custom-store developers |
| Evidence state | Unconfirmed, treated as pre-launch. The source carries no proof of any kind. If the founder supplies installs, reviews, or a named merchant with permission, it becomes early, and the proof set in Section 5 gets its first rows. The owner has planned the first route to proof: case studies from the client stores of implementers in Run 2's paid usability engagement, admitted only under the intake rule in Section 5 |
| Motion | Hybrid. Run 1 is self-serve and product-led: App Store install, free plan, 14 day trial with no card, sandbox store. Run 2 is outbound-led, then partnership-led, per the owner's decision of 2026-11-03: reach implementers by email, LinkedIn, and job posts on Upwork and Fiverr; run a paid small engagement in which they give usability feedback; interview them; build case studies with the client stores they work with; then offer a partnership program with affiliate incentives, referral traffic, and more. Its numbers are set in `DECISIONS.md`: $150 a session, 25% of referred stores' subscriptions for 24 months, and the rest in D33 to D41 |

### Run order

`gtm-builder` builds one GTM per run, so it runs once per audience. The two audiences have different buyers, different offers, and different economics. A blended run would produce Phase 6 pillars true of neither and a Phase 8 whose channels serve one and waste the other.

**Run 1, Shopify merchants.** The offer is the product itself, the pricing is decided and public, and the competitor research is tractable. Global, USA first. The GCC appears in each dashboard as a secondary market for later, there if needed, not pursued now.

**Run 2, Shopify implementers, is a standalone go-to-market** (owner decision, 2026-11-03). It runs all nine phases, the lead magnet, and the deck on its own evidence, and it does not borrow structure from Run 1 or wait for Run 1's review. It cites Run 1 only where an implementer has to show a client what Pico does. Its Phase 1 rates the planned engagement and partner offer, and its Phase 9 prices partner economics rather than plans, with every number set in `DECISIONS.md` D33 to D41.

**Run 3, Shopware 6 and custom stores, is deferred.** Different platform, different competitors, a likely European center of gravity to confirm in research, and different billing rails. Run it after Run 1 if Shopware turns out to matter commercially. Closed by the owner: deferred (D9).

**Shoppers are not an audience.** They use the widget, but they never buy Pico. Shopper benefits are evidence offered to the merchant, never a separate GTM.

---

# 1. PROJECT INFORMATION

## Shared, both runs

| Field | Value |
|---|---|
| Project name | Pico |
| Project website | **picofinds.com** (D1). Read from the live site's footer contact address, us@picofinds.com, in the owner's screenshots, 2026-11-03. The search index has no page for it yet. Name check, 2026-11-03: no App Store listing named Pico was found. The nearest is "Piko ‑ Pickup Reminder", an unrelated app |
| Shopify App Store listing | **Not live on 2026-11-03**, since no listing was found in the App Store index. Submitted in week 1 as "Pico AI Shopping Assistant", planned live in week 3 with a buffer to week 6. Until then, merchant calls to action use the site's own "Connect your store" button (D2) |
| Category name | AI shopping assistant, also called conversational product discovery. On the Shopify App Store it sits between the chat and the search and discovery categories. Shopify also curates an "AI Shopping Assistants" collection, 17 apps in the snapshot read on 2026-11-03. Pico lists in the Chat category, where the slate's direct substitutes list (D42) |
| One-liner, from the source | Pico is an AI shopping assistant that lets shoppers describe what they want in plain language and returns real products from the merchant's own catalog |
| Core promise, verbatim | "Recommendations come only from synced catalog data. Pico does not invent prices, stock, or capabilities." Narrowed form in Section 5 |
| How it is delivered | A chat widget on the storefront, managed from a seven-page merchant dashboard |
| Platforms today | Shopify, through OAuth, webhooks, and a theme app embed called Pico Assistant. Shopware 6, through Admin API keys and a widget script, no custom plugin. Any custom store that implements Pico's HTTP catalog API |
| Business model | Subscription, monthly or yearly, priced by conversation quota. Free covers 50 conversations a month, Growth covers 600 for $49, Pro covers 2,000 for $99. New accounts get a 14 day Growth trial with no card, then drop to Free. Each plan connects one store. **Decided 2026-11-03:** yearly prices give two months free, Growth $490 and Pro $990 (D26). A fourth plan fills the anchor: Scale, $299 a month or $2,990 a year for 6,000 conversations (D27). One conversation is a chat thread with at least one AI reply, and the same shopper on the same device within 24 hours counts once (D24). At the quota, Pico alerts at 80% and 100%, gives paid plans a 10% grace allowance, then pauses, and never charges overage (D25) |
| Billing rails | Shopify Billing for App Store installs. Paddle, or InstaPay with EGP pricing in Egypt, for Shopware and custom stores |
| Shopify's revenue share on App Store income | 0% on the first $1M of lifetime revenue, 15% above that, since Shopify ended the annual reset in 2025 ([Shopify changelog](https://shopify.dev/changelog/update-to-shopifys-app-developer-revenue-share)). App charges are set in USD. Local-currency estimates exist for 14 currencies, none of them AED, SAR, or EGP. A Phase 9 input for net price |
| Origin market | **An Egypt-based team selling in USD worldwide, USA first** (D5). Read from two of the owner's own materials: the source's EGP and InstaPay billing rail, and the site's default region, Egypt, listed first in its footer |

## Run 1, Shopify merchants

| Field | Value |
|---|---|
| Target geography, **decided** | Global, **USA first**: 1,253,193 live US Shopify stores (StoreLeads, 2026). The GCC (Saudi Arabia, UAE, Kuwait, Qatar, Bahrain, Oman) is shown as a secondary go-to-market for later, kept in the dashboards for reference and not pursued now. Owner decision, 2026-11-03 |
| Niche focus, **confirmed by Phase 4** | Shopify merchants, US first, whose shoppers struggle to find the right product by browsing or keyword search: catalogs with many similar or technical products, and stores that sell in more than one language. Arabic-speaking storefronts belong to the secondary GCC market for later. Proposed from the feature set, then confirmed by Phase 4, with catalog cutoffs of 100 products for Level 1 and 250 for Level 2 (D53). Step 0.H frames it: Health, Sports, Pets & Animals, Autos & Vehicles, and Consumer Electronics hold up to about 488,000 live Shopify stores (StoreLeads, 2026, overlap unknown, an upper bound) |
| Who pays, **confirmed by Phase 5** | The store owner on small stores. The ecommerce manager or head of ecommerce on larger ones |
| Who installs | The owner, or the agency or developer who runs the store. The second case is the bridge to Run 2 |
| Who uses | The merchant uses the dashboard. Shoppers use the widget |

## Run 2, Shopify implementers

| Field | Value |
|---|---|
| Niche focus, **decided by the owner** | A standalone go-to-market for every kind of Shopify implementer: build agencies at every Partner Directory tier, Plus agencies, CRO agencies, Shopify developers, theme developers and designers, and freelancers on Upwork and Fiverr, who install and maintain apps for client stores. US-serving first, wherever the implementer is based |
| Channels, **decided by the owner** | Email, LinkedIn, and job posts on Upwork and Fiverr. Owner decision, 2026-11-03 |
| Engagement path, **decided by the owner** | 1. A paid small engagement in which the implementer installs Pico on a store they work on and gives usability feedback. 2. An interview. 3. A case study with the client store, written only with the merchant's and the implementer's permission. 4. An offer to join a partnership program with affiliate incentives, referral traffic, and more, designed to win them over from the tools they use now. **Decided 2026-11-03:** $150 for a session of up to 90 minutes (D33), $75 for an optional interview (D34), 25% of each referred store's subscription for 24 months and 30% for lead partners (D35), and referral traffic routed from merchants' setup requests, with no volume promised (D39) |
| What they need from Pico | A product their clients keep paying for, a setup that does not break the theme, a way to manage several client stores, and a reason to recommend Pico over the app already in their stack. The source supplies the first two in part. The last two are decided: the existing admin role on each client store now, a free agency workspace once 10 partners each have 3 or more active stores (D23), and the partner terms in D35 |
| What exists for them today, per source | A downloadable setup skill for Cursor, Claude Code, Codex, and Antigravity covering Shopify, Shopware 6, and custom apps. A sandbox store. Role based access with owner, admin, analyst, and support roles |
| What does not exist, per source | Any partner, referral, or affiliate program. Any multi-store or agency plan, since each plan connects one store. Any agency dashboard across client stores. Any stated development store policy. Step 0.G found that Shopify App Pricing lets an app mark paid plans "free for testing" on other partners' development stores, so C11 can be a billing setting rather than a program cost |

---

# 2. COMPETITORS

The skill wants 5 to 6 named competitors with websites, and its Step 2.1 is an external research step where you source them.

**Status of the slates below.** Accepted by the owner (D10). Confirmed or swapped slot by slot by the full Step 0 on 2026-11-03, using installs, reviews, App Store shelf, implementer stacks, and billing unit as evidence that buyers evaluate each one. Reasons and sources for every slot are in `research/2026-11-03-step-0-slate-decision.md`. **Accepted by the owner on 2026-11-03** (D10). Run 1 slot 1 was swapped, Run 2 slot 3 was named, and every other slot was confirmed. Facts were read through the search index, so each slate competitor's listing, pricing page, and reviews get a page-loaded check before Steps 2.1 and 2.7.

**This market is too large for one slate, so the run uses three tiers.**

| Tier | Size | Used by |
|---|---|---|
| Slate | 6 per run | Phase 2, every table. This is what the skill means by competitors |
| Watchlist | About 20 | Step 1.1 feature presence, so Phase 1 competitiveness scores reflect the whole market and not just the slate |
| Landscape | Everything found | Awareness, Phase 3 indirect positioning, and later refreshes. Lives in the research file |

**Selection rule:** a competitor earns a slot only if the buyer actually evaluates it. Not who you think of as a rival, who they consider instead. `RESEARCH-PROMPTS.md` Step 0 sources the slate. It was run in full on 2026-11-03, and the landscape it found is indexed in `research/2026-11-03-step-0-slate-decision.md`.

## Run 1 slate, Shopify merchants

| Slot | Source from | Slate | Step 0 decision | Why it belongs | Swap note |
|---|---|---|---|---|---|
| 1 | Closest direct substitute, same category, same promise | **Chatty AI Chatbot & Live Chat**, [App Store](https://apps.shopify.com/chatty), [pricing](https://chatty.net/blog/ai-chatbot-pricing/) | **Swapped** from Manifest AI | AI sales chat with recommendations, upsells, and checkout links. Bills per AI conversation, with a free plan of 50 AI conversations a month: Pico's unit and Pico's free allowance. About 1,900 reviews and about 9,000 detected installs (StoreLeads, 2026). Manifest AI has about 61 reviews and about 330 installs, and its paid prices were not visible, so its "price band" reason could not be confirmed | Swap to Zipchat AI ([App Store](https://apps.shopify.com/zipchat)) if Phase 2 finds buyers compare growth-stage chat apps: installs up 100% in a year, but billed per AI reply, not per conversation, and no free plan on its pricing page. Manifest AI moves to the watchlist |
| 2 | Free or low-cost alternative with most of the attention | Shopify Inbox with the Inbox agent (the AI sales associate), [Shopify News](https://www.shopify.com/news/fall-26-edition-merchant), [Help](https://help.shopify.com/en/manual/inbox/assigning-your-ai-staff-member) | **Confirmed** | Free and native. About 358,000 detected installs and about 5,810 reviews. Answers product, policy, and order questions, suggests products, and since the Fall '26 Edition (2026-10-28) starts checkout from the chat. Personalizes with Shop sign-in. Needs new customer accounts | None. This slot is not optional |
| 3 | Where they solve it today without help | Shopify's own search and filters: Search & Discovery with semantic search, collections, filters, and search analytics, [Shopify Help](https://help.shopify.com/manual/online-store/search-and-discovery/search) | **Confirmed**, two facts updated | What every merchant already has. Semantic search covers eligible stores, now in more languages than English per [Shopify's changelog](https://changelog.shopify.com/posts/semantic-search-now-supports-more-languages). It also reports **"Searches with no results" and "Searches with no clicks"** for the search bar ([Help](https://help.shopify.com/en/manual/online-store/storefront-search/search-and-discovery-analytics)) | For ICP Level 2, name the store's existing search app: Boost, Smart Product Filter & Search, or Searchanise, about 50,000 detected installs together. All three are on the watchlist |
| 4 | Better-known adjacent option they find first | Tidio with Lyro, [App Store](https://apps.shopify.com/tidio-chat) | **Confirmed** | The most-installed third-party chat app after Inbox (about 27,500 installs, about 1,356 reviews). Lyro recommends from Shopify product data, skips out-of-stock items, bills per AI conversation, and answers in 48 languages including Modern Arabic | Swap to Gorgias Shopping Assistant for ICP Level 2 stores already on Gorgias (about 25,100 installs, growing). Rep AI stays on the watchlist: about 1,000 installs, priced per visitor, English and Spanish only |
| 5 | Build it or hire it | Build: a developer connects an LLM through the Storefront Catalog MCP on UCP, using Shopify's [AI Toolkit](https://shopify.dev/docs/apps/build/ai-toolkit). Hire: live chat staff on Inbox or a helpdesk | **Confirmed**, both halves | Not a company. Cost bands from Step 0.D: freelance builds $30 to $1,000, agency builds $8,000 to $90,000 per agency guides (vendor-sourced), US chat staff median $21.53 an hour (BLS, May 2025), UK floor £12.71 an hour, offshore outsourced $6 to $16 an hour (vendor-sourced) | Keep both halves. Hire matters to small stores, build matters to Level 2 |
| 6 | Institutional option, often a partner rather than a rival | Shopify's agentic commerce stack: Agentic Storefronts (ChatGPT, Copilot, AI Mode, Gemini, Meta), the catalog MCP servers on UCP, WebMCP on every storefront, Shop.md, and the agentic knowledge base, [Shopify News](https://shopify.com/news/agentic-commerce-momentum), [Fall '26](https://www.shopify.com/news/fall-26-edition-merchant) | **Confirmed**, widened | Shopify itself, moving discovery into AI agents on and off the store. Pico's job is on-store discovery, so this is both a substitute and a context Pico has to fit into | None. Never position against Shopify, see Section 5 |

## Run 1 watchlist

For Step 1.1 feature presence. 22 names, confirmed or changed by Step 0 on 2026-11-03. Sources and reasons in `research/2026-11-03-step-0-slate-decision.md`.

- **AI shopping assistants and AI sales chat:** Rep AI, Zipchat AI, Dialog, Alhena AI, Wizybot, Manifest AI (moved down from slot 1), Verifast (replaces Octocom: 144 reviews against 10, Arabic named), Moose AI Chatbot & Live Chat (replaces Wantly: about 8,100 installs, up 463%), Luma (added: an Arabic-first Shopify app for the right to left row).
- **Support platforms with a shopping role:** Gorgias Shopping Assistant, Intercom Fin for Ecommerce, Klaviyo Customer Agent. Chatty moved up to slot 1.
- **Search and discovery:** Fast Simon, Boost AI Search & Filter, Searchanise, Doofinder, Smart Product Filter & Search (added: the most-reviewed search app).
- **Recommendations, quizzes, video, messaging:** Rebuy, Octane AI, RevenueHunt, Tolstoy, Zoko.
- **Platform agents to monitor, not scored:** Microsoft Brand Agents through Clarity, Google's Business Agent, Meta Business AI on WhatsApp.

## Run 2 slate, Shopify implementers

Here the question is different: what does an implementer recommend, install, or build instead of Pico.

| Slot | Source from | Slate | Step 0 decision | Why it belongs | Swap note |
|---|---|---|---|---|---|
| 1 | Closest direct substitute: an AI shopping assistant with an agency program | Gorgias Shopping Assistant and the Gorgias agency partner program, [Gorgias help](https://helpcenter.gorgias.com/en-US/agency-partner-program-81969) | **Confirmed** | On 13 of 26 sampled agency stack pages, where agencies display Gorgias tiers as credentials. Agency program: 20% for 2 to 3 years, plus a 15% bounty at Elite (help center, updated 2026-01-22). Now has a pre-purchase Shopping Assistant | Rep AI appeared on none of the 26 pages, so the brief's swap condition did not hold. Rep AI's program stays on the watchlist |
| 2 | Free or low-cost alternative | Shopify Inbox with the Inbox agent | **Confirmed** | The zero-setup recommendation an implementer can make in one sentence, with nothing to maintain. Shopify's own developer docs point merchants who want AI chat without code to it | None |
| 3 | Where they solve it today without help | **Rebuy plus Shopify Search & Discovery**, [Rebuy partners](https://www.rebuyengine.com/partners) | **Named** by Step 0.F | Rebuy is the only discovery app on more than three of 26 sampled agency stack pages (7, plus a blog mention), with about 15,200 installs, up 24.7%. No dedicated search app appeared on any page, so search is left to Shopify's native app. Rebuy pays agencies a 5% managed share for active work regardless of who referred the brand | Nosto for Plus-level agencies (3 of 26 pages) |
| 4 | Better-known adjacent option | Klaviyo Customer Agent, [Klaviyo](https://www.klaviyo.com/solutions/ai/customer-agent) | **Confirmed** | Klaviyo is on 17 of 26 sampled agency stack pages, the most of any app. Customer Agent now lists 113 languages, answers on web chat, email, SMS, and WhatsApp, and starts at $50 a month for 75 conversations. It arrives inside K:Partners, a relationship the agency already has | Intercom Fin if Phase 2 finds support-led agencies matter more |
| 5 | Build it | Custom build on the Storefront Catalog MCP on UCP with an LLM, using Shopify's AI Toolkit in a coding agent | **Confirmed** | Billable hours for the agency, and the same workflow Pico's setup skill targets. Freelancers already sell builds ($30 to $1,000) and installation of existing AI chat apps (about $100) | None. This is the most important Run 2 slot for developers |
| 6 | Institutional option | Shopify Partner Program and Partner Directory, [Shopify Help](https://help.shopify.com/en/partners/partner-program/how-to-earn) | **Confirmed**, widened | Defines what implementers expect from an app partner, and is the venue where they are found. Shopify pays 20% of a referred merchant's subscription, $2,500 per Plus referral, and since 2026-08-10 a launch partner share of 20% of subscription plus 0.1% of eligible online GMV for 4 years | None |

## Run 2 watchlist

13 names, confirmed or changed by Step 0 on 2026-11-03. Reasons in `research/2026-11-03-step-0-slate-decision.md`.

Rep AI Partner Program, Zipchat agency program (added: the only program found that lets agencies resell under their own brand at their own pricing), Tidio Agency Partner Program, Intercom Solution Partner Program, Octane AI partners, Fast Simon partners, Nosto (added), Recharge, Okendo, and LoyaltyLion programs (added: benchmarks from the apps agencies list most), Voiceflow, Chatbase, and freelance AI chatbot gigs on Upwork, Fiverr, and Storetasker, as a segment. **Removed:** the Rebuy and Klaviyo programs, now inside slots 3 and 4. Boost and Searchanise, which appeared on none of the 26 sampled agency stack pages and have no partner program found. They stay on the Run 1 watchlist.

---

# 3. PRODUCT FEATURES LIST

Phase 1 runs the skill's two-axis Product Feature Matrix as written for Run 1. Run 2 rates the implementer-facing rows plus the candidate partner elements, see `SKILL-ADAPTATION.md`.

Items marked **stated** came from the source and are in the product. Items marked **candidate** are not in the product per the source, or the source is silent. They are here to be rated and then kept or cut during Phase 1, which is what the matrix is for. **A candidate is never claimed in copy.**

## Shopper-facing, stated

| # | Feature | Source |
|---|---|---|
| 1 | Natural language request, interpreted by an AI model, matched against the synced catalog by keywords, synonyms, and minimum or maximum price | stated |
| 2 | Product cards with image, name, price, in stock or out of stock label, and a View link. Merchant sets how many per reply | stated |
| 3 | Add to cart from the card, using the store's own cart on Shopify and Shopware. Picks an in stock variant. Blocks out of stock items | stated |
| 4 | One clarifying question when a request is too vague | stated |
| 5 | Suggested reply chips on the opening screen and after each answer | stated |
| 6 | Product comparison inside a chat reply | stated |
| 7 | Replies in the shopper's language, a language switcher, Arabic right to left, and widget text translated for 10 languages | stated |
| 8 | Personalized welcome by personality, or the merchant's custom text | stated |
| 9 | Session memory across a page reload on the same device | stated |

## Merchant-facing, stated

| # | Feature | Source |
|---|---|---|
| 10 | Overview: conversations, product click through rate, and add to cart rate, 30 days against the prior 30, plus integration and sync health | stated |
| 11 | Discovery analytics: funnel with step conversion, searches, product result rate, zero result rate, clicks, top phrases, zero result and weak click phrases, product impressions and clicks | stated |
| 12 | Catalog sync on demand, retry, sync log, product and variant counts, searchable product list | stated |
| 13 | Assistant voice controls: name, subtitle, greeting, chips per language, languages, four personalities, warmth 1 to 5, length, emoji, clarification style, recommendations per reply, custom welcome, tone guidelines up to 1,000 characters, custom add to cart confirmation, preview | stated |
| 14 | Plan and usage: quota meter, upgrade, cancel with a reason, optional 50 percent retention offer for two billing periods | stated |
| 15 | Account: email verification, password reset, role based access with owner, admin, analyst, support, in-dashboard feedback | stated |

## Setup and platform, stated

| # | Feature | Source |
|---|---|---|
| 16 | Shopify OAuth install, webhooks, encrypted tokens, theme app embed, guided checklist: authorize, enable embed, sync, confirm the widget was seen | stated |
| 17 | Shopware 6 connection through the Admin API with no custom plugin. Run 3 only | stated |
| 18 | Custom store connection through Pico's HTTP catalog API | stated |
| 19 | Sandbox store with a sample outdoor gear catalog on the real API | stated |
| 20 | Downloadable setup skill that Cursor, Claude Code, Codex, and Antigravity can follow, including dashboard steps | stated |
| 21 | Free plan, plus a 14 day Growth trial with no card | stated |
| 22 | EGP pricing paid by InstaPay in Egypt. Applies to Shopware and custom stores, not Shopify App Store installs | stated |

## Candidates, not in the product per source

| # | Candidate | Why it is here | Source |
|---|---|---|---|
| C1 | Revenue attribution, orders and revenue influenced by Pico | The source lists it as a current limit. The whole category sells on it | candidate |
| C2 | Semantic or vector search | A current limit. Shopify's free native search has it for eligible stores | candidate |
| C3 | Multi-store plan or agency workspace | A current limit, since each plan connects one store. The first thing Run 2 will ask for | candidate |
| C4 | Comparison screen in the widget | A current limit. Comparison happens in chat replies only | candidate |
| C5 | Human handoff or live chat | Source is silent. Merchants assume it, and most competitors have it. **Not built, not claimed, not in launch scope** (D12) | candidate |
| C6 | Order status, returns, and policy answers | Source is silent. Shopify Inbox, Gorgias, Fin, and Tidio cover these. **Out of scope by design: Pico is a pre-purchase assistant** (D13) | candidate |
| C7 | Messaging channels beyond the storefront, such as WhatsApp or Instagram | Source is silent. Matters most in Arabic-speaking markets. **Not in scope until the GCC opens** (D14) | candidate |
| C8 | Integrations with the marketing stack, such as GA4 or Klaviyo | Source is silent. **Not in launch scope. A GA4 event export comes first, built with C1** (D15) | candidate |
| C9 | Holdout or A/B measurement of incremental lift | Would let Pico measure the outcome the category claims | candidate |
| C10 | Partner, referral, or affiliate program | Source is silent. Run 2 designs it | candidate |
| C11 | Free installs on Shopify development stores for implementers | Source is silent. Implementers expect it | candidate |
| C12 | Proactive prompts, such as on product pages | Source is silent. Several competitors lead with it | candidate |

## What Step 0 found about these rows

Recorded so Phase 1 scores against current evidence. None of it changes what Pico does, and Phase 1 still makes the call. Sources in `research/`.

| Row | Finding, 2026-11-03 | What Phase 1 should weigh |
|---|---|---|
| 1, 2, 3 | Dozens of App Store listings describe catalog-only answers, product cards, and add to cart, including apps with no reviews. Tidio's Lyro skips out-of-stock items | Table stakes, as Section 5 already assumes |
| 7 | Intercom Fin and Tidio Lyro answer in Arabic, Klaviyo Customer Agent lists 113 languages, the Inbox agent replies in the customer's language, Rep AI is English and Spanish only. None of them documents right to left product cards, a language switcher, or separate merchant copy per language. Arabic-first apps exist on Shopify (Luma, shamz.ai), and Salla ships its own Arabic AI search | Arabic replies are not rare. The right to left widget combination is the narrower row to score |
| 11 | Shopify's free Search & Discovery already reports "Searches with no results" and "Searches with no clicks" for the search bar. Two small apps, ShopGenie and Seekr, describe similar reports | Score it for conversational requests only. The demand driver test in `SKILL-ADAPTATION.md` Phase 1 fails as written for search-bar terms |
| 16 | Shopify app embeds are off by default after install and stay active only on the theme where they were enabled. They work in vintage and Online Store 2.0 themes | The activation risk is documented by Shopify and recurs on every theme change |
| 19 | No competitor sampled offered a sandbox store with a sample catalog | Test its competitiveness in Step 1.1 |
| 20 | Shopify ships its own skills and MCP server for coding agents (AI Toolkit) | A distribution fit, not a differentiator |
| 21 | Chatty and CartPilot also start at 50 free conversations. Trials of 7 to 30 days are common | Commodity |
| C3, C10 | Every agency program found has a recurring share and tiers. Klaviyo and Intercom Fin offer multi-store views | The Run 2 floor, as `SKILL-ADAPTATION.md` predicted |
| C11 | Shopify App Pricing lets an app mark paid plans free for testing on other partners' development stores | A billing setting, cheap to deliver |

**Deliberately not offered, and not to be rated:** checkout inside the chat, since Pico adds to the store's own cart and the store's checkout takes over. Revenue or conversion reporting, until C1 ships. Answers about orders, returns, or policies, out of scope by design (D13). One plan covering several stores. Naming these plainly is useful, because the category has trained buyers to assume all four.

---

# 4. BUSINESS CONTEXT

The skill's fourth input block. None of these came from the source, so each is resolved in `DECISIONS.md` with its type shown.

```
Current team structure:      Assumption (D6). Founder-led, two people: the founder runs
                             go-to-market and partnerships, one engineer runs product and
                             setup support. Design and video contracted by the asset
Monthly burn rate:           Decision (D31). The GTM spends at most $3,000 a month in cash,
                             $9,000 over the first 90 days. Company burn sits outside the plan
Runway remaining:            Decision (D32). Spend is released in 30-day blocks, each needing
                             at least 6 months of runway after it, checked by the CFO
Channels tried, and results: Researched (D7). None tried with recorded results, pre-launch
```

"None tried, pre-launch" is a real answer, and it is why Phase 8 opens every channel with something a buyer can check.

Three more lines the run needs that the source does not carry:

```
App Store listing live, and since when:   Not live on 2026-11-03. Planned live in week 3 (D2)
Installs, active stores, paying stores:   None recorded, pre-launch (D8)
App Store rating and review count:        None, no listing yet (D8)
```

## Decisions that change the output, all closed on 2026-11-03

Ordered by what they block. Each was proposed here, then closed by the owner or in `DECISIONS.md`, with the decision numbers shown.

| # | Decision | Blocks | Note | Closed on 2026-11-03 |
|---|---|---|---|---|
| 1 | Website and App Store listing URLs, and whether the listing is live | Phase 2 own row, Step 2.1, deck slide 1 | Pico's Phase 2 row is filled from this brief and the site, with strengths and weaknesses taken from the source's capabilities and its own current limits | **Closed.** Website picofinds.com (D1). Listing not live, submitted in week 1, planned live in week 3 (D2). The site is aligned with the US-first plan before the first Run 2 email (D3) |
| 2 | The proof set: installs, reviews, any merchant who agrees to be named, and in what wording | Phase 6, Phase 7 stage 6, deck | Empty and closed, see Section 5 | **Closed by the owner: empty and closed for customer proof.** In each run, the Supporting Proof Point and the Social Proof headline in all nine copy drills carry open proof, a claim the reader can check now, labelled as such (D4) |
| 3 | Target geography: global English-speaking Shopify stores, Arabic-speaking markets first, or both with one as primary | Phase 4, Step 0.E, Phase 8 | **Proposed:** Run 1 primary is English-speaking Shopify stores globally, with Arabic-speaking stores as a named secondary segment. Reason: most Shopify stores are in English-speaking markets, and in Egypt and Saudi Arabia many stores are on WooCommerce, Salla, Zid, or local builders that Pico reaches only through the custom API. Reverse it if the founder's network and early users are in the Gulf or Egypt | **Answered by the owner: global, USA first.** The GCC is shown as a secondary go-to-market for later, there if needed and not pursued now. Step 0.E supports it: the US, UK, Canada, and Australia hold about 1.79 million live Shopify stores, and Saudi Arabia is mostly on Salla, Zid, and WooCommerce. Egypt, outside the GCC, stays in research as context only |
| 4 | Run 2 offer: partner program, revenue share, multi-store or agency plan, development store installs, agency dashboard | Run 2 Phase 1 and Phase 9 | None existed. Run 2 designed it | **Closed.** The owner's outline: a paid usability engagement, interviews, case studies with client stores, then a partnership program, reached by email, LinkedIn, Upwork, and Fiverr. The numbers: $150 a session (D33), $75 an interview (D34), 25% for 24 months, 30% for lead partners, a 10% managed share, no bounty (D35), monthly payouts (D36), 30 sessions in 60 days (D37), deal registration (D38), routed setup requests for traffic (D39), tiers and standing (D40), no separate agency price under Shopify Billing (D41), free development store installs (D22), and a workspace once 10 partners qualify (D23) |
| 5 | Whether Shopware 6 and custom stores get their own run | Run 3 | Defer. Shopify first | **Closed by the owner: deferred.** EGP prices stay out of Runs 1 and 2 (D9) |
| 6 | Status of C5 to C8: human handoff, order and policy answers, messaging channels, marketing integrations | Phase 1 scoring, Step 1.1, Phase 2.10 | Treated as not built | **Closed.** None is built or claimed. Handoff waits on a demand trigger (D12), order answers are out of scope by design (D13), channels wait for the GCC (D14), and a GA4 export comes first among integrations (D15) |
| 7 | Pricing gaps: yearly prices, EGP prices, the definition of a conversation, overage behavior at quota, and whether a fourth tier is in scope | Phase 9 | Review rather than rebuild. Tidio's published definition was the benchmark: "a customer interaction initiated through any channel integrated with Tidio that has at least one reply from our AI agent" ([Tidio](https://www.tidio.com/blog/chatbot-pricing/)) | **Closed.** A conversation is a thread with at least one AI reply, once per shopper and device per 24 hours (D24). Alerts, grace, pause, and never overage at the quota (D25). Two months free on yearly plans (D26). A fourth tier, Scale, $299 for 6,000 (D27). EGP prices stay in Run 3 (D9) |
| 8 | Confirmation of both slates, slot by slot | Phase 2 | The slates in Section 2, after a full Step 0 rerun | **Closed by the owner,** who asked on 2026-11-03 for all dashboards to be built on them without changing a slot. Run 1 slot 1 swapped to Chatty, Run 2 slot 3 named, every other slot confirmed (D10). Any later swap reopens Phase 2 |

---

# 5. POSITIONING AND CLAIM CONSTRAINTS

Phase 3 writes positioning statements, Phase 6 writes twenty-seven headlines across nine copy drills, and the deck compresses all of it. All three will reach for the claims below, so the narrowed form has to be here rather than remembered.

**The governing sensitivity.** This category sells on conversion and revenue lift, and Pico measures neither. Competitors lead with lift claims. Pico's own dashboard shows revenue attribution as unavailable. So every Pico claim stays inside what Pico measures: what shoppers asked, what they were shown, what they clicked, and what they added to cart. The moment a draft says sales, revenue, conversion, or ROI about Pico, it has left the evidence.

**The second sensitivity.** Shopify is Pico's platform, its billing rail, its distribution, and now a competitor through Inbox, semantic search, and Agentic Storefronts. Copy never disparages Shopify or its native tools. Position on what Pico is built around, never on what Shopify lacks.

## The narrowing drill

| Do not write | Write instead | Counter-example that forces the narrowing |
|---|---|---|
| "Pico never makes things up." "Zero hallucinations." "100% accurate." | "Product cards show names, prices, and stock from your synced catalog. Recommendations are drawn from synced products." | The AI model writes the reply text, including comparisons, so prose can still describe a product imperfectly even when every card comes from the catalog |
| "The only AI assistant that sticks to your real catalog." | "Built around your synced catalog." | Manifest AI, Wantly, DBestChatBot, Fast Simon, and Bloomreach all describe catalog-only or in-stock answers. Tidio's Lyro skips out-of-stock items, and Step 0.A found dozens of App Store listings describing catalog-only answers. Catalog grounding is table stakes, not a differentiator, until Phase 2 says otherwise |
| "Live stock." "Real-time inventory." | "Stock as of the last catalog sync. On Shopify, webhooks keep the catalog updated." | Shopware and custom stores sync on demand or by job, and the source mentions webhooks for Shopify only. Confirm webhook coverage for stock before using "updated" |
| "AI-powered semantic search." "Understands what shoppers mean." | "Shoppers ask in their own words. An AI model reads the request, then Pico matches it to your catalog by keywords, synonyms, and price range." | The source states there is no semantic vector search. A request whose words match nothing in the catalog returns nothing |
| "Smarter than Shopify search." | Do not compare. Describe the conversation: "Shoppers who don't know the product name can describe what they need." | Shopify's free Search & Discovery has semantic search for eligible stores, now in more languages than English per Shopify's changelog (Step 0.C) |
| "Fully multilingual store." "Speaks every language." | "Replies follow the shopper's language. Widget text is translated for 10 languages: English, Arabic, German, Greek, Spanish, French, Italian, Dutch, Portuguese, and Turkish." | Outside those 10, the widget text is not translated. Product cards show catalog text as synced, and translation of it is never implied (D20) |
| "The Arabic AI shopping assistant." "Best for Arabic." "Understands every Arabic dialect." | "Arabic replies display right to left, with a language switcher and separate merchant copy per language." | No dialect handling is stated. Arabic-first assistants already exist for Salla, Zid, and Shopify, Salla ships its own Arabic AI search, and Intercom Fin and Tidio Lyro answer in Arabic (Step 0.E) |
| "Shoppers can buy right in the chat." "Checkout in chat." | "One tap adds the product to your store's own cart on Shopify and Shopware." | Pico adds to cart. Checkout stays in the store. Custom stores may not show the button at all, since it appears only when the platform supports it |
| "Compare products side by side." | "Pico can compare products inside its reply." | There is no comparison screen |
| "Pico remembers your shoppers." | "The conversation survives a page reload on the same device." | No cross-device memory, and no personalization from order history, is stated |
| "Increases sales." "Boosts conversion." "Pays for itself." "Drives revenue." | "See what shoppers asked for, what they clicked, and what they added to cart." | Revenue attribution is not measured. The dashboard says so |
| "Shows you what customers want that you don't sell." | "Shows phrases shoppers asked the assistant that returned no products or few clicks, which points to gaps in the catalog or in how products are described." | A zero result can mean a missing product, or a product described in words the shopper did not use. Shopify's Search & Discovery already reports search-bar terms with no results and no clicks, so Pico's report is about what shoppers asked the assistant, never a view Shopify lacks (Step 0.C) |
| "Sounds exactly like your brand." | "Set personality, warmth, answer length, emoji use, clarification style, and up to 1,000 characters of tone guidelines." | Controls shape the voice. They do not guarantee it |
| "Works with any store." | "Shopify and Shopware 6 today. Other stacks connect by implementing Pico's HTTP catalog API." | WooCommerce, BigCommerce, Salla, and Zid are not supported natively. A custom store needs development work |
| "Installs itself." "No developer needed." "Zero setup." | "Install from the App Store and follow a four-step checklist. Developers can hand the setup to a coding agent with Pico's downloadable setup skill." | OAuth authorization and the theme embed still need someone with store access. Shopify app embeds are off by default after install and stay active only on the theme where they were enabled (Step 0.F). Themes are claimed through the app embed and tested on Dawn and Horizon before launch (D16). Headless storefronts are not claimed (D17). Speed impact is measured against a 10-point Lighthouse budget and published, never claimed as none (D18) |
| "Free forever." "Unlimited." | "Free covers 50 conversations a month." | Every plan has a conversation quota |
| "One plan for all your stores." "Built for agencies." | "Each plan connects one store." | The source says so. Agency features are candidates, not product |
| "Pay locally across the Middle East." "Pay with InstaPay." in Shopify copy | "Shopware and custom stores in Egypt can pay in EGP by InstaPay." | Shopify App Store installs bill through Shopify Billing. InstaPay is Egypt only |
| "Shopware with no installation." | "Connects to Shopware 6 through the Admin API, with no custom plugin. A widget script goes on the storefront." | A script is still added. Shopware 5 is not mentioned. Run 3 only |
| "Cheaper than Rep AI." "Unlike other chatbots." Any named comparison | No comparison in customer-facing copy unless Phase 2 has a sourced, dated finding. A pricing-model contrast, per conversation against per visitor, is allowed only after checking the competitor's current pricing page, with the date recorded | Prices in this category changed between sources dated months apart. A stale comparison is a false claim. Step 0.A also found billing units of conversation, AI reply, visitor, resolution, session, and commission, and conflicting prices on the same vendor's own pages |
| "Shopify's search is broken." "Your store is losing sales." | "Shoppers who can't find a product by browsing can ask for it." | Insults the merchant's own setup and the platform Pico depends on, and cannot be shown for any given store |
| Run 2: "Earn recurring revenue." "Certified partner." "White label." "Guaranteed leads." "Join the Pico Partner Program" before the partner page is live in week 6 | "Paid usability sessions: we pay you $150 to install Pico on a store you work on and tell us what works and what breaks." And: "Partners earn 25% of each referred store's subscription for 24 months." And: "Pico gives developers a sandbox and a setup skill their coding agent can follow." | The terms are decided (D33 to D40) and live on picofinds.com/partners from week 6. Traffic cannot be promised as a number until Pico has merchants to refer, so copy describes the routing instead (D39). No certification or white label exists in the source |
| Run 2: "We'll feature your agency in a case study." "Case study with your client." | "With your client's written permission, we write up what changed on their store and credit your work." | A case study is a proof point only under the intake rule below: exact wording, source, and recorded permission from the merchant and the implementer |
| Run 1: "Built for the Middle East." "GCC-ready." in primary-market copy | Keep GCC out of US-first copy. Arabic right to left stays a feature line, worded as above | The GCC is a secondary market for later, per the owner |

## The proof set

**Empty and closed for customer proof.** The source carries no customer, install count, review, testimonial, outcome, or named merchant.

| Proof point | Exact permitted wording | Source | Permission |
|---|---|---|---|
| None yet | | | |

**The intake rule for adding a row.** Name the proof point, its exact permitted wording, its source, and recorded permission from whoever it is about. A row is added only when all four can be filled. A paraphrased proof point is an unapproved proof point.

**Open proof fills the copy drills (D4).** Each Social Proof headline becomes an Open Proof headline, an invitation to check a claim now, and each Supporting Proof Point names a checkable artifact: the sandbox store, the plan page, the four-step checklist, the Analytics page, or Shopify's own documentation. Open proof is labelled as such and never presented as a customer result.

**What can still be said honestly.** The feature set in Section 3 with its narrowed wording, the method of grounding answers in the synced catalog, the low-risk start, and what Pico does not do. Early merchants know they are early.

**Set up before the first paying merchant,** because the chance to capture proof arrives before anyone asks for it:

1. A permission clause in the terms of service covering whether usage outcomes may be cited, in what form, and whether the store may be named.
2. A capture point in the product at value realization, for example when a store's zero result rate first falls after a catalog fix, so the detail is recorded while it is fresh.
3. A rule that process proof is not a proof point. Showing the dashboard, the analytics, or the setup checklist is evidence of seriousness. It belongs in copy and does not go in this table.
4. The owner's planned first source of proof: Run 2's paid usability engagement and the case studies built with implementers' client stores. Each case study enters this table only when all four fields can be filled, with permission recorded from both the merchant and the implementer.

## Also banned in every phase

Any install, store, merchant, or conversation count for Pico. Any rating or review count for Pico. Any conversion, revenue, average order value, or ROI figure attributed to Pico. Any testimonial or named merchant. Any partner rate other than the published terms in D35. Any unsourced market statistic, including Shopify store counts, which range from about 2.8 million to about 6.9 million depending on the tracker, so one source with its method and date, or the figure stays out. Any guarantee. Any claim of semantic or vector search, checkout in chat, or support automation. Any of the adjacent outcomes listed as not offered in Section 3. Any claim that Shopify Inbox, Search & Discovery, or another Shopify tool lacks Arabic, right to left, or any other feature: describe what Pico does instead. Any industry statistic on site search or zero-result rates, until a primary source is page-loaded (Step 0.H found them all secondhand).

**A note on SaaS Relaunch house rules.** This brief was built by SaaS Relaunch, whose own rules exclude fee amounts and refuse paid ads and cold outbound for its own acquisition. Neither applies here. Pico's public plan prices come from the Pico source and are used as product facts, and Phase 8 decides Pico's channels on their merits. For Run 2, the owner chose email, LinkedIn, Upwork, and Fiverr on 2026-11-03.

Mechanics, matching the skill's own deck rule: no em dashes. Commas, periods, or restructure. Also avoid leverage, unlock, seamless, robust, streamline, cutting-edge, and empower.
