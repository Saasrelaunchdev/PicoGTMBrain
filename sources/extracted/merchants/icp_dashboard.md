<!-- build: xlsx -->
# Run 1, Dashboard 4: Ideal Customer Profile, Shopify merchants

Step 4.1 of gtm-builder v3.1, with the maturity reading from `SKILL-ADAPTATION.md` Phase 4: Level 1 is a store that has not solved product discovery by conversation at all, Level 2 is a store that started and stalled. Primary market: global, USA first. The GCC is on its own sheet as the secondary market for later (owner decision, 2026-11-03). Built on 2026-11-03.

Rules applied: every count names one tracker with its method and date, and two trackers are never mixed in one figure. Bands no tracker publishes are planning bands from `DECISIONS.md` D53 and D54, labelled as such. Field changes from the adaptation file: "Revenue, $" reads as the store's annual sales band, "Team Size" is the store team, and four rows are added that predict fit better than revenue: Shopify plan, catalog size and complexity, storefront languages, and monthly sessions.

## Sheet: ICP

| Attribute | ICP Level 1: no conversational discovery yet | ICP Level 2: started and stalled |
|---|---|---|
| Segment | Shopify stores, USA first, whose shoppers need help choosing between many similar or technical products, running Shopify's own search and filters with no AI shopping assistant turned on | Growing Shopify brands and retailers, USA first, already paying for a search, quiz, recommendation, or chat app, whose shoppers still fail to find products |
| Sub-industries | Health (supplements), Sports (outdoor gear, Pico's own sandbox catalog), Pets & Animals, Autos & Vehicles (parts and fitment), Consumer Electronics. Home & Garden as the adjacent category | The same five, plus Home & Garden and Beauty & Fitness, where quiz and recommendation apps are already installed |
| Location | United States first: 1,253,193 live Shopify stores (StoreLeads, page dated 2026-10-30). The UK, Canada, and Australia next. GCC: secondary, for later, see the Secondary_GCC sheet | United States first, then the UK, Canada, and Australia. Plus merchants cluster in the US: 29,556 of 81,318 Plus domains (StoreLeads, 2026) |
| Revenue, $ (annual sales band) | About $150,000 to $3 million a year, a planning band `DERIVED` from the session band (D53) | About $1.5 million to $30 million a year, same method |
| Team Size (store team) | Owner-run or a small team of 1 to 10 people (D53). The owner installs and decides, so the buying committee collapses (Dashboard 5) | An ecommerce team of 10 to 50 people, plus an agency or developer (D53) |
| Business Maturity | Selling with steady traffic, past launch, with a catalog large enough that browsing and keyword search stop working: 100 or more products (D53) | Has already invested in discovery or chat tools, reads its own search analytics, and is weighing whether to replace or add to a tool that stalled |
| Business Model | Brand selling direct, or a retailer or reseller of many similar products | Brand, multi-brand retailer, or B2B wholesale on Shopify |
| Best Engagement Model | Self-serve: sandbox first, App Store install, four-step checklist, free plan, 14 day Growth trial with no card | Agency-installed or assisted onboarding, through the founding cohort (Dashboard 5) and the implementers in Run 2. Free plan to trial, then Growth or Pro |
| Organization Challenges and Pain Points | Shoppers who don't know a product's name leave or email to ask. The owner answers the same pre-purchase questions by hand. Little time to configure tools. Wary of app bills that grow without warning, the top complaint class in reviews (Dashboard 2, Reviews_2.7) | A paid search or quiz app still leaves requests unmatched. The chat app answers support questions but does not help shoppers choose. Reports do not show what shoppers asked an assistant. Too many apps, each with its own bill |
| Why Should They Choose Us (Value Proposition Hypothesis) | See what shoppers ask for, including requests that found nothing. Product cards from the synced catalog. Try the shopper experience in a sandbox before installing. Start free, 50 conversations a month | Insight into what shoppers ask the assistant, with zero result and weak click phrases as a list of catalog fixes for the team. A sync log behind every card. A predictable quota per plan, up to 2,000 conversations on Pro for $99. A setup skill their developer's coding agent can follow |
| Strategic Goals Related to Our Product/Service | Help shoppers find the right product without adding staff. Learn which products or descriptions shoppers cannot find. Keep the app stack light and costs predictable | Turn shoppers' requests into catalog and copy fixes. Give the ecommerce team evidence for merchandising decisions. Consolidate tools without losing coverage |
| Triggers | A run of repeat pre-purchase questions. A new product line. Opening "Searches with no results" in Shopify's own analytics. Preparing for peak season. A theme change or redesign. News of AI shopping assistants, such as Shopify's Fall '26 Edition | Switching chat apps: AI-first chat apps are growing from small bases while older live chat apps shrink (StoreLeads, 2026, directional). A search or quiz app renewal. A redesign or replatform. A new market or language. An agency recommendation |
| Shopify plan | Basic or Grow | Advanced or Plus. Plus: about 54,200 merchants on 81,318 domains (StoreLeads, 2026) |
| Catalog size and complexity | 100 or more products, with similar or technical items, variants, sizes, or fitment rules that make browsing fail. 853,366 Shopify stores sell 100 or more, 28.2% of those in StoreLeads' product bands (State of Shopify 2026) | 250 or more products, with many variants and specs. 500,646 stores, 16.5% (same source) |
| Storefront languages | English. A second storefront language fits the 10 languages the widget text is translated for | One or more. Multilingual stores fit the same 10 languages. Not sized, because no tracker publishes storefront language. Asked at intake (D53) |
| Monthly sessions | 10,000 to 100,000 (D53). Fit check at 2% of sessions starting a conversation, an assumption (D54): 200 to 2,000 conversations a month, so Growth or Pro | 100,000 to 1 million. Fit check: 2,000 to 20,000 conversations, so Pro, then Scale up to about 300,000 sessions, then a custom plan (D27) |

## Sheet: Sizing

Frames for each level, not market sizes. Every figure is StoreLeads, which counts stores it detects as live and selling. Install counts are global, because US-only install counts were not read. `DERIVED` marks arithmetic done in this run. Source detail in `research/2026-11-03-step-0h-market-sizing.md`.

| Lens | Figure | Method | Date | Source | Used for |
|---|---|---|---|---|---|
| Live US Shopify stores | 1,253,193 | StoreLeads detected live stores, US page | 2026-10-30 | [StoreLeads US](https://storeleads.app/reports/shopify/US/top-stores) | Location frame, both levels |
| US stores in the five help-me-choose categories | About 192,500 | `DERIVED`: Health 53,037 + Sports 54,409 + Pets & Animals 33,697 + Autos & Vehicles 31,469 + Consumer Electronics 19,902. Overlap between categories unknown, so an upper bound | 2026 | [StoreLeads US](https://storeleads.app/reports/shopify/US/top-stores) | Level 1 frame |
| US Home & Garden stores | 159,779 | StoreLeads category count, US | 2026 | Same | Adjacent category |
| English-speaking core: US, UK, Canada, Australia | About 1.79 million | `DERIVED` from four StoreLeads country counts | 2026 | [StoreLeads](https://storeleads.app/reports/shopify) | Next markets after the US |
| Installs of the three largest third-party search apps | About 49,500, global | `DERIVED`: Boost 20,487 + Smart Product Filter & Search about 16,300 to 16,600 + Searchanise about 12,600 to 12,800. Overlap unknown | 2026 | StoreLeads app pages, via `research/2026-11-03-step-0b-indirect-competitors.md` | Level 2 frame: stores already paying for discovery |
| Installs of 16 third-party AI and live chat apps | About 86,700 to 88,300, global | `DERIVED` from StoreLeads app pages. Overlap unknown, so not a store count | 2026 | `research/2026-11-03-step-0h-market-sizing.md` Section 7 | Level 2 frame: stores that may switch chat apps |
| Shopify Inbox installs | About 355,400 to 358,000, global | StoreLeads app page | 2026 | [StoreLeads Inbox](https://storeleads.app/reports/shopify/app/inbox) | The free native default every level weighs Pico against |
| Shopify Plus | About 54,200 merchants on 81,318 domains, global. US: 29,556 domains | StoreLeads Plus statistics | 2026-11-03 | [StoreLeads Plus](https://storeleads.app/reports/shopify/list-of-shopify-plus-stores) | Level 2 upper end |
| Translation app installs | Weglot 19,291 (page about 767 days old), Langify 10,157 | StoreLeads app pages | Stale | [Weglot](https://storeleads.app/reports/shopify/app/weglot), [Langify](https://storeleads.app/reports/shopify/app/langify) | Lower bound for multilingual stores |
| Catalog size cutoff | 100 or more products: 853,366 stores, 28.2%. 250 or more: 500,646, 16.5% | StoreLeads stores by number of products, platform wide. `DERIVED` shares of the 3,030,662 stores in its bands | 2026 | [StoreLeads State of Shopify](https://storeleads.app/reports/shopify) | Level 1 and 2 filter |
| US Level 1 frame after the cutoff | About 54,300 | `DERIVED`: about 192,500 × 28.2%, assuming US stores in the five categories match the platform-wide share. One tracker | 2026 | The two rows above | Level 1 frame |
| Annual sales band | Level 1 about $150,000 to $3 million. Level 2 about $1.5 million to $30 million | `DERIVED`: monthly sessions × 12 × 1.4% conversion (Littledata, 2,800 Shopify sites, 2023) × an order value of $90 to $180. A planning band, not a tracker figure | 2026-11-03 | `DECISIONS.md` D53 | Revenue row |
| Monthly sessions band | Level 1: 10,000 to 100,000. Level 2: 100,000 to 1 million | Planning band set by decision, since no tracker publishes sessions per store | 2026-11-03 | `DECISIONS.md` D53 | Quota fit |

**Reading the frames.** Level 1 is large and unproven: up to about 192,500 US stores in the five categories, and about 54,300 after the 100-product cutoff (`DERIVED`). Level 2 is smaller and easier to find: stores already paying for search or chat are visible through app install trackers. Both sit beside a free native agent installed on about 358,000 stores.

## Sheet: Secondary_GCC

Secondary go-to-market, **for later**. Shown for reference and not pursued now (owner decision, 2026-11-03). Source detail in `research/2026-11-03-step-0e-arabic-markets.md`.

| Attribute | GCC: Saudi Arabia, UAE, Kuwait, Qatar, Bahrain, Oman |
|---|---|
| Status | Secondary, for later. No GCC copy, channel, or budget in the primary plan |
| Live Shopify stores | UAE 26,986. Saudi Arabia 4,480. Kuwait 3,790. Qatar 2,265. Bahrain at least 367 and Oman at least 471, from city and area pages with no national total. `DERIVED`: at least about 38,400 across the six (StoreLeads, 2026). Many UAE stores run English storefronts. Stores with an Arabic storefront language: no tracker publishes it, so it is asked at intake when the GCC opens (D11) |
| Platform context | Saudi Arabia is mostly WooCommerce (36.8%), Zid (16.4%), and Shopify (13.5%) of detected ecommerce sites (wmtips), and Salla leads by store count in another tracker. Pico reaches Salla and Zid stores only through its custom catalog API |
| How shoppers ask | Social and messaging heavy. 79% of UAE shoppers use social media to research products (RetailX, secondhand). WhatsApp's role is inferred, not measured. Pico has no WhatsApp channel (candidate C7, not built) |
| What Pico would offer | Arabic replies display right to left, with a language switcher and separate merchant copy per language. Arabic is one of the 10 languages the widget text is translated for |
| Competition there | Arabic-first Shopify apps (Luma, shamz.ai). Verifast names Arabic. Fin and Lyro answer in Arabic. Salla ships its own Arabic AI search. Meta's business agent on WhatsApp |
| Billing | Shopify Billing in USD. Shopify shows no local-currency estimate for AED, SAR, KWD, or QAR. Cards may need international transactions enabled |
| Agencies | Partner Directory profiles in Dubai list Arabic right to left development as a service. Counted from the directory's filters when the GCC opens (D11) |
| ICP if opened | UAE Shopify stores with Arabic or bilingual storefronts, in the same help-me-choose categories. Sized when the GCC opens, starting from the UAE's 26,986 stores (D11) |
| Condition to open it, decided | The US founding cohort is full and at least 5 GCC stores have asked for Pico in one quarter (D11). Messaging channels are reviewed then (D14) |
