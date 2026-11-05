# Do not say

The claim hygiene spine. Check every claim here before it ships. Left column is forbidden or risky, right column is the safe replacement. Never a ban without a replacement.
last_reviewed: 2026-11-04

## Hard bans

| Do not say | Say instead |
|---|---|
| "Increases sales." "Boosts conversion." "Pays for itself." "Drives revenue." Any ROI or lift figure | "See what shoppers asked for, what they clicked, and what they added to cart." Revenue attribution is not measured, and the dashboard says so |
| "Pico never makes things up." "Zero hallucinations." "100% accurate." | "Product cards show names, prices, and stock from your synced catalog." |
| "Live stock." "Real-time inventory." "Checks live stock." | "Stock as of your last catalog sync." Add "updated by webhook on Shopify" only after the inventory webhook ships |
| "Only recommends what is in stock." | "Shows stock on every card, and keeps out-of-stock items out of the cart." |
| "AI-powered semantic search." "Understands what shoppers mean." | "An AI model reads the request, then Pico matches it to your catalog by keywords, synonyms, and price range." |
| "Shoppers can buy right in the chat." "Checkout in chat." | "One tap adds the product to your store's own cart." |
| "Compare products side by side." | "Pico can compare products inside its reply." |
| "Pico remembers your shoppers." | "The conversation survives a page reload on the same device." |
| "Shows you what customers want that you don't sell." | "Shows phrases shoppers asked the assistant that returned no products or few clicks, which points to gaps in the catalog or in how products are described." |
| "Sounds exactly like your brand." | "Set personality, warmth, answer length, emoji use, clarification style, and up to 1,000 characters of tone guidelines." |
| "Fully multilingual." "Speaks every language." | "Replies follow the shopper's language. Widget text is translated for 10 languages." |
| "Works with any store." | "Built for Shopify." Shopware 6 and custom stores belong to a later go-to-market |
| "Installs itself." "No developer needed." "Zero setup." | "Install from the App Store and follow a four-step checklist. Developers can hand the setup to a coding agent with Pico's setup skill." |
| "No impact on speed." | The measured Lighthouse difference on Dawn, as published on the technical one-pager, once measured |
| "Free forever." "Unlimited." | "Free covers 50 conversations a month." |
| "One plan for all your stores." "Built for agencies." | "Each plan connects one store." |
| Any install, store, merchant, review, rating, or conversation count for Pico | Nothing. Pico is pre-launch. Use open proof from `ops/copy-bank.md` |
| Any testimonial, named merchant, logo, or case study | Nothing until the proof log has an entry with exact wording, source, and recorded permission |
| "Your store is losing sales." "Shopify's search is broken." | "Shoppers who can't find a product by browsing can ask for it." |
| "Smarter than Shopify search." Any claim that a Shopify tool lacks something | Do not compare. Describe what Pico does |
| "Cheaper than Chatty." "Unlike other chatbots." Any named comparison | No comparison in copy that customers see without a sourced, dated, page-loaded finding, rechecked before each use |
| "Pay with InstaPay." EGP prices in Shopify copy | Nothing. Shopify installs bill in USD through Shopify Billing |
| "No surprise charges. Pico pauses before it bills you more." before the pause ships | "A quota meter shows usage on the Plan & Usage page." Use the pause line once the quota behavior is SHIPPED |

## Implementer bans

| Do not say | Say instead |
|---|---|
| "Earn recurring revenue." "Guaranteed leads." Any income or traffic number | "Partners earn 25% of each referred store's subscription for 24 months." Merchants who ask for setup help are offered listed partners |
| "Join the Pico Partner Program" before week 6. "Certified partner." "White label." | "Paid usability sessions: we pay you $150 to install Pico on a store you work on and tell us what works and what breaks." |
| "We'll feature your agency in a case study." | "With your client's written permission, we write up what changed on their store and credit your work." |
| Any rate other than 25%, 30%, and 10% managed | The published terms only, quoted exactly |
| A partner invitation, outside link, or email request inside Upwork or Fiverr | Nothing on the platform. Implementers find picofinds.com/partners on their own |

## In video, demos, and screenshots
- Nothing IN BUILD, ROADMAP, or OUT appears on screen as usable. The pause at quota, yearly prices, Scale, and the partner page are labeled "coming soon" until shipped.
- Sandbox data is labeled as sample data on screen. No real store data without recorded permission.
- No caveat gets dropped for pacing. If the stock line needs "as of the last sync", it gets said.

## Claims that need scoping
- **"The only assistant that sticks to your catalog."** Counter-example: Manifest AI, Wantly, Fast Simon, and dozens of App Store listings describe catalog-only answers, and Lyro skips out-of-stock items. Safe form: "Built around your synced catalog."
- **"Only Pico shows unanswered questions."** Counter-example: Shopify Search & Discovery reports search-bar terms with no results and no clicks, and Tidio lists questions Lyro could not answer. Safe form: insight into what shoppers asked the assistant.
- **"The Arabic AI shopping assistant."** Counter-example: Arabic-first Shopify apps exist (Luma, shamz.ai), Salla ships Arabic AI search, Fin and Lyro answer in Arabic. Safe form: "Arabic replies display right to left, with a language switcher and separate merchant copy per language." GCC copy only, later.
- **"No vendor pays implementers before a referral."** Holds for every program found on 2026-11-03, internally. In copy, describe Pico's offer, never the others'.
- **"A sandbox no competitor offers."** Holds for the slates checked on 2026-11-03. Internal only, and recheck before any use.

## Historical and reputational material
- picofinds.com led with Shopware, Arabic, and Egypt, and carried three lines broader than the product supports. The replacements above are the fix. Handle it, do not repeat the old lines.
- The listing name is "Pico AI Shopping Assistant" because "Piko ‑ Pickup Reminder" exists. Never shorten it on the listing.
