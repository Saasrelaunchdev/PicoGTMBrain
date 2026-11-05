# Template, merchant lifecycle email

Audience: merchants. Stages 4 to 7. Product-led lifecycle in `reference/app-store-engine.md`. Voice reference: `examples/first-insight-email.md`.

## The sequence and what each email does

| Email | Trigger | Job | Status |
|---|---|---|---|
| Setup | Install | The four-step checklist, with a link to the theme editor | SHIPPED as a flow, copy to write |
| Sync failure | A failed sync job | Retry from the Catalog page | IN BUILD, week 2 |
| First insight | End of the first week of conversations | Top phrases, phrases that found nothing, one suggested fix | IN BUILD, week 4 |
| Weekly summary | Weekly | What changed, with sync health | IN BUILD, week 4 |
| Trial ending | 3 days before the 14 day trial ends | What moves to Free, the quota meter, the upgrade | Copy to write |
| Quota alert | 80% and 100% of quota | What happens next, the upgrade | IN BUILD |
| Monthly usage | Monthly | Conversations, clicks, add to cart, against the prior month | IN BUILD, week 8 |
| Review request | After Analytics opened and one fix made | Ask once, no incentive | Copy to write |

## Shape of one email
1. **Subject.** Concrete and specific to their store: "3 phrases your shoppers asked this week found nothing".
2. **First line.** The number or phrase from their own Analytics page.
3. **Body.** Two to four short paragraphs. Only data Pico measures.
4. **One suggested action,** named page and step.
5. **One call to action.**
6. **Footer.** Sent from a named person, an unsubscribe link, the postal address.

## Rules
- Only data Pico measures: conversations, results, clicks, add to cart, zero result and weak click phrases. No sales figure.
- No pressure tactics, no false urgency. The trial end date is real, so state it plainly.
- An email for an IN BUILD trigger ships only when the trigger ships.

Guardrails: merchants only, the merchant's own data, `rules/feature-status.md` for every trigger, `ops/QA-checklist.md` before sending.
