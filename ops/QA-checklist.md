# QA checklist, run before shipping any output

Go through every item against the draft. Each one is answerable yes or no by looking at the draft. If any item fails, fix the draft, then run the list again. Machine pass first: `python3 tools/brain.py lint <file>`.

## Writing
- [ ] No em dashes anywhere.
- [ ] None of the banned words: leverage, unlock, seamless, robust, streamline, cutting-edge, empower, or a variant.
- [ ] Paragraphs of one to three sentences. Numbers and named pages instead of adjectives.
- [ ] Every price carries its unit, for example "$49 a month for 600 conversations".

## Channel
- [ ] The asset is for an in-scope channel: App Store, content and search, product-led lifecycle, cold email to US implementers, hand-sent LinkedIn, Upwork or Fiverr job posts.
- [ ] Not paid ads, not cold outbound to store owners, not GCC or Arabic-market, not LinkedIn automation, not cold email to UK sole traders or the EU. If it is, stop and redirect.
- [ ] On Upwork or Fiverr: no partner pitch, no outside link, no email request.
- [ ] Cold email: sender identity, an advertisement notice, the US postal address, and a working opt-out.

## Claims
- [ ] No revenue, sales, conversion, ROI, or lift claim about Pico or a client.
- [ ] No install, review, rating, or merchant count, and no testimonial or named merchant.
- [ ] Every capability mentioned is SHIPPED in `rules/feature-status.md`, or carries "coming soon" in the same sentence.
- [ ] The quota pause line appears only if the pause behavior is SHIPPED.
- [ ] Stock is "as of your last catalog sync", never live.
- [ ] Every "only", "first", "best", "never", and "no other" is cleared by `rules/do-not-say.md`.
- [ ] Every proof slot uses open proof that names what to check and where, and none reads as a customer result.
- [ ] No named competitor comparison, and nothing about what a Shopify tool lacks.
- [ ] Partner terms, if any, quoted exactly: 25% for 24 months, 30% for lead partners, 10% managed share.

## Naming and strategy
- [ ] Vocabulary matches `rules/glossary.md`: Pico, Pico AI Shopping Assistant, conversation, synced catalog, zero result phrases.
- [ ] Nothing contradicts a decided verdict in `ops/decisions.md`: USA first, GCC later, no overage, every feature on every plan, open proof.

## Audience and stage
- [ ] One audience only, merchants or implementers, never both.
- [ ] Copy matches the funnel stage in `reference/customer-journey-merchants.md` or `reference/customer-journey-implementers.md`.
- [ ] Exactly one call to action.

## Video and demos
- [ ] Read aloud without stumbling.
- [ ] Nothing IN BUILD, ROADMAP, or OUT shown as usable, and sandbox data labeled as sample data.

## Voice
- [ ] Reads like the matching file in `examples/`.

## After shipping
- [ ] Asset filed in `pages/` or listed in `ops/asset-index.md`.
- [ ] Anything the work taught you logged in `ops/signal-log.md`, and an `asset.shipped` event added with `python3 tools/brain.py event asset.shipped`.
