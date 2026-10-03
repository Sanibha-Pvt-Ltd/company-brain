# Stage A — App deep-dive

Run per app by the assigned member. Output: `members/<member>/apps/<cat>/<app>.md` (your own folder; re-runs keep earlier dated sections and add a new `## <date>` block).

Inputs: `negatives.md`, `listing.json`, member's screenshots/PDFs, the lens (`research/categories/<cat>/lens.md`, or the latest `members/*/drafts/<cat>/lens.md` if not yet promoted). Read the lens first and answer every question in it. Work through every section; skip none. If a section lacks data, say so in one line with `[UNKNOWN]` and move on.

## A1 Snapshot
Name, developer, App Store id, price model, rating + rating count (from listing), first release, last update, update cadence and what the last 5 release notes say they invest in `[DATA:listing.json]`. Positioning one-liner from title/subtitle/description: which promise and keywords they lead with (ASO read).

## A2 Business performance (web)
US downloads/revenue estimates, trend, inflection points and likely causes (match against release notes, ads, press) — from public Appfigures/Sensor Tower/Similarweb pages, press, founder interviews. Report ranges and sources. Developer background: other apps, team size, funding, cross-promo. If nothing public: `[UNKNOWN]`, don't guess.

## A3 Monetization
Model (weekly/monthly/annual/lifetime/consumable/ads), prices, trial, intro offers, price history (reviews saying "price went up"). From screenshots: paywall placement, hard vs soft, dismissability, copy, design, number of paywall touchpoints, exit/discount offers. Paywall tool clues (Superwall/RevenueCat) from web/SDK pages if findable.

## A4 Acquisition
ASO: title/subtitle/keywords, screenshot story, rating-prompt timing. Paid: Meta Ad Library, TikTok Creative Center — analyse 5+ creatives (hook in first 3s, angle, format, CTA). Organic: Reddit, TikTok, YouTube, press, creator seeding.

## A5 Product teardown (from the member's real screenshots)
Order screens into the user journey even if uploaded shuffled; flag gaps. Table per screen:
`# | stage (first-launch / onboarding / permission / paywall / core-task / result / upsell / settings) | what user sees | what user can do | verbatim copy | psychological lever | friction or dark pattern | tag`
Then: time-to-value (taps from launch to first useful result; before or after paywall?), onboarding length and promises, permission framing, core loop, retention hooks (notifications, widgets, streaks), trust signals and trust breakers.

## A6 Failure mining — 1–2★ reviews (the core step)
Input: `negatives.md` (newest first). Read ALL of it, not a sample.
1. Header: total negatives analysed, date span, country mix, app versions covered. Compare to the true rating distribution on the listing (e.g. 1★ share of all ratings) to say how representative this sample is.
2. Classify every review into the lens taxonomy (one primary cluster each; note secondary). Table: `cluster | count | % of negatives | last-90-days count | trend (↑ ↓ →) | typical version spike`. Counts must be real.
3. For each cluster with ≥3% share: what users expected vs what they got; 3 verbatim quotes (stars, date, version); root cause hypothesis `[INFERRED]`.
4. Time analysis: did any app version / date trigger a spike? What changed ("used to be good before version N")?
5. Churn signals: "switching to X", "went back to Y", competitor mentions — list with counts.
6. Anger index: reviews threatening refunds/chargebacks/reporting to Apple; billing-trap language ("charged", "cancel", "free trial", "scam").
7. **Opportunities**: for each top-5 cluster, the promise Sanibha can make on screenshot 1 and the product rule that guarantees it (e.g. "No ads, ever" → no ad SDK; "Cancel in one tap" → in-app cancel deep link).
8. If positive reviews are also provided: what delighted users say in their own words (= marketing copy candidates).

## A7 Tech & ops (light)
SDK/stack clues, iOS APIs the core feature requires and their limits, localization, support channels.

## A8 Verdict
- Why this app wins or loses, one paragraph.
- Top 3 to copy, top 3 to beat, the single most exploitable weakness.
- Every lens question answered (list them with answers).
- Evidence-strength grade per section: strong / medium / weak.

Frontmatter: `type: app`, plus `reviews_analysed: <n>`, `screens_analysed: <n>`.
