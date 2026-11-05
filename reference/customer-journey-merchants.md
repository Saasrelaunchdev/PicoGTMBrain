# Customer journey, merchants

Load to match copy to a funnel stage, plan lifecycle emails, or diagnose activation. Distills the merchant Customer Journey Funnel (2026-11-03). Targets live in `innovation/metrics.json`. Quotes are illustrative personas, not real merchants.

| Stage | Mindset and trigger | Touch-points | KPIs and targets (90 days after the listing is live) | Owner |
|---|---|---|---|---|
| 1. Problem awareness | "Shoppers keep emailing to ask which one fits." Repeat questions, a new line, peak prep | Shopper Words Test, Findability Scorecard, catalog guides, answers in AI assistants | Scorecard completions that open the sandbox: 25% | Marketing |
| 2. Solution discovery | "Dozens of AI chat apps. Which help shoppers choose?" A Shopify announcement, a roundup | App Store listing, comparison pages with sourced and dated facts, sandbox link | Listing visit to install: 3% | Marketing |
| 3. Vendor evaluation | "Will it say something wrong, break my theme, surprise me with a bill?" | Sandbox, plan page with every quota, the "what Pico does not do" list, technical one-pager | Sandbox visit to install: 10% | Product |
| 4. Trial | "Let me see it on my own store before I pay." The install | Four-step checklist, trial emails, in-dashboard prompts, setup skill | Widget seen within 24 hours: 65%. Median install to widget seen: under 20 minutes. Trial to paid by day 30: 15% of installs | Product and CS |
| 5. Value realization | "Shoppers are using it. What are they asking?" First week of conversations | Analytics, Overview, first insight and weekly summary emails (week 4), proof capture point (week 6) | Catalog fixes from the report: 3 per founding store in 60 days | CS |
| 6. Expansion and advocacy | "We hit the quota. Is Pro worth it?" The meter, a good month | Upgrade prompt, review request after a fix, case study invitation, referral to implementer partners | 10 unincentivized reviews by day 90. 20 founding stores by day 60 | CS and marketing |
| 7. Renewal | "Is this still worth it this month?" Each charge, a theme change | Monthly usage summary (week 8), embed check after theme changes, cancel flow with reason and retention offer | Monthly uninstall rate under 15%. Embed still active after a theme change: 90% | CS and product |

## Stage 4, the activation sub-funnel

| Step | What happens | Drop-off question | Target |
|---|---|---|---|
| 1. Install | Added from the App Store | Left at the permissions screen? | |
| 2. Authorize | OAuth, tokens stored encrypted | Did the installer have rights? | 95% of installs |
| 3. Enable the embed | Pico Assistant switched on in the theme editor. Embeds are off by default and live only on the theme where enabled | On, and on the live theme? | 70% within 24 hours |
| 4. Sync | Catalog sync with counts and log | Did any job fail? | 90% within 24 hours |
| 5. Widget seen | The checklist confirms a visitor saw it | Has anyone seen it yet? | 65% within 24 hours, median under 20 minutes |
| 6. First conversation | A shopper asks something | Are shoppers opening it? | 50% within 7 days |
| 7. Plan and quota | Trial ends, Free or a paid plan through Shopify Billing | Will the quota run out mid-month? | 15% on a paid plan by day 30 |

Interventions: a setup email with the checklist, an in-dashboard prompt linking to the theme editor, retry from the Catalog page, the sync failure email (week 2), an upgrade prompt at 80% of quota. At 100%, open conversations finish, paid plans get 10% grace, then the launcher pauses (IN BUILD). Never an overage charge.

## Key insights
- **Critical success factors:** the embed on, on the live theme, after every theme change. The first value moment inside the trial: the merchant opens the zero result phrases and recognizes a fix. The quota and the conversation definition clear before the first charge. A listing that earns installs before any review exists.
- **Blockers:** the embed left off. Free's 50 conversations running out mid-month. Paying by card in USD through Shopify Billing. The free Inbox agent as the default comparison while Pico has no reviews.
- **Accelerators:** start from the merchant's own words, the Words Test and the Scorecard into the sandbox. Implementers install for client stores. A proof capture point at the first fall in a store's zero result rate. An embed check after every theme change.
