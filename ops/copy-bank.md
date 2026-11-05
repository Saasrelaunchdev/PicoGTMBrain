# Copy bank, approved language

Pre-approved lines, safe to reuse verbatim. Every line has passed `rules/do-not-say.md`. Lines tagged `[IN BUILD]` may ship only once the capability is SHIPPED in `rules/feature-status.md`. Rewriting an approved line turns a checked claim into an unchecked one.

When a decision changes a claim, grep this file for the old phrasing first.

## One-line positioning
- Merchants: "Pico shows merchants what their shoppers ask for, and answers shoppers with products drawn from the store's own synced catalog."
- Merchants, listing headline: "An AI shopping assistant for Shopify that answers from your own catalog."
- Merchants, short: "Pico finds it in your catalog."
- Implementers: "Pico pays implementers for a first session on a store they work on, and, with the client's permission, credits their work in the case study that follows."
- Implementers, short: "Paid to test it. Credited when it works."

## Reframes
- "Not another AI chatbot that tries to answer everything, a shopping assistant built around your synced catalog that shows you what shoppers asked for."
- "Not a smarter search bar, a conversation for shoppers who don't know a product's name."
- "Not one more app to manage, a low-risk way to see what your shoppers are asking for."
- "Not another affiliate program that pays after the referral, a paid session that starts before any referral exists."
- "Not a build you have to maintain, an app you set up in four steps or hand to your coding agent."
- "Pico answers product questions. Keep your help desk for orders and people."

## Hooks
- "Let shoppers describe what they need."
- "See the requests that found nothing."
- "Try it before you install anything."
- "We pay you $150 to install Pico on a store you work on and tell us what works and what breaks."
- "Show clients what their shoppers couldn't find."

## Merchant headlines
- "For shoppers who don't know the product's name."
- "Every card comes from your synced catalog."
- "From question to cart in one tap."
- "See where requests stop between question and cart."
- "Find out what shoppers looked for and missed."
- "Your last 30 days against the 30 before."
- "Start free with 50 conversations a month."
- "Four steps from install to live widget."
- "No theme code to edit."
- `[IN BUILD]` "No surprise charges. Pico pauses before it bills you more."

## Implementer headlines
- "Install without editing theme code."
- "Hand setup to your coding agent."
- "Test it before any client store."
- "Bring your client their shoppers' own words."
- "Give each person the access they need."
- "A month-on-month view for your client report."
- "Paid to test Pico on a store you work on."
- "A case study that credits your work."
- `[IN BUILD, week 6]` "25% of each referred store's subscription, for 24 months."

## Proof points (customer proof, the closed set)
None on 2026-11-04. The proof log is empty and closed. Anything that reads as a customer result is fabrication.

## Open proof (checkable now, use as-is)
- "Open the sandbox before you install anything." The Sandbox link in picofinds.com's top menu runs a sample outdoor gear catalog on Pico's real API.
- "Ask the sandbox in your own words, then check what it matched."
- "Open any card and check it against the catalog." Every sandbox card has a View link.
- "Give the sandbox a vague request and see what it asks."
- "Read the setup skill before your agent runs it."
- "Read Shopify's own docs on app embeds before you install."
- `[IN BUILD]` "The plan page states each plan's quota and what counts as one conversation."

## Calls to action
One per asset, never stacked.
- Merchants, before the listing is live: "Connect your store". After: "Install free from the Shopify App Store".
- Merchants, evaluation: "Open the sandbox store". Lead magnet: "Get my Findability Score".
- Implementers: "Apply for a paid session". "Download the setup skill". "Read the technical one-pager". `[IN BUILD, week 6]` "Read the terms on Pico's partner page".

## Customer language (verbatim, promoted from the signal log)
None yet. Real phrasing from merchants and implementers lands here only after it appears in `ops/signal-log.md` and passes triage.
