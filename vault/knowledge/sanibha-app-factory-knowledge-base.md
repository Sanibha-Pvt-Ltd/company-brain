---
type: knowledge
updated: 2026-10-04
---

# Sanibha App Factory — Knowledge Base

Compiled from one long working session plus the saved project notes. Written to be pasted into another LLM as background context.

## 0. How to read this file

- **Provenance:** Facts come from web research done during the session, files the founder uploaded (AppTweak/Appfigures exports), and decisions the founder stated. Items marked **[ESTIMATE]** are my own modeling assumptions. Items marked **[UNVERIFIED]** could not be traced to a primary source.
- **Staleness warning:** The plan changed many times. Section 2 is the timeline. Where an earlier decision conflicts with a later one, the later one wins.
- **Left out on purpose:** API keys and credentials, personal finances, family details, home/office address, and intern candidate details beyond first-name assignments.
- **Coverage limit:** This covers only the session it was compiled from. Other chats are not included.

## 1. Venture thesis and constraints

- **Business model:** A portfolio ("app factory") of narrow consumer utility/wellness apps for the US market, built by an India-based team. Find one or two winners, scale them with paid acquisition, use the cash to fund the rest.
- **Core thesis:** Win on performance-marketing execution (best LTV/CAC among competitors), not on product or technical differentiation. The founder has 12+ years in performance marketing and analytics.
- **Goal:** Prove a business run from India can reach $10M+ net revenue in 2-3 years on paid marketing, then raise a follow-on round from US VCs.
- **Funding:** Self-funded with a $100K reserve. Decided not to raise now. A US VC raise is a milestone roughly a year out. Plan is to flip to a Delaware C-Corp at that point.
- **Company:** Sanibha Pvt. Ltd. (Gurgaon). Formal incorporation was still in process as of 29 Sep 2026.
- **Platform:** US market first, native iOS only (PWA path abandoned, see section 2).
- **Team:** Founder (solo on marketing and product) plus 3 engineering interns. The VP of Engineering from the founder's previous company declined to join.

## 2. Decision timeline (read in order; the last entry is current)

1. Started as utility/productivity apps only; widened to any evidence-backed consumer category after research surfaced Health & Fitness and Food & Drink opportunities.
2. Built a 15-factor weighted scoring matrix over 20 ideas, which later grew to 28 categories.
3. Settled on a matrix **re-weighted for the LTV/CAC execution thesis** as the authoritative ranking (section 3).
4. **Constraint discovered:** Meta ad account approval takes about a month; Apple App Store review takes about 2-3 months; creatives take about a week.
5. **PWA-first pivot:** Test with web apps while waiting for approvals. Wave 1 narrowed to apps that were PWA-viable and fully AI-codeable to about 90% of the category leader: Fax, Baby tracker, Pets tracker, Weather.
6. Fax build in Lovable stalled and was paused.
7. **PWA constraint dropped** when 3 interns were hired. Decision: native iOS apps only.
8. Baby tracker paused (it ranks #12 on the thesis-weighted list). Priority redirected to Fax, Mileage tracker, Document scanner, Calorie tracker.
9. **Current Phase 1 build list (12 apps):** Storage cleaner, Recipe importer, Fax, Calorie counter, Document scanner/PDF toolkit, Universal TV remote, Plant identifier, Sleep tracker, Baby tracker, AI resume builder, Habit tracker, Immigration case tracker.
   - **Tension to be aware of:** Storage cleaner (#19), Plant ID (#18), Baby tracker (#12) and Immigration tracker (#15) rank low on the thesis-weighted list but are in the 12. The list was set partly from intern assignment submissions, not from the ranking alone.
10. **Intern app mapping:**
    - Ganesh: Storage cleaner, Calorie counter, Plant identifier, Habit tracker
    - Kushagra: Fax, Baby tracker, Sleep tracker, Universal TV remote
    - Harshil: AI resume builder, Recipe importer, Immigration case tracker, Document scanner
11. **Phase 0 (must finish before any app coding):** six internal marketing-intelligence tools: design-system auditor, onboarding-flow benchmarker, store-listing watcher, review-mining agent, ad-tracking digest, paywall tracker. Split: Ganesh (design auditor, onboarding benchmarker), Kushagra (store-listing watcher, paywall tracker), Harshil (review-mining agent, ad-tracking digest).
12. **Architecture decisions (latest):**
    - Fully siloed codebase and backend per app. No shared code. All code AI-written from shared spec templates.
    - User identity siloed per app; no cross-app account linking unless the user opts in.
    - One shared Firebase project for Crashlytics and Analytics only (one-time setup by Kushagra). Each app's backend logic stays separate.
    - A shared SanibhaDesignKit (design tokens, motion/haptics, shared review-gate component) owned by Ganesh. Color, icon and voice stay distinct per app.
    - Kushagra goes deep on backend for his own 4 apps; no cross-app architect role.
13. **Open:** the native framework (Swift vs React Native) was discussed but no final decision is recorded. I leaned React Native for team-resilience reasons, then the founder chose siloed codebases. Treat as undecided.

## 3. Scoring method and rankings

### 3.1 The 15 factors (general matrix; each scored 1-5, 5 is best)

Organic growth evidence, paid marketing efficiency, creative differentiation, new-entrant friendliness, competitive saturation (inverse), regulatory complexity (inverse), build complexity (inverse), usage frequency/retention, monetization fit, US TAM, data/privacy sensitivity (inverse), seasonality (inverse), exit optionality, urgency/specificity of problem, platform/trust risk (inverse).

- Score formula: weighted average = SUMPRODUCT(scores, weights) / SUM(weights).
- **General weights:** regulatory 3.0, build complexity 2.5, new-entrant 2.0, saturation 2.0, TAM 2.0, monetization 2.0, data sensitivity 2.0, paid efficiency 1.75, usage frequency 1.75, urgency 1.5, platform/trust 1.5, creative 1.25, organic 1.0, exit 0.75, seasonality 0.5.
- **Thesis-weighted changes:** paid efficiency 3.0, build complexity 3.0, regulatory 2.5, retention 2.5, monetization 2.5, urgency 2.0, platform/trust 2.0, data sensitivity 2.0; TAM down to 1.0, exit down to 0.25, creative down to 0.5.
- Lesson: the same scores rank differently under different weights (Fax is #9-10 on the general matrix, tied #1 on the thesis-weighted one). Always say which lens a ranking uses.

### 3.2 Thesis-weighted ranking (authoritative, 21 categories)

| Rank | Category | Score |
|---|---|---|
| 1 (tie) | Mileage/expense tracker | 3.74 |
| 1 (tie) | Fax app | 3.74 |
| 3 | Document scanner/PDF toolkit | 3.68 |
| 4 | AI calorie/food tracker | 3.67 |
| 5 | AI resume builder | 3.60 |
| 6 | Recipe import/organizer | 3.57 |
| 7 | Sleep tracker | 3.56 |
| 8 | TV Remote | 3.49 |
| 9 | AI voice/meeting transcription | 3.24 |
| 10 | AI photo editor | 3.14 |
| 11 | Screen mirroring | 3.10 |
| 12 | Baby tracker | 3.00 |
| 13 | Period/cycle tracker | 2.96 |
| 14 | Flight tracker | 2.95 |
| 15 | Immigration case tracker | 2.84 |
| 16 | Spam call blocker | 2.70 |
| 17 | File converter | 2.63 |
| 18 | Object/plant ID | 2.52 |
| 19 | Storage/photo cleaner | 2.48 |
| 20 | AR tape measure | 2.42 |
| 21 | Authenticator/2FA | 2.15 |

### 3.3 Categories scored only on the general matrix (not on the thesis-weighted tab)

Pets tracker 3.87 (#1 general), Focus app 3.77, Education/flashcards 3.63, Habit tracker 3.53, Weather 3.30, Currency converter 3.04. Subscription-cancel/tracker apps were analyzed qualitatively and not scored (see 4.30).

### 3.4 PWA viability (informational, was a column in the matrix)

- **Not PWA-viable (native-only need):** Mileage tracker (continuous background GPS), Spam call blocker (CallKit), AR tape measure (ARKit), Storage cleaner (photo-library access), TV Remote and Screen mirroring (local device networking/protocols).
- **Partial:** AI transcription (background recording), Sleep tracker (overnight sensing), Authenticator (secure key storage).
- This no longer matters because the plan is native iOS only.

## 4. Category intelligence (what the research found)

### 4.1 Fax app
- Leader: FAX from iPhone (Municorn Limited, Cyprus). About $26.8M gross revenue per year ($18.7M net after Apple's 30%). Break-even CPI $23.78 vs market CPI $4.06 (about 6x headroom). Ranks #1 organically for "fax". About 55-70% organic traffic.
- Weakness: downloads down 37% while revenue up 22%; store listing frozen about 12 months; keyword ranks fell; 158 of 1,000 reviews (16%) confirmed fake. Cyprus entity means no US dispute venue. "Unlimited" plans have a hidden fair-use cap.
- Municorn runs a portfolio (scanner, calorie counter, step counter, eSIM apps) on one developer account; a cross-product billing failure was documented (continued eSIM charges after cancellation).
- Challengers: iFax (worst billing complaint found: $399.99 charged on day 2 of a trial; website price differs from in-app price), FaxBurner (strong 4.9 iOS rating, but the free tier is 5 pages lifetime), Genius Fax (same small team as Genius Scan, 4.9 from 40K reviews), eFax, MetroFax.
- Market: online fax about $3.16B (2026), about 9.5% CAGR. About 89% of healthcare orgs still use fax. Twilio shut down its fax API; Telnyx positions as the migration path.

### 4.2 Document scanner / PDF toolkit
- Leader: CamScanner (INTSIG, Shanghai). About $10M/month. 2019 malware incident via an ad SDK (Google Play removal, silent subscription sign-ups); India banned it in 2020; reviews in 2026 still cite the incident.
- Genius Scan (The Grizzly Labs, France): 15 years, bootstrapped, profitable, about 10 people, 5M+ MAU. Founder stated principles: no dark patterns, no ads (ugly gambling ads converted best and were removed anyway), grandfather old buyers, reject weekly billing, raised price from about $20 to $40/year with inelastic demand. Said paid-ranking competitors "are not as profitable as they look."
- Others: Adobe Scan, Microsoft Lens (free, no subscription), SwiftScan. Documented paid-UA case: ChatPDF reported +320% ROAS and -42% CAC.

### 4.3 AI calorie / food tracker
- MyFitnessPal: $310M revenue in 2025, down 5.7% YoY. Barcode scanner moved to paid and users called it a betrayal. Recent reviews skew negative even though the lifetime rating is high. Its AI Meal Scan was independently benchmarked at 71.2% food-ID accuracy and ±18% portion error (lookup-table portions, not depth sensing).
- PlateLens claims ±1.1-1.4% MAPE with a published validation. Cal AI ±14.6%, Foodvisor ±16.2%. **[UNVERIFIED]** Cal AI ownership and revenue conflict across sources (acquired by MyFitnessPal vs a16z-backed vs $40M ARR bootstrapped); do not cite.
- Health & Fitness has the best trial-to-paid (35.0%) but the worst first-renewal retention (30.3%).

### 4.4 Recipe import / organizer
- ReciMe (Melbourne): raised about $1.3-2M (angels include Marissa Mayer). Founders narrowed to one feature (the importer); retention tripled and subscribers grew 20x in six months. Revenue undisclosed. **[UNVERIFIED]** the $3M/month figure in the one-pager has no primary source.
- Accuracy is source-dependent: near-perfect on clean blogs, worse on TikTok/Instagram captions.
- Complaints: free tier too tight, one user lost about 90% of saved recipes after an update, billing and support complaints. Osta added intrusive ads and users migrated back to ReciMe.

### 4.5 Mileage / expense tracker
- MileIQ (Microsoft since 2015, bundled with 365 Business Premium). Every competitor researched (MileIQ, Everlance, TripLog, Driversnote) had documented phantom or missed trips. Complaints include a "half-mile rule" that silently misses trips, with one user claiming thousands of dollars lost in deductions.
- Everlance was acquired by Motus (Feb 2025) after raising only $250-500K and tracking 4B miles in 2025.
- ClearCheckbook reached about $198K per year from a $15 start, organically.
- Pattern: standalone success tends to end in acquisition, not independent scale.

### 4.6 AI resume builder
- Rezi: about $3.06M annualized (Stripe-verified via TrustMRR), pricing $29/month or $149 lifetime. It shipped an "ATS Hack Mode" (invisible keyword text) that independent research says now backfires.
- BOLD Limited is alleged in a filed federal antitrust case (Rocket Resume v. BOLD, April 2026) to secretly own 8 "competing" resume brands. This is an allegation, not a finding. Zety and Resume.io were reported billing every 4 weeks as "monthly."

### 4.7 Sleep tracker
- Jan 2024 revenue: Calm $7.68M/month, Headspace $4.02M, Sleep Cycle $1.36M, BetterSleep $1.22M, Waking Up $1.20M. Correction: an earlier $700K figure for BetterSleep was wrong.
- BetterSleep retroactively moved a one-time-purchase user to a $99 subscription. Sleep Cycle is publicly traded (June 2021 IPO). Reports of lost sleep history exist. Smart-alarm accuracy took Sleep Cycle years to tune.

### 4.8 TV Remote
- Appfigures August 2026 (user-supplied): the leader (EVOLLY.APP, Singapore) about $4M/month; four others $410K, $660K, $1M, $850K (about $6.9M/month for the five).
- Leader complaints: a user's Apple ID was locked over a disputed $40 charge after a same-day cancellation, boilerplate support, "lifetime" purchases that still show paywall prompts.
- Measured Apple Search Ads niche data (Adapty 2026): "Remote Control" sub-niche converts 77.6% install-to-paid at $0.56 CPA. This is the only category with a measured CPA and conversion rate together.
- EVOLLY.APP runs a multi-app portfolio (screen mirroring, scanner, plant ID, AI note-taker, phone cleaner).

### 4.9 Screen mirroring
- Five apps total about $2.265M/month: Evolly $380K, TV Miracast $85K, Smart TV View Toggle $380K, Desidari $690K, Ozuna $730K.
- Worst trust profile in the project: fake paywall buttons, hidden weekly option shown only at cancel, "pay before you can test," independent legitimacy scores near 0. Real audio/video sync is a genuine engineering problem. AirPlay/Chromecast are free native alternatives.

### 4.10 Storage / photo cleaner
- Cleanup (Codeway): about $90.7M per year; break-even CPI $12.83 vs $2.90 market; holds 83-99% Apple Search Ads share of voice on core keywords. This is a spend war, not an efficiency gap. Zero rating removals in 366 days; ships every 13 days.
- AI CleanKit: Apple removed 297 ratings (73% five-star). AI Cleaner (Grimlax) collapsed (downloads -88%). None of the four were ever featured by Apple.

### 4.11 Baby tracker
- Huckleberry raised $12.5-16M (Series A 2021); no public revenue **[UNVERIFIED]** for the $830K/month figure. An analyst doubted another raise. Name collisions with unrelated "Huckleberry" companies polluted research.
- Pebbi positions on privacy/offline/shared care. Tottli is a new iOS-native minimalist ("log a feed in five seconds, one hand, in the dark"). Robin Baby leads with voice logging.
- Parenting apps market about $717M (2026).

### 4.12 Pets tracker
- Market about $2.74-4.7B. 11Pets (a tiny unfunded 4-person team) forced a subscription and locked users out of their own pets' medical records.
- Rover (marketplace) was acquired by Blackstone for about $2.3B in Feb 2024 (a different, capital-heavy business). Whistle was discontinued after two acquisitions. PetDesk sells B2B to vet clinics.
- Pets is the only "tracker" with no human-health, children's-data, or consent-law exposure. The population is renewable (new pets over decades).

### 4.13 Period / cycle tracker
- Flo: $275M revenue (2025), $1B+ valuation. Severe legal history: FTC enforcement (2021) for sharing health data with Facebook/Google/Flurry despite privacy promises, plus a $59.5M class settlement (Google $48M, Flo $8M, Flurry $3.5M). Post-Roe risk makes it worse. Recommendation: avoid.

### 4.14 Spam call blocker
- Robokiller (Bending Spoons): 1.5/5 and 88% unfavorable on one site, 125% price hike ($39.99 to $89.99/year), users suspect it causes the spam it claims to stop. Truecaller (public) about $150M+/year, revenue declining.

### 4.15 File converter and AR tape measure
- File converter: worst billing-fraud environment found. Multiple unrelated operators charge $1-2 for one conversion then $40-75+ recurring, some rotating domains.
- AR tape measure: Apple's free Measure app uses the same ARKit. One app locks the user's own created floor plan behind a paywall.

### 4.16 AI voice/meeting transcription
- Otter.ai faces a federal class action (In re Otter.AI Privacy Litigation) over recording consent. 12 US states require all-party consent. Otter cut Pro minutes from 6,000 to 1,200 without lowering the price.
- Notability reversed a 2021 forced-subscription move within days after backlash (a positive model).
- Moved to last priority because of legal complexity.

### 4.17 Authenticator / 2FA
- 2024 Twilio/Authy breach exposed 33M phone numbers (TOTP seeds not exposed). Hardest design problem (secure but recoverable), culturally expected free. Recommendation: avoid.

### 4.18 Flight tracker
- Flightradar24: $175M raised, 50K+ crowdsourced receivers, B2B data sales, a Swedish GDPR reprimand (aircraft registration can be personal data). Flighty: about 10 people across 7 countries, licensed data (6 feeds including Cirium), 18-month beta with pilots for ground truth. App in the Air shut down in 2024.
- Dropped because of data-licensing dependency, not coding difficulty.

### 4.19 Weather
- Windy.app about $600K/month (about $7.2M/year run-rate); Windy.com about $3.5M ARR. WeatherFlow rebranded to Tempest and pivoted to hardware and B2B data. Data is free (NOAA/ECMWF/GFS), so winners differentiate on UX and alerting.
- Clime (Mosaic S.r.l., owned by Bending Spoons since 2024): 1.1M ratings, 4.5 stars, aggressive paywalls, templated release notes, broad privacy collection. One reviewer praised grandfathering of Pro buyers.

### 4.20 Education / flashcards
- Chegg (NYSE) Academic Services revenue fell 57% YoY in one quarter due to free AI tools. Quizlet moved "Learn" mode behind a paywall; Knowt launched as "free Quizlet alternative" then paywalled features too.

### 4.21 Habit tracker and Focus app
- Habit: Habitica 32M+ registered users, Streaks 21M+ downloads; 43% of users disengage after initial adoption (one source). Clean trust environment.
- Focus: Forest 60M+ users, $4 one-time purchase, funds real trees. A one-time $4 product cannot support paid CPI above $4, so it is structurally incompatible with a paid-acquisition thesis.

### 4.22 Currency converter, Books/Reference
- Currency: about $1.3B market; XE (Euronet) has 100M+ users; complaints are mild. Invoice-generator apps appear to be free lead-gen, not standalone products.
- Books/Reference: dominated by platform defaults; Merriam-Webster has 50-60M downloads but only about $6-40K/month. Rejected.

### 4.23 Second-number/burner apps
- Burner about $1M/month on iOS; rejected because the core feature (anonymity) is also the abuse vector (harassment, verification bypass).

### 4.24 Subscription-cancel / tracker apps
- Market about $0.52B (2025). Rocket Money (acquired for $1.275B, Dec 2021) has about 65% share and takes 35-60% of negotiated savings. Model B trackers (Bobby, ReSubs, Subby) are manual, one-time-purchase, no bank link.
- An independent test found only 2 of 8 apps caught all 14 known subscriptions. Not prioritized: it shares Focus app's one-time-price problem, and it is ironic for a subscription-funded portfolio.

## 5. Cross-category patterns

1. **Billing-trust failure is near-universal.** Trial-to-subscription surprise, forced paywalls, hard-to-cancel flows, and support black holes recur in almost every category. This is the main differentiation wedge: be the honest operator.
2. **"Previously free, now paywalled" and "retroactive deal change" recur** (Quizlet, Knowt, 11Pets, BetterSleep, The Dyrt, Photoroom, Otter, Clime). Never retroactively lock existing users' data or features. Grandfather buyers.
3. **Data loss is a distinct severe failure** for apps whose value is accumulated history (ReciMe, Sleep Cycle, 11Pets). Treat history as irrevocable.
4. **Revenue scale and trust are decoupled in the short term** (Photoroom 1.4/5 Trustpilot with $94-220M ARR). Honest billing is a differentiator, not a prerequisite for revenue.
5. **Commodity categories with a free native alternative** (file converter, AR measure, screen mirroring, authenticator) produce deceptive billing, because it's the only lever left.
6. **Winners by type:** commodity categories are won by marketing and capital (Municorn, Codeway); accuracy categories by measurable technical superiority (PlateLens, Sleep Cycle); narrow-scope categories by editorial discipline (ReciMe, Genius Scan).
7. **Acquisition is the common endgame** for independent standalone apps (MileIQ, Everlance, Rocket Money, Cal AI claim).
8. **Operators reuse infrastructure across many apps** (Codeway, HubX, Municorn, EVOLLY.APP, Glority, Mosaic). Shared billing/support backends inherit one app's complaints into all.
9. **Release cadence tracks business health** (Codeway ships every 13 days; declining competitors stop shipping).
10. **Origin-country trust matters when something goes wrong** (CamScanner/China, Glority/China). Be transparent about where the team is based.

## 6. Portfolio operators studied

- **Bending Spoons** (Nasdaq: BSP): $1.31B revenue in 2025, 500M+ MAU, 9M+ paying customers. Growth is mostly acquisition and operations: in 2025 it sourced about 2,500 targets, analyzed about 200, and closed 6; underwriting hurdle about 65% levered IRR. Post-acquisition it consolidates ops in Milan, with large staff cuts typical (60-80% per an outside advisor). Internal analytics tooling, continuous paywall/price A/B testing, price increases often above 80%, deliberately restricted free tiers. Bought Mosaic (Clime, 17+ apps) from IAC in 2024 for about $160M after revenue fell from $199M (2019) to $156M (2023). Mosaic portfolio includes Clime, Dawn AI, PerfectPrep, Typeright, PDF Hero, Textkiller, iTranslate apps, Blossom (plant care), Sleep, Sleepzy, Moodnotes, Window, Stepz, Productive.
- **Transferable lessons:** shared infrastructure, continuous paywall testing, and a "Pico"-style analytics habit. **Counter-position:** their restricted-free-tier playbook is what users complain about, which is the opening for an honest operator.
- **HubX** (Turkey, 2022): 600M+ users, 40+ products, $50M raise (Sep 2026) at $1.2B pre-money with no prior VC. **Codeway** (Turkey, 2020): $400M+ ARR (funding status conflicting across sources). **Air Apps** (Portugal, 2018): $70.3M 2025 revenue, unfunded per sources. **AppNation** (Turkey, 2021): $35M 2024 revenue, unfunded.

## 7. Unit-economics benchmarks

### 7.1 Measured CPI/CPA data points (the only ones found)
- TV Remote niche: $0.56 CPA, 77.6% install-to-paid (Apple Search Ads, Adapty 2026).
- Utilities category CPI on iOS: about $2-4 (average about $2.90).
- Codeway break-even CPI $12.83 and Municorn break-even CPI $23.78. These are incumbents' break-even ceilings, not market rates.
- For all other categories there is no measured CPI. Everything else in the 28 per-category models was an **[ESTIMATE]**.

### 7.2 Adapty 2026 subscription benchmarks
- Global install-to-trial about 10.9% (weekly plans 9.8%, monthly 0.3%, annual 1.8%).
- Trial-to-paid: card-gated opt-out trials 48.8%; no-card opt-in 18.2%; freemium 2.6%. Health & Fitness 35.0% (highest named), Entertainment 19.1% (lowest named).
- Utilities: highest first-renewal retention (58.1%); weekly plans are 73.6% of category revenue; trials add +85.1% to LTV (largest). Lifestyle: trials reduce LTV 21.2%. Productivity and Graphics/Design: trials reduce LTV.
- Web vs in-app: web paywall converts 1.10% vs in-app 1.60%; web has better month-1 retention (64.5% vs 46.2%) but worse month-6 (20% vs 30%); 12-month LTV $35.80 web vs $40.10 in-app, even after saving the app-store fee.
- Lifestyle direct install-to-paid reaches roughly 18-38%.

### 7.3 Fax budget model **[ESTIMATE]**
- Assumptions: $10 CPI, 4,000 installs, 9-10% install-to-trial, 48.8% trial-to-paid, $15/month, 6 paying months. Total first test about $47.5K (including $7.5K creative testing).
- Result: LTV:CAC about 0.39x with payback about 15 months. Install-to-trial was the binding constraint.
- A similar TV Remote model landed near 0.40x. Earlier versions used unsupported placeholders (35% install-to-trial); these were corrected.
- The 28-category model workbook was stripped back to show only measured inputs, because every row had at least one estimated input (usually price or average paying months).

### 7.4 TAM figures
- Market-report TAMs varied 5-15x by source (authenticator $1.2-13.4B, sleep $1.07-17.5B, resume builder $0.47-9.5B). Many reports measure hardware or enterprise segments, not apps. Prefer named-app revenue over report TAMs.
- Search volume: no Ahrefs/Semrush/Keyword Planner access during the session, so all search-volume statements are directional proxies. Weather was the exception (Ahrefs-style data showed Windy.app at 313K monthly visits, 8K searches for "windy app", India 33.6% of traffic).

## 8. Paid acquisition mechanics

### 8.1 Meta
- Learning phase exits at about 50 optimization events per ad set within 7 days. Below that, delivery is volatile or "Learning Limited." Budget rule: minimum weekly budget = 50 x cost per purchase.
- The June 2024 reduction to about 10 events applies to Purchase and **Mobile App Install** campaigns, not **Mobile App Event** campaigns. A subscription purchase inside an installed app is an App Event, so plan for 50.
- Only purchases attributed to a Meta ad click or view (default 7-day click, 1-day view) count. Organic purchases cannot be pooled in. CAPI recovers genuinely Meta-driven conversions the pixel misses (pixel-only captures about 40-70%).
- 50 is the floor, not the ceiling. About 100+ per week supports broad targeting; larger volumes keep improving delivery and placement efficiency.
- Don't spread thin: 12 apps launched at once risks every ad set stuck in Learning Limited. Concentrate budget on 2-3 apps. Bridge strategy: temporarily optimize for an upper-funnel event (trial start, onboarding complete), then switch to Purchase.
- Creative: UGC-style outperforms studio (about 34% lower CPI, Meta data cited in third-party sources). Hook in about 1.5 seconds, problem-agitate-demo structure, captions on, creative fatigues in 7-10 days, validate 20-30 hooks cheaply before human shoots.
- New Meta ad accounts take about a month to approve. Submit early.

### 8.2 Apple Search Ads
- No fixed 50-event rule. Apple guidance: budget for at least about 5 conversions per day for Maximize Conversions; wait about two weeks before judging; changing Target CPA resets learning. Discovery campaigns graduate keywords at about 10 conversions.
- Attribution does not depend on ATT or SKAdNetwork, so it is a cleaner data environment than Meta on iOS. Suggested to validate priority apps here first or in parallel.

### 8.3 ATT opt-in (App Tracking Transparency)
- Industry opt-in is about 15-35%. Gaming 39%, e-commerce 36%, publications 19%, education 14%. Utilities likely sit toward the low end.
- Levers: **timing** (never on first launch; below 15% when asked immediately) and a **full-screen pre-prompt** (30-35% better than modals; 65%+ opt-in reported in one source's best case). The pre-prompt must only educate; coercive design risks App Store rejection. Apple allows one system prompt per install, so the design must be right before launch.
- Define a "first value moment" per app: Fax after first successful send; Baby tracker after first logged entry; Sleep after first completed session; TV remote after first successful control; Scanner after first scan/export; Calorie after first logged meal.
- Pre-prompt copy: one sentence tying the ask to a benefit already delivered.

## 9. Legal, privacy and payments

- **Hosting:** US cloud region (AWS us-east-1, Supabase US, etc.), not India.
- **Laws:** CCPA/CPRA and other state privacy laws apply broadly. COPPA analysis for Baby tracker: a parent-operated app marketed to adults is not automatically covered, so verifiable parental consent flows are likely unnecessary. HIPAA likely does not apply to consumer wellness apps. Mileage tracker is most exposed on location-data laws. The amended COPPA Rule took effect April 22, 2026 (broader personal-information definition including photos/voice, written retention policy required). The Apitor settlement shows the real risk: a third-party SDK sending a child's data overseas.
- **Engineering requirements for child-data apps:** written retention policy with a deletion job, in-app account deletion (including a clear owner-transfer choice when caregivers are shared), SDK inventory reviewed before each addition, encryption at rest for photos/voice, no child data to ad networks, a specific privacy policy. This should still be reviewed by a privacy lawyer before launch.
- **Payments:** a merchant of record (Paddle was considered; the decision is now "merchant-of-record for web plus Apple/Google IAP for in-app," Paddle not confirmed). For native iOS, Apple IAP is the main flow. A Delaware entity is the standard route for Stripe but a merchant of record avoids the India Stripe limitation.
- **Billing rules for every app:** no trial converts without an on-screen reminder at least 24 hours before the charge; no 4-week cycle labeled monthly; plain-language refund policy on the pricing page; same price shown everywhere; a 3-step cancellation flow (Cancel visible on the account screen, then a confirmation with an optional retention offer no more prominent than "cancel anyway," then a final confirm; identical labels throughout; cancel in the billing system immediately while access continues to period end); historical user data never locked by downgrade or lapse.
- **Failure-mode rules distilled from competitors:** don't strip the free tier after launch; grandfather existing buyers; make error and payment-failure states visible (failed-payment banner); surface failures with specific messages.

## 10. Product and build specs created

- **QuickFax (fax app):** Single Home + Compose screen (document, fax number, cover note, Send, recent list), Sending, Success, a real Send Failed screen with specific messages keyed to failure reason, History, Account with failed-payment banner and the 3-step cancel. Visual language: ink-navy and paper-white, one coral primary accent, monospace for brand/numbers/titles, rotated postmark-style status stamps. Mockup: https://claude.ai/artifact/2roxwjT8PMpfHtjjd86xZH (a warm food-app-style variant was tried and rejected).
- **Fax backend (Telnyx):** POST /v2/faxes with a Bearer key; HTTP 202 means accepted, not delivered. Webhook order: fax.queued, fax.media.processed, fax.sending.started, fax.delivered (or fax.failed with failure_reason such as user_busy, destination_invalid, sender_call_dropped, account_disabled). Limits: 50MB and 350 pages. Telnyx does not retry, so retry logic must be built. Pricing from $0.007/page plus separate SIP transmission cost. Needs a Telnyx account, a fax-enabled number, and a Fax Application with a webhook URL. A leaked API key was shared in chat once and should be treated as compromised and rotated.
- **"mFax" naming trap:** several unrelated companies use "mFax"/"mfax" (Documo, mfax.io, mfax.to). Documo's API is gated behind a $150+/month plan. Telnyx was chosen instead.
- **BabyLog (baby tracker):** Home timeline with big circular Feed/Diaper/Sleep buttons and a date strip generated dynamically from the device date (Today plus the 4 previous days), timer or manual time entry for feeds and sleep (both pre-filled with device time), diaper multi-select, growth tracking with WHO percentile charts and an empty state, milestones with age-based suggestions, caregiver sharing (invite validation, duplicate-email error, owner cannot self-remove), and the 3-step cancel. Rules: every screen shows real saved data, never placeholders; sleep timer persists by storing the start timestamp, not an in-memory counter. Visual language: dusk-navy and cream, coral primary, sage for sleep, lavender for milestones, warm serif headers. Mockup: https://claude.ai/artifact/Rg3Nz6938Ji7PSg6tmdR2w
- **Pets tracker, Weather:** specs drafted (multi-caregiver sharing and milestones for Pets; niche activity weather for Weather). No mockups built.
- **Sanibha App Building Playbook:** a shared cross-app requirements doc (ATT strategy, billing, privacy, analytics, design, codebase policy). Its build script was written but the file was not generated or delivered.
- Other deliverables: scoring matrix workbook, LTV/CAC sheets, TAM workbook, 28-category UA model workbook, investor one-pagers, BabyLog privacy requirements doc.
