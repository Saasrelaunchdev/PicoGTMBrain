# Step 0.H: Market and ICP sizing

**Date checked:** 2026-11-03. **Prompt:** `../RESEARCH-PROMPTS.md` Step 0.H. **Extends:** `2026-11-03-step-0-first-pass.md` Section 7. **Feeds:** Phase 4 for both runs.

**The rule this file follows.** Shopify does not publish a store count. Every figure names its tracker, method, and date. **Two trackers are never mixed in one figure.** StoreLeads is the primary tracker here because it publishes counts by country, category, app, and plan from one method. Arithmetic done here is marked `DERIVED`. Gaps left in this pass were closed later on 2026-11-03 in `2026-11-03-tbd-resolution-research.md` and `../DECISIONS.md`.

**Method and limits.** Web search only, because this session's network policy blocks page loads. StoreLeads pages were read through the search index. Their headline figures and their own quarterly tables sometimes differ by a few percent, and both are shown where they do.

---

## 1. The two trackers, and why they disagree

| Tracker | What it counts | Live Shopify stores | Date | Source |
|---|---|---|---|---|
| **StoreLeads** | Stores it detects as live and selling, with category, country, plan, and app data | **3,225,094** headline. Its own 2026 Q3 table shows 3,108,808 | Page current on 2026-11-03 | [StoreLeads State of Shopify 2026](https://storeleads.app/reports/shopify) |
| StoreLeads, earlier reading | Same method | About 2.83 million | 2026-02 | First pass, via [ecomm.design](https://ecomm.design/how-many-shopify-stores-are-there/) |
| **BuiltWith** | Websites with a Shopify technology footprint, including dormant domains with leftover scripts | **6,903,597** live, plus about 363,000 redirecting domains | 2026-02 | Via [ecomm.design](https://ecomm.design/how-many-shopify-stores-are-there/) and [Linkmybooks](https://linkmybooks.com/blog/how-many-sellers-are-on-shopify), secondary |

**Use StoreLeads for Phase 4,** with its date. BuiltWith measures footprints, not merchants. The gap between 2.83 million in February and 3.23 million now is one tracker's growth over about eight months, not a disagreement.

---

## 2. Live Shopify stores by country, StoreLeads

| Country | Live stores | Share of StoreLeads total | Page date | Source |
|---|---|---|---|---|
| United States | 1,253,193 (Q3 table: 1,184,882) | 38.9% | 2026-10-30 | [StoreLeads US](https://storeleads.app/reports/shopify/US/top-stores) |
| United Kingdom | 242,245 in the global report, 234,860 on the UK page | 7.5% | UK page 2026-10-09 | [StoreLeads UK](https://storeleads.app/reports/shopify/GB/top-stores) |
| Canada | 149,714 | 4.6% | 2026 | [StoreLeads](https://storeleads.app/reports/shopify) |
| Australia | 142,174 | 4.4% | 2026 | Same |
| Germany | 104,242 | `DERIVED` about 3.2% | 2026 | Same |
| United Arab Emirates | 26,986, up 15% year over year | | 2026 | [StoreLeads AE](https://storeleads.app/reports/shopify/AE/top-stores) |
| Egypt | 16,122, up 63% year over year | | 2026-10-16 | [StoreLeads EG](https://storeleads.app/reports/shopify/EG/top-stores) |
| Saudi Arabia | 4,480 (Q3 chart: 4,517) | | 2026-10-09 | [StoreLeads SA](https://storeleads.app/reports/shopify/SA/top-stores) |

**`DERIVED`:** US, UK, Canada, and Australia together hold about 1.79 million stores, roughly 55% of the StoreLeads total. That is the English-speaking core of open decision 3's default. More Arabic-market counts are in `2026-11-03-step-0e-arabic-markets.md`.

---

## 3. Shopify Plus, StoreLeads

| Measure | Figure | Source |
|---|---|---|
| Domains on Plus | 81,318 | [StoreLeads Plus statistics](https://storeleads.app/reports/shopify/list-of-shopify-plus-stores) |
| Distinct Plus merchants | About 54,212, because one Plus merchant can run several domains | Same |
| By country (domains) | US 29,556 (36.3%), UK 6,375, Germany 5,584, France 4,406, Canada 3,844, Australia 3,797, Netherlands 2,895, Czech Republic 1,944, Denmark 1,782, Hong Kong 1,569. Country pages show US 29,813 and UK 6,350 | Same |
| By category (domains) | Apparel 20,573, Beauty & Fitness 10,196, Home & Garden 9,944, Sports 4,576 | Same |
| Earlier reading | A February 2026 citation gives 55,964 Plus domains, closer to today's merchant count than today's domain count. Treat the February figure as unresolved | [ecomm.design](https://ecomm.design/how-many-shopify-stores-are-there/) |

The first pass range of "about 52K to 85K" mixed merchants and domains. **For Phase 4, Plus means about 54,200 merchants on 81,300 domains, StoreLeads, 2026-11-03.**

---

## 4. Stores by vertical, especially where shoppers need help choosing

StoreLeads category counts, global and US. Only the top three global shares are published, so other shares are `DERIVED` from the 3,225,094 total.

| Category | Global stores | Global share | US stores | Why it matters to Pico |
|---|---|---|---|---|
| Apparel | 875,022 (category page: 836,839) | 27.1% | 366,464 (29.2%) | Large, but choice is mostly size and style. Quizzes and visual tools compete |
| Home & Garden | 409,956 | 12.7% | 159,779 (12.7%) | Many similar products with specs |
| Beauty & Fitness | `DERIVED` about 351,500 | 10.9% | 132,780 (10.6%) | Quiz incumbent (Octane AI's largest category, 39% of its stores) |
| **Health** (closest to supplements) | 145,397 | `DERIVED` 4.5% | 53,037 | Ingredient and goal questions |
| **Sports** (outdoor gear sits here, and is Pico's own sandbox catalog) | 119,887 | `DERIVED` 3.7% | 54,409 | Technical choice, the source's example request is hiking boots |
| **Pets & Animals** | 85,610 | `DERIVED` 2.7% | 33,697 | Size, age, and diet questions |
| **Autos & Vehicles** (auto parts) | 76,148 | `DERIVED` 2.4% | 31,469 | Fitment questions, a hard case for keyword matching |
| **Consumer Electronics** | 61,221 | `DERIVED` 1.9% | 19,902 | Compatibility and spec questions |
| Computers | 50,863 | `DERIVED` 1.6% | 15,844 | Same |
| Electronics & Electrical | 9,445 | | | |

Sources: [StoreLeads State of Shopify](https://storeleads.app/reports/shopify), [US page](https://storeleads.app/reports/shopify/US/top-stores), [Apparel](https://storeleads.app/reports/shopify/category/Apparel), [Sports](https://storeleads.app/reports/shopify/category/Sports) (page marked 298 days old), [Electronics & Electrical](https://storeleads.app/reports/shopify/category/Computers/Electronics%20&%20Electrical).

**`DERIVED`, for Phase 4 only:** the five help-me-choose categories in bold total about 488,000 stores globally (145,397 + 119,887 + 85,610 + 76,148 + 61,221) and about 192,500 in the US. Category overlap inside StoreLeads is not stated, so this is an upper bound. It is a sizing frame, not a market size claim, and it does not go into customer copy.

---

## 5. Stores by catalog size

| Finding | Source |
|---|---|
| **Platform-wide catalog size distribution, found later on 2026-11-03:** of 3,030,662 stores in StoreLeads' product bands, 853,366 sell 100 or more products (28.2%) and 500,646 sell 250 or more (16.5%). 30.0% sell 1 to 9 | [StoreLeads State of Shopify 2026](https://storeleads.app/reports/shopify), `2026-11-03-tbd-resolution-research.md` Section 6 |
| Apparel only: 18.3% of Apparel stores sell 1 to 9 products, 16.4% sell 10 to 24, 14.8% sell 100 to 249 | [StoreLeads Apparel](https://storeleads.app/reports/shopify/category/Apparel) |
| StoreLeads breaks app installs down by catalog size on each app's page, which could size Pico's catalog band later from competitor install bases | StoreLeads app pages (0.B) |

**Why it matters.** Pico's niche (`../GTM-BRIEF.md` Section 1) assumes catalogs with many similar or technical products. A store with 1 to 9 products rarely needs conversational discovery. The catalog-size cutoffs are set from that distribution: 100 or more products for ICP Level 1, 250 or more for Level 2 (`../DECISIONS.md` D53).

---

## 6. Stores with more than one storefront language, or using Markets

| Proxy | Figure | Source |
|---|---|---|
| Weglot installs | 19,291, page about 767 days old, stale | [StoreLeads Weglot](https://storeleads.app/reports/shopify/app/weglot) |
| Langify installs | 10,157, down about 20% year over year | [StoreLeads Langify](https://storeleads.app/reports/shopify/app/langify) |
| Translate & Adapt (Shopify's own) installs | Not found. StoreCensus pages conflict, 962 and 0 | `2026-11-03-tbd-resolution-research.md` |
| Stores with more than one published language, or with Shopify Markets for several countries | Not found. Not sized: storefront language is asked at intake (D53) | |

**What it means.** The multilingual segment is real but unsized. Third-party translation apps show at least tens of thousands of stores, and Shopify's free Translate & Adapt likely covers far more. A direct count needs page access to StoreLeads' language filters. Until then, "stores that sell in more than one language" in the niche stays a hypothesis with a lower bound, not a size.

---

## 7. Install counts for AI chat and AI shopping assistant apps, StoreLeads

StoreLeads detects a subset of installs, so these are lower bounds. Year over year as shown on each app page. Two figures where the detail page and the ranking list differ.

| App | Installs | Year over year | Source |
|---|---|---|---|
| Shopify Inbox | 355,420 to 358,008 | down 5.7% | [StoreLeads](https://storeleads.app/reports/shopify/app/inbox) |
| Tidio | 27,499 to 27,707 | down 10.2% | [StoreLeads](https://storeleads.app/reports/shopify/app/tidio-chat) |
| Gorgias | 25,120 to 25,614 | up 13.7% | [StoreLeads](https://storeleads.app/reports/shopify/app/helpdesk) |
| Chatty | 8,968 | down 1.7% | [StoreLeads](https://storeleads.app/reports/shopify/app/chatty) |
| **Moose AI Chatbot & Live Chat** | 8,039 to 8,194 | **up 463.2%** | [StoreLeads](https://storeleads.app/reports/shopify/app/moosedesk) |
| Re:amaze | 3,741 to 3,882 | down 12.9% | [StoreLeads](https://storeleads.app/reports/shopify/app/reamaze) |
| Willdesk | 3,260 to 3,290 | down 28.1% | [StoreLeads](https://storeleads.app/reports/shopify/app/self-faq) |
| Richpanel | 2,555 to 2,778 | up 25.9% | [StoreLeads](https://storeleads.app/reports/shopify/app/customer-support) |
| **Zipchat** | 1,952 to 2,135 | **up 100.4%** | [StoreLeads](https://storeleads.app/reports/shopify/app/zipchat) |
| SmartBot | 1,341 to 1,363 | up 6.5% | [StoreLeads](https://storeleads.app/reports/shopify/app/smartbot) |
| Rep AI | 1,007 to 1,012 | up 3.9% | [StoreLeads](https://storeleads.app/reports/shopify/app/rep-ai-sales-associate) |
| **Commslayer** | 863 to 1,001 | **up 387.6%** | [StoreLeads](https://storeleads.app/reports/shopify/app/commslayer) |
| Wizybot | 944 to 961 | up 13.2% | [StoreLeads](https://storeleads.app/reports/shopify/app/wizybot) |
| VanChat | 424 | up 52.0% | [StoreLeads](https://storeleads.app/reports/shopify/app/vanchat) |
| **Dialog** | 379 | **up 121.6%** | [StoreLeads](https://storeleads.app/reports/shopify/app/dialog-ai-sales-assistant) |
| Manifest AI | 308 to 334 | up 12.5% | [StoreLeads](https://storeleads.app/reports/shopify/app/manifest-ai-shopping-assistant) |
| **Verifast** | 298 | **up 195.0%** | [StoreLeads](https://storeleads.app/reports/shopify/app/verifast-sales-assistant) |

**The pattern Phase 4 should read.** AI-first chat apps are growing fast from small bases (Moose, Commslayer, Verifast, Dialog, Zipchat), while older live chat apps shrink (Tidio, Willdesk, Re:amaze) and Inbox dips. Merchants are switching chat apps. **A store replacing its chat app is a buying trigger** for the ICP table, and it is a moment when Pico is weighed against these apps directly. The StoreLeads pages carry different dates, so treat the growth rates as directional.

**`DERIVED`:** the 16 third-party apps above total about 86,700 to 88,300 detected installs, depending on which StoreLeads figure is used, against about 357,000 for Inbox alone. Overlap between apps is not known, so this is not a count of stores.

---

## 8. Install counts for search and discovery apps, StoreLeads

| App | Installs | Year over year |
|---|---|---|
| Boost AI Search & Filter | 20,487 | down 18.2% |
| Smart Product Filter & Search | 16,290 to 16,597 | down 19.2% |
| Searchanise | 12,606 to 12,808 | up 14.6% |
| Doofinder | 3,311 to 3,355 | |
| Fast Simon | 1,984 to 1,989 | |
| Rebuy (recommendations, for comparison) | 15,008 to 15,175 | up 24.7% |
| RevenueHunt (quiz) | 12,070 | |
| Octane AI (quiz) | 4,286 to 4,328 | |

Sources in `2026-11-03-step-0b-indirect-competitors.md`, opening table. **`DERIVED`:** the three largest third-party search apps hold about 49,500 detected installs. These stores already pay for discovery, which is ICP Level 2 in `../SKILL-ADAPTATION.md`.

---

## 9. Shopify Partner Directory agencies by tier and country

| Measure | Figure | Source |
|---|---|---|
| US, March 2026 | 33 Platinum, 45 Premier, 255 Plus, 342 Select | [US tier counts, an agency-published guide](https://sherocommerce.com/top-shopify-agencies-in-the-us/), secondary |
| Worldwide, older and conflicting | 14 or about 86 Platinum, 42 Premier, 451 Plus, 505 Select | [mgroupweb](https://mgroupweb.com/blogs/shopify-partner-directory/), [Qualimero](https://qualimero.com/en/blog/shopify-partner), secondary |
| Canada location page | 259 partners | [Partner Directory](https://www.shopify.com/partners/directory/locations/canada) |
| Egypt location page | 33 partners | [Partner Directory](https://www.shopify.com/eg/partners/directory) |
| All registered partners | 700,000+, mostly Registered tier | Secondary, 0.F |
| Worldwide total, found later on 2026-11-03 | About 3,754 partners listed, July 2025, unnamed method. The current split by tier and country needs the directory's filters loaded directly, so the plan uses the US tier counts above | [Hashnode](https://hashnode.com/posts/top-100-shopify-agencies-worldwide-curated-directory-of-the-best-global-partners/6868a833eb6a1a9a7a2bb511), secondary |

---

## 10. Site search usage and zero-result rates

**No primary source could be loaded.** Every figure below is secondhand. None is usable in Pico copy. Phase 9's Anchor 1 (cost of the problem) should keep these as context with the `SECONDHAND` mark, or wait for a page-loaded check of the original reports.

| Measure | Figure as cited | Cited to | Where seen | Mark |
|---|---|---|---|---|
| Sites that don't adequately support search needs | 56%, from a 2026 benchmark of 170+ sites | Baymard | Secondary summaries | `SECONDHAND` |
| No-results pages that create frustration | About 50% of ecommerce sites | Baymard | [Baymard article](https://baymard.com/research-articles/no-results-page) | Primary page, read through index |
| Zero-result rate, industry average | 10% to 15% of searches, attributed to Baymard. Other vendors say 12% to 24% or 12% to 18%. A "healthy" target under 5% could not be traced to a source | Baymard and vendors | [Hello Retail](https://helloretail.com/en/blog/2026-02-24-ecommerce-search-statistics/), [Findbar](https://findbar.io/?p=12510), [Doofinder](https://www.doofinder.com/de/ecommerce-glossar/zero-result-rate) | `SECONDHAND`, `VENDOR` |
| Share of visitors who use site search | 30% to 40% attributed to Forrester, 15% to 30% in another source | Forrester and vendors | [Xictron](https://www.xictron.com/en/blog/site-search-analytics-onsite-search-2026/) | `SECONDHAND` |
| Search benchmark from a search vendor | 2024 holiday benchmark report | Prefixbox | [Prefixbox PDF](https://www.prefixbox.com/blog/wp-content/uploads/2024/09/2024-Search-Benchmark-Report-and-Best-Practices-Holiday-Edition.pdf) | `VENDOR`, not read |
| Shopify's own guidance on no-results pages | Exists | Shopify | [Shopify blog](https://www.shopify.com/au/blog/no-results-found) | Not read for figures |

**What can still be said honestly.** Shopify's native analytics show each store its own "Searches with no results" (0.C). That store-specific number, which the merchant can open today, is a better input to Phase 9's Anchor 1 than any industry average.

---

## Summary for Phase 4

| ICP lens | Size, with source | Status |
|---|---|---|
| English-speaking Shopify stores (US, UK, Canada, Australia) | About 1.79 million live stores, StoreLeads, 2026 | Sourced |
| Help-me-choose categories | Up to about 488,000 stores globally, StoreLeads, overlap unknown | `DERIVED` upper bound |
| Stores already paying for search or discovery | About 49,500 detected installs across the top three search apps, plus Rebuy and quiz apps | Sourced lower bound |
| Stores switching chat apps | Directional, from install growth and decline | Trigger, not a size |
| Plus merchants | About 54,200 merchants on 81,300 domains | Sourced |
| Arabic-market Shopify stores (six countries) | About 64,000, StoreLeads | Sourced, see 0.E |
| Catalog size cutoff | 100 or more products for Level 1, 28.2% of stores. 250 or more for Level 2, 16.5% | Sourced, StoreLeads |
| Multilingual stores | Lower bound from translation apps. Total not sized, asked at intake (D53) | Gap, closed by method |
| Annual sales band (ICP "Revenue, $" field) | Level 1 about $150,000 to $3 million, Level 2 about $1.5 million to $30 million, `DERIVED` from session bands (D53) | Planning band |
