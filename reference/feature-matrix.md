# Feature matrix, both audiences

Load to decide what leads a message, what is table stakes, and what is roadmap. Distills the two Product Feature Matrices (2026-11-03). Status of every row lives in `rules/feature-status.md`.

## The model
Each row is scored on demand (wanted by one, some, most, all) and competitiveness (commodity, most vendors, a few others, unique), each mapped to a -20 to +20 axis. Quadrants: Q1 Hero (high demand, high advantage), Q2 Differentiator (low demand, high advantage), Q3 Commodity (low, low), Q4 Table Stakes (high demand, low advantage). Three pairings are not allowed and were checked on every row: some with most vendors, all with unique, one with commodity. A candidate in any quadrant is a roadmap finding, never a claim.

## Merchants: 22 stated rows, 12 candidates

| Quadrant | Rows |
|---|---|
| Q1 Hero | 14 Quota meter and plan controls (7.3, 4.6), Hero once the conversation definition and no-overage rule ship |
| Q2 Differentiator | 6 Comparison in reply, 7 Shopper language with Arabic RTL, 11 Discovery analytics, 12 Sync log, 17 Shopware 6, 18 Custom catalog API, 19 Sandbox store (-0.6, 15.8), 20 Setup skill (-13.1, 14.6), 22 Egypt local payment, C3 Multi-store plan, C4 Comparison screen, C9 Holdout lift measurement |
| Q3 Commodity | 4 Clarifying question, 5 Reply chips, 8 Personalized welcome, 9 Session memory, 15 Roles, C7 WhatsApp, C10 Partner program, C11 Dev store installs |
| Q4 Table Stakes | 1 Natural language requests, 2 Product cards, 3 Add to cart, 10 Overview metrics, 13 Voice controls, 16 Shopify install and checklist, 21 Free plan and trial |
| Q4, missing | C1 Revenue attribution (14.9, -4.3), C2 Semantic search, C5 Human handoff, C6 Order and policy answers, C8 GA4 and Klaviyo, C12 Proactive prompts |

**What it says.** Pico's differentiators sit where US merchant demand is low today. The weightiest roadmap rows are table stakes Pico lacks: C1, C5, C6, C8. The one candidate that could differentiate is C9, holdout measurement, the only honest answer to the category's lift claims. In the GCC, row 7 would move toward Hero.

## Implementers: 7 product rows, 3 candidates, 12 program elements

| Quadrant | Rows |
|---|---|
| Q1 Hero, none built | C3 Multi-store workspace (11.7, 5.3), P3 Case studies with client stores (8.9, 3.7), P11 Pay for managing (10.2, 6.9) |
| Q2 Differentiator | 18 Custom catalog API, 19 Sandbox store, 20 Setup skill, 7 Per-language copy with Arabic RTL, 11 Client-visible analytics, P1 Paid usability engagement (-0.6, 17.2), P2 Paid interviews, P5 Co-marketing, P9 White label, P10 Client discount, P12 Partner manager |
| Q3 Commodity | P7 Certification and training |
| Q4 Table Stakes | 16 Theme app embed install, 15 Roles, P4 Referral traffic |
| Q4, missing | C10 Recurring revenue share, C11 Dev store installs, P6 Directory listing, P8 Tier badges |

**What it says.** The partner floor is table stakes Pico does not have yet. The real differentiators save hours before a client sees anything: the sandbox, the setup skill, and the paid engagement, which pays before any referral. Build order for program elements: dev store installs and the paid sessions first, then case studies, the share, and the directory, then tiers, managed pay, and the workspace on its trigger.

## Demand drivers

**Merchants: the Shopper Words Test.** A free first session: install on Free (50 conversations), type 10 to 20 requests the way shoppers ask, for example Shopify's own "Searches with no results" terms rephrased as questions, and read the requests that returned no products or few clicks. It separates a missing product from a product described in words the shopper did not use. Variants: findability review (white glove), sandbox tour, words against the catalog check (week 10), the Findability Scorecard, the implementer-run audit.

**Implementers: the Paid Usability Session.** $150 for up to 90 minutes: install Pico on a store they work on, run the Shopper Words Test with phrases from the client's customers, report what worked, what broke, and how long setup took. Paid on the platform where they were found. Variants: Client Store Findability Audit, sandbox developer test, setup walkthrough video, Agency AI Shopping Readiness Scorecard, co-authored case study.
