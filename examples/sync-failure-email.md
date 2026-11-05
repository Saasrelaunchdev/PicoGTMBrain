# Example, sync failure email (merchants, stage 4)

Status: proposed gold standard, written on 2026-11-05 as the brain's live test from the `lifecycle-email` load set only. The email ships when its trigger ships (IN BUILD, week 2). Values in brackets are filled at send time. Founder approval pending.

---

**From:** [named person] at Pico
**Subject:** The catalog sync on [store name] didn't finish

Hi [first name],

Pico's catalog sync on [store name] stopped before it finished on [date and time]. Products, prices, and stock that changed since your last completed sync may not show in Pico's product cards until a sync finishes.

Open the Catalog page and retry the sync. The sync log on the same page lists each sync job with its counts, so you can see when the retry is done.

[Open the Catalog page]

[Named person]
Pico, picofinds.com

You're receiving this because you installed Pico. [Unsubscribe]. [US postal address]

---

## Why this works
- The subject names the store and what happened, so the merchant knows before opening it.
- It says what a failed sync can mean for shoppers without claiming live stock, because cards come from the synced catalog.
- One action on one named page. Retry and the sync log are SHIPPED on the Catalog page.

## What the brain could not supply
Logged as a RISK signal on 2026-11-05 and routed to the engineer before the trigger ships:
- What shoppers see while a sync has failed or only partly finished.
- Whether the sync log shows the cause of a failure.
- The support path after a retry fails. A second call to action would break the one-CTA rule, so the email leaves it out until a route is decided.
