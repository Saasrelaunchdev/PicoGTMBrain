# Run 2, Step 1.1: Feature demand research, Shopify implementers

**Date checked:** 2026-11-03. **Prompt:** `../RESEARCH-PROMPTS.md` Step 1.1, Run 2. **Run 2 is a standalone go-to-market** (owner decision, 2026-11-03). **Feeds:** `../run-2-implementers/01-product-feature-matrix/`.

**Method and limits.** Web search only, because this session's network policy blocks page loads. Evidence comes from Step 0.F and 0.G, from `2026-11-03-run-2-step-2-1-competitor-research.md`, `2026-11-03-run-2-step-2-7-review-analysis.md`, and `2026-11-03-run-2-channel-rules.md`, and from searches for this step. Implementer feedback in public is thin: agencies rarely review the apps and programs they use. Where demand is inferred from behavior (what agencies display, what freelancers sell), it says so.

---

## 1. Implementer-facing product rows

| # | Row | Who else offers it to implementers, with evidence | Central to their offer? | Evidence implementers want it | Reading for Phase 1 |
|---|---|---|---|---|---|
| 20 | Setup skill that Cursor, Claude Code, Codex, and Antigravity can follow | **None found among apps.** Shopify ships its own `shopify` and `ucp` skills and a Dev MCP server in the AI Toolkit ([shopify.dev](https://shopify.dev/docs/apps/build/ai-toolkit)) | Shopify's own direction | Shopify building it says developers work this way. No count of coding-agent users found | Wanted by some. Unique to us among apps |
| 19 | Sandbox store on the real API | **None found.** Vendors offer free plans, trials, and demos | Not offered | Agencies test apps on staging before client stores (agency blog, `VENDOR`). Researchers pay developers $100 to $150 an hour for their time (channel rules file), so a test that needs no client store saves real hours | Wanted by some. Unique to us |
| 16 | Shopify install through a theme app embed, no theme code edits, four-step checklist | Every modern app uses theme app extensions. Shopify says app blocks are "automatically and entirely removed" from themes on uninstall ([shopify.dev](https://shopify.dev/docs/apps/build/online-store/theme-app-extensions/ux)). Script tags stop running on 2027-03-01 | Expected | Agencies gatekeep app sprawl and speed: stores average 15 to 20 apps per one source, and one vendor study links 16+ apps to slower PageSpeed (`VENDOR`). A merchant complained of a widget left after removal (Zipchat) | Wanted by all. Most vendors can do this |
| 18 | Custom store HTTP catalog API | Alhena, Dialog, Rep AI, Tidio, and Klaviyo's open APIs reach other platforms | Common at the high end | Headless and Hydrogen builds need a non-Liquid path. StoreLeads detects Hydrogen on 901 US stores | Wanted by some. A few others can do this |
| 15 | Roles: owner, admin, analyst, support | Helpdesks and Shopify itself (collaborator accounts) | Common | Agencies work inside client accounts | Wanted by most. Commodity |
| 7 | Per-language assistant copy, 10 interface languages, Arabic right to left | Multilingual replies are common. Right to left cards with a switcher and per-language copy were not documented by others | Rare as a combination | Gulf agencies sell Arabic right to left builds as a service (0.E), the later market | Wanted by one in the US market. Unique to us |
| 11 | Discovery analytics a client can see | Tidio's unanswered questions, Fin's knowledge gaps, Dialog's insight into questions | Secondary | CRO agencies sell evidence for test ideas (0.F). An implementer needs something to show the client | Wanted by some. A few others can do this |

## 2. Program elements, candidates, and the owner's planned path

| # | Element | Who else offers it, with evidence | Central? | Evidence implementers want it | Reading for Phase 1 |
|---|---|---|---|---|---|
| C10 | Affiliate incentives, a recurring revenue share | Nearly every program: Gorgias 20% for 2 to 3 years, Rep AI 10% to 25%, Tidio up to 25%, Octane AI 20%, Okendo 20%, Rebuy 5% to 15% plus 5% managed, Shopify 20% of subscription plus 0.1% of GMV for launch partners (0.G) | Core | 11 of 26 sampled agency pages display vendor tiers (0.F) | Wanted by most. Commodity |
| C3 | Multi-store or agency workspace | Klaviyo client health dashboards, Intercom Fin multi-store workspaces, Zipchat agency-branded store management, and Shopify's Partner Dashboard store access | Secondary | Agencies manage many client stores. Each Pico plan connects one store | Wanted by most. A few others can do this |
| C11 | Free installs on development stores | Any app can mark plans "free for testing" on other partners' dev stores through Shopify App Pricing | Expected | Agencies build on dev stores before transfer | Wanted by most. Most vendors can do this |
| P1 | **Paid usability engagement** (owner's plan) | **None found.** Vendors pay for referrals, not for product feedback. Research platforms pay participants (channel rules file) | Not offered by apps | Developers expect $100 to $150 for a 60-minute session on research platforms (`VENDOR` benchmarks) | Wanted by some. Unique to us |
| P2 | Interviews | Common in vendor research, rarely offered as a program element | | Research incentive norms apply | Wanted by some. A few others can do this |
| P3 | **Case studies built with the client store** (owner's plan) | Gorgias publishes partner stories ([Gorgias](https://www.gorgias.com/partner-stories)). Klaviyo runs partner awards | Secondary | Agencies use case studies as their own marketing. Vendor directories list partners | Wanted by most. A few others can do this |
| P4 | **Referral traffic** to implementers (owner's "traffic") | Lead sharing in Gorgias's program, vendor agency directories (Gorgias, Rebuy, Klaviyo, Tidio), the Shopify Partner Directory | Core in mature programs | Directories exist because agencies want leads | Wanted by most. Most vendors can do this |
| P5 | Co-marketing | Gorgias (Premier, Elite), Okendo tiers, Octane | Higher tiers | Agencies list vendor badges | Wanted by some. A few others can do this |
| P6 | Partner directory listing | Gorgias, Rebuy, Klaviyo, Tidio directories | Common | As above | Wanted by most. Most vendors can do this |
| P7 | Certification and training | Gorgias, Klaviyo (curriculum per tier), Rebuy Academy, Octane | Common | Tiers require it | Wanted by some. Most vendors can do this |
| P8 | Tier badges an agency can display | Every mature program | Common | 11 of 26 pages show tiers | Wanted by most. Most vendors can do this |
| P9 | White label or resale under the agency's brand | **Zipchat only**, among those found | Rare | No evidence of demand beyond Zipchat's offer | Wanted by one. A few others can do this |
| P10 | Client discount the agency can pass on | Rep AI Elite (15%), LoyaltyLion (10% with 10% to the partner) | Rare | | Wanted by some. A few others can do this |
| P11 | Pay for managing, not only referring | Rebuy's 5% managed share, Recharge's billable hours | Rare | Agencies charge for implementation work | Wanted by most. A few others can do this |
| P12 | Dedicated partner manager | Gorgias, Octane | Higher tiers | | Wanted by some. Most vendors can do this |

## 3. What Step 1.1 means for Phase 1, Run 2

1. **The recurring share is the floor.** C10, directory listing, tier badges, and dev store access are table stakes, as `../SKILL-ADAPTATION.md` predicted.
2. **The owner's paid usability engagement has no equivalent among the vendors found.** It scores as a differentiator. It pays the implementer before any referral exists, which no affiliate program does.
3. **Multi-store management (C3) is wanted by most and offered by a few.** It is the precondition the adaptation file named, and it is the strongest candidate for the Hero quadrant once built.
4. **Case studies with client stores (P3) carry the most value for both sides:** marketing for the implementer, first proof for Pico. They are gated by permission (`../GTM-BRIEF.md` Section 5).
5. **The setup skill and the sandbox are Pico's real developer differentiators,** because they cut the hours an implementer spends before a client sees anything.
