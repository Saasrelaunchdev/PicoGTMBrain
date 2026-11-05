# Run 2, Step 2.7: Implementer feedback analysis

**Date checked:** 2026-11-03. **Prompt:** `../RESEARCH-PROMPTS.md` Step 2.7, Run 2. **Feeds:** Step 2.8 positioning vectors in `../run-2-implementers/02-competitive-market-analysis/`.

## Method, and its limits

- **Sources searched:** the Shopify Community and the Shopify Developer Community forums, agency blog posts, vendor partner pages and job posts, App Store reviews that mention agencies or affiliates, and Reddit snapshots. Partner Slack is private. All through the web search index on 2026-11-03.
- **The evidence is thin, and that is a finding.** Agencies seldom post public reviews of the apps and partner programs they use. Most of what exists is vendor-written. No source yielded a countable set of implementer reviews for any single competitor, so frequencies are "seen" counts across the whole set, not per competitor.
- **Implementer behavior is used as evidence where reviews are missing:** what agencies display on their own pages (0.F), what freelancers sell (0.D), and what programs require (0.G).
- **Classification, per the prompt:** each complaint is marked as about the product, the client experience, or the partner program.

---

## 1. What implementers value, from behavior and the few reviews found

| Theme | Evidence | Frequency | Competitors it favors |
|---|---|---|---|
| A vendor tier the agency can display | 11 of 26 sampled agency pages show vendor tiers: Recharge Elite, Klaviyo Elite and Master, Gorgias Elite, Okendo Platinum, Rebuy Silver, LoyaltyLion Gold, Loop Platinum, Attentive Pioneer | 11 pages | Gorgias, Klaviyo, Rebuy |
| Integration with the client's core stack | Agencies pair apps by integration, such as Klaviyo with Gorgias and Recharge with Klaviyo | Recurring across the 26 pages | Klaviyo, Gorgias |
| Leads from vendor directories | Gorgias, Rebuy, Klaviyo, and Tidio each run an agency directory. Gorgias describes "lead sharing" | 4 directories | Gorgias, Rebuy, Klaviyo |
| Recurring revenue share | Every program found pays one, mostly around 20% for 12 to 36 months | 15 or more programs | All |
| Paid implementation work | Rebuy pays a 5% managed share for active work, Recharge pays billable hours, freelancers sell app installs for about $100 | 3 | Rebuy, Recharge |
| Being "good citizens" on speed | Agency blogs describe vetting apps and testing on staging before live stores (`VENDOR`) | Seen 2 | Lightweight apps |

## 2. What implementers dislike or wish for

| Complaint | Evidence | Seen | About |
|---|---|---|---|
| Commission confusion and payout problems | A partner did not get the full commission on a client's theme purchase. A Plus upgrade dropped a partner's commission to 0%, and the partner support route did not work. An app reviewer reported affiliate commissions siphoned by coupon sites and no notifications of commissions. A commission-tracking vendor lists manual, delayed payouts and attribution errors as common (`VENDOR`) | 4 | Partner program |
| Program requirements that grow | Gorgias freezes the share without one closed deal a year and sets ARR floors per tier. Klaviyo sets referred MRR, managed MRR, and curriculum requirements per tier | 2 programs | Partner program |
| Support burden the agency absorbs | Merchant reviews in Run 1 Step 2.7: billing surprises (Gorgias, Tidio), wrong answers (Gorgias, Inbox, Tidio), widgets left after removal (Zipchat). Each lands on the agency that recommended the app | Recurring, merchant side | Client experience |
| App sprawl and speed | Stores average 15 to 20 apps per one source. One vendor study links 16+ apps to a PageSpeed score 15 points lower (`VENDOR`) | Seen 3 sources | Product |
| Theme residue after uninstall | Developers ask how to remove theme files on uninstall. Shopify says theme app extension blocks are removed automatically. Direct theme edits are not | Seen 2 forum threads | Product |
| Vendors that "build everything then disappear" | One Reddit snapshot from a small agency about Shopify itself | Seen 1 | Partner program |

## 3. Per competitor, what the evidence supports

| Competitor | Positive themes | Negative themes | Mostly about |
|---|---|---|---|
| Gorgias and its agency program | Displayed tiers, dedicated partner manager, event budget, co-marketing, directory leads | Share freezes without a deal a year. Clients' billing surprises fall on the agency | Partner program, client experience |
| Klaviyo and K:Partners | Present in most stacks, client health dashboards, training, awards | Tier requirements in MRR and curriculum | Partner program |
| Rebuy and its program | Managed share for active work, directory, certification | Program model changed on 2026-01-01, with a transition through 2026 | Partner program |
| Tidio | Up to 25% for up to 3 years, an agency directory | Merchant billing and limit complaints (Run 1) | Client experience |
| Custom builds on Shopify's agent tools | Billable hours, full control | Maintenance, migrations, and the removed Storefront MCP tools stay with the builder | Product |

## 4. Patterns to carry into Step 2.8

1. **Vectors 1 and 2, what competitors lead in:** established partner economics (tiers, shares, directories), and presence in the stack agencies already sell (Klaviyo, Gorgias).
2. **Vectors 3 and 4, reversed complaints Pico can lead in:**
   - "Paid from the first engagement", reversed from shares that freeze, payouts that are late or wrong, and requirements that must be met before any income. The owner's paid usability engagement pays before any referral exists.
   - "Proof the implementer co-owns", reversed from client support burden and the absence of anything to show clients. Case studies built with the client store, credited to the implementer, plus discovery analytics the client can see.
3. **The product claim that carries over from Run 1, narrowed:** Pico installs through a theme app embed with no theme code to edit, and Shopify removes app blocks when an app is uninstalled. Speed impact is measured against Built for Shopify's 10-point Lighthouse budget and the number is published, never claimed as none (`../DECISIONS.md` D18).
