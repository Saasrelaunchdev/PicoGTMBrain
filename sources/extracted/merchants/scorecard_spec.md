<!-- build: docx -->
# Run 1, Scorecard spec for ScoreApp: Shopify Store Findability Scorecard

The implementation brief for the scorecard in `lead_magnet_spec.xlsx`. Built on 2026-11-03. Check each element against ScoreApp's current builder at setup, since this run could not load ScoreApp's pages.

## 1. Landing page

**Headline:** How easily can shoppers find your products in their own words?

**Subhead:** Seven questions, a score from 0 to 100, and three fixes you can make this week.

**Three bullets:**

- See where shoppers who describe a product may miss it.
- Get three fixes matched to your score.
- Get the Shopper Words Test worksheet to check ten real phrases against your catalog.

**CTA button:** Get my Findability Score

**Footer line:** Your score is your own assessment, based on your answers. It is not a measurement of your store.

## 2. Questions

Seven questions, one per screen, in the order and with the answer options and points in the Questions sheet. Question 4 names Shopify's report exactly as it appears in the admin, "Searches with no results", so the merchant can find it.

## 3. Results pages

Each tier page shows the score, the tier name, the message from the Results sheet, and three fixes.

### 0 to 39: Shoppers can find their way

1. Open "Searches with no results" in Shopify's search analytics once a month and act on the top terms.
2. Add the words customers use in emails to product titles and descriptions.
3. Run the Shopper Words Test on ten phrases each season.

### 40 to 69: Some shoppers may be getting lost

1. Run the Shopper Words Test on ten phrases from customer emails and chats.
2. Rewrite titles for the products that missed, using the shoppers' words.
3. Try the same phrases in the Pico sandbox store to see how a conversation handles them.

### 70 to 100: Shoppers ask in words your catalog doesn't use

1. Run the Shopper Words Test on your ten most frequent pre-purchase questions.
2. Install Pico on the free plan to see what shoppers ask, what they click, and the phrases that find nothing.
3. Apply for the founding cohort for hands-on onboarding.

## 4. Email sequence

Plain text, one CTA each, sent from a named person. Bodies below are drafts, 60 words or fewer.

**Email 1, day 0. Subject: Your Findability Score: [score]**
Your score is [score], in the tier "[tier]". It is based on your answers, not a scan of your store. The three fixes for your tier are below, and the Shopper Words Test worksheet is attached. It works best with your last month of customer emails.

**Email 2, day 2. Subject: Ten phrases your shoppers might use**
The fastest way to find gaps is to read your customers' own words. Pull ten phrases from emails, chats, and "Searches with no results". Then check each one against your product titles. Here is a worked example on our sandbox store's sample outdoor gear catalog. Try your own phrases there.

**Email 3, day 5. Subject: See what shoppers ask, on your own store**
Pico is an AI shopping assistant that answers with products from your synced catalog and shows you what shoppers asked for, including the phrases that found nothing. Free covers 50 conversations a month. Setup is four steps. It does not answer order or returns questions.

**Email 4, day 8. Subject: Last note on your Findability Score**
We're taking a founding cohort of 20 stores, with hands-on onboarding, a direct line to the founder, and 50% off any paid plan for six months. If your score was 70 or above, reply to this email and we'll set it up. Otherwise, the worksheet and the sandbox are yours to keep.

## 5. Setup and compliance

| Item | Specification |
|---|---|
| Tags | Tag each lead by tier and by answers to questions 3 and 7, so email 3 can be tailored |
| Routing | 70 to 100 tier leads go to the founder for the founding cohort |
| Tracking | Source and campaign parameters on every link, so Dashboard 7 stage 1 KPIs can be counted |
| Email rules | Every email carries a working unsubscribe link and a postal address, per the CAN-SPAM requirements in `research/2026-11-03-run-2-channel-rules.md` |
| Claims | Every line follows `GTM-BRIEF.md` Section 5. No industry statistics, no outcome claims, no competitor names |
| Secondary market, for later | An Arabic version for the GCC is not built now |
