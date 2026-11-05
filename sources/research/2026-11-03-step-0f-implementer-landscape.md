# Step 0.F: The implementer landscape (Run 2 audience)

**Date checked:** 2026-11-03. **Prompt:** `../RESEARCH-PROMPTS.md` Step 0.F. **Extends:** `2026-11-03-step-0-first-pass.md` Section 5.

**Method and limits.** Web search only, because this session's network policy blocks page loads. **Implementers are reported as segments, counts, and patterns, never as a named list,** per the brief and the run rules. Directories, marketplaces, communities, and events are named, because they are venues, not prospects. Agency pages sampled for the stack analysis are anonymized (A01 to A26). Their URLs are held out of this file and the sample can be reproduced from the method notes in Section 9.

---

## 1. Segment summary

| # | Segment | How many, and from where | Where they gather | What they publish | How they charge | How they choose apps, per evidence | Sources |
|---|---|---|---|---|---|---|---|
| 1 | **Partner Directory agencies** | US, March 2026: 33 Platinum, 45 Premier, 255 Plus, 342 Select (Registered not listed). Worldwide, older and conflicting: 14 or about 86 Platinum, 42 Premier, 451 Plus, 505 Select. Location pages seen: Canada 259 partners, Egypt 33. Shopify's whole program is reported at 700,000+ partners, mostly Registered | Partner Directory, Partner Slack, DotDev, vendor partner days | Case studies, "technology partners" pages listing app partner tiers | Projects, retainers | App partner tiers displayed as credentials (Section 7) | [mgroupweb](https://mgroupweb.com/blogs/shopify-partner-directory/), [Qualimero](https://qualimero.com/en/blog/shopify-partner), [US tier counts, an agency-published guide](https://sherocommerce.com/top-shopify-agencies-in-the-us/), [Partner Directory, Canada](https://www.shopify.com/partners/directory/locations/canada), [Partner Directory, Egypt](https://www.shopify.com/eg/partners/directory), [Help: directory](https://help.shopify.com/partners/directory/how-it-works) |
| 2 | **CRO agencies** specializing in Shopify | No count found. Roundups repeat a set of 10 to 15 names, mostly self-ranked (first pass) | Same as 1, plus CRO tooling communities | Test results, CRO playbooks | Retainers, sometimes performance-linked | Stack in the sample: Intelligems, Shoplift, Hotjar, Microsoft Clarity, GA4, Rebuy, Octane AI. They sell measured conversion, so they will ask for measurement Pico does not have (C1, C9) | Sample A09 to A12 |
| 3 | **Freelance Shopify developers** | Storetasker says it reviewed 15,000+ Shopify developers, designers, and marketers and accepts under 5%. Upwork and Fiverr Shopify counts not found | Upwork, Fiverr, Storetasker, r/shopify | Gigs and profiles | Fixed-price gigs and hourly. AI chatbot gigs $30 to $1,000, one job post at $15 to $35 an hour (0.D) | **Some already sell installation of existing AI chat apps** (Tidio, VanChat, SmartBot, Verifast) for about $100 (0.D, F07) | [Storetasker](https://storetasker.com/), [Fiverr](https://www.fiverr.com/gigs/shopify-ai) |
| 4 | **Theme developers and designers** | About 200 to 224 Theme Store listings, many presets of the same theme, built by selected Theme Partners. Dawn is the most-used theme. One tracker says about 33% of stores run custom themes. One premium theme house claims 60,000+ merchants per theme (first pass) | Theme Store, dev forum | Themes, theme docs | Theme sales, custom theme projects | Theme choice decides where app blocks can appear. App **embed** blocks work in vintage and Online Store 2.0 themes, app blocks only in Online Store 2.0 | [Qualimero](https://qualimero.com/en/blog/shopify-theme-store), [Meetanshi](https://meetanshi.com/blog/shopify-themes-statistics/), [Martechvibe](https://martechvibe.com/article/wecommerce-acquires-assets-of-archetype-themes-inc), [shopify.dev](https://shopify.dev/docs/apps/build/online-store/theme-app-extensions/configuration) |
| 5 | **Headless and Hydrogen developers** | StoreLeads detects Hydrogen on 901 US stores (page updated 2025-12-05) and 64 in Morocco. No global count found. Hydrogen 2026-10 released | Hydrogen docs, dev forum | Starters, demos | Custom builds | Theme app embeds do not apply to Hydrogen. An app must offer a script or component path. **Pico's headless support is not in the source. Decided later on 2026-11-03: not claimed, with a widget script path for developers, untested (`../DECISIONS.md` D17)** | [StoreLeads US](https://storeleads.app/reports/technology/Shopify%20Hydrogen/country/US), [Hydrogen 2026-10](https://hydrogen.shopify.dev/update/hydrogen-2026-10-now-available) |
| 6 | **App integration and Plus migration specialists** | No count found. A service category in the Partner Directory | Partner Directory, vendor directories | Migration guides | Projects | Integration depth with the client's existing stack | [Partner Directory technologies](https://www.shopify.com/partners/directory/technologies) |
| 7 | **Consultants, course creators, YouTubers, newsletter writers** | No count found | YouTube, newsletters, podcasts, LinkedIn | App roundups and reviews | Sponsorships, affiliate commissions, courses | Most category roundups found in 0.A to 0.C were written by a vendor in the category. Affiliate programs (0.G) pay creators to recommend | Pattern from 0.A Section 1 |
| 8 | **Developers building through coding agents** | No count found. Shopify's AI Toolkit supports Claude Code, Codex, Cursor, Antigravity CLI, Hermes, and VS Code. An unofficial MCP community Discord lists 10,000+ members | AI Toolkit docs, dev forum, coding-agent communities | Skills, MCP configs | Same as 1 and 3 | **Install by skill and MCP is now Shopify's own pattern** (one `shopify` skill, a `ucp` skill, the Dev MCP server). Pico's downloadable setup skill fits it | [AI Toolkit](https://shopify.dev/docs/apps/build/ai-toolkit), [skills consolidated](https://shopify.dev/changelog/posts/ai-toolkit-skills-have-been-consolidated), [Tenten community list](https://tenten.co/shopifymcp/docs/communities/top-30-communities) |
| + | Arabic-language and Gulf agencies | See 0.E Section 5. Egypt location page: 33 partners. Gulf partner profiles list Arabic right to left builds as a service | | | | Gulf agency pages in the sample list Tabby, Tamara, WhatsApp, and cash on delivery setup, not chat apps | 0.E, sample A22 to A26 |

**Ecosystem scale, from Shopify.** Shopify says its partner ecosystem generated nearly 7 times Shopify's own revenue in 2025, $6.86 for every dollar Shopify earned ([Shopify](https://www.shopify.com/news/a-world-with-more-builders)). Third-party estimates of 37,300 active app partners and 16,000+ public apps conflict with others and are not used.

---

## 2. The stack analysis: which apps appear on implementer pages

**Sample.** 26 agency "technology partners", "our stack", or "integration partners" pages, plus agency-written stack posts, found through the search index on 2026-11-03, short of the 30 the prompt asks for because the index exposes partner lists unevenly. By location as stated or implied: UK 4, US 4, Australia 4, UAE 5, Europe 3, unstated 6. By type: Shopify build agencies 17, CRO agencies 4, UAE build agencies 5. Partner tiers stated on the pages: 3 Platinum, 4 Premier, 3 Plus, 1 Select, the rest unstated.

**Bias, stated plainly.** Most queries named common stack apps (Klaviyo, Gorgias, Rebuy, Okendo, Recharge, Searchanise, Boost, Tidio, Tolstoy), so pages listing those names were more likely to be found. Frequencies of named apps are inflated. **The absence of AI chat and AI shopping assistant apps is still informative,** because two queries named Tidio and AI chatbots explicitly and returned no agency stack page listing them.

| App | Pages listing it (of 26) | Category | Note |
|---|---|---|---|
| **Klaviyo** | 17 | Email, SMS, and now Customer Agent | Tiers cited: Elite, Elite Master, Master Platinum |
| **Gorgias** | 13 | Helpdesk, and now Shopping Assistant | Tiers cited: Elite, partner. One agency is Gorgias-only |
| Recharge | 8 | Subscriptions | Tiers cited: Elite, Premier, Agency Partner of the Year |
| Okendo | 8 | Reviews | Tier cited: Platinum |
| **Rebuy** | 7, plus 1 blog mention | **Recommendations and upsell** | Tier cited: Silver Certified |
| Yotpo | 6 | Reviews and loyalty | |
| Intelligems | 4 | Price and offer testing | All four CRO agencies |
| Nosto | 3 | **Search and recommendations** | All at Plus or enterprise level |
| Tabby, Tamara | 3 each | Buy now, pay later, Gulf | All UAE agencies |
| Microsoft Clarity | 3 | Analytics | CRO agencies |
| LoyaltyLion, Loop Subscriptions, Hotjar, GA4, WhatsApp Business | 2 each | | |
| Attentive, Tolstoy, Aircall, Shoplift, SKIO, Rivo, Swap, HighCohesion, Checkout.com, Network International, Octane AI (blog) | 1 each | | |
| **Any AI shopping assistant or AI chat app** (Tidio, Chatty, Zipchat, Rep AI, Manifest AI, Dialog, and the rest of 0.A) | **0** | | |
| **Any dedicated search app** (Boost, Searchanise, Algolia, Searchspring, Klevu, Doofinder, Fast Simon) | **0** | | One page mentions "advanced search" without naming an app |

**What this shows.**

1. **No AI shopping assistant has a place in the sampled implementer stacks.** The seat Pico wants is held, where it is held at all, by **Gorgias** (helpdesk with a Shopping Assistant) and **Klaviyo** (with Customer Agent). Both arrive inside relationships agencies already have, with tiered agency programs.
2. **Discovery in the standard stack means recommendations, not search or chat.** Rebuy is the discovery app agencies list. Search is left to Shopify's native app or to whatever the merchant already has, and Nosto appears at the enterprise end.
3. **Agencies display app partner tiers as credentials.** Elite, Platinum, Premier, Master, Partner of the Year. A tier is marketing for the agency, which is part of why agencies join programs. A Pico program with no tier has nothing for the agency to display.
4. **Gulf agencies build for local payments and WhatsApp,** not for on-site AI chat, in this sample.

---

## 3. CRO agencies, in more detail

From sample pages A09 to A12 and the first pass:

- **Tools they standardize on:** Intelligems for price and offer tests, Shoplift for theme A/B tests, Hotjar or Microsoft Clarity for heatmaps, GA4 and GTM for tracking, Rebuy and Octane AI as conversion apps.
- **What they sell:** measured lift. They will ask Pico for a holdout test or conversion data, which Pico does not have (C1, C9).
- **What Pico can offer them honestly:** qualitative discovery data, what shoppers asked for in their own words and what returned nothing, which is research input for CRO hypotheses. This is a Run 2 Phase 1 hypothesis, not a claim.

---

## 4. Freelancers, in more detail

- **Marketplaces:** Upwork, Fiverr, Storetasker. Storetasker vets: 15,000+ reviewed, under 5% accepted ([Storetasker](https://storetasker.com/)).
- **AI chat work they sell (0.D):** generic ChatGPT bots ($30 to $250), store-connected agents ($250 to $1,000), and **installation of existing AI chat apps** (about $100). The last is the Run 2 opening for a freelancer: Pico can be the app they install, and the setup skill shortens that job.

---

## 5. Theme developers and the theme app embed

- App embed blocks are supported in **vintage and Online Store 2.0 themes**. They are **off by default after install** and must be turned on under Theme Settings > App embeds. They are **active only on the theme where they were enabled**, so a theme switch needs the merchant to enable the embed again ([shopify.dev](https://shopify.dev/docs/apps/build/online-store/theme-app-extensions/configuration), [verify support](https://shopify.dev/docs/apps/build/online-store/verify-support)).
- **Consequence for Pico.** The brief's open question on theme compatibility narrows: the embed mechanism works on all Online Store themes per Shopify, while whether Pico's widget renders cleanly on each theme is tested on Dawn and Horizon before launch and in every paid session (`../DECISIONS.md` D16). The activation risk the brief already names, "the embed left off", is a documented Shopify behavior, and it recurs on every theme change. That matters to theme developers and agencies, who change themes for clients.

---

## 6. Developers who build through coding agents

- Shopify ships its own coding-agent tooling: the AI Toolkit as a plugin, skill files, or the Dev MCP server, recently merged into one `shopify` skill, plus a `ucp` skill ([shopify.dev](https://shopify.dev/docs/apps/build/ai-toolkit)).
- Pico's downloadable setup skill for Cursor, Claude Code, Codex, and Antigravity follows the same pattern. That is a distribution fit, not a differentiator: the same developers are also given everything they need to build Pico's job themselves (0.D Section 1a).
- Count of developers using coding agents on Shopify: no Shopify-specific source found. The nearest proxy, found later on 2026-11-03: 14.1% of Stack Overflow's 2025 respondents use AI agents at work daily, and 47.1% use AI tools daily (`2026-11-03-tbd-resolution-research.md` Section 7).

---

## 7. How implementers choose apps, the evidence

| Signal | Evidence | Source |
|---|---|---|
| Partner program tier as a credential | 11 of 26 sampled pages state a vendor tier (Recharge Elite, Klaviyo Elite, Gorgias Elite, Okendo Platinum, Rebuy Silver, LoyaltyLion Gold, Loop Platinum, Attentive Pioneer) | Sample |
| Integration with the client's core stack | Pages pair apps by integration (Klaviyo with Gorgias, Recharge with Klaviyo) | Sample, [Recharge integrations](https://getrecharge.com/integrations/?integration=klaviyo) |
| Vendor directories send work to agencies | Rebuy, Gorgias, and Klaviyo run agency directories | [Rebuy partners](https://rebuy.partnerpage.io/), [Gorgias agencies](https://agencies.gorgias.com/), [Klaviyo directory](https://connect.klaviyo.com/) |
| Measured results for CRO agencies | CRO pages lead with testing tools | Sample A09 to A12 |
| Third-party partner graphs | Partnerbase tracks shared partners between agencies and vendors, a tool for Run 2 targeting later | [Partnerbase](https://partnerbase.com/full-fat-commerce/gorgias) |
| Setup work as revenue | Freelancers charge to install existing AI chat apps | 0.D |

Partner program terms (revenue share, tiers, dev stores) are in `2026-11-03-step-0g-partner-programs.md`.

---

## 8. Communities and events

| Venue | What it is | Size, where found | URL |
|---|---|---|---|
| Shopify Developer Community Forums | Shopify's developer forum on Discourse, where Shopify routes developer troubleshooting | No member count found | [community.shopify.dev](https://community.shopify.dev/about), [announcement](https://shopify.com/partners/blog/announcing-the-new-shopify-dev-community-forums) |
| Shopify Partners Slack | Peer community for partners | 25,000+ per one listicle, unverified | [Tenten list](https://tenten.co/shopifymcp/docs/communities/top-30-communities) |
| Shopify Community | Merchant forum | Nearly 900,000 members per one source | [community.shopify.com](https://community.shopify.com/) |
| r/shopify | Merchant and implementer subreddit | 280,000 to 384,000 members across snapshots | [Hive Index](https://thehiveindex.com/communities/r-shopify/), [GummySearch](https://gummysearch.com/r/shopify/) |
| r/ShopifyDevelopment | Developer subreddit | About 1,000 members | [GummySearch](https://gummysearch.com/r/ShopifyDevelopment) |
| Shopify developers Discord | No official one found. An unofficial MCP community Discord lists 10,000+ | | [Tenten list](https://tenten.co/shopifymcp/docs/communities/top-30-communities) |
| **Shopify Editions** | Product releases, now Winter, Spring, and Fall in 2026 | | [Fall '26](https://www.shopify.com/editions/fall2026) |
| **DotDev 2026** | Shopify's in-person developer and partner event, Toronto, 2026-07-21 to 22. Active partner account required, up to 6 tickets per partner organization | | [dotdev.shopify.com](https://dotdev.shopify.com) |
| Vendor partner days around DotDev | Example: a Partner Day in Toronto on 2026-07-20 hosted by a search vendor | | [Nosto](https://www.nosto.com/?p=112804) |
| Shopify at NRF 2026 | Partner-facing booth in New York, January 2026 | | [Shopify partner events](https://www.shopify.com/event/nrf2026-partners) |
| Third-party ecommerce events | Shoptalk, eTail, and regional events agencies attend | | [2026 events calendar](https://www.letstalkshop.com/blog/ecommerce-conferences-and-events-to-attend-2026) |

---

## 9. Method notes for reproducing the stack sample

Queries run on 2026-11-03 through the search index: Shopify Plus agency "technology partners" with common stack apps; agency "our tech stack" and recommended apps; agency partners pages naming search vendors; Shopify CRO agency tools and partners; UK, Australian, Canadian, US DTC, German and Dutch, and Dubai agency partner pages; agency "apps we recommend" pages naming AI chat and search apps. A page entered the sample if it was an agency's own partner, stack, or integration page, or an agency-written stack post, and named at least one app. Vendor directories (Rebuy, Gorgias, Klaviyo) were used as sources, not as sample rows. Agency names and URLs are kept out of this file under the no-named-implementer rule. They can be supplied separately if the owner wants an evidence appendix.
