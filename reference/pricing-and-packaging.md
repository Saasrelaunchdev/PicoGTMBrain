# Pricing and packaging, merchants

Load for plan questions, pricing pages, upgrade prompts, and ROI conversations. Distills the merchant Pricing and Packaging dashboard and D21 to D29. Status of each element is in `rules/feature-status.md`. ROI inputs about Pico's effect are always left blank for the merchant.

## The value metric
Per conversation, which holds. It matches what Pico does and measures, matches the unit Chatty and Tidio Lyro use, and the merchant can watch it on the quota meter. Secondary metric: stores per plan, one store each.

A conversation is a chat thread that gets at least one AI reply. Messages from the same shopper on the same device within 24 hours belong to the same conversation. Fair use: up to 50 AI replies per conversation.

Rejected denominators: per visitor (charges for traffic that never asks), per resolution and commission (need outcome measurement Pico lacks and would invite banned claims), per AI reply (the shopper controls the length), per seat (value lives in shopper conversations).

## The tiers

| Plan | Monthly | Yearly | Conversations | Position | Month 6 target share |
|---|---|---|---|---|---|
| Free | $0 | | 50 | Entry, where every trial lands | 60% of active installs |
| Growth | $49 | $490 (IN BUILD) | 600 | Hero | 70% of paying stores |
| Pro | $99 | $990 (IN BUILD) | 2,000 | Hero+ | 22% |
| Scale (IN BUILD) | $299 | $2,990 | 6,000, plus a 30-minute onboarding call | Anchor | 8% |
| Custom | About $0.05 a conversation | | By request | Off the plan page | |

14 day Growth trial with no card. Every feature on every plan. One store per plan. Charges in USD through Shopify Billing for App Store installs. Founding cohort: 50% off any paid plan for 6 billing periods.

## At the quota (IN BUILD)
Alerts at 80% and 100% in the dashboard and by email. Open conversations finish. Paid plans get a 10% grace allowance at no charge, then the launcher pauses until the next cycle or an upgrade, which applies at once. No overage charge, ever.

## Findings that shape copy
- Growth to Pro is 2.0 times the price for 3.3 times the conversations, a clear upgrade past 600.
- Pico's price per conversation sits below every per-conversation vendor sampled. Internal input only.
- Shopify's revenue share is 0% on the first $1M of lifetime app revenue, so net price equals list price until then.
- At the $0.02 model cost ceiling, gross margin before other costs is 76% on Growth and 60% on Pro and Scale. Free costs about $1 a month per store in model use.

## Expansion levers
Conversation quota (prompted at 80%), stores (one plan each), billing period (yearly, two months free). Capability by tier: none, by design.

## ROI anchors, always completed by the merchant
- **Cost of the problem:** monthly searches with no results × the share who would have bought × average order margin, all the merchant's own numbers. Plus hours a week answering questions by hand × the cost of an hour (US customer service median $21.53, BLS, May 2025).
- **Alternatives, not like for like:** Growth equals about 2.3 hours of a US service rep. The free Inbox agent costs nothing, so the case rests on what the merchant learns, not on price.
- **Breakeven:** extra orders a month equal to the plan price divided by the merchant's average order margin. Example input only: at a $30 margin, Growth needs 2 orders a month.

Never state a typical customer value, a payback period, or a multiple for Pico. A formula with a blank is honest. A filled-in example is an income claim.

## Calculator
Inputs: average order margin, searches with no results a month, share who would buy, hours a week, cost of an hour. Outputs: breakeven orders per plan, years of Growth covered by one order, margin at stake, cost of answering by hand. The workbook lives in the build repo's Google folder.
