# TBD resolution: the research pass

**Date checked:** 2026-11-03. **Why this file exists:** the owner asked on 2026-11-03 for every unknown placeholder and open decision in the build to be resolved. Facts that research can answer are answered here, with a source and the date checked. Everything else became a decision with an owner, or an operating assumption with a measurement point, in `../DECISIONS.md`. **Feeds:** `../DECISIONS.md`, `../GTM-BRIEF.md`, both run folders, and the walkthrough.

**Method and limits.** Web search only, because this session's network policy blocks page loads, the same method as every other file in `research/`. Marks: `VENDOR` (a company with a stake in the answer), `2ND` (a secondary source citing a primary one), `DERIVED` (arithmetic done here). **This is research, not legal advice.**

---

## 1. Pico's own presence

| Question | Finding | Source |
|---|---|---|
| Website | **picofinds.com.** The footer of the live site, in the screenshots the owner supplied on 2026-11-03, gives the contact address us@picofinds.com, and the project is named PicoFinds. The search index holds no page for the domain yet, so the site is new or not yet indexed | Owner's screenshots, 2026-11-03. Searches for "picofinds" and "picofinds.com", 2026-11-03, no result |
| What the site says | Headline: "An AI shopping assistant for Shopware and Shopify that answers in English and Arabic, and only recommends what is in stock." Sub line: "Pico searches your real catalog, checks live stock, and gives shoppers a product card with a single add-to-cart tap." Buttons: "Connect your store", "Book a tailored demo". Region selector set to Egypt. Footer regions: Egypt, Saudi Arabia, United Arab Emirates, United States, Germany, Greece, United Kingdom. Footer pages: For Shopware merchants, Pricing, Privacy, Terms, Refunds | Owner's screenshots, 2026-11-03 |
| Shopify App Store listing | **Not found.** No listing named Pico in the App Store search index. The nearest name is "Piko ‑ Pickup Reminder", an unrelated app (Step 0.A). Treated as not live on 2026-11-03 | Search, 2026-11-03 |
| Installs, reviews, rating | None found, because no listing was found | Same |

## 2. Shopify platform rules that close open decisions

| Rule | Finding | Source |
|---|---|---|
| **Billing for App Store apps** | Apps that use off-platform billing cannot be distributed through the Shopify App Store, unless Shopify has said otherwise. Charges go through Shopify's billing tools or Shopify Managed Pricing, and merchants must be able to change plans without contacting support or reinstalling | [Shopify App Store requirements](https://shopify.dev/docs/apps/launch/shopify-app-store/app-store-requirements) |
| Billing intervals | Recurring plans support `EVERY_30_DAYS` and `ANNUAL`. Usage plans carry a capped amount | [Shopify billing API reference](https://shopify.dev/docs/api/shopify-app-react-router/v1/apis/billing.md) |
| Subscription discounts | A discount is a percentage or a fixed amount with `durationLimitInIntervals`, the number of billing intervals it covers | [AppSubscriptionDiscount](https://shopify.dev/docs/api/admin-graphql/latest/objects/AppSubscriptionDiscount) |
| **Storefront speed** | Built for Shopify requirement 2.2.1: an app must not lower the storefront Lighthouse performance score by more than 10 points, measured before and after install | [Built for Shopify requirements](https://shopify.dev/docs/apps/launch/built-for-shopify/requirements) |
| App review time | Shopify staff in the community forum: usually 5 to 10 business days, longer in busy periods. 2026 forum threads report waits of 20 to 30 days or more. The confirmation email says up to 2 weeks | [Shopify Community](https://community.shopify.com/t/how-long-does-it-take-for-an-app-review-to-be-completed/264027), [Shopify developer forum](https://community.shopify.dev/t/longer-app-store-review-times-what-you-need-to-know/31728) |
| Partner payouts to app developers | A $25 minimum per payout. A 30-day hold on a new partner's first payout since 2024-07-29. Payouts twice a month per third-party documentation | [Shopify Help: getting paid](https://help.shopify.com/en/partners/getting-started/getting-paid), [Shopify changelog](https://shopify.dev/changelog/partner-payout-schedule-update), [Mantle docs](https://docs.heymantle.com/shopify-payouts) `2ND` |

## 3. Freelance platform fees and terms

| Item | Finding | Source |
|---|---|---|
| Upwork client marketplace fee | Reported in 2026 as up to 7.99% on the Basic plan, 3% for qualifying US clients paying by bank, plus a contract initiation fee of $0.99 to $14.99. The 2026 sources disagree, and Upwork's own pricing page read in the channel rules file was stale | [Monitask](https://www.monitask.com/blog/upwork-fees/), [GigRadar](https://gigradar.io/blog/upwork-fees) `2ND` |
| Upwork freelancer fee | 0% to 15%, set per contract and shown before a proposal is sent | Same `2ND` |
| Upwork conversion fee | A mirror of Upwork's help article gives 13.5% of estimated earnings over the next 12 months, falling to a nominal $1 after two years of working together | [Upwork help, mirror](https://z3n-cab-workshop-2.zendesk.com/hc/en-us/articles/9642905068570-The-Upwork-Conversion-Fee) `2ND` |
| Fiverr buyer service fee | 5.5% of the order, plus $3.50 on orders under $200, per Fiverr's help center as read in the channel rules file. Other 2026 sources conflict on the small-order fee | `2026-11-03-run-2-channel-rules.md`, [ConductAtlas](https://conductatlas.com/platform/fiverr/fiverr-terms-of-service/buyer-service-fee-structure/) `2ND` |

## 4. Email law outside the US, and the US postal address

| Jurisdiction | Finding | Source |
|---|---|---|
| United States, address | A valid physical postal address: the sender's street address, a USPS-registered post office box, or a private mailbox registered with a commercial mail receiving agency | [FTC CAN-SPAM guide, archived](https://webarchive.library.unt.edu/web/20130214054537/http://business.ftc.gov/documents/bus61-can-spam-act-compliance-guide-business), [Federal Register, 2008 rule](https://www.govinfo.gov/content/pkg/FR-2008-05-21/html/E8-11394.htm) |
| United Kingdom | Under PECR, B2B marketing email to **corporate subscribers** (companies, LLPs, Scottish partnerships, some public bodies) needs no prior consent, but must identify the sender and offer an opt-out. **Sole traders and other partnerships are individual subscribers** and are treated like consumers. UK GDPR still applies to the named person | [ICO: business-to-business marketing](https://ico.org.uk/for-organisations/direct-marketing-and-privacy-and-electronic-communications/business-to-business-marketing/) |
| Germany | UWG section 7 generally requires prior consent, including for business recipients | [Overloop](https://overloop.com/blog/b2b-cold-email-germany-gdpr-compliance) `VENDOR`, [Fieldfisher EU e-marketing table](https://res.cloudinary.com/fieldfisher/image/upload/v1706627634/PDFs/EU_e-marketing_requirements_-_January_2024_lqpl6s.pdf) |
| France | Prospecting between professionals is allowed on an objection basis, when the message concerns the recipient's role and carries an opt-out | Same sources. They conflict for some countries |

## 5. Pricing and funnel benchmarks

| Benchmark | Figure | Source | Mark |
|---|---|---|---|
| Annual plan discount | Average 16% across about 6,000 SaaS companies (ProfitWell). 17% across about 6,000 transactions (Vendr 2024). 16.7%, two months free, is the most common offer in a 1,000+ company study | [Monetizely](https://www.getmonetizely.com/articles/whats-the-optimal-discount-for-annual-developer-subscriptions-2024-data-driven-guide), [VentureBeat](https://venturebeat.com/business/essential-saas-benchmarks-for-a-competitive-advantage-vb-live/) | `2ND` |
| Shopify app trial to paid | The median Shopify app converts 15% to 20% of trial installs to paying merchants. Top quartile 42.5% | [Taylor Sicard](https://taylorsicard.com/blog/shopify-app-onboarding-benchmarks) | Practitioner post |
| Shopify app install to subscribe or trial | 29.89% on average across 400+ apps, 49.96% top quartile | [convert2x](https://convert2x.com/learn/shopify-app-conversion-optimization) | `VENDOR` |
| Shopify app uninstall rate | No published benchmark found | | Gap, set as a target in `../DECISIONS.md` |
| App Store listing visit to install | No published benchmark found | | Gap, set as a target |
| Cold email reply rate | 3.43% on average, top 10% of B2B SaaS campaigns about 10.7% (Instantly 2026 report, as cited). A 2026 median of 2.1% in a 28,400-lead study. 3% to 6% called good for broad B2B | [Lemlist](https://lemlist.com/blog/cold-email-response-rate), [Visionary Marketing](https://visionary-marketing.co.uk/blog/b2b-cold-email-statistics-2026), [Apollo](https://www.apollo.io/insights/what-is-a-good-benchmark-for-reply-rates-in-cold-outreach) | `2ND`, `VENDOR` |
| Chat widget engagement | Floating widgets reach about 1% to 5% of visitors, proactive or multi-placement setups 5% to 10%. Definitions differ by vendor | [Alhena](https://alhena.ai/blog/ai-assisted-commerce-revenue-metric/), [Alby](https://alby.com/?p=877) | `VENDOR` |
| Shopify store conversion rate | 1.4% on average across 2,800 Shopify sites, 2023. Above 3.2% is the top 20% | [Littledata](https://littledata-lp.netlify.app/ecommerce-conversion-rate) | Benchmark study |
| Average order value | Americas $183 (Dynamic Yield, October 2025, an enterprise panel, not Shopify only). Median $312 for 2,934 Shopify stores with at least 250 orders in H1 2026 (Shogun, skewed to larger stores). No Shopify-wide figure found | [Ringly summary](https://www.ringly.io/blog/ecommerce-aov-statistics-2026) | `2ND` |

## 6. Store counts that were gaps

| Question | Finding | Source |
|---|---|---|
| **Catalog size, platform wide** | StoreLeads, State of Shopify 2026, stores by number of products: 1 to 9: 884,998. 10 to 24: 545,153. 25 to 49: 394,806. 50 to 99: 352,339. 100 to 249: 352,720. 250 to 999: 308,168. 1,000 to 4,999: 140,735. 5,000 to 9,999: 24,570. 10,000 to 24,999: 15,281. 25,000 to 99,999: 11,892 | [StoreLeads State of Shopify 2026](https://storeleads.app/reports/shopify) |
| `DERIVED` | The bands sum to 3,030,662 stores. **853,366 sell 100 or more products, 28.2%.** 500,646 sell 250 or more, 16.5%. 30.0% sell 1 to 9. One tracker, one page | Same |
| Annual sales by store | StoreLeads attaches a modelled sales estimate to each store but publishes no band table. Third-party band tables found do not name a method | [StoreLeads blog](https://storeleads.app/blog/2019/12/28/revenue-estimates), [Ringly](https://www.ringly.io/blog/storeleads-gorgias-shopify-installs) |
| Monthly sessions by store | No platform-wide distribution found | Gap, bands set in `../DECISIONS.md` |
| Stores with more than one storefront language | No tracker publishes storefront language. StoreCensus pages for Translate & Adapt conflict (962 and 0) | [StoreCensus](https://www.storecensus.com/stats/app/translate-and-adapt) |
| Bahrain | No national total in the index. City pages: Manama 282 (March 2026), Riffa 65 (February 2026), Janabiyah 11, Hamala 9. `DERIVED` lower bound: at least 367 | [StoreLeads Manama](https://storeleads.app/reports/shopify/BH/city/Manama), [Riffa](https://storeleads.app/reports/shopify/BH/city/Riffa) |
| Oman | No national total in the index. Muscat Governorate 413, Al Batinah North 30, Dhofar 28, 11 on Plus. `DERIVED` lower bound: at least 471 | [StoreLeads Oman](https://storeleads.app/reports/shopify/OM/top-stores), [Muscat Governorate](https://storeleads.app/reports/shopify/OM/region/Muscat%20Governorate) |
| Arabic-language storefronts | Not published by any tracker found. RTL King, one Arabic app, shows 2 installs | [StoreLeads RTL King](https://storeleads.app/reports/shopify/app/rtl-king-arabic) |

## 7. Implementer counts and rates

| Question | Finding | Source |
|---|---|---|
| Shopify gigs on Fiverr | **40,000+ results** on Fiverr's Shopify category page. Gigs, not people: one seller can list several | [Fiverr Shopify category](https://block.fiverr.com/gigs/shopify) |
| Shopify freelancers on Upwork | **No public headcount.** Upwork's US "Hire the best Shopify developers" page shows a 4.8 rating from 4,810 client reviews, Canada 718 | [Upwork US](https://www.upwork.com/hire/shopify-developers/us/), [Upwork Canada](https://www.upwork.com/hire/shopify-developers/ca/) |
| Partner Directory size | About 3,754 partners worldwide, July 2025, unnamed method | [Hashnode](https://hashnode.com/posts/top-100-shopify-agencies-worldwide-curated-directory-of-the-best-global-partners/6868a833eb6a1a9a7a2bb511) `2ND` |
| App ecosystem earnings | Shopify: the app ecosystem earned $1.3 billion in 2025 | [Shopify News](https://www.shopify.com/news/a-world-with-more-builders) |
| Freelance Shopify developer rates | Global median about $33 an hour across 730+ contracts. Mid-level about $78, senior about $133. US mid-level $62 to $100 | [Lemon.io](https://lemon.io/rate-calculator/shopify-developers/), [goLance](https://golance.com/hiring/best-freelance-shopify-developers-hourly-rate), [Second Talent](https://www.secondtalent.com/cost-to-hire/shopify-developer/) `VENDOR` |
| Developers using AI agents | Stack Overflow 2025: 47.1% of respondents use AI tools daily, 14.1% use AI agents at work daily | [Stack Overflow Developer Survey 2025](https://survey.stackoverflow.co/2025/) |
| Client stores per implementer | No source found | Gap, planning band set in `../DECISIONS.md` |

## 8. Prices of the tools the plan uses

| Tool | Price found | Source | Mark |
|---|---|---|---|
| ScoreApp | Starter $39, Business $99, Pro $149 a month, Enterprise from $799 | [Toolradar](https://toolradar.com/tools/scoreapp/pricing) | `2ND` |
| LinkedIn Sales Navigator Core | $119.99 a month billed monthly, about $89.99 a month billed yearly | [Valley](https://www.joinvalley.co/blog/linkedin-sales-navigator-cost-explained-2026) | `2ND` |
| A small, fast model for the assistant's replies, for cost planning | Claude Haiku 4.5: $1 per million input tokens, $5 per million output tokens | [Price Per Token](https://pricepertoken.com/pricing-page/model/anthropic-claude-haiku-4.5) | `2ND`. Pico's actual model is not stated in the source |
| Cost per hire, US, nonexecutive | SHRM 2025: average $5,475, median $1,200 | [Pin](https://www.pin.com/blog/cost-per-hire-benchmarks/) | `2ND` |

---

## What stayed unfound, and where it went

| Gap | Resolution | Where |
|---|---|---|
| Shopify app uninstall and listing conversion benchmarks | Targets set by the CMO, reviewed at day 30 | `../DECISIONS.md` D44 |
| Annual sales and monthly sessions bands | Planning bands derived from session ranges, Littledata's 1.4% conversion, and an order value range of $90 to $180 | D53 |
| Share of sessions that start a conversation | Operating assumption 2%, inside the vendor-reported 1% to 5%, measured in the founding cohort | D54 |
| Tokens per conversation | Operating assumption, with a cost ceiling of $0.02 per conversation | D28 |
| Upwork headcount, client stores per implementer, implementer revenue | Planning bands, asked in the session application form | D55 |
| Multilingual and Arabic storefront counts | Not sized. Storefront language is a qualifier asked at intake | D53, D11 |
| Agency counts in Dubai, Kuwait, Qatar, Jordan, Morocco, Shopify Markets by country | Out of scope until the GCC opens | D11 |
