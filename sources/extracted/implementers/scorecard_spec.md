<!-- build: docx -->
# Run 2, Scorecard spec for ScoreApp: Agency AI Shopping Readiness Scorecard

The implementation brief for the scorecard in `lead_magnet_spec.xlsx`. Built on 2026-11-03. Check each element against ScoreApp's current builder at setup, since this run could not load ScoreApp's pages.

## 1. Landing page

**Headline:** When a client asks for AI shopping help, how ready is your answer?

**Subhead:** Seven questions for Shopify developers and agencies, a score from 0 to 100, and three next steps.

**Three bullets:**

- See where your current answer leaves gaps: setup, theme risk, and what you can show the client.
- Get three next steps matched to your score.
- Get the Client Store Findability Audit template to run with your next client.

**CTA button:** Get my readiness score

**Footer line:** Your score is your own assessment, based on your answers.

## 2. Questions

Seven questions, one per screen, in the order and with the options and points in the Questions sheet. Question 3 names Shopify's free Inbox agent neutrally, as one answer among others.

## 3. Results pages

### 0 to 39: Ready for now

1. Keep a note of the requests clients make about AI shopping help.
2. Bookmark the Pico sandbox store for the next client who asks.
3. Use the Client Store Findability Audit template on one client store.

### 40 to 69: Clients are asking ahead of your stack

1. Try the shopper flow in the Pico sandbox store.
2. Download the setup skill and point your coding agent at a store you work on.
3. Run the audit template with phrases from one client's customers.

### 70 to 100: A fit for a paid session

1. Apply for a paid usability session. We pay $150 to install Pico on a store you work on and tell us what works and what breaks.
2. Ask your client for permission first, with the one-page permission template.
3. Ask about a case study that credits your work, with your client's written permission.

## 4. Email sequence

Plain text, one CTA each, sent from a named person. Bodies are drafts, 60 words or fewer.

**Email 1, day 0. Subject: Your readiness score: [score]**
Your score is [score], in the tier "[tier]". It is based on your answers. Your three next steps are below, and the Client Store Findability Audit template is attached. It works best with phrases from one client's customer emails and chats.

**Email 2, day 2. Subject: What a zero result phrase tells your client**
A phrase that returns no products can mean a missing product, or a product described in words shoppers don't use. Both are fixes you can propose. Here is a worked example on our sandbox store's sample outdoor gear catalog. Try your client's phrases there.

**Email 3, day 5. Subject: Paid to test it on a store you work on**
We pay $150 for a usability session: install Pico on a store you work on, run the Shopper Words Test, and report what works and breaks. If we met on Upwork or Fiverr, payment stays on that platform. Reply to apply.

**Email 4, day 8. Subject: Last note on paid sessions**
Session participants get a case study offer, with their client's permission, and an invitation to the partner program: 25% of each referred store's subscription for 24 months. The first cohort is 30 sessions. Reply to apply, or read the terms at picofinds.com/partners.

## 5. Setup and compliance

| Item | Specification |
|---|---|
| Tags | Tag each lead by tier and by answers to questions 1, 3, and 5, so email 3 can be tailored |
| Routing | 70 to 100 tier leads go to the founder for a paid session |
| Tracking | Source and campaign parameters on every link: cold email, LinkedIn, or the partner page |
| Email rules | Every email carries a working unsubscribe link and a postal address, per CAN-SPAM. Scorecard emails go only to people who opted in on the form, with consent recorded, which is what UK PECR and EU rules require for individuals. Cold email stays US-only in the first 90 days (D48) |
| Platforms | The scorecard is never linked from inside Upwork or Fiverr messages |
| Claims | Every line follows `GTM-BRIEF.md` Section 5. No income, lead, or traffic figure. No competitor criticized |
| Secondary market, for later | A version for Gulf agencies is not built now |
