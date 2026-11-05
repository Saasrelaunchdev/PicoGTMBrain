<!-- build: xlsx -->
# Run 2, Dashboard 1: Product Feature Matrix, Shopify implementers

A standalone go-to-market for every kind of Shopify implementer: build agencies at every Partner Directory tier, Plus and CRO agencies, Shopify developers, theme developers, and freelancers on Upwork and Fiverr. US-serving first, wherever they are based. Built on 2026-11-03 with gtm-builder v3.1, Steps 1.2 to 1.7.

**What is rated, per `SKILL-ADAPTATION.md` Phase 1, Run 2.** For an implementer the product is Pico plus the partner relationship, and most of the relationship does not exist yet. So the matrix rates the seven implementer-facing product rows (7, 11, 15, 16, 18, 19, 20), three candidates (C3, C10, C11), and twelve program elements found in Step 1.1 (P1 to P12), including the owner's planned path: the paid usability engagement (P1), interviews (P2), case studies with client stores (P3), and referral traffic (P4). A Program_Elements sheet adds Delivery Effort and Funnel Role, because an element can be wanted and differentiated and still cost Pico more to run than it returns.

Evidence: `research/2026-11-03-run-2-step-1-1-feature-demand.md`, Steps 0.F and 0.G, and Run 2 Steps 2.1 and 2.7. Scores are analyst judgments from that evidence. A candidate or planned element in the Hero quadrant is a design finding, never a claim. Partner numbers are set in `DECISIONS.md` D33 to D41.

## Sheet: Scoring

### Step 1.2: Demand and competitiveness

| # | Row | Status | Demand | Competitiveness |
|---|---|---|---|---|
| 16 | Shopify install through a theme app embed, no theme code edits, four-step checklist | Stated | Wanted by all | Most vendors can do this |
| 15 | Roles: owner, admin, analyst, support | Stated | Wanted by most | Commodity: should be free |
| 18 | Custom store HTTP catalog API, a path for headless builds | Stated | Wanted by some | A few others can do this |
| 19 | Sandbox store on the real API, no client store needed | Stated | Wanted by some | Unique to us: only we can do this |
| 20 | Setup skill that Cursor, Claude Code, Codex, and Antigravity can follow | Stated | Wanted by some | Unique to us: only we can do this |
| 7 | Per-language assistant copy, 10 interface languages, Arabic right to left | Stated | Wanted by one | Unique to us: only we can do this |
| 11 | Discovery analytics a client can see: zero result and weak click phrases | Stated | Wanted by some | A few others can do this |
| C10 | Affiliate incentives: a recurring revenue share | Candidate | Wanted by most | Commodity: should be free |
| C3 | Multi-store or agency workspace across client stores | Candidate | Wanted by most | A few others can do this |
| C11 | Free installs on development stores | Candidate | Wanted by most | Most vendors can do this |
| P1 | Paid usability engagement, the owner's plan | Planned | Wanted by some | Unique to us: only we can do this |
| P2 | Paid interviews | Planned | Wanted by some | A few others can do this |
| P3 | Case studies built with the client store, credited to the implementer | Planned | Wanted by most | A few others can do this |
| P4 | Referral traffic to implementers | Planned | Wanted by most | Most vendors can do this |
| P5 | Co-marketing | Candidate | Wanted by some | A few others can do this |
| P6 | Partner directory listing | Candidate | Wanted by most | Most vendors can do this |
| P7 | Certification and training | Candidate | Wanted by some | Commodity: should be free |
| P8 | Tier badges an agency can display | Candidate | Wanted by most | Most vendors can do this |
| P9 | White label or resale under the agency's brand | Candidate | Wanted by one | A few others can do this |
| P10 | Client discount the implementer can pass on | Candidate | Wanted by some | A few others can do this |
| P11 | Pay for managing a client store, not only for referring it | Candidate | Wanted by most | A few others can do this |
| P12 | Dedicated partner manager | Candidate | Wanted by some | A few others can do this |

### Step 1.3: Scatter plot scores, -20 to +20

Bands used, the same as Run 1: demand from "wanted by one" (-20 to -11) through "some" (-10 to -0.1), "most" (+0.1 to +15) and "all" (+15 to +20). Competitiveness from "commodity" (-20 to -11) through "most vendors" (-10 to -0.1), "a few others" (+0.1 to +10) and "unique" (+10 to +20).

| Row | Demand Score | Competitiveness Score |
|---|---|---|
| 16 Theme app embed install | 16.8 | -6.1 |
| 15 Roles | 5.2 | -13.4 |
| 18 Custom catalog API | -3.6 | 4.2 |
| 19 Sandbox store | -1.9 | 15.6 |
| 20 Coding agent setup skill | -0.8 | 14.3 |
| 7 Per-language copy, Arabic RTL | -14.2 | 12.6 |
| 11 Client-visible discovery analytics | -2.3 | 6.4 |
| C10 Recurring revenue share | 12.4 | -15.1 |
| C3 Multi-store workspace | 11.7 | 5.3 |
| C11 Dev store installs | 9.4 | -4.8 |
| P1 Paid usability engagement | -0.6 | 17.2 |
| P2 Paid interviews | -6.8 | 1.4 |
| P3 Case studies with client stores | 8.9 | 3.7 |
| P4 Referral traffic | 10.6 | -3.2 |
| P5 Co-marketing | -3.1 | 3.3 |
| P6 Directory listing | 9.8 | -6.6 |
| P7 Certification and training | -5.4 | -12.2 |
| P8 Tier badges | 11.3 | -7.7 |
| P9 White label | -15.3 | 7.4 |
| P10 Client discount | -4.6 | 5.8 |
| P11 Pay for managing | 10.2 | 6.9 |
| P12 Partner manager | -5.9 | 2.6 |

<!-- chart: scatter label=1 x=2 y=3 title="Run 2 Product Feature Matrix: demand (x) against competitiveness (y)" -->

## Sheet: Quadrants

### Step 1.4: Quadrant assignment

Quadrant 1 Hero Features: high demand, high competitive advantage. Quadrant 2 Differentiators: low demand, high advantage. Quadrant 3 Commodities: low demand, low advantage. Quadrant 4 Table Stakes: high demand, low advantage.

| Row | Quadrant | Rationale |
|---|---|---|
| C3 Multi-store workspace | Q1 Hero Features, candidate | Agencies manage many client stores, and each Pico plan connects one. Klaviyo client health dashboards, Intercom Fin multi-store workspaces, and Zipchat's agency-branded management show a few vendors offer it. **The adaptation file predicted table stakes. The evidence puts it in Hero as a candidate. Either way it is the precondition for the whole run** |
| P3 Case studies with client stores | Q1 Hero Features, planned | Marketing for the implementer and the first proof for Pico. Gorgias publishes partner stories and Klaviyo runs awards, but a case study built with the client store and credited to the implementer is rarer. Gated by permission from the merchant and the implementer |
| P11 Pay for managing | Q1 Hero Features, candidate | Agencies charge for implementation work. Rebuy pays a 5% managed share regardless of who referred the brand, and Recharge pays billable hours. It keeps an implementer active after the install |
| 18 Custom catalog API | Q2 Differentiators | Headless builds need a non-Liquid path. StoreLeads detects Hydrogen on 901 US stores. Pico's headless support is not in the source: not claimed, with a widget script path for developers, untested (D17) |
| 19 Sandbox store | Q2 Differentiators | None found among vendors. Saves the implementer hours before any client store is touched. Demand sits just below the line |
| 20 Coding agent setup skill | Q2 Differentiators | None found among apps, and Shopify's own AI Toolkit ships the same pattern. Moves toward Hero as coding-agent use grows: 14.1% of developers use AI agents at work daily (Stack Overflow 2025) |
| 7 Per-language copy, Arabic RTL | Q2 Differentiators | Low demand among US-serving implementers. Gulf agencies sell Arabic right to left builds as a service, so it matters in the GCC, the later market |
| 11 Client-visible discovery analytics | Q2 Differentiators | CRO agencies sell evidence for test ideas, and an implementer needs something to show the client. Tidio, Fin, and Dialog offer related views |
| P1 Paid usability engagement | Q2 Differentiators, planned | No vendor found pays implementers for product feedback. It pays before any referral exists. For freelancers who already sell app installs at about $100, it reads as paid work and moves toward Hero |
| P2 Paid interviews | Q2 Differentiators, planned, weak | Common in vendor research, rarely a program element. Low demand on its own. Valuable to Pico as input to Dashboards 3 and 6 |
| P5 Co-marketing | Q2 Differentiators | Offered at higher tiers by Gorgias, Okendo, and Octane |
| P9 White label | Q2 Differentiators | Only Zipchat offers resale under the agency's brand. No evidence of wider demand |
| P10 Client discount | Q2 Differentiators | Rep AI Elite and LoyaltyLion offer it. Some agencies pass savings to clients |
| P12 Partner manager | Q2 Differentiators | Higher tiers at Gorgias and Octane. Costly to staff |
| P7 Certification and training | Q3 Commodities | Every mature program has it, and it is free in each |
| 16 Theme app embed install | Q4 Table Stakes | Every modern app uses theme app extensions. Shopify removes app blocks on uninstall. Implementers gatekeep app sprawl and theme residue |
| 15 Roles | Q4 Table Stakes | Agencies work inside client accounts. Standard in helpdesks and in Shopify itself |
| C10 Recurring revenue share | Q4 Table Stakes, missing | Nearly every program pays one, mostly around 20% for 12 to 36 months. A program without one is not a program to an agency |
| C11 Dev store installs | Q4 Table Stakes, missing | Any app can mark plans free for testing on other partners' development stores through Shopify App Pricing. Cheap to provide |
| P4 Referral traffic | Q4 Table Stakes, planned | Gorgias, Rebuy, Klaviyo, and Tidio run agency directories and lead sharing. Pico cannot promise traffic as a number until it has merchants to refer |
| P6 Directory listing | Q4 Table Stakes, missing | As above |
| P8 Tier badges | Q4 Table Stakes, missing | 11 of 26 sampled agency pages display vendor tiers. A program with no tier gives the agency nothing to show |

### Step 1.5: Entry validation

| Rule | Check across all 22 rows | Result |
|---|---|---|
| If "Wanted by some", exclude "Most vendors can do this" | P7 and P12 were first read as "most vendors". P7 moved to "Commodity", because training is free in every program found. P12 moved to "A few others", because a dedicated partner manager appears only at higher tiers (Gorgias Premier and Elite, Octane) | No violations remain |
| If "Wanted by all", exclude "Unique to us" | Row 16 is "wanted by all" and "most vendors" | No violations |
| If "Wanted by one", exclude "Commodity: should be free" | Rows 7 and P9 are "wanted by one", and neither is "commodity" | No violations |

**What the matrix says.** The partner floor (C10, C11, P4, P6, P8) is table stakes Pico does not have, as `SKILL-ADAPTATION.md` predicted. The Hero quadrant holds three things to build, none of which exists: a multi-store workspace (C3), case studies credited to the implementer (P3), and pay for managing (P11). Pico's real differentiators for implementers are the ones that save hours before a client sees anything: the sandbox (19), the setup skill (20), and the paid usability engagement (P1), which pays before any referral.

## Sheet: Program_Elements

### Side table: delivery effort and funnel role, program elements only

Effort is what it costs Pico to run, judged from what each element needs. Costs in money come from the 90-day budget in `DECISIONS.md` D31.

| Element | Quadrant | Delivery Effort | Why | Funnel Role | Build order, decided (D35 to D41, D56) |
|---|---|---|---|---|---|
| C11 Dev store installs | Q4 | Low | A setting in Shopify App Pricing: plans marked free for testing on other partners' development stores | Activate: test before transfer to the client | 1, before outreach starts |
| P1 Paid usability engagement | Q2 | Medium | $150 a session, about $162 to $177 with platform fees (D31, D33), recruiting, scheduling, a findings template | Acquire and activate: first contact, first install | 1, the opening move |
| P2 Paid interviews | Q2 | Low | Team time and $75 per interview (D34). Can run inside P1 | Insight for Dashboards 3 and 6 | 1, inside P1 |
| P3 Case studies with client stores | Q1 | Medium to High | Writing, data from the client store, and recorded permission from the merchant and the implementer | Advocacy, and Pico's first proof | 2, after the first engagements |
| C10 Recurring revenue share | Q4 | Medium | Tracking, payouts, a partner portal, and the platform rules on Upwork and Fiverr | Convert to partner, retain | 2, terms in D35 and D36: 25% for 24 months, monthly payouts |
| P6 Directory listing | Q4 | Low to Medium | A page on Pico's site listing partners who agree | Routes merchants to implementers | 2 |
| P8 Tier badges | Q4 | Low | The tier criteria are set: partner, and lead partner at 5 active stores (D40) | Advocacy | 3 |
| P11 Pay for managing | Q1 | Medium | A 10% managed share (D35), with the managing implementer recorded by deal registration (D38) | Retain: keeps the implementer active after install | 3 |
| C3 Multi-store workspace | Q1 | High | Product work: one view across client stores, while each store keeps its own plan under Shopify Billing (D41) | Retain and expand: the next client store | 3, built once 10 partners each have 3 or more active stores (D23) |
| P4 Referral traffic | Q4 | High until Pico has merchants to refer | Traffic depends on Run 1 working first. Routed setup requests from week 6, counted monthly for partners (D39) | Retain partners | 4, never promised as a number |
| P5 Co-marketing | Q2 | Medium | Content time per partner | Advocacy | 4 |
| P10 Client discount | Q2 | Low to Medium | Shopify Billing supports subscription discounts, so it is possible. Not offered at launch: the share carries the incentive (D35) | Convert the client | 4 |
| P7 Certification and training | Q3 | Medium | Course content and upkeep | Activate partners | 5, with the partner portal at 25 partners (D36) |
| P12 Partner manager | Q2 | High | Headcount | Retain top partners | 5, when partner-referred stores pass 25% of paying stores, the D35 review point |
| P9 White label | Q2 | High | Product and billing work, low demand | None now | Not planned |

## Sheet: Demand_Drivers

### Step 1.6: The demand driver

**The Paid Usability Session.** It meets both rules in a form specific to implementers: it gives immediate value (paid work from the first contact) and it reveals a problem their current stack does not show them for conversational requests.

| Attribute | Description |
|---|---|
| What it is | A fixed-scope, paid session. The implementer installs Pico on a store they work on, a development store or a client store with the merchant's permission, using the setup skill or the four-step checklist. They run the Shopper Words Test with phrases from the client's customers, then report what worked, what broke, and how long setup took. $150 for up to 90 minutes, paid on the platform where they were found (D33) |
| Immediate value | Paid work from the first contact, before any referral exists, plus a findings list for the client store that the implementer can show the client |
| How it helps in problem identification | It shows the implementer, and their client, which shopper phrases returned no products or few clicks, which points to gaps in the catalog or in how products are described |
| How it exposes the need to use Pico | The gaps reappear every day shoppers ask in their own words, and the implementer has now seen setup take minutes on a real store. The next client store becomes a repeat deployment |
| ICP fit | Level 1 first: freelancers and small studios, who already sell app installs for about $100. Level 2 agencies with build or CRO services next |
| Conversion role | Moves an implementer from first contact to first install, then to the interview, a case study with permission, and the partnership offer |
| Top-of-funnel use case | The Upwork and Fiverr job posts, and the first message in cold email and LinkedIn outreach |

### Step 1.7: Demand driver variants

| Variant Name | Perceived Value | Ease of Delivery | Delivery Type | Description | TOFU Use Case |
|---|---|---|---|---|---|
| Paid Usability Session | High | Medium | Service-based white glove, paid | The Step 1.6 driver | Upwork and Fiverr job posts, cold email, LinkedIn |
| Client Store Findability Audit | High | Medium | Value using the software itself, delivered by the implementer | The implementer runs the Shopper Words Test on a client store and hands the client a gap list, using Pico's template | A service the implementer can sell, offered in cold email |
| Sandbox Developer Test | Medium | Easy | Value using the software itself | Install the setup skill in a coding agent and point it at the sandbox store, with no client store needed | LinkedIn posts, developer forums, the Shopify Developer Community |
| Setup Walkthrough | Medium | Easy | Light tool | A recorded install on a development store, from the checklist or a coding agent, with the uninstall shown too | Cold email follow-up, the partner page |
| Agency AI Shopping Readiness Scorecard | Medium | Easy | Self-assessment scorecard (ScoreApp) | Seven questions on the implementer's stack, client base, and AI work, scored for readiness. Specified in the lead magnet | Cold email, LinkedIn, the partner page |
| Co-authored case study | High | Hard | Service-based white glove | A write-up of what changed on a client store, credited to the implementer, with permission from both | After the first engagements, as the reason to stay |
