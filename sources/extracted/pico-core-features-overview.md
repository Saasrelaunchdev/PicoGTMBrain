# Source: Pico Core Features Overview

Text transcription of `2026-11-02-pico-core-features-overview.pdf`, the product document dated 2026-11-02. It is the only source this pack was built from. Wording is kept as written so that every narrowed claim in `../GTM-BRIEF.md` can be traced back to it. Layout is converted to Markdown and the author line is left out.

---

## Product overview

Pico is an AI shopping assistant that lets shoppers describe what they want in plain language and returns real products from the merchant's own catalog. It runs as a chat widget on the storefront and is managed from a merchant dashboard.

- **Platforms:** Shopify and Shopware 6, plus any custom store that implements Pico's HTTP catalog API.
- **Buyers:** e-commerce merchants, and the agencies or developers who set up their stores.
- **Core promise:** recommendations come only from synced catalog data. Pico does not invent prices, stock, or capabilities.
- **Plans:** monthly or yearly, priced by conversation quota. Free covers 50 conversations a month, Growth 600 ($49), Pro 2,000 ($99). New accounts get a 14 day Growth trial with no card, then drop to Free. Each plan connects one store.

## Shopper features (storefront widget)

A shopper opens a floating chat on the store, asks for a product in their own words, and gets product cards with price and stock plus a one tap add to cart.

- **Natural language search:** requests like "waterproof hiking boots under 150 euro" are interpreted by an AI model, then matched against the synced catalog using keywords, synonyms, and minimum or maximum price filters.
- **Product cards:** image, name, price, in stock or out of stock label, and a View link to the product page. Recommendation count per reply is set by the merchant.
- **Add to cart from the card:** uses the store's own cart on Shopify and Shopware. The button only appears when the connected platform supports it, and out of stock items cannot be added. The widget picks an in stock variant automatically.
- **Clarifying questions:** when a request is too vague, the assistant asks one follow up question before recommending.
- **Suggested replies:** tappable chips on the opening screen and after each answer.
- **Product comparison in chat:** the assistant can compare products inside its reply. There is no separate comparison screen in the widget yet.
- **Multilingual:** replies follow the shopper's language, a language switcher appears when the merchant enables several, and Arabic displays right to left. Product card and input text is translated for English, Arabic, German, Greek, Spanish, French, Italian, Dutch, Portuguese, and Turkish.
- **Personalized welcome:** the opening message adapts to the assistant's personality, or shows the merchant's custom text.
- **Session memory:** the conversation survives a page reload on the same device.

## Merchant dashboard features

The dashboard has seven pages. Merchants connect a store, control how the assistant speaks, and see how shoppers use it.

| Page | What the merchant can do |
|---|---|
| Overview | See conversations, product click through rate, and add to cart rate for the last 30 days, each compared with the prior 30 days. Check integration and catalog sync health. Revenue attribution is shown as unavailable because it is not measured yet. |
| Analytics | Product discovery funnel with step to step conversion. Charts for searches, product result rate, zero result rate, and product clicks over time. Top search phrases. Zero result and weak click phrases, which show what shoppers asked for that the catalog could not answer. Product level impressions and clicks. |
| Catalog | Sync the catalog on demand, retry failed sync jobs, and read the sync log. See product and variant counts, last successful sync, and a searchable product list with availability. |
| Integrations | Connect Shopify through OAuth, Shopware 6 with Admin API keys, or a custom store with a catalog API and token. Create a sandbox store. Test the connection. Follow the Shopify checklist: authorize, enable the theme embed, sync, and confirm the widget was seen. |
| Assistant | Set display name, subtitle, greeting, and suggestion chips, with separate copy per language. Choose enabled languages and a default. Tune personality (professional, friendly, expert, playful), warmth from 1 to 5, response length, emoji use, clarification style, and recommendations per reply. Add a custom welcome message, brand tone guidelines up to 1,000 characters, and a custom add to cart confirmation. Preview before saving. |
| Plan & Usage | See the plan and the conversation quota meter. Upgrade through Paddle, or pay by InstaPay in Egypt. Cancel with a reason, with an optional 50 percent retention offer for two billing periods. |
| Settings | View account and organization details. |

Also included: email verification, password reset, role based access (owner, admin, analyst, support), and an in dashboard feedback widget.

## Integrations and platform support

Pico connects to Shopify and Shopware 6 today, and to any other stack through an HTTP catalog API.

| Platform | How it connects | Storefront install | Billing |
|---|---|---|---|
| Shopify | OAuth app install, catalog sync, and webhooks. Tokens are stored encrypted. | Theme app embed called Pico Assistant, which takes the public widget ID. | Shopify Billing for App Store installs |
| Shopware 6 | Admin API access keys, with an optional sales channel key. No custom plugin. Syncs parent products, variants, prices, stock, media, and categories. | Widget script added to the storefront. | Paddle, or InstaPay in Egypt |
| Custom store | Any stack that implements the Pico HTTP catalog API, authenticated with an API token. | Widget script added to the storefront. | Paddle, or InstaPay in Egypt |
| Sandbox | Sample outdoor gear catalog running on the real Pico API, for trying the shopper flow before connecting a store. | Included demo widget. | No plan needed |

Setup can also be done by a coding agent. Pico offers a downloadable skill for Shopify, Shopware 6, and custom apps that Cursor, Claude Code, Codex, and Antigravity can follow, including the dashboard steps.

## Possible differentiators and current limits

These are the points the code supports, listed so they can be tested against competitors. Whether other vendors do the same is for the analysis to judge.

### Possible differentiators

- **Arabic and multilingual shopping:** replies in the shopper's language, right to left layout, a language switcher, and separate merchant copy for each language.
- **Catalog grounded answers:** recommendations come from synced products, prices, and live stock. Add to cart appears only when the platform supports it.
- **Merchant controlled voice:** personality, warmth, answer length, emoji use, clarification style, and brand tone guidelines.
- **Unanswered question insight:** analytics list zero result and weak click phrases, so merchants see what their catalog cannot answer.
- **Shopware without a plugin:** connects through the Admin API and Store API.
- **Agent assisted setup:** downloadable skills let a coding agent install Pico.
- **Local payment for Egypt:** EGP pricing paid by InstaPay, alongside Paddle and Shopify Billing elsewhere.
- **Low risk start:** a free tier, a 14 day Growth trial with no card, and a sandbox.

### Current limits

- Revenue attribution is not measured. Analytics cover discovery, clicks, and add to cart actions.
- Search matches keywords and synonyms with price filters. An AI model reads the question, but there is no semantic vector search.
- Each plan connects one store.
- Product comparison happens inside chat replies only, with no comparison screen.

---

## What the source does not carry

Recorded so that nobody infers these from silence. Each is either an open decision in `../GTM-BRIEF.md` or a `{TBD}`.

- No website URL and no Shopify App Store listing URL.
- No customers, installs, active stores, conversation volumes, reviews, ratings, testimonials, or named merchants.
- No revenue, conversion, or average order value figure of any kind.
- No competitors named.
- No team, burn, runway, or channel history.
- No target geography, although EGP pricing, InstaPay, and Arabic right to left support point at Egypt and the wider Arabic-speaking market.
- No partner, referral, affiliate, or agency program, and no multi-store or agency plan.
- No statement on human handoff, live chat, order status, returns, or policy answers.
- No statement on messaging channels beyond the storefront widget.
- No statement on which Shopify themes, headless storefronts, or Shopware versions are supported.
- No definition of what counts as one conversation against the quota.
- No yearly prices and no EGP prices.

**One internal disagreement, kept visible.** The platform table says Shopware 6 connects through Admin API access keys "with an optional sales channel key." The differentiators list says it "connects through the Admin API and Store API." These are probably the same thing described two ways, since a sales channel access key is what the Store API uses, but it is a status question for the founder, not something to resolve silently.
