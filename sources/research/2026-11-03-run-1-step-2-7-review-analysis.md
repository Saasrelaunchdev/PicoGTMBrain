# Run 1, Step 2.7: Review analysis, Shopify merchants

**Date checked:** 2026-11-03. **Prompt:** `../RESEARCH-PROMPTS.md` Step 2.7, Run 1 (the skill's G2 step, substituted to the Shopify App Store). **Feeds:** Step 2.8 positioning vectors in `../run-1-merchants/02-competitive-market-analysis/`.

## Method, and what it can and cannot show

- **Source:** Shopify App Store review pages (`apps.shopify.com/<app>/reviews`, including rating-filtered pages) read through the web search index on 2026-11-03. The index returns summaries of indexed review pages, not every review. The prompt asked for at least the 50 most recent reviews and every 1 to 3 star review from the last 12 months. **That depth needs page loads, which this session's network policy blocks.**
- **Frequency, stated honestly:** "Seen" counts the distinct reviews describing a theme in the indexed snippets read. "Recurring" means the index summary said the theme recurs without listing each review. Counts are a floor, not a share of all reviews.
- **G2:** not used. The prompt allows it only where a vendor has a real G2 page with reviews, and no G2 page could be loaded.
- **Complaint classes**, per the prompt: wrong or irrelevant products, made-up answers, pricing or billing surprise, setup or theme conflict, support responsiveness, language quality, results not arriving. One more class was needed and is added: **missing handoff or channel**.

---

## 1. Per competitor

### Chatty, 4.9 stars (about 1,899 reviews), one snapshot showing 15 one-star and 6 two-star

| Positive themes | Frequency | Negative themes | Frequency | Complaint class |
|---|---|---|---|---|
| Responsive support team and setup help | Recurring | Charged after a free trial, because the store had installed before | Seen 1 | Pricing or billing surprise |
| Easy setup | Recurring | A bug lost a day of customer requests, slow fix | Seen 1 | Support responsiveness |
| Multi-language support | Seen, recurring per one summary | Needs daily attention, support blamed the training content, "$49" plan called poor value | Seen 1 | Results not arriving |
| | | One agent logged in at a time, no logout, no after-hours messaging (2024) | Seen 1 | Setup or theme conflict |

### Shopify Inbox, 4.6 stars (about 5,808 reviews), about 4% one-star

| Positive themes | Frequency | Negative themes | Frequency | Complaint class |
|---|---|---|---|---|
| Accurate, on-brand AI answers that cut repetitive work | Recurring | Inaccurate product information led to a costly order issue, agent disabled, merchant asked for source visibility and controls | Seen 1 | Made-up answers |
| Free and native | Implied by volume | No way to hand the chat to a human (Shopify replied that the agent offers staff) | Seen 1 | Missing handoff or channel |
| | | The agent report shows negative feedback but cannot pinpoint the conversation | Seen 1 | Results not arriving |
| | | September 2026 redesign: too much information at chat start, missing back buttons, contacts near zero | Seen 1 or more | Setup or theme conflict |
| | | Wants email, SMS, and WhatsApp in Inbox | Seen 1 | Missing handoff or channel |
| | | Older: spam (2022 to 2023), no after-hours off switch, size and font limits | Recurring in older reviews | Setup or theme conflict |

### Shopify Search & Discovery, 2.6 stars (about 514 reviews), 21% one-star, down from 4.3 in a 2022-era snapshot

| Positive themes | Frequency | Negative themes | Frequency | Complaint class |
|---|---|---|---|---|
| Free and native (older reviews) | Older snapshot | Search returns "hundreds of unrelated products" (October 2026) | Seen 1 | Wrong or irrelevant products |
| | | Synonyms removed without notice | Seen 1 | Setup or theme conflict |
| | | Availability filter will not stay on, breaking size filtering | Seen 1 | Setup or theme conflict |
| | | Filter caps | Seen 1 | Setup or theme conflict |

### Tidio, 4.8 stars (about 1,350 reviews)

| Positive themes | Frequency | Negative themes | Frequency | Complaint class |
|---|---|---|---|---|
| Easy to set up | Recurring | Lyro limit reached each month while the merchant's count showed less | Seen 1 | Pricing or billing surprise |
| Lyro handles most questions, including fit and specs. One reviewer reports about 90% resolution (`CLAIM`) | Recurring | A plan that needed three other apps to work | Seen 1 | Pricing or billing surprise |
| | | Branding removal costs more than the tool, upsells, arbitrary limits | Seen 2 or more | Pricing or billing surprise |
| | | Slow, email-only support, lost tickets | Seen 2 or more | Support responsiveness |
| | | Widget made checkout hard to click in one theme | Seen 1 | Setup or theme conflict |
| | | Wrong order information. Random information not given to it | Seen 2 | Made-up answers |
| | | Real-time reporting inaccurate | Seen 1 | Results not arriving |

### Rep AI, 4.5 stars (125 reviews), 94% five-star, about 4% one-star

| Positive themes | Frequency | Negative themes | Frequency | Complaint class |
|---|---|---|---|---|
| Quick, easy setup | Seen several | Products would not load (October 2026) | Seen 1 | Setup or theme conflict |
| Responsive account manager | Seen several | No reliable support, no reply during the trial | Seen 1 | Support responsiveness |
| Help setting up an A/B test. "Price is right" (one) | Seen 1 each | Too expensive for a tool that did not work | Seen 1 | Pricing or billing surprise |
| Sales lift and ticket reduction (Step 0) | Recurring, `CLAIM` | Plans expensive without hands-on setup (Step 0) | Seen 1 | Pricing or billing surprise |

### Coverage apps

| App, rating | Positive themes | Negative themes, with class |
|---|---|---|
| Zipchat, 4.8 to 4.9, about 95% five-star | Mostly positive, developer replies | Widget left on the site after removal (setup or theme conflict). Bot did not meet needs (results not arriving). Learning curve to train and tune (setup). Support time zone (support responsiveness) |
| Gorgias, 4.3 (709) | AI agent handling 40 to 50% of tickets (`CLAIM`). Account support in some cases | $780 overcharge and slow refund, a $400 charge during a perceived trial, spam voicemails billed as tickets at $2.20, older tripled prices and billable auto-replies, a cancelled account charged for two months (pricing or billing surprise, 5 or more). Performance collapse after a suspected model change (results not arriving). Incorrect replies, tickets closed unanswered, promises the store could not keep (made-up answers). Slow human support (support responsiveness) |
| Manifest AI, 4.3 (62) with 7 one-star | Support team, ease of setup. Ticket reduction and sales gains (`CLAIM`) | Service denied a week after paying and migrating (pricing or billing surprise). Initial response hurdles (results not arriving) |
| Dialog, 5.0 (38) | Responsive team. **Insight into customer questions.** Instant answers without contacting support. Straightforward setup | None found |
| Wizybot, 4.5 to 4.7 (about 167), Step 0 | Sales from pre-purchase answers, cart recovery, hands-on support | Slow post-sale support. WhatsApp collection link showing only 3 products. Product sync stuck |
| Willdesk, 4.7 (about 380), Step 0 | Support team, mobile app, quick setup | AI fees not disclosed on the listing (pricing or billing surprise). Weak variant handling (wrong or irrelevant products). Random automated reply with the bot disabled (made-up answers) |
| VanChat, 4.9, Step 0 | Less support workload, product-page knowledge, multilingual replies | 1,500-character instruction cap (setup). One unexpected charge (pricing or billing surprise) |

---

## 2. Across the set: complaint classes, ranked

Distinct negative reviews seen, across the 12 apps above and the Step 0 search apps.

| Rank | Complaint class | Reviews seen | Where |
|---|---|---|---|
| 1 | **Pricing or billing surprise** | 16 or more | Gorgias (5+), Tidio (4+), Chatty, Rep AI (2), Manifest AI, Willdesk, VanChat, plus Step 0 search and recommendation apps: Boost price rises, Doofinder request-based cost, Fast Simon bot traffic billing, Wiser share of all sales, Glood widget cost |
| 2 | **Setup or theme conflict** | 12 or more | Search & Discovery (3), Inbox (2+), Chatty, Tidio, Rep AI, Zipchat (2), VanChat, Wizybot sync, Smart Product Filter & Search theme conflicts |
| 3 | **Support responsiveness** | 8 or more | Tidio (2+), Gorgias, Rep AI, Chatty, Zipchat, Wizybot, Smart Product Filter & Search |
| 4 | **Made-up answers** | 7 or more | Gorgias (3), Tidio (2), Inbox, Willdesk |
| 5 | **Results not arriving** | 7 or more | Chatty, Inbox reporting, Tidio reporting, Zipchat, Gorgias, Manifest AI |
| 6 | Missing handoff or channel | 3 or more | Inbox (2), Chaterimo (Step 0) |
| 7 | Wrong or irrelevant products | 2 or more | Search & Discovery, Willdesk variants, Chatty per a first-pass third-party review |
| 8 | Language quality | 0 | None seen. Multilingual replies were praised, not criticized |

## 3. Positive themes, ranked

| Rank | Theme | Where |
|---|---|---|
| 1 | Responsive, hands-on vendor support and setup help | Chatty, Rep AI, Manifest AI, Dialog, Wizybot, Willdesk, Gorgias in some cases |
| 2 | Easy, quick setup | Chatty, Tidio, Rep AI, Manifest AI, Dialog, Willdesk, Luma (about 15 minutes, Step 0) |
| 3 | The AI resolves most questions and cuts tickets | Tidio, Gorgias, VanChat, Rep AI, Inbox |
| 4 | Sales lift (`CLAIM`) | Rep AI, Wizybot, Manifest AI |
| 5 | Insight into what customers ask | Dialog |
| 6 | Multilingual replies | Chatty, VanChat |

---

## 4. The four patterns `RESEARCH-PROMPTS.md` asked Step 2.7 to check

| Pattern to check | Result |
|---|---|
| 1. Catalog accuracy as a strength competitors already hold | **Partly confirmed.** Accuracy is praised (Inbox, Tidio) and also the subject of complaints (Inbox, Tidio, Gorgias, Willdesk). It is not owned by anyone. The opening is narrower than accuracy: **answers a merchant can trace back to the catalog**, which is what the Inbox reviewer asked for ("source visibility") |
| 2. Billing surprise as the loudest complaint | **Confirmed.** It is the commonest class across the set. But Inbox and Search & Discovery are free, so "predictable cost" is a vector Pico can lead only against paid assistants, never against Shopify's free tools |
| 3. Irrelevant recommendations | **Seen, but rarer than expected** (rank 7). Watch it honestly: Pico matches by keywords and synonyms without vector search |
| 4. Results that never arrive, and lift claims merchants doubt | **Confirmed in a specific form:** merchants cannot see what happened inside conversations (Inbox's report, Tidio's reporting). Dialog is praised for the opposite, insight into customer questions. Pico's analytics show what was asked, shown, clicked, and added to cart, which fits this opening, and must stay on the discovery side because Pico cannot claim lift |

## 5. Vector inputs for Step 2.8

- **Vectors 1 and 2, what competitors lead in (from praise):** responsive, hands-on vendor support with easy setup, and support automation that resolves most questions (orders, returns, handoff, channels).
- **Vectors 3 and 4, reversed complaints Pico can lead in:** "Insight into what shoppers ask" (reversed from results that never arrive and reports that cannot pinpoint a conversation) and "Answers traceable to the catalog" (reversed from made-up answers and the request for source visibility). "Predictable cost" is kept as a Phase 9 argument against paid assistants, not a vector, because Shopify's free tools lead it outright.
