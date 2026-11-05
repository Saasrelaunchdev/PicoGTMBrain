---
title: Pico Go-To-Market Master Context
project: Pico
type: gtm_context_file
purpose: Single source of truth for any AI agent or human executing Pico go-to-market work, for both audiences.
version: 1.0
last_updated: 2026-11-04
status_notes: Pre-launch. No installs, reviews, customers, or results exist, and the customer proof log is empty and closed. The Shopify App Store listing is not live (submission week 1, live target week 3). The quota pause behavior, the published conversation definition, yearly prices, the Scale tier, the partner page, and every program element are decided but IN BUILD. Never claim revenue, conversion, or ROI. Never disparage Shopify.
canonical_vocabulary: Pico, PicoFinds, Pico AI Shopping Assistant, Pico Assistant (theme app embed), merchant, shopper, implementer, conversation, synced catalog, product card, zero result phrases, weak click phrases, discovery funnel, Analytics page, Overview, Plan & Usage, sandbox store, setup skill, Shopper Words Test, Paid Usability Session, founding cohort, partner, lead partner, managed share, deal registration, open proof, proof log
---

# Pico Go-To-Market Master Context

This file distills two complete go-to-markets for Pico into one read: one for Shopify merchants, one for the implementers who set up Shopify stores. It exists so that any agent can execute Pico go-to-market work precisely without re-deriving strategy.

If you are an AI agent, read Section 0 first.

---

## 0. Agent operating instructions

**What this file is.** The distilled output of nine dashboards per audience (feature matrix, competitive analysis, positioning, ICP, buying committee, value proposition, customer journey, assets library, pricing), two lead magnets, two deck outlines, a 56-entry decision log, and a research pass dated 2026-11-03. Sources are listed in `ops/asset-index.md`. Every section is authoritative unless a status flag says otherwise.

**How to use it.**

1. Before any customer-facing copy, load the four files in `rules/`. They govern names, status, claims, and mechanics, and they override older phrasing you may pattern-match to.
2. Pick one audience: merchants or implementers. Never blend them in one asset.
3. Write to the funnel stage (Section 13). Do not sell past the stage.
4. Obey the strategic verdicts (Section 9). Do not contradict them, and do not describe a decided direction as shipped.
5. Use `ops/copy-bank.md` verbatim where a line exists. Run `ops/QA-checklist.md` before returning anything.

**Hard guardrails, never violate:**

- No revenue, sales, conversion, ROI, or lift claim about Pico or about a client's results. Pico measures what shoppers asked, saw, clicked, and added to cart.
- No invented proof. No install count, review count, rating, testimonial, named merchant, or metric. The customer proof log is empty.
- No unshipped capability in the present tense. Check `rules/feature-status.md` for every capability you mention.
- No disparaging Shopify or its tools, and no comparative claim about a named competitor in copy that customers see without a sourced, dated finding.
- No copy for an excluded channel (Section 14). Refuse and offer the in-scope channel.
- No em dashes, and none of the banned words in `rules/writing-rules.md`.

---

## 1. House writing rules

Short paragraphs, one to three sentences. Specific numbers, named capabilities, and checkable facts over adjectives. Commas or a restructure instead of em dashes. Banned words: leverage, unlock, seamless, robust, streamline, cutting-edge, empower, and their variants. The register is plain and exact, because merchants are wary of app bills and AI claims, and implementers carry the support burden of anything they recommend. Full rules: `rules/writing-rules.md`.

---

## 2. Canonical vocabulary

| Term | Rule |
|---|---|
| Pico | The product and brand in prose. Company and domain: PicoFinds, picofinds.com |
| Pico AI Shopping Assistant | The App Store listing name, always in full on the listing |
| Pico Assistant | The theme app embed's name in the Shopify theme editor |
| merchant / shopper / implementer | The store that pays / the person asking in the widget / the agency, developer, or freelancer who sets stores up |
| conversation | The billing unit: a chat thread with at least one AI reply, counted once per shopper and device per 24 hours |
| synced catalog | Where every product card comes from. Stock is as of the last catalog sync |
| zero result phrases, weak click phrases | Requests to the assistant that returned no products, or products nobody clicked. Never "searches" alone, since Shopify reports search-bar terms |

Full table, banned near-synonyms, and distinctions: `rules/glossary.md`.

---

## 3. Status ledger

Legend: SHIPPED live now. PARTIAL partly live. IN BUILD decided and unshipped, mark "coming soon" or omit. ROADMAP vision, never a launch claim. OUT out of scope by decision, never claimed.

- Shopper widget: natural language requests, product cards, add to cart, one clarifying question, reply chips, comparison inside a reply, replies in the shopper's language with Arabic right to left, welcome, session memory on one device: SHIPPED.
- Dashboard: Overview, Analytics, Catalog, Integrations, Assistant voice controls, Plan & Usage, Settings, four roles: SHIPPED.
- Setup: Shopify OAuth, theme app embed, four-step checklist, sandbox store, setup skill for coding agents, Free plan, 14 day Growth trial with no card: SHIPPED.
- Shopify App Store listing and Shopify Billing: IN BUILD (submit week 1, live target week 3).
- Quota alerts at 80% and 100%, 10% grace, launcher pause, published conversation definition: IN BUILD.
- Yearly prices, the Scale tier, founding cohort discount: IN BUILD.
- Inventory webhook (week 1), sync failure email (week 2), first insight and weekly summary emails (week 4), proof capture point (week 6), monthly usage summary (week 8), words against the catalog check (week 10): IN BUILD.
- Paid usability sessions, interviews, case studies, partner page, partner share, deal registration, payouts: IN BUILD.
- Revenue attribution, GA4 export, holdout lift measurement, multi-store agency workspace, partner portal: ROADMAP.
- Human handoff, order and policy answers, WhatsApp and Instagram, white label, bounties, headless claims: OUT.

Line by line with weeks and triggers: `rules/feature-status.md`.

---

## 4. Claim hygiene ledger

Every superlative and capability claim passes `rules/do-not-say.md`. The five scoping drills that matter most:

- "Never makes things up" becomes "Product cards show names, prices, and stock from your synced catalog." The AI writes reply text, so prose can still describe a product imperfectly.
- "The only assistant that sticks to your catalog" becomes "Built around your synced catalog." Catalog grounding is table stakes.
- "Semantic search" or "understands what shoppers mean" becomes "An AI model reads the request, then Pico matches it to your catalog by keywords, synonyms, and price range." There is no vector search.
- "Shows what customers want that you don't sell" becomes "Shows phrases shoppers asked the assistant that returned no products or few clicks." A zero result can be a missing product or a product described in other words.
- "Live stock" becomes "Stock as of your last catalog sync."

---

## 5. What Pico is

Pico is an AI shopping assistant for Shopify stores. Shoppers describe what they want in plain language, and Pico replies with product cards drawn from the store's own synced catalog: image, name, price, stock label, and a View link, with one-tap add to the store's own cart. When a request is vague, it asks one clarifying question.

The merchant manages it from a seven-page dashboard. The Analytics page shows the discovery funnel from request to result, click, and cart, the top phrases shoppers used, and the zero result and weak click phrases. The Overview compares 30 days against the prior 30, with sync health.

It installs from the App Store through a theme app embed with no theme code to edit, and a four-step checklist confirms the widget was seen. A sandbox store with a sample outdoor gear catalog runs on the real API, so anyone can try it first. A downloadable setup skill lets Cursor, Claude Code, Codex, and Antigravity run the setup.

Plans are priced by conversations a month: Free 50, Growth 600 for $49, Pro 2,000 for $99, and Scale 6,000 for $299 (IN BUILD). Yearly plans give two months free (IN BUILD). Every feature is on every plan. Each plan connects one store.

The company is PicoFinds, an Egypt-based team selling in USD worldwide, USA first. Planning basis: founder-led, two people.

---

## 6. Feature matrix: what leads, what is table stakes

Scored on demand (wanted by one, some, most, all) against competitiveness (commodity, most vendors, a few others, unique), each on a -20 to +20 axis.

**Merchants.** The only Hero is cost the merchant can predict: the quota meter with a published conversation definition and no overage. Differentiators sit where US demand is low today: the sandbox store, the coding agent setup skill, discovery analytics on what shoppers asked the assistant, the right to left widget, the custom catalog API. Table stakes: natural language requests, product cards, add to cart, voice controls, the Shopify install, the free plan. Table stakes Pico lacks, in roadmap weight order: revenue attribution, human handoff, order and policy answers, GA4 and Klaviyo, proactive prompts. The one candidate that could differentiate is holdout lift measurement.

**Implementers.** The partner floor (recurring share, development store installs, directory listing, tier badges) is table stakes Pico does not yet have. Hero rows, none built: a multi-store workspace, case studies credited to the implementer, pay for managing client stores. Real differentiators today: the sandbox, the setup skill, and the paid usability engagement, which no vendor found offers.

**Demand drivers.** Merchants: the Shopper Words Test, a free first session where the merchant types 10 to 20 requests the way shoppers ask and reads the phrases that found nothing. Implementers: the Paid Usability Session, $150 for up to 90 minutes on a store they work on.

Detail: `reference/feature-matrix.md`.

---

## 7. Competitive market analysis

**Merchant slate:** Chatty, Shopify Inbox with the Inbox agent, Shopify Search & Discovery, Tidio with Lyro, build or hire, and Shopify's agentic commerce stack, plus a 22-name watchlist. The free native agent is the default comparison, on about 358,000 stores (StoreLeads, 2026). Reviewers praise responsive support and easy setup most, and complain most about billing surprises (16+), then setup and theme conflicts, slow support, made-up answers, and results never seen.

| Vector, 0 to 10 | Leader | Pico now | Pico target |
|---|---|---|---|
| 1. Easy setup with responsive help | Chatty 8.9 | 6.8 | 7.9 |
| 2. Support automation breadth | Tidio 8.9 | 1.3 | 1.3, by design |
| 3. Insight into what shoppers ask | Pico 8.3 | 8.3 | 9.1 |
| 4. Answers traceable to the catalog | Pico 7.7, Search & Discovery 7.1 | 7.7 | 8.4 |

**Implementer slate:** the Gorgias agency program, Shopify Inbox, Rebuy plus Search & Discovery, Klaviyo Customer Agent with K:Partners, a custom build with Shopify's AI Toolkit, and the Shopify Partner Program. No AI shopping assistant appears on 26 sampled agency stack pages. Every program found pays after a referral or a closed deal, mostly about 20% for 12 to 36 months.

| Vector, 0 to 10 | Leader | Pico now | Pico target |
|---|---|---|---|
| 1. Established partner economics | Shopify Partner Program 9.1 | 0.4 | 4.6 |
| 2. Presence in the stack agencies sell | Klaviyo 9.3 | 0.2 | 2.1 |
| 3. Paid from the first engagement | Build 6.9 | 0.0 | 8.8 |
| 4. Proof the implementer co-owns | Build 6.8 | 1.1 | 8.3 |

Scores are analyst judgments from cited evidence. Pico's merchant scores rest on documented capability, and its implementer scores on the current state, since nothing runs yet. Detail: `reference/competitive-analysis-merchants.md`, `reference/competitive-analysis-implementers.md`, `reference/competitor-battlecards.md`.

---

## 8. Ideal customer profile and buying committee

**Merchants, Level 1:** US Shopify stores whose shoppers need help choosing between many similar or technical products (health, sports and outdoor, pets, auto parts, consumer electronics), on Shopify's own search with no AI assistant. 100 or more products, 10,000 to 100,000 monthly sessions, a team of 1 to 10, about $150,000 to $3 million a year (planning bands). The owner is user, manager, and decision maker in one person. About 54,300 US stores after the catalog cutoff (calculated, one tracker).

**Merchants, Level 2:** growing brands already paying for a search, quiz, or chat app whose shoppers still miss products. 250 or more products, 100,000 to 1 million sessions, 10 to 50 people plus an agency. The committee holds: ecommerce manager (user), head of ecommerce (manager), founder (decision maker), and a fourth column, the implementer, who rarely signs and can block by never enabling the theme embed.

**Implementers, Level 1:** freelancers and small studios, 1 to 5 people, under $250,000 a year, 2 to 10 active client stores, often on Upwork and Fiverr, who sell app installs for about $100 and have no AI shopping assistant in their build. The freelancer decides alone, and the merchant client pays.

**Implementers, Level 2:** build and CRO agencies, 6 to 50 people, 10 to 100 active client stores, that have deployed AI chat before and want something repeatable. Developer (user), project or account lead (manager), agency owner (decision maker), merchant client (budget holder).

**Design partners.** Merchants: the founding cohort of 20 US stores. Implementers: the paid usability cohort of 30 sessions in 60 days.

Detail: `reference/icp-personas-merchants.md`, `reference/icp-personas-implementers.md`, `reference/market-sizing.md`.

---

## 9. Strategic verdicts (decided)

1. **Two standalone go-to-markets.** Merchants and implementers each have their own positioning, channels, and targets. Shopware 6 and custom stores wait for a deferred third run.
2. **USA first, global English next. The GCC is for later,** and opens only when the US founding cohort is full and at least 5 GCC stores ask for Pico in one quarter.
3. **Merchants: position on insight and traceability, not support automation.** Pico leads on what shoppers ask and on answers traceable to the synced catalog. It deliberately does not do handoff, orders, or policies.
4. **Implementers: position on paid-first and co-owned proof, not partner economics.** Pay for the first session, credit the case study, then offer the partnership.
5. **Open proof, never invented proof.** Every proof field invites the reader to check something now. Customer proof enters only with exact wording, a source, and recorded permission.
6. **No overage, ever.** Alerts, grace, pause. Billing surprise is the category's most frequent complaint.
7. **One value metric.** Plans differ only in conversations a month. No feature gating.
8. **No separate agency price.** Shopify Billing charges each store, so partners earn a share instead.

Full log with dates and reopen triggers: `ops/decisions.md`.

---

## 10. Value proposition: merchants

**Brand promise.** Shoppers find products from your catalog by asking in their own words, and you see what they asked for.

**Positioning.** Built around your synced catalog, with insight into what shoppers ask: the phrases shoppers used, how requests move from results to clicks and add to cart, and which phrases returned nothing or drew few clicks. Stated as what Pico is built around, never as something only Pico does.

| Pillar | Reasons to believe |
|---|---|
| 1. Shoppers ask in their own words | Matched to your catalog by keywords, synonyms, and price range. Cards you can check against the last sync. One clarifying question, one tap to cart |
| 2. See what your shoppers asked for | Discovery funnel. Requests that found nothing. Overview, 30 days against the prior 30 |
| 3. A low-risk start | Sandbox store before install. Free plan and a 14 day Growth trial with no card. Four-step setup, no theme code |

Nine drills with headlines and copy: `reference/value-proposition-merchants.md`.

---

## 11. Value proposition: implementers

**Brand promise.** We pay you to try Pico on a store you work on, and we credit your work when your client agrees.

**Positioning.** An AI shopping assistant built for the people who set up stores: a sandbox and a setup skill that cut setup hours, an Analytics page the client can see, a paid first session, and case studies credited to the implementer.

| Pillar | Reasons to believe |
|---|---|
| 1. Set up without touching theme code | Theme app embed, removed on uninstall. Setup skill for coding agents. Sandbox store |
| 2. Show your client what shoppers ask | Zero result and weak click phrases. Four roles. Overview with sync health |
| 3. Get paid to shape it | $150 a session. A case study that credits your work. 25% of each referred store's subscription for 24 months, 30% for lead partners |

Nine drills: `reference/value-proposition-implementers.md`.

---

## 12. Positioning statements

**Merchant core claim.** Pico shows merchants what their shoppers ask for, and answers shoppers with products drawn from the store's own synced catalog.

- Against AI sales and support agents: not another AI chatbot that tries to answer everything, a shopping assistant built around your synced catalog that shows you what shoppers asked for.
- Against search, quiz, and custom builds: not a smarter search bar, a conversation for shoppers who don't know a product's name.
- Against doing nothing: not one more app to manage, a low-risk way to see what your shoppers are asking for.

**Implementer core claim.** Pico pays implementers for a first session on a store they work on, and, with the client's permission, credits their work in the case study that follows.

- Against vendors with agency programs: not another affiliate program that pays after the referral, a paid session that starts before any referral exists.
- Against custom builds and the native agent: not a build you have to maintain, an app you set up in four steps or hand to your coding agent.
- Against offering nothing: not a new service line to build from scratch, a paid first session on a store you already work on.

**Defensibility.** Both leads are narrow and copyable. The merchant lead compounds only if Pico ships the loop that turns each zero result phrase into a catalog fix and shows whether the fix worked. The implementer lead compounds through credited case studies and repeat deployments across client stores.

**The two objections that matter most.** "Why not the free Shopify Inbox agent?" Pico costs more, and the case rests on what the merchant learns from what shoppers asked, checkable on the free plan. "Is the partner program real?" The terms are decided and published on picofinds.com/partners from week 6, and no partner has been paid yet, so the first payout on the 15th must land on time.

Detail: `reference/positioning.md`, `reference/positioning-verdict.md`, `reference/objection-handling.md`.

---

## 13. Customer journey funnels

Seven stages per audience. Merchants: stage 2 happens on the App Store and in AI answer engines, stage 4 holds an activation sub-funnel, stage 7 is a monthly charge that ends with an uninstall. Implementers: stage 4 is the paid usability engagement, stage 7 is the next client store.

| Stage | Merchant target, first 90 days | Implementer target, first 90 days |
|---|---|---|
| 1. Problem awareness | 25% of scorecard completions open the sandbox | Cold email reply rate 5%, LinkedIn acceptance 30% |
| 2. Solution discovery | Listing visit to install 3% | 10 qualified applicants per Upwork post |
| 3. Vendor evaluation | Sandbox visit to install 10% | Offers accepted |
| 4. Trial or engagement | Widget seen within 24 hours on 65% of installs, median under 20 minutes, trial to paid 15% by day 30 | 30 sessions by day 60, median setup under 30 minutes |
| 5. Value realization | 3 catalog fixes per founding store in 60 days | 15 interviews |
| 6. Expansion and advocacy | 10 unincentivized reviews by day 90, 20 founding stores by day 60 | 3 case study permissions from both sides, 15 partner sign-ups |
| 7. Renewal or repeat | Monthly uninstall rate under 15% | 10 implementers on a second client store, every payout on the 15th |

**Critical success factor, merchants:** the theme embed is switched on, on the live theme, and stays on. Shopify app embeds are off by default after install. **Primary blocker, implementers:** platform rules, Upwork's 24-month non-circumvention term and Fiverr's off-platform ban.

Detail: `reference/customer-journey-merchants.md`, `reference/customer-journey-implementers.md`, `innovation/metrics.json`.

---

## 14. Campaign and channel plan

**Merchant channels:** the Shopify App Store, content and search (including AI answer engines), and the product-led lifecycle. The Shopper Words Test is the top-of-funnel asset in each: listing screenshots, a worksheet guide, a guided sandbox tour. Channel engine: `reference/app-store-engine.md`.

**Implementer channels:** cold email (US recipients only in the first 90 days), LinkedIn messages sent by hand, and job posts on Upwork and Fiverr. The Paid Usability Session is the opener in each. Channel engine: `reference/outreach-engine.md`.

**Excluded, refuse and redirect:** paid ads, cold outbound to store owners, GCC or Arabic-market assets, LinkedIn automation or LinkedIn Ads, any partner pitch inside Upwork or Fiverr, cold email to UK sole traders or anyone in the EU, and Gulf agency outreach.

**Lead magnets:** the Shopify Store Findability Scorecard (merchants) and the Agency AI Shopping Readiness Scorecard (implementers), both on ScoreApp. Detail: `reference/marketing-campaigns.md`, `reference/lead-magnets.md`, `reference/launch-plan.md`.

---

## 15. Quick-reference cheatsheet

- **Merchant one-liner:** Pico shows merchants what their shoppers ask for, and answers with products from the store's own synced catalog.
- **Implementer one-liner:** Paid to test it. Credited when it works.
- **Merchant hook:** the Shopper Words Test. **Implementer hook:** the Paid Usability Session, $150 for up to 90 minutes.
- **Flagship differentiator, merchants:** zero result and weak click phrases from what shoppers asked the assistant.
- **Table stake to win:** setup in four steps through the theme app embed.
- **Proof points on file:** none. Use open proof: the sandbox, the plan page, Shopify's documentation, the setup skill file.
- **Plans:** Free 50, Growth $49 for 600, Pro $99 for 2,000, Scale $299 for 6,000 (IN BUILD). Yearly: $490, $990, $2,990 (IN BUILD).
- **Partner terms (IN BUILD, week 6):** 25% for 24 months, 30% at five active paying stores, 10% managed share, payouts on the 15th, $50 minimum.
- **Founding cohort:** 20 US stores, 50% off for 6 billing periods, opens 2026-12-01.
- **Default rival, merchants:** the free Shopify Inbox agent. Never disparaged.
- **Do not say:** increases sales, never makes things up, semantic search, live stock, checkout in chat, only, free forever, Pico Partner Program before week 6.
- **Always:** no em dashes, open proof labelled as checkable, stock as of the last catalog sync.

---

*End of the Pico GTM master context. When status changes, update the ledger in `rules/` first, then this file, then `ops/decisions.md`, then the copy.*
