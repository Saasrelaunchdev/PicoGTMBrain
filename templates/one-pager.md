# Template, one-pager

Three variants share this shape: the technical one-pager (developers, both audiences' technical readers), the merchant decision summary (Level 2 decision makers), and the client-facing findings one-pager (implementers hand it to their client).

## Technical one-pager
1. **What it is,** one sentence.
2. **Install path.** Shopify OAuth, webhooks, encrypted tokens, the Pico Assistant theme app embed, the four-step checklist.
3. **Uninstall.** What happens to app embed blocks, per Shopify's documentation.
4. **Speed.** The measured Lighthouse difference on Dawn, against a 10-point budget. Leave the section out until measured.
5. **Themes.** Claimed through the theme app embed. Tested on Dawn and Horizon. Headless not claimed.
6. **Setup skill.** What it covers, which coding agents follow it, where to download it.
7. **Roles and access.** Owner, admin, analyst, support.

## Merchant decision summary
What it does, what it costs with units, how the trial will be judged with Pico's own metrics, and the breakeven arithmetic with the merchant's margin left blank.

## Client findings one-pager
The phrases the store's shoppers asked that found nothing, the suggested fixes, setup time, and what Pico does and does not do. Written so the implementer can sign it.

Guardrails: shipped capabilities only, no "no impact" speed claim, `rules/do-not-say.md`, `ops/QA-checklist.md` before sharing.
