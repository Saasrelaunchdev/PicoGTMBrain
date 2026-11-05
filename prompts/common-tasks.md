# Prompt library, common Pico GTM tasks

Filled, runnable prompts for recurring jobs. Each assumes the agent has loaded the router (`CLAUDE.md` or `AGENTS.md`). Tools without file access: paste `adapters/portable-control-layer.md` first. Tools with a shell: `python3 tools/brain.py context <task> --audience <a> --format cat` prints the exact load set.

There is no paid ads, cold outbound to store owners, LinkedIn automation, or GCC work in this GTM, so there are no prompts for them. Asked for one, refuse and offer the in-scope channel.

## Merchants

**App Store listing.** "Load `templates/app-store-listing.md`, `reference/app-store-engine.md`, `reference/value-proposition-merchants.md`, and `examples/app-store-listing.md`. Draft or update the Pico AI Shopping Assistant listing, field by field. Shipped capabilities only, per `rules/feature-status.md`. Then run `ops/QA-checklist.md` and list every capability mentioned with its status flag."

**Catalog guide.** "Using `templates/seo-article.md` and `reference/app-store-engine.md`, write a catalog guide for [category] merchants: how shoppers describe [products], and how to name products so they are found. Sample phrases labeled as examples. No industry statistics. End with the Shopper Words Test and the sandbox CTA. QA before returning."

**Comparison page.** "Draft a 'when Pico fits and when it doesn't' page against [option], using `templates/seo-article.md`. Every fact about [option] must be sourced and dated from `reference/competitive-analysis-merchants.md`. Mark any fact older than 30 days for a page-loaded recheck. No disparagement. QA before returning."

**Lifecycle email.** "Write the [email] from `templates/lifecycle-email.md` for a merchant in stage [n], matching `examples/first-insight-email.md`. Only data Pico measures. If its trigger is IN BUILD, say so at the top. QA before returning."

**Review reply.** "Reply to this App Store review using `templates/review-reply.md`: [paste review]. Then give me the signal-log entry and the `review.received` event to add."

## Implementers

**Cold email.** "Using `templates/cold-email.md`, `reference/outreach-engine.md`, and `examples/cold-email-paid-session.md`, write a first email to a [freelancer / agency] who [context]. Under 120 words, CAN-SPAM footer, no partner terms. QA before returning."

**LinkedIn.** "Write a connection note and first message for a [role] at a [segment], from `templates/linkedin-message.md`. Sent by hand. QA before returning."

**Upwork or Fiverr.** "Write the [Upwork job post / Fiverr brief] for the Paid Usability Session from `templates/marketplace-job-post.md`, matching `examples/upwork-job-post.md`. Nothing about the partner program. QA before returning."

**Partner invitation, from week 6.** "Write the partnership invitation for a session participant met by [email / LinkedIn], quoting the terms from `reference/partner-program.md` exactly. Refuse if they were met on Upwork or Fiverr."

## Sales, partners, and strategy

**Call prep.** "Prepare me for a call with a [persona] at a [segment]. Load the matching `reference/icp-personas-*.md`, `reference/objection-handling.md`, and `reference/competitor-battlecards.md`. Give the three objections they will raise and the honest answers."

**Objection.** "Draft a response to '[objection]' for [audience], grounded in `reference/objection-handling.md`. Say not yet where the answer is not yet."

**Strategy question.** "Answer from `context/Pico_GTM_Master_Context.md` and `ops/decisions.md` only: [question]. Cite the decision IDs. If the brain does not settle it, say so and propose an open item."

**Investor or advisor update.** "Write a monthly update from `innovation/LEDGER.md`, `reference/launch-plan.md`, and the newest file in `snapshots/`. Internal numbers are allowed here. No claim that is not in an event."

## The compounding loop

**Log a signal.** "Log this in `ops/signal-log.md`: [paste note]. Keep the verbatim. Classify the type, assign a disposition with the thresholds in that file, add tags, and if it is a PATCH or AMEND, list exactly which files change. Then run `python3 tools/brain.py signal` with the same fields."

**Log an activity.** "Record this as an event: [what happened]. Pick the type from `reference/innovation-accounting.md`, fill `data` and `refs`, and run `python3 tools/brain.py event`."

**Weekly review.** "Run the Monday loop: `python3 tools/brain.py tripwires`, triage new signals, update WATCH counters, then `python3 tools/brain.py ledger`. Report what changed and what did not."

**Snapshot.** "Run `python3 tools/brain.py snapshot [label]`, then fill every section from [data]. Diff section 6 against `rules/feature-status.md` and finish with what this changes, including 'no ledger change this period' if that is the honest answer."

**Amend.** "This changed: [fact]. Follow the AMEND procedure: the `rules/` ledger first, then the master context with a version bump, then a dated `ops/decisions.md` entry with what it does not change, then grep and fix the copy bank, then `python3 tools/brain.py build`."

**Audit.** "Run `python3 tools/brain.py audit`, then produce one real asset using only the brain and QA it. Report anything the brain could not supply."
