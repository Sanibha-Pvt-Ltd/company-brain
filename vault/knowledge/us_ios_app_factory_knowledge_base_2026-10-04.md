---
type: knowledge
updated: 2026-10-04
---

# US iOS Consumer-App Factory — Competitive Positioning & Unit-Economics Knowledge Base

**Version:** 1.0  
**Compiled:** 4 October 2026  
**Audience:** Founder, product, design, growth, analytics, and investment teams  
**Geography / platform:** US iPhone first; operations from India  
**Format:** Portable Markdown knowledge base; search by category, product concept, metric, or competitor.

> **Scope and provenance.** This document consolidates the research and strategic hypotheses developed in the conversation, including the early paid-acquisition and paywall discussion and the sequence of 12 planned category audits. It is **not** a new live scrape of all App Store pages. Competitor descriptions, screenshots, prices, ratings, and customer-review examples reflect the earlier conversation's public-source research at the time it was done. Screenshots often came from publicly indexed or historical material, not synchronized captures of every current US App Store first-three-screenshot sequence. Where supporting evidence was incomplete, the document explicitly says so. **Ten category audits were taken through full strategic recommendations; AI Resume Builder was started but not finished, and Immigration Case Tracker was discussed at concept level but not given a 20-app audit.**

## Contents

1. [Evidence taxonomy and known limitations](#1-evidence-taxonomy-and-known-limitations)
2. [Company strategy, decision principles, and research method](#2-company-strategy-decision-principles-and-research-method)
3. [Acquisition economics and paywall research](#3-acquisition-economics-and-paywall-research)
4. [Shared lessons across the app portfolio](#4-shared-lessons-across-the-app-portfolio)
5. [Category 01 — Storage Cleaner](#5-category-01--storage-cleaner)
6. [Category 02 — Calorie Counter](#6-category-02--calorie-counter)
7. [Category 03 — Plant Identifier](#7-category-03--plant-identifier)
8. [Category 04 — Habit Tracker](#8-category-04--habit-tracker)
9. [Category 05 — Fax](#9-category-05--fax)
10. [Category 06 — Baby Tracker](#10-category-06--baby-tracker)
11. [Category 07 — Sleep Tracker](#11-category-07--sleep-tracker)
12. [Category 08 — Universal TV Remote](#12-category-08--universal-tv-remote)
13. [Category 09 — Recipe Importer](#13-category-09--recipe-importer)
14. [Category 10 — Document Scanner / PDF Toolkit](#14-category-10--document-scanner--pdf-toolkit)
15. [Category 11 — AI Resume Builder — partial audit](#15-category-11--ai-resume-builder--partial-audit)
16. [Category 12 — Immigration Case Tracker — concept only](#16-category-12--immigration-case-tracker--concept-only)
17. [Portfolio comparison and next actions](#17-portfolio-comparison-and-next-actions)
18. [Source and verification index](#18-source-and-verification-index)

---

## 1. Evidence taxonomy and known limitations

Use these labels in subsequent work:

- **[PUBLIC]** A claim recorded from a publicly accessible App Store description, published price, developer information, Apple documentation, or publicly accessible product page at the time of research. It is *not* necessarily current today.
- **[REVIEW]** A qualitative customer review, discussion, or complaint. Valuable for identifying hypotheses; **not** a representative frequency estimate or proof that the product is defective.
- **[VISUAL]** Interpretation of visible public product marketing or screenshots. Some images were historical/third-party and were **not** the exact US live screenshot sequence for all 20 apps.
- **[MODEL]** Hypothetical financial or behavioral assumptions. **Not** an observed US iOS subcategory benchmark.
- **[THESIS]** Proposed strategy, concept, positioning, copy, UI direction, funnel, or experiment. Requires validation.
- **[TODO]** Research not completed or evidence missing.

**Special caution:**

1. The 20-app sets are **relevant competitor cohorts**, generally not independently verified *top-20 revenue/download* rankings. Only the storage-cleaner work separately noted nine apps on one earlier observed Utilities grossing list.
2. Public App Store in-app-purchase listings are **not proof of the paywall offer** shown to a first-time US user, their trial eligibility, their final payment, or realized ARPU.
3. Public rating counts are **cumulative ratings**, not installs, MAU, active subscriptions, or revenue.
4. Color, screenshot sequences, and messaging themes are **qualitative**; no complete coded image inventory for all ~200 storefronts was finished.
5. Competitor technical functionality and integrations may differ by model, account, OS version, region, or subscription tier.
6. Earlier narrative was at times more confident about *uniqueness* than justified. Several ideas initially called whitespace—memory-focused cleaner, Plant ER, swipe TV remote, anti-streak habits, photo calorie logging, pay-per-fax, and job-match resumes—were later found to have established competitors. The recommendations below reflect the **refined**, narrower opportunity.
7. Several D30 numerical examples use **illustrative** conversion and pricing assumptions. The baby-tracker worked example used **5% install→trial × 35% trial→paid = 1.75% install→paid**, producing **~$0.69** D30 RPI. A *different* 2.1% install→paid assumption produces **~$0.82** with the same price mix. Never mix the two denominators; see §§3 and 10.
8. RevenueCat/Adapty rates for Utilities, Productivity, or North America do **not** imply measured rates for specific apps, US Meta traffic, or their actual D30 cash recovery.

---

## 2. Company strategy, decision principles, and research method

### 2.1 Operating thesis

**[THESIS]** Build a US-facing, iOS-first portfolio of focused consumer software apps with product/engineering/growth operations substantially in India. The repeatable advantage sought is distribution, funnel experimentation, monetization, analytics, and disciplined capital allocation—not simply faster app coding. Launch narrow experiences, test paid channels, retain winners, and recycle capital where possible by **D30**.

Historical founder context from the ongoing venture: significant paid-media and consumer-app operating experience, including >$500M managed marketing budgets and >200M installs across businesses. Investor ambition was a repeatable platform capable of discovering and scaling multiple $10M–$100M+ products. These founder statements are *provided venture context*, not independent diligence findings.

### 2.2 Design-and-marketing principles discovered

1. **Different-looking ≠ different-feeling.** Colors and decorative UI can be copied. Different first-use experiences, category mental models, recurring behaviors and reliable outcomes are harder to copy.
2. **Own a problem moment, not a menu of features.** Examples: “Is it safe to delete this?”; “What do I eat next?”; “Is my plant recovering?”; “How do I restart?”; “Did this fax transmit?”; “What happened while I slept?”; “Will this remote work with my TV?”; “Which saved recipe can I cook tonight?”; “Does this PDF meet the stated technical requirement?”
3. **The creative, App Store page, onboarding and paywall should tell the same story.** The actual in-app demonstration must substantiate the advertisement.
4. **Do not mistake a competitor feature for whitespace.** Ask whether the app makes that job its primary workflow and whether we can measure an objectively better outcome.
5. **Show value before a high-risk paywall where feasible.** Example: test remote compatibility before charging; show a useful fax quote; show cleaner categories; let users inspect document checks. However, test the effect on *net D30 proceeds per install*, not just sentiment.
6. **Make AI explain uncertainty.** Especially important for food portion estimates, plant health, photo-deletion similarity, sleep correlations, resume claims and document readiness.
7. **Optimize reliability in utility categories.** A broken command, inaccurate record, lost recipe, or failed document export can outweigh clever design.
8. **Avoid building an incumbent’s complete feature set.** The MVP should prove the distinctive behavior and the paid-funnel hypothesis.
9. **Separate direct use-case fit from long-term monetization.** Episodic apps (fax, one-time PDF repair) differ from recurring apps (baby coordination, sleep, habits, meal decisions).
10. **Measure cohorts by channel, device/segment, creative and paywall**, and always reconcile trial conversion with actual D30 cash collection.

### 2.3 Reusable 20-app audit procedure

For each subcategory:

- Define a cohort of 20 relevant US iPhone apps; distinguish grossing/ranked results from editorial or competitive choices.
- Record name, publisher, platform/category, public rating count, core proposition, exact headline and visible first three screenshots **when accessible**, prices/IAPs, trial evidence, release notes and sources.
- Cluster into visual/positioning territories; do **not** invent numeric frequency counts without a coded sample.
- Examine one-star through five-star reviews. Keep actual quotes short and distinguish incident from systemic issue.
- Identify a *functional* gap, an *interaction* gap and a *trust/monetization* gap; check incumbents for each.
- Draft a six-screenshot App Store story, three campaign-specific Meta hooks, and a matching onboarding-to-paywall path.
- Define one category-specific activation event, one recurring-value event, D7/D30 engagement, refunds, and D30 **net** proceeds/install.
- Design a control versus challenger experiment. Abort an idea if it is visually distinctive but has no measurable user or business benefit.

---

## 3. Acquisition economics and paywall research

### 3.1 Exact D30 marketing payback relationship

For a paid install cohort:

```text
D30 net RPI = Σ over payment products [
    P(install → paid product by D30) × cash collected by D30
    × (1 − applicable App Store commission)
    × (1 − realized refunds/payment losses)
] + other net D30 revenue per install

Maximum break-even CPI (marketing-only) = D30 net RPI
D30 marketing ROAS = D30 net RPI / CPI
D30 contribution per install = D30 net RPI − CPI − attributable serving/support/processing costs
```

**[MODEL]** Many previous worked examples use `0.85 × 0.95 = 0.8075` net retention, representing an assumed **15% Apple fee for eligible developers** and **5% refunds/payment losses**. They are scenarios, not validated realized rates. Tax treatment, commissions, chargebacks and product-tier eligibility must be modeled using actual payouts. Some developers or transactions are subject to different Apple commissions; **do not hardcode 15% for every scaled product**.

- At **$99.99 annual upfront**, illustrative net receipts/payer ≈ **$80.74**.
- At **$49.99 annual upfront**, illustrative net receipts/payer ≈ **$40.37**.
- At **$39.99 annual upfront**, illustrative net receipts/payer ≈ **$32.29**.
- At $5 CPI and $99.99 annual with all payers annual, install→paid must be roughly **6.2%** for D30 marketing breakeven.
- At $4 CPI and $49.99 annual, install→paid must be roughly **9.9%**.
- **Weekly/monthly vs annual mix materially changes D30 cash collection.** An annual list price cannot be multiplied by *all* paid conversions unless all those subscribers actually choose and pay annual upfront by D30.
- Trial length, trial-start date, payment timing, direct paid purchases, free trial cancellation, in-app purchase routing, and refunds can change the D30 cohort significantly.

### 3.2 Funnel benchmarks discussed earlier

**[PUBLIC / cross-category; check report definitions before reuse]** Earlier research consulted [RevenueCat State of Subscription Apps](https://www.revenuecat.com/state-of-subscription-apps) and [Adapty](https://adapty.io/). Examples previously cited: RevenueCat 2026 Utilities median **D30 download→trial around 6.5%**, North America all-category median **download→trial around 7.1%** and **trial→paid around 34.2%**, and North America overall **D35 download→paid around 2.8%**. Adapty utilities data was described as **13.8% install→trial and 26.2% trial→paid** using its own cohort definitions; productivity regional numbers differed. **Do not combine rates from different sources or denominators** into a faux precise US Meta KPI. D30 vs D35, trial→paid window, paid vs organic, and different trial/paywall architectures all matter.

**[MODEL]** A deliberately conservative hypothetical Meta starting funnel discussed: **5% install→trial × 30% trial→paid = 1.5% install→paid via trial**. This is not a measured US iOS benchmark. Earlier niche planning ranges were also modeled, not retrieved niche-level actuals. Use them as sensitivity tests only.

**[MODEL]** Earlier “factory-level CPI below $2” was an **exploratory heuristic**, not a category-agnostic acceptable target. A TV remote with low initial net revenue may need CPI far below $2, while a proven $100/year focus product with strong paid conversion might support more. Correct operating decision: compute target CPI per app from **observed D30 net RPI**, apply a margin buffer, and allocate spend by incremental cohort ROAS.

### 3.3 Compiled D30 numerical scenarios from category audits

All rows below are **illustrative scenarios, not observed results**, using the 0.8075 net-retention assumption, first payments collected by D30 and **only one monthly charge** where applicable. Corrected arithmetic is shown.

| Category | Install→paid scenario | Annual mix / price | Monthly mix / price | Approx. net D30 RPI | Notes |
|---|---:|---|---|---:|---|
| Baby Tracker (original worked panel) | **1.75%** | 70% × $65 | 30% × $9.99 | **$0.69** | 5% trial ×35% conversion; **at 2.1% paid rate it would instead be $0.82** |
| Sleep Tracker | 2.1% | 80% × $59.99 | 20% × $9.99 | **$0.85** | Wearable users may activate differently |
| Universal TV Remote | 1.5% | 70% × $39.99 | 30% × $8.99 | **$0.37** | Compatibility is major funnel filter |
| Recipe Importer | 1.5% | 75% × $39.99 | 25% × $5.99 | **$0.38** | Subscription value may be delayed |
| Scanner / PDF Toolkit | 2.1% | 70% × $59.99 | 30% × $9.99 | **$0.76** | Free competition constrains pricing |

Illustrative *all-annual* cleaner case: $49.99 × 1.5% install→paid × 0.8075 ≈ **$0.61 net D30 RPI**. Illustrative $99.99 all-annual focus case: 2% install→paid × $99.99 × 0.8075 ≈ **$1.61 net D30 RPI**. These are ceilings for marketing breakeven, **not recommended bidding amounts**.

### 3.4 Paywall operating stack versus competitor intelligence

**Own-app paywall analytics and experimentation:** [Superwall](https://superwall.com/), [Adapty](https://adapty.io/), [RevenueCat](https://www.revenuecat.com/), Apphud, Qonversion and Purchasely. Common capabilities include impression-to-trial/paid measurement, paywall A/B tests, revenue dashboards, experiment assignment and subscriber lifecycle tracking. Confirm exact features, integration constraints and current pricing directly with the vendor.

**Competitive paywall research:** [MWM Intelligence](https://mwm.ai/mwm-intelligence), [Paywall Screens](https://www.paywallscreens.com/), PaywallPro, BuildNext, and intelligence offerings from monetization platforms. They may show captured paywalls, onboarding sequences, price changes or *estimated* metrics, but **do not reveal an arbitrary competitor's actual install→trial, trial→paid or realized ARPU** unless the publisher supplies those data. Historical screenshots and predicted MRR are not equivalent to current first-party conversion metrics.

**Recommended internal grain:** `app × country × acquisition channel × campaign × creative × device/TV brand (where relevant) × App Store product page × onboarding variant × paywall variant × subscription product × install cohort`. Event sequence: install → activated → paywall viewed → trial → billed → refund → D7/D30 proceeds → first renewal → retained value.

---

## 4. Shared lessons across the app portfolio

### 4.1 Product differentiation matrix

| Category | Incumbent mental model | Proposed sharper mental model | Recommended working concept | Audit status |
|---|---|---|---|---|
| Storage Cleaner | Find junk, free GB, swipe duplicates | Recover storage **with informed deletion control** | **KeepSpace** — “Make space. Keep what matters.” | Completed strategy |
| Calorie Counter | Log food, count macros, photograph meal | Decide what food fits the **rest of today** | **NextPlate** — “Know what fits. Eat what you love.” | Completed strategy |
| Plant Identifier | Identify, diagnose, water reminders | Guided troubleshooting **plus recovery follow-up** | **Plant ER** | Completed strategy |
| Habit Tracker | Checklists, streaks, gamification | Help people **restart after missed days** | **Again** | Completed strategy |
| Fax | Scan/sign/send, transmission status | **Handle the entire important-document send** and failure recovery | **Fax Concierge** | Completed strategy |
| Baby Tracker | Feed/sleep/diaper database | One-screen **caregiver shift handoff** | **Together** | Completed strategy |
| Sleep Tracker | Sleep scores, charts, snoring | **One actionable experiment for tonight** | **Tonight — Sleep Detective** | Completed strategy |
| Universal TV Remote | Simulated button remote and brand logos | **Prove compatibility**, then make control reliable | **Remote Ready** | Completed strategy |
| Recipe Importer | Save Reels, cookbook, grocery lists | Move saved inspiration into **meals actually cooked** | **Cooked** | Completed strategy |
| Scanner/PDF | Scan/edit/merge/sign/compress toolbox | Prepare file for **stated submission requirements** | **ReadyPDF** | Completed strategy |
| AI Resume Builder | Template, AI bullet, ATS score | Map each job requirement to **truthful evidence** | **ProofPoint** | **Partial audit only** |
| Immigration Case Tracker | Status feed, prediction, case history | **Calm official status + next action** | **Stop Checking / Case Flight Tracker** | **Concept only, no 20-app audit** |

These names are **working concepts**; trademark, domain, App Store name availability and brand conflicts have **not** been checked.

### 4.2 Where the original whitespace ideas needed correction

- **Storage “Memory Cleaner”** was already adjacent to Swipewipe, CleanMyPhone and photo-preservation products; refined to safety/inspectability + real storage results.
- **Food photo counting** is widespread (Cal AI, SnapCalorie, Foodvisor etc.); refined to *pre-meal decisions* and confidence-aware tracking. MyFitnessPal already has next-meal guidance.
- **Plant diagnosis** is sold by PictureThis and PlantIn; refined to guided multi-step differential assessment + follow-up.
- **Anti-streak habits** is served by (Not Boring) Habits/Atoms/others; refined to personalized **comeback workflow**.
- **Delivery tracking/pay-per-fax** already exists; refined to cohesive end-to-end job, pricing clarity and actionable failure response.
- **Shared baby logging** already exists across Huckleberry, Nara, Cubtale, Baby Connect; refined to *handoff*, not mere sync.
- **Sleep coaching** already exists; refined to transparent personal experiments and minimal scores, with caution about causal inference.
- **Eyes-free TV navigation** already exists (Kraftwerk 9, RoByte); refined to first-command verification and dependable reconnect.
- **Social recipe importing** already exists at scale (ReciMe, Pestle etc.); refined to conversion of saves into cooking.
- **Scan→sign** already exists (iScanner etc.); refined to user-specified technical submission readiness.
- **Job-description matching, before/after AI edits and claim verification** already exist; resume evidence mapping remains a *hypothesis requiring deeper audit*.

### 4.3 Recurring versus episodic needs

| Predominantly episodic | Naturally recurring (if product works) |
|---|---|
| Fax sending, PDF-size repair, AI resume for a short job search, plant identification | Baby care during newborn lifecycle; habit tracking; repeated meal decisions; recurring sleep observations; daily TV remote use; household photo organization |

**Do not equate “frequent use” with “high willingness to pay.”** TV remotes face free official alternatives; habit trackers face extremely cheap options; sleep has native Apple metrics. Conversely, episodic fax tasks can support real paid transactions if the user is blocked and the product reliably completes the task.

---
## 5. Category 01 — Storage Cleaner

**Status:** Full category strategy completed, with visual-evidence limitations. **Working brand:** KeepSpace. **Category tagline:** *Make space. Keep what matters.*

### 5.1 Twenty competitor names

**Nine previously observed high-grossing US Utilities cleaners:** Cleanup: Phone Storage Cleaner (Codeway/Deep Flow), Cleaner Guru (GM UniverseApps), Swipewipe (MWM), AI Cleaner (Grimlax), Cleaner Kit (BP Mobile/AIBY), CleanX (TapSuite), Cleaner Neat (Smart Tool Studio), Smart Cleaner (NAICOO), Clean Manager (Quiet). An earlier snapshot described Utilities positions **#1, #4, #11, #12, #17, #30, #54, #58, #97** respectively; **historical ranking snapshot, not current ranks or category-wide share**.

**Eleven relevant alternatives:** CleanMyPhone, Clever Cleaner, Slidebox, Boost Cleaner, Cleaner (Seven Mile Apps), Phone Cleaner (AlgoTwist), Minus Photos, Phone Cleaner: More Storage, Cleaner (CheeseJoy), AI Cleaner+ (BEGAMOB), Phone Cleaner (Sound Jedi).

**Competitor territories:**

- Cleanup, Cleaner Guru, Cleaner Kit, AI Cleaner: speed, duplicates, one-tap/AI storage recovery, visible GB claims.
- Swipewipe: playful swiping, nostalgia, photo timeline and everyday engagement.
- CleanMyPhone: careful cleaning and preserving memories.
- Clever Cleaner: useful free/basic cleaning, straightforwardness; low-friction competitor to subscriptions.
- Slidebox: manual photo organization rather than just deletion.

**[VISUAL]** Blue/white/purple utility interfaces, storage bars, duplicate-photo grids, progress meters, GB recovery and phone mockups recur. Swipewipe's peach/rainbow style occupies playful emotional territory. No verified quantitative color counts. Exact current US first-three images of all 20 were **not** captured.

### 5.2 Review insights, positive and negative

**[REVIEW]** Frustrations: surprising weekly charges, unclear trial conditions, near-duplicate recommendations that include meaningful photos, inability to preview videos adequately, anxiety about deletion recovery, confusing “free storage” claims, and ads promising more ease than the app delivers. Strong reviews praise quick organization of thousands of photos, grouping, saved time, manual deselection and visible results. Some individual allegations about deletion/data loss are disputed by developers; do not report as systemic failure rates.

**Important technical caveat:** Apple's Photos *Recently Deleted* typically retains deleted photos for 30 days, with iCloud Photos synchronization applying across devices; a cleaner must not imply it provides a proprietary guaranteed restoration system. **Potential cleanup**, **items moved to Recently Deleted**, and **actual storage freed** are distinct states. Apple already offers native duplicate merging and storage optimization.

### 5.3 Explored alternatives and refined favorite

Explored: *Memory Cleaner*, daily 25-photo declutter, storage-by-year time machine, Never Delete protection, explainable AI grouping, storage-recovery planning, honest pricing. **Refinement:** “Memory Cleaner” is already partially occupied; make **user-approved safe cleaning** primary and memory preservation supporting.

**[THESIS]** Lead with recognizable need (free space), then show why the app is safer: explicit category recommendations; distinguish exact duplicates from merely similar images; compare photos at high resolution; default exclude favorited images when appropriate; require approval; explain recovery and synchronization truthfully. Avoid absolute guarantees such as “100% safe” or “recover 12GB instantly” unless validated.

### 5.4 Proposed UX and six storefront screenshots

Product journey: **scan → estimate possible savings → categorize → compare/show why → approve → observe actual freed storage**.

1. **“Find hidden space on your iPhone.”** Large honest estimate, category breakdown and visible review action.
2. **“See exactly what you're deleting.”** Similar-photo contact sheet; “recommended to keep” with explainable rationale; manual compare.
3. **“You decide what stays.”** Review and exclusion indicators; honest Recently Deleted description.
4. “Find the videos taking up the most space.”
5. “Your camera roll, finally organized.”
6. “A little cleaner every week.”

**Visual:** neutral off-white functional UI; restrained confirmation greens; real photographs in review contexts; no decorative synthetic AI assurances. **Working identity:** KeepSpace. **Primary promise:** “Make space. Keep what matters.”

### 5.5 Acquisition and monetization

**Meta tests:**

- **A/control:** “Your iPhone storage is almost full.” → scan → possible GB savings.
- **B/favorite:** “What if your cleaner deletes the wrong photo?” → compare similar photos → approve.
- **C/segment:** “You saved all these screenshots. Now what?” → organize screenshots by usefulness.

**Paywall:** Test paywall-before-scan versus scan/preview-first, free-small-cleanup versus preview-only, annual versus weekly/lifetime, and transparency copy. Track refund rate and **net D30 proceeds/install**, not only trial starts. Public prices previously noted: Cleanup ~$7.99–$11.99/week / $29.99 annual products; Cleaner Guru multiple $4.99–$9.99 products; Cleaner Kit ~$4.99–$6.99 products; Swipewipe ~$4.99–$9.99/week and ~$29.99 annual; Clever Cleaner combines free use and paid options. **Public products only; not observed first-user paywalls.**

**[MODEL]** All-annual $49.99, 1.5% install→paid and 80.75% net retention yields **~$0.61 D30 net RPI**. A $4 CPI would require ~9.9% install→paid *if all payers purchased annual upfront at that price*. Avoid extrapolating this directly to Meta actuals.

### 5.6 KPI and go/no-go

Measure install→scan, scanned→review started, compare→approved, actual MB freed, accidental-deletion support claims, refund rate, trial/paid funnel, D7/D30 return, and **D30 net RPI by Meta creative**. Main risk: a market where photo-organizing differentiation can be copied and where Apple native capabilities offer free alternatives. **Go** only if customer trust can be demonstrated in actual behavior and economics, not by copy alone.

**Primary source starting points:** [Cleaner Guru](https://apps.apple.com/us/app/cleaner-guru-clean-up-storage/id1476380919), [Cleaner Guru screenshots/review summary](https://www.insanelymac.com/blog/cleaner-guru-review/), [Cleaner Kit teardown](https://www.insanelymac.com/blog/cleaner-kit-clean-up-storage-review/), [Swipewipe teardown](https://www.insanelymac.com/blog/swipewipe-photo-cleaner-review/), [Clever Cleaner teardown](https://www.insanelymac.com/blog/clever-cleaner-review/), [Apple Photos support](https://support.apple.com/guide/iphone/delete-or-hide-photos-and-videos-iphb4defbde9/ios).

---

## 6. Category 02 — Calorie Counter

**Status:** Full category strategy completed. **Working brand:** NextPlate. **Tagline:** *Know what fits. Eat what you love.*

### 6.1 Twenty competitor names

MyFitnessPal, Lose It!, Cal AI, MacroFactor, Cronometer, MyNetDiary, YAZIO, Lifesum, Foodvisor, SnapCalorie, Foodnoms, FatSecret, Carb Manager, My Macros+, Healthi, Noom, Nutritionix Track, Eat This Much, Stupid Simple Macro Tracker, WeightWatchers.

**Incumbent territories:** MyFitnessPal—comprehensive platform, Lose It!—accessible weight loss, Cal AI/SnapCalorie/Foodvisor—camera-based entry, MacroFactor—adaptive targets, Cronometer/MyNetDiary—data quality, Lifesum/YAZIO—lifestyle, Noom—behavior, Eat This Much—meal planning. **“AI photo calorie counting,” “ATS-like food scoring,” “simpler tracker,” and “AI next meal” are not unique.** MyFitnessPal markets next-meal advice and planning features.

**[VISUAL]** Palettes vary widely: MFP blue, Lose It! orange, Cal AI white/minimal food, MacroFactor dark analytics, Lifesum green. Repeated screen structures are food photo, calorie number/ring, macro bars, diary, weight graph. Exact 20-app first-three screenshot sequencing was not fully captured.

### 6.2 Reviews: friction, trust, and value

**[REVIEW]** Complaints about food logging taking too many taps after redesigns, inability to trust AI portion estimation, missing cooking oils/sauces, inconsistent barcodes, incorrect serving sizes, food databases with duplicate entries, metric overload, and guilt-inducing streaks. Strengths praised: quick photo recognition, repeat-meal logging, credible/curated food databases, personalized targets, and long-term progress. **AI nutrition data must distinguish photo-based estimates from verified product-label entries**, and show uncertainty rather than fabricated exactness.

### 6.3 Six explored directions

Camera-only tracker; single daily calories-left number; traffic-light nutrition; adaptive budget for dinners out; protein-first tracker; **decision-first nutrition companion**. Original favorite “one-number calorie app” evolved because many incumbents already foreground calorie budgets; final favorite is **decision-first**, subject to validation against MFP and meal-planning competitors.

**[THESIS]** Reframe from **“What did I eat?”** to **“What can I eat next?”**. The home screen should show a user's remaining targets, then practical options based on chosen foods, time and planned evening events. The food diary continues in the background and corrections remain easy. Not medical nutrition advice or a clinically validated solution.

### 6.4 Proposed UX and storefront

Home example: **850 calories available today** (illustrative), dinner choices, actual meal/menu camera, one-tap repeat foods, manageable confidence/portion controls. Avoid large nutrition charts on main screen. Editorial food photography, cream/olive/tomato/sage palette; hidden complexity.

1. **“Know what fits your day.”** Show simple daily budget and meal choices.
2. **“See how your favorite meals fit.”** Real meal, plausible estimate, editable portion.
3. **“Plan dinner in seconds.”** Relevant suggested choices.
4. “Snap it. Check it. Log it.”
5. “Your usual meals, one tap away.”
6. “See progress without the pressure.”

**Ad A/control:** photograph meal → estimated macros. **Ad B/favorite:** “Can pizza fit my goals tonight?” → portion decision. **Ad C:** “Still logging the same breakfast every morning?” → one-tap repeat food.

### 6.5 Economics and testing

Public US examples earlier collected: MFP ~$19.99/month, $79.99/year; MacroFactor ~$11.99/month/$71.99/year; Cronometer ~$10.99/month/$59.99/year; MyNetDiary ~$8.99/month/$59.99/year; Lifesum had $99.99–$119.99 annual listed products. **These are product listing examples, not necessarily current offers**.

Track install→first logged food, AI estimate corrected, repeated meal logging, percentage logging multiple meals on at least three days/week, D7/D30 logging retention, install→trial→paid, actual D30 net proceeds/install. Test photo-first versus dinner-decision storefront; pre-meal vs post-meal sessions; visible range versus false certainty; trial length. **Risk:** behavior changes accrue over days; monetization cannot be inferred from a clever first interaction.

**Starting sources:** [MyFitnessPal](https://apps.apple.com/us/app/myfitnesspal-calorie-counter/id341232718), [Cal AI](https://apps.apple.com/us/app/cal-ai-calorie-tracker/id6480417616), [MacroFactor](https://apps.apple.com/us/app/macrofactor-macro-tracker/id1553503471), [Cronometer](https://apps.apple.com/us/app/cronometer-calorie-counter/id1145935738), [Foodnoms](https://apps.apple.com/us/app/nutrition-tracker-foodnoms/id1479461686), [Foodvisor](https://apps.apple.com/us/app/foodvisor-ai-calorie-counter/id1064020872).

---

## 7. Category 03 — Plant Identifier

**Status:** Full category strategy completed. **Working brand:** Plant ER. **Tagline:** *Find out what's wrong. Know what to check. Follow your plant's progress.*

### 7.1 Twenty competitor names

PictureThis, PlantIn, Plantum, Planta, Plant Parent, Blossom, Plant App, Plantify, LeafSnap, Greg, Flora, PlantSnap, PlantNet, Seek by iNaturalist, iNaturalist, PlantAI, Photone, Happy Plant, GrowIt, Planter.

**Incumbent territories:** PictureThis/PlantIn—identify and diagnose, Plantum/Plantify—AI identification, Planta/Greg/Plant Parent/Blossom—care and reminders, Seek/PlantNet/iNaturalist—free biodiversity identification, Photone—light measurement, Flora/Happy Plant—gamified care. AI identification, disease diagnosis, watering reminders and plant journals are all **established**.

**[VISUAL]** Botanical green/mint, big healthy leaves, camera scanning, encyclopedia detail, watering calendars, cheerful pet-care tone. The opportunity is to lead with symptomatic plant imagery and a calm structured diagnostic flow, not generic plant taxonomy.

### 7.2 Reviews and trust issues

**[REVIEW]** A PlantIn reviewer described following watering guidance but watching a plant deteriorate; Planta users describe schedules needing adjustment to household conditions and season; people complain of generic advice (“water/light/soil”), redundant subscription prompts, and tracking apps that become chores. Positives: personalized reminders, plant collection, photographs, notes and practical guidance. Symptoms such as yellow leaves may arise from several causes; **photo-only causal diagnosis is unsafe to treat as certain**.

### 7.3 Explored alternatives and favorite

Plant ER symptom-first assessment; Tamagotchi-like collection; recovery diary; condition-based care; beginner simplified UI; generic garden management. **Favorite: Plant ER + recovery monitoring**, not “identify the plant name.”

Journey: photograph symptom → ask contextual soil/light/drainage/recent-change questions → show potential causes/uncertainty → suggest grounded low-risk checks → schedule follow-up → compare user-submitted observations. Avoid guaranteeing that damaged leaves will re-green, promising diagnoses, or a medical-like recovery score without evidence.

### 7.4 Proposed storefront

1. **“Why are your plant's leaves turning yellow?”** Symptom-focused houseplant photo.
2. **“Understand what to check first.”** Soil moisture, light, drainage checkcards.
3. **“Follow your plant's progress.”** Dated before/follow-up photos and actions.
4. “Know when to check your plants.”
5. “All your plants, in one place.”
6. “Identify plants in seconds.”

**Visual:** cream, deep forest, restrained terracotta problem indicators, soft mint progress; supportive diagnostic UI rather than overwhelming encyclopedia.

### 7.5 Acquisition, pricing, retention

**Meta A/control:** “What's this plant called?” **B/favorite:** “Your plant is turning yellow. Why?” **C:** “Stop watering your plants just because it's Tuesday.”

Public pricing examples earlier recorded: PictureThis premium products ~$39.99, ~$49.99 family; PlantIn ~$6.99–$8.99 weekly, ~$29.99 annual, ~$49.99 lifetime; Planta ~$7.99–$9.99 monthly, ~$35.99–$47.99 yearly. **Test offers, not validated economics:** $39.99 annual care, $7.99 monthly, $4.99 one-time report. Early assessment should give some usefulness before premium plan. Episodic identifiers may fail to become retained plant collectors. KPIs: first completed assessment, plant added, follow-up submitted, second plant added, D7/D30 retained, paid conversion, D30 net proceeds/install. Start with common US houseplants and frequent symptoms; don't build universal plant encyclopedia.

**Starting sources:** [PictureThis](https://apps.apple.com/us/app/picturethis-plant-identifier/id1252497129), [PlantIn](https://apps.apple.com/us/app/plantin-plant-identifier-care/id1527399597), [Planta](https://apps.apple.com/us/app/planta-plant-garden-care/id1410126781), [Plantum](https://apps.apple.com/us/app/plantum-ai-plant-identifier/id1476047194), [Plant Parent](https://apps.apple.com/us/app/plant-parent-plant-care-guide/id1612792132), [Plantify](https://apps.apple.com/us/app/plantify-ai-plant-identifier/id6474967729).

---

## 8. Category 04 — Habit Tracker

**Status:** Full strategy completed. **Working brand:** Again. **Tagline:** *The habit tracker that helps you start again.*

### 8.1 Twenty competitor names

Productive, Streaks, Habitify, HabitKit, everyday, Strides, Do Habits, Way of Life, Atoms, (Not Boring) Habits, Fabulous, Routinery, RoutineFlow, Finch, Habitica, Habit Rabbit, Tangerine, Avocation, HabitShare, Coach.me.

**Incumbent territories:** Streaks/everyday—unbroken chains; HabitKit/Way of Life—heatmaps; Habitify—multi-device and some automatic logging; Atoms/Fabulous—behavior coaching; Routinery/RoutineFlow—timed step sequences; Finch/Habitica/Habit Rabbit—gamified care; HabitShare—social accountability; (Not Boring) Habits/Avocation/Do Habits—anti-streak/flexible approaches. **Anti-streak, autopilot and game mechanics are not unique.**

**[VISUAL]** Crowded with sophisticated styles: circles, dark colorful heatmaps, character pets, planners, minimalist timers, editorial guidance. Color alone is unlikely to stand out. Unusual primary screen: the moment a person **returns after a gap**.

### 8.2 Reviews and learning

**[REVIEW]** People abandon tracker after missing a few days, lose streak and feel demotivated, dismiss routine reminders, find the tracking itself burdensome, dislike inflexible daily scheduling or busy coaching interfaces. Positives: fast check-off, visible progress, satisfying sound/haptics, emotional attachment to a pet, and accountability with friends. **Do not equate losing a streak with losing actual historical progress.**

### 8.3 Explored directions and favorite

One Habit; automatic HealthKit measurement; streak-free consistency; why-I-failed behavior analytics; social buddy; RPG; **Comeback Coach**. **Favorite** is personalized restart workflow, not the phrase “no guilt.”

Core flow: create one habit → set normal goal **and tiny backup version** → track normally → after missed sessions ask one light-friction obstacle question → offer smaller attainable restart or schedule adjustment → preserve long-term history and celebrate a genuine return. Example workout goal 45 minutes, backup 10 minutes. Don't infer causal behavioral patterns from two observations.

### 8.4 Proposed storefront

1. **“Missed a few days? Your progress isn't gone.”** Interrupted timeline and return action.
2. **“Get back on track in two minutes.”** Smaller next action.
3. **“Learn what helps you stay consistent.”** Evidence-based completion pattern.
4. “Track progress without starting over.”
5. “Make your goals fit real life.”
6. “Check in with one tap.”

**Visual:** warm cream/forest/terracotta/charcoal; gaps in progress remain visible; returning after a gap represented as continuation rather than reset. Avoid punitive messaging and designing a product that requires daily attention to the tracking itself.

### 8.5 Acquisition, pricing and measurement

**Meta A/control:** “Build habits that last.” **B/favorite:** “Why do you always restart your habits on Monday?” **C:** “Maybe your habit isn't the problem. Maybe your schedule is.”

Public price examples previously captured: Streaks ~$5.99 one-time; HabitKit ~$11.99/year and $29.99 lifetime; everyday ~$29.99/year; (Not Boring) Habits ~$14.99/year; Atoms ~$39.99/year; Habitify ~$49.99/year; Fabulous/Productive/Finch various annual tiers. Many cheap or free substitutes limit subscription willingness to pay. Proposed test: free basic, premium flexible coaching ~$39.99/year or ~$6.99/month; hypothetical lifetime ~$79.99.

**North Star hypothesis:** **habit recovery rate** = users who miss ≥3 scheduled opportunities and resume within the following seven days / users who miss ≥3 scheduled opportunities. Also measure daily active, D30 retention, paid retention, cost per retained habit user, D30 net RPI. **Risk:** the distinctive recovery feature may not appear until well after the trial; demonstrate the backup habit during onboarding. Experiment with recovery prompt vs generic reminder; fixed vs adaptable goals; early paywall vs value demonstration.

**Starting sources:** [Streaks](https://streaksapp.com/), [Habitify](https://www.habitify.me/), [HabitKit](https://habitkit.app/), [Atoms](https://atoms.jamesclear.com/), [Fabulous](https://www.thefabulous.co/), [Finch](https://finchcare.com/).

---
## 9. Category 05 — Fax

**Status:** Full strategy completed. **Working brand:** Fax Concierge. **Tagline:** *Important documents. Handled.*

### 9.1 Twenty competitors

FAX from iPhone: Send Doc App (Municorn), iFax, Fax.Plus, Tiny Fax, FaxBurner, Genius Fax, eFax, MyFax, FAX from iPhone & iPad (BP Mobile/AIBY), FAX for iPhone (7270356 Canada), FaxFile, EaseFax, Fax from iPhone: Free of ad (Must Have Apps), Send Fax App (Madduck), FAX from iPhone – Send Doc (Octagonlab), Fax From iPhone: Send & Receive (Ringtones LLC), Send Fax From iPhone Now (Sparktonic), Easy Fax (CoolMobileSolution), FaxPal, Cheapfax.

**Existing positions:** Municorn/BP Mobile/Tiny Fax—“fax machine on phone”/scan-send; iFax/eFax/Fax.Plus—professional/security and enterprise; Genius Fax/FaxPal/FaxFile/EaseFax/Cheapfax—credits or pay-as-you-go; FaxBurner/Fax.Plus—delivery status/receipt. **Fax tracking, delivery confirmation, and pay-per-fax already exist.**

**[VISUAL]** Dark/blue/white office utility, document icons, send fax flow, signatures, shields and completed checkmarks. Not every current first-three-image position was verified. Working alternative: a credible logistics-like **document transmission journey**, rather than a physical fax machine.

### 9.2 Reviews and customer job

**[REVIEW]** Customer usually needs one important medical/insurance/administrative form sent urgently. Frustrations: forced weekly subscription for one use; paid fax fails or takes multiple attempts; uncertainty about receipt; trial cancellation disputes; sensitive documents; confusing failure statuses. Praised: affordable per-use, clear confirmation, reliable fast delivery, responsive support. 

**Critical legal/technical distinction:** A provider's positive **fax transmission confirmation** does **not** establish that an employee read or processed the document, or that it legally satisfied a deadline. Avoid promise “recipient processed paperwork.” Healthcare-data protection and HIPAA/business associate requirements depend on who uses the service, the service's role, and the actual processing relationship; do not claim blanket compliance from a padlock icon.

### 9.3 Explored concepts, refined favorite, UX

“FedEx for Fax” delivery tracking; Pay-per-Fax; templates by recipient type (medical, insurance, government, legal); Scan/sign/fax; **Fax Concierge** end-to-end. Refined because status and credits are existing features. Distinguish via **preparation, disclosed price, accurate technical status, meaningful failure path, receipt storage** in one understandable experience.

Flow: **choose task or skip to direct fax → scan/import → preview pages → enter recipient number → display full price and conditions → transmit → accurate status events → downloadable technical confirmation → actionable retry/support on failure**.

- Format-valid phone number is **not verified ownership** of recipient.
- Error messages only show actual provider return codes; distinguish busy, disconnected, unsupported numbers if reliable.
- Status must not be simulated. Claims about refund/credit protection must match policy.
- Retention/deletion and sensitive records handled transparently.

### 9.4 Proposed storefront

1. **“Important documents. Sent with confidence.”** Transmission confirmation state.
2. **“Scan, sign and send in minutes.”** Preparation workflow.
3. **“Know exactly what happened.”** Actual transmit timeline and report.
4. “See the price before you send.”
5. “If it fails, we'll help you retry.”
6. “Your fax history, organized.”

**Visual:** navy/cloud/teal/confirmation-green; avoid overclaiming legal receipt. Primary UI views: intent selector, preview/price, sent/failed state.

### 9.5 Monetization and experiment

Public US IAP examples in earlier audit: Municorn ~$9.99/week, ~$29.99/month, ~$249.99/year; iFax ~$9.99 weekly/$24.99 monthly; Tiny Fax ~$6.99 weekly/$19.99 monthly/$79.99 annual; Fax.Plus Basic ~$8.99/month, Premium ~$17.99/month; Genius Fax ~$0.99 credit and ~$6.99/10 credits; Cheapfax advertises ~$0.50/page. Vendor API example Telnyx public rate ~$0.007 per page **plus SIP/transmission charges**; **not an all-in fax operating cost**.

**[THESIS]** Segment occasional one-time payers from recurring business users. Test hypothetical ~$4.99 per transaction versus ~$12.99/month recurring plan. Test subscription-first vs transaction-first on D30 **net** contribution including fax-provider charges, failures, support and refunds. **Ad A/control:** “Send a fax from your iPhone.” **B/favorite:** “Your insurance paperwork has been sent. Here's your confirmation.” **C:** “Need one fax? Pay for one fax.” High-intent search/Apple Search Ads may be more natural than broad Meta for urgent fax needs.

Metrics: successful transmissions/paid transaction, first attempt success, retry recovery, mean pages, API spend/pages, refund/contact rate, transaction contribution, D30 net RPI; distinguish **success** and **recipient processed**.

**Starting sources:** [Municorn](https://apps.apple.com/us/app/fax-from-iphone-send-doc-app/id978931264), [iFax](https://apps.apple.com/us/app/ifax-app-send-fax-from-iphone/id331514859), [Fax.Plus](https://apps.apple.com/us/app/fax-plus-receive-send-fax/id1170782544), [Tiny Fax](https://apps.apple.com/us/app/tiny-fax-send-fax-from-iphone/id675468902), [FaxBurner](https://apps.apple.com/us/app/fax-burner-iphone-fax-app/id392640124), [Genius Fax](https://apps.apple.com/us/app/genius-fax-faxing-app/id566504821), [FaxPal](https://apps.apple.com/us/app/faxpal-quick-fax/id6761170777).

---

## 10. Category 06 — Baby Tracker

**Status:** Full strategy completed. **Working brand:** Together. **Tagline:** *One baby. Everyone on the same page.*

### 10.1 Twenty competitors

Huckleberry, Baby Tracker – Newborn Log (Nighp), Sprout Baby Tracker, Nara Baby, Baby Connect, Cubtale, Glow Baby, Baby Daybook, Talli Baby, Napper, Onoco, BabyTime, Baby Tracker My Baby (Aleksei Neiman), Just Hatched, BabyTrack, Baby Tracker Pro & Newborn Log, BabyTracker – Feeding & Diaper, Baby Feed Timer – Lunama, Baby Signal, Simply Baby Tracker.

**Public positioning:** Huckleberry—tracking plus SweetSpot nap prediction and premium sleep guidance; Napper—sleep planning; Baby Connect/Nara/Cubtale/Onoco/Baby Daybook—shared caregiver information; Sprout/Nighp—comprehensive logs; Nara—calm aesthetic; Talli—low-friction logging. **Shared family logs and voice logging already exist.** Nighp/Huckleberry have substantial cumulative US rating bases; historical ratings are not MAU.

**[VISUAL]** Pastel teal/blue/pink/peach, baby's photo, feed/sleep/diaper icons, last-event timestamp, chronological logs, sleep report. More meaningful differentiator: organize around **right now / my turn / handoff** rather than isolated tracking database tables.

### 10.2 Review insights

**[REVIEW]** Sleep-deprived parents forget when they fed or changed baby; want trustworthy caregiver sync and seamless overnight handoff; some report sync timestamp errors or disappearing filter views; too many prompts and charts can raise anxiety; some parents gradually need less exhaustive tracking. Positive: quick one-handed feeding logs, partner sharing, useful pediatrician records, sleep guidance where appropriate, and peace of mind. The product should reduce mental effort, not pressure parents to obsessively log every detail.

### 10.3 Refined opportunity and UX

Ideas evaluated: one-screen Baby Cockpit, Night Shift, voice input, shared timeline, **caregiver handoff**, calming selective tracking. **Favorite:** a brief for the next caregiver, not a simple shared activity log. Flow:

**record basic events → assign/present current caregiver context → summarize actual recorded feed/sleep/diaper events and caregiver notes → invite other caregiver → “I'm taking over” → link summary to original timestamps/entries**.

- Every underlying event retains who recorded it and the actual timestamp.
- Summaries must not invent unlogged feeding or medicine details.
- Medication logs are not a basis for AI dosage instructions; display recorded facts, defer clinical care to clinicians.
- Baby sleep predictions are estimates, not medical directives.
- Explicit access control, revocation, export, timezones, offline sync and concurrency resolution matter.

### 10.4 Screenshots and design

1. **“One baby. Everyone on the same page.”** Baby status cockpit.
2. **“Know what happened while you were away.”** Overnight handoff summary.
3. **“Take over without asking 10 questions.”** Caregiver accepts responsibility for logging a shift.
4. “Log with one hand. Even at 3 AM.”
5. “Share care with the people you trust.”
6. “Track what's important. Skip the rest.”

**Visual:** sage/cream/terracotta plus dark navy one-hand night mode, large tap targets, information hierarchy optimized for 3 AM.

### 10.5 Monetization, model correction and funnel

Public US price examples: Huckleberry Plus ~$11.99/month or $68.99/year, Premium ~$14.99/month or $119.99/year; Baby Connect Family ~$6.99/month/$49.99 annual; Onoco ~$8.99/month/$59.99 annual; Cubtale ~$6.99–$8.19/month/$49.99 annual; Napper ~$14.99/month/$89.99 plan; Nara various ~$6.99–$9.99 products/lifetime; Baby Daybook varied products.

**[THESIS]** Free core logging and basic sharing; premium AI-free/AI-assisted handoff summaries, caregiver workflow and advanced reports, at illustrative ~$49.99–$69.99 annual or ~$7.99 monthly. Challenge: paying only for a generated paragraph is unlikely sustainable when free shared logging exists. Must show genuinely reduced coordination effort.

**[MODEL, reconciled]** The original worked baby-tracker panel assumed **5% install→trial × 35% trial→paid = 1.75% install→paid (17.5 expected payers/1,000)**, a 70% annual mix at $65 and 30% monthly at $9.99. The result is **0.0175 × ($45.50 + $2.997) × 0.8075 = ~$0.69 net D30 RPI.** Under a separate assumption of **2.1%** install→paid with the same price mix, the answer would be **~$0.82**. Keep funnel and arithmetic paired; do not switch the paid-conversion numerator mid-calculation.

**Meta A/control:** “Remember every feed, nap and diaper.” **B/favorite:** “What happened while I was sleeping?” → partner handoff. **C:** “Track your newborn with one hand.”

Metrics: D7/D30 **family** retention, invite acceptance, second caregiver active rate, handoffs/week among active multi-caregiver families, trial/paid, cohort net proceeds/install, plus permission/reliability support. Category has finite newborn lifecycle; measure realistic cohort duration rather than perpetual retention.

**Starting sources:** [Huckleberry](https://apps.apple.com/us/app/huckleberry-baby-tracker/id1169136078), [Baby Connect](https://apps.apple.com/us/app/baby-connect-newborn-tracker/id326574411), [Cubtale](https://apps.apple.com/us/app/cubtale-baby-tracker/id1541460870), [Napper](https://apps.apple.com/us/app/napper-baby-sleep-tracker/id1491340863), [Nara Baby](https://apps.apple.com/us/app/nara-baby-pregnancy-tracker/id1444639029), [Baby Daybook](https://apps.apple.com/us/app/baby-daybook-newborn-tracker/id1446283219).

---

## 11. Category 07 — Sleep Tracker

**Status:** Full strategy completed. **Working brand:** Tonight — Sleep Detective. **Tagline:** *Stop tracking bad sleep. Start improving it.*

### 11.1 Twenty competitors

Sleep Cycle, SleepWatch, AutoSleep, Pillow, ShutEye, SleepScore, Sleepzy, NapBot, Sleep++, Sleep Tracker: Recorder, Sound (Leap Health), RISE, BetterSleep, SnoreLab, Sleep Reset, Sleep.com, Prime Sleep Recorder, Oura, Bevel, Athlytic, Sleepbot.

These span phone-only, Watch-based, standalone wearable, snore-specific, and behavioral sleep products. **Apple's native Sleep Score in watchOS 26** materially complicates basic third-party scoring. **RISE already gives forward-looking advice; SleepScore/Pillow/SleepWatch interpret data; SnoreLab already encourages remedy comparison.** The gap is narrower than generic sleep coaching.

**[VISUAL]** Navy/black/purple, big sleep score, stage charts, nightly histograms, orange/teal sleep indicators, smart alarm, reports. New framing: **tonight's useful experiment**, not last night's score. Wearable limitations need clear disclosure.

### 11.2 Reviews and product-quality lessons

**[REVIEW]** Scores may disagree with how rested users feel; some wearables/apps miss awakenings or second sleep periods; recordings/alarms may be unreliable; users question how scores are calculated; subscription resentment especially against native or low-priced alternatives. Strengths: automated logging, understandable trends, sleep-sound library, practical personalized suggestions. Avoid making every user feel they “failed” a score. Sleep logs are imperfect observations, not clinical diagnoses.

### 11.3 Explored concepts and refined favorite

No Sleep Score; Sleep Detective; tonight-first planner; environmental/noise detective; sleep recovery; snoring. **Favorite:** simple personal behavioral experiments using available HealthKit history, with transparent caveats. Flow:

**Import sleep history (consent) → subjective restedness check → identify one low-risk behavior → choose a 7-night observation → check compliance lightly → compare baseline with subsequent nights → show sample size and uncertainty → choose next step**.

Example hypothesis: earlier caffeine cutoff may associate with improved duration for that individual. **Do not infer causation from a tiny uncontrolled study.** Do not market as an insomnia or sleep-apnea diagnosis/treatment, or substitute for medical evaluation. Avoid custom alarm in MVP because reliability obligations are high.

### 11.4 Proposed storefront

1. **“You know you slept badly. What can you try tonight?”** A short understandable report.
2. **“Discover which habits may affect your sleep.”** One experiment.
3. **“See what changed over seven nights.”** Non-causal observation vs baseline.
4. “All your sleep data. None of the overwhelm.”
5. “Understand your nights without another score.”
6. “Build a bedtime routine that fits your life.”

**Visual:** midnight navy/cream/sage/slate, spacious editorial type, no giant proprietary 74/100. **Meta A/control:** “Find out how well you really slept.” **B/favorite:** “You know you slept badly. What should you try tonight?” **C:** “Your Apple Watch knows how you slept. Now put that data to work.”

### 11.5 Prices and economics

Examples collected: AutoSleep ~$8.99 one-time; SleepWatch ~$4.99 monthly/$39.99 annual; Pillow ~$19.99 monthly/$49.99 annual product; ShutEye ~$9.99 monthly/$59.99 annual; RISE up to ~$69.99 annual; SleepScore ~$9.99 monthly/$59.99 annual; SnoreLab ~$7.99 monthly/$39.99 annual. Public App Store product examples only.

**[MODEL]** I→trial 6%, T→P 35%, hence I→paid **2.1%**. Annual mix 80% at $59.99, monthly 20% at $9.99, 0.8075 net → **~$0.85 D30 RPI**. Conversion and CPI must be measured in actual cohorts. Suggested premium experiments ~$49.99 annual/$7.99 monthly, with basic data views free.

KPIs: Health authorization, data availability, first experiment created, completed experiment, second experiment started, user-reported usefulness (without implied clinical outcomes), paid conversion, D30 net proceeds/install. Risk: delayed experiment value, Apple's built-in analysis, expensive free/one-time alternatives, sleep anxiety from overtracking, medical claims.

**Starting sources:** [Apple sleep tracking and score support](https://support.apple.com/guide/watch/track-your-sleep-apd830528336/watchos), [AutoSleep](https://autosleepapp.tantsissa.com/), [SleepWatch](https://www.sleepwatchapp.com/), [Pillow](https://pillow.app/), [RISE](https://www.risescience.com/), [SleepScore](https://www.sleepscore.com/), [SnoreLab](https://www.snorelab.com/).

---

## 12. Category 08 — Universal TV Remote

**Status:** Full strategy completed. **Working brand:** Remote Ready. **Tagline:** *Your TV. Connected. Ready.*

### 12.1 Twenty competitors and additional free incumbents

TV Remote – Universal Control (EVOLLY), Universal Remote TV Control (BEGAMOB), Universal TV Remote (Kraftwerk 9), Rokie (Kraftwerk 9), Smartify (Kraftwerk 9), Remotie (Kraftwerk 9), Universal Remote・TV Control (Ozuna), TV Remote for Roku Devices (Ozuna), TV Remote for Roku (Netsis), Remote for Firestick (Netsis), Universal Remote TV Control (Desidari), Unimote (Yohan Teixeira), Universal Remote for Roku TV (Yohan Teixeira), RoByte (Tinybyte), Universo (Nemo Apps), TVRem (Electronic Team), Any TV Remote (Klebo), TV Remote • Universal Control (WarthogLab), TV Remote Control – Universal (Remote Sunrise), TV Remote – Universal Control (Fire Technologies).

**Critical free alternatives not in 20:** official Roku app, Amazon Fire TV app, Samsung SmartThings, LG ThinQ and Apple's built-in Apple TV Remote/Control Center. A paid generic remote must offer meaningful convenience and/or support for multiple ecosystems. Swiping, touchpads, app launching, keyboard and multi-TV switching are **already present** among third-party apps (Kraftwerk 9, RoByte, EVOLLY, etc.).

**[VISUAL]** Purple/dark-blue/black backgrounds, TV-brand logos, physical D-pad, volume keys, on/off and app tiles; some newer touchpad-based UI. Proposed visual status taxonomy: verified/supported/not-tested/unavailable/connected.

### 12.2 Review-driven opportunity

**[REVIEW]** Users discover incompatibility after paying; device works day 1 but disconnects later; network wake-on command unavailable for some TV configurations; paywall interrupts every remote press; purchases don't unlock expected actions; unclear brand support. Praised: immediate pairing, reliable repeat connection, large controls, one app for several TVs, accessible UI. Some power-on limitations are inherent to TV firmware/network standby/CEC/IR and are **not fixable by app-side UI**.

### 12.3 Refined concept and experience

Earlier favorite “Eyes-Free Remote” found to be existing competitor capability. Refined to **Connect & Prove** + **pleasant eyes-free mode**.

Onboarding: **request iOS local-network permission with explanation → discover supported device → pair via verified platform pathway → user sends harmless test navigation → ask user to confirm TV actually responded → present exact supported/unsupported commands → optional premium offer**.

Returning user: direct launch to remote of last paired TV; automatic reconnection; meaningful troubleshooting on failure. Touchpad plus classic D-pad accessibility option. Disabled keyboard/power commands for unsupported devices. Brand/device-specific adapters and regression testing lab required; don't claim all TVs or all commands work.

### 12.4 Proposed storefront and ads

1. **“Find your TV. Test the remote.”** Verified command.
2. **“Your favorite controls, one swipe away.”** Touchpad plus essentials.
3. **“Reconnect without the hassle.”** Clear diagnostic states.
4. “One remote for your household.”
5. “Type on your phone, not your TV.”
6. “Know exactly which features work.”

**Meta A/control:** “Lost your TV remote?” **B/favorite:** “Will a remote app actually work with your TV?” → show genuine first successful command. **C:** “A remote you don't have to look at.” TV ecosystem-specific App Store Custom Product Pages: Samsung/LG/Roku/Fire TV/Google TV where supported, *without suggesting brand affiliation*.

### 12.5 Pricing, D30 and technical go/no-go

Public US prices earlier captured: EVOLLY ~$6.99/week/$39.99 annual/$44.99 lifetime; BEGAMOB ~$9.99 weekly/$29.99 annual; Kraftwerk 9 products ~$2.99–$5.99 weekly/$34.99 annual/$14.99 lifetime; RoByte some ~$3.99/$23.99 products; TVRem advertised free use. **Plan shown to first-time user may differ.**

**[MODEL]** I→trial 5%, T→P 30%=1.5% paid; 70% annual $39.99 +30% monthly $8.99 ×0.8075 ⇒ **~$0.37 D30 net RPI**. All-annual $39.99 case requires **~6.2% I→paid at $2 CPI** and **~9.3% at $3**. High price sensitivity from official free apps.

Metrics: permission success, device discovered, paired, **first verified working command**, next-day reconnection, paid conversion per TV ecosystem, refunds/support by device family, D7/D30 actual remote usage, D30 proceeds/install. Build a representative physical hardware test bench before wide UA. **Go/no-go:** reliable discovery/pair/control/reconnect on targeted hardware, low returns and support; otherwise visual polish is irrelevant.

**Starting sources:** [EVOLLY](https://apps.apple.com/us/app/tv-remote-universal-control/id1539090879), [BEGAMOB](https://apps.apple.com/us/app/universal-remote-tv-control/id1581765635), [Kraftwerk 9](https://apps.apple.com/us/app/universal-tv-remote/id1439422220), [RoByte](https://apps.apple.com/us/app/robyte-remote-for-roku-tv-app/id1099541177), [Roku official](https://www.roku.com/mobile-app), [Amazon Fire TV official](https://www.amazon.com/gp/help/customer/display.html?nodeId=GJQ2KD6W4CLLPJPA), [Apple TV Remote](https://support.apple.com/en-us/108778), [Apple Local Network permissions](https://support.apple.com/en-us/102229).

---
## 13. Category 09 — Recipe Importer

**Status:** Full strategy completed. **Working brand:** Cooked. **Tagline:** *Saved it. Cook it.* / *Less saving. More cooking.*

### 13.1 Twenty competitors

ReciMe, Paprika, Recipe Keeper, Pestle, Crouton, Mela, CookBook, Umami, Deglaze, Flavorish, Stashcook, Just the Recipe, Reciply, AnyList, Samsung Food, MealBoard, Plan to Eat, Cooklist, Copy Me That, Prepear.

**Incumbent territories:** ReciMe/Pestle/CookBook/Flavorish—social/import; Paprika/Mela/Recipe Keeper—permanent digital cookbook; Pestle/Crouton—guided cook mode; MealBoard/Plan to Eat—calendar, meal queues and groceries; AnyList—household grocery list; Cooklist—pantry awareness; Just the Recipe—remove blog distractions. **Import Instagram/TikTok, generate grocery lists, and generic “what should I cook?” are not unique.**

**[VISUAL]** Social-save cards, digital cookbook grids, editorial food photography, green/cream or functional calendar/grocery interfaces. Avoid replicating the incumbent first-three hero images “import → save → grocery.”

### 13.2 Customer reviews and deeper job

**[REVIEW]** People save hundreds of recipes and prepare very few; forget which of several pasta recipes they liked; find imports with missing oil, wrong quantities or unreliable video transcription; dislike mandatory full-week meal planning; don't know ingredients they have; worry about losing a treasured library. Positives: rapid import, source attribution, easy retrieval, hands-free step-by-step, private annotations, personal cookbook that accumulates value for years. **An imported recipe should distinguish source-extracted quantities from AI-inferred quantities.**

### 13.3 Explored concepts and refined favorite

Recipe Inbox; Mise-en-place/prep mode; Taste memory; “What's for dinner?”; **Saved → Cooked**. Refined favorite combines **Inbox → Want to cook queue → Tonight decisions → Cooked/favorite + My Version**.

Primary flow: **share a Reel/site/screenshot → review extraction → put recipe in inspiration or cooking queue → narrow tonight's possibilities by time/ingredients/diet → cook → preserve adjustments and ratings → promote proven recipes to family favorites**.

A user's favorite adapted recipe has higher retained value than an unedited link to a blog post. Be wary of calling AI pantry availability “verified” without user input or dependable integrations.

### 13.4 Six storefront screenshots and visual direction

1. **“You saved 100 recipes. Let's cook one.”** Inspiration / want-to-cook / cooked count.
2. **“Find something to make tonight.”** Filters by time, ingredients and mood.
3. **“Keep the recipes your family actually loves.”** Cook history and personal notes.
4. “Import from Instagram, TikTok and more.”
5. “Everything you need, in one cooking view.”
6. “From saved recipe to grocery list.”

**Visual:** creamy paper/olive green/tomato red/honey, clear food photography, visible distinction between saved inspiration and cooked favorites. **Meta A/control:** “Save any recipe from Instagram.” **B/favorite:** “You've saved hundreds of recipes. How many have you cooked?” **C:** “What can I make tonight from my saved recipes?”

### 13.5 Public pricing examples and D30

Paprika ~$4.99 once; Mela ~$6.99 premium unlock; Recipe Keeper ~$19.99 Pro; AnyList ~$9.99/year individual/$14.99/year household; Pestle ~$24.99/year/lifetime products ~$39.99–$49.99; Crouton ~$14.99 annual; MealBoard ~$12.99 upgrade; ReciMe public IAPs include ~$39.99 and ~$59.99 Plus products (offer eligibility differs); Plan to Eat website ~$49/year and separately listed iOS price ~$54.99/year. Extremely inexpensive incumbents challenge subscription pricing. **One-off importer features may have weak subscription justification.**

**[MODEL]** 5% I→trial, 30% trial→paid (1.5% I→paid), 75% annual at $39.99, 25% monthly at $5.99, factor .8075 ⇒ **~$0.38 net D30 RPI**. Proposed price tests: free limited collection; ~$39.99 annual; ~$5.99 monthly; hypothetical ~$79.99 lifetime. Validate willingness to pay with working imported recipes, not surveys alone.

Metrics: install→successful import, source-specific import success/correction and AI processing cost, import→queue, **saved-to-cooked rate (recipes cooked within 30 days)**, first→second cooked recipe, repeat cooking, D30 paid proceeds/install. Avoid initial build of retailer/pantry real-time sync, general AI chef chatbot, proprietary recipe social network or overbroad nutrition. Social-platform import APIs and copyright/source attribution are real constraints.

**Starting sources:** [ReciMe](https://recime.app/), [Paprika](https://www.paprikaapp.com/), [Pestle](https://pestlechef.app/), [Crouton](https://crouton.app/), [Mela](https://mela.recipes/), [AnyList](https://www.anylist.com/), [Plan to Eat](https://www.plantoeat.com/), [MealBoard](https://www.mealboard.com/).

---

## 14. Category 10 — Document Scanner / PDF Toolkit

**Status:** Full strategy completed. **Working brand:** ReadyPDF. **Tagline:** *Your document. Ready for the next step.*

### 14.1 Twenty competitors and default-free substitutes

Adobe Scan, CamScanner, iScanner, Genius Scan, Scanner Pro, Tiny Scanner, SwiftScan, TapScanner, Scan Hero, Mobile Scanner (Glority), TurboScan Pro, vFlat Scan, Scan Shot, QuickScan, Adobe Acrobat Reader, PDF Expert, PDFgear, Smallpdf, Xodo, UPDF. Additional: Foxit, Wondershare PDFelement. **Apple Preview/Files/Notes** provide native scan, fill and sign; PDFgear markets free PDF editing. Category contains many very large established user bases and strong free substitutes.

**Territories:** Adobe/CamScanner/iScanner—feature-rich toolboxes; Genius Scan/Scanner Pro—dependable scanning, local enhancement, automation; SwiftScan—scan/edit/send; vFlat—curved page/book flattening; Adobe/PDF Expert/UPDF—professional editing; PDFgear—free general-purpose tools. **iScanner already has Scan-to-Sign; task-first UI alone is not novel.**

**[VISUAL]** Blue/purple gradients, scanner frame, phone showing PDF pages, signature tools, floating documents, huge proof claims. Proposed identity: **document readiness checklist** with transparent pass/review/not-checked states.

### 14.2 Reviews and trust

**[REVIEW]** PDF too large to share/upload; scan quality or page skew; premium purchase fails to unlock; difficulty restoring saved documents; dislike weekly paywall for occasional task; anxiety about storage location and sensitive files. Positives: reliable edge detection, quick OCR, multiple pages, clear sharing/export and local processing. There is not yet hard evidence for the *frequency* of rejected submissions due to page-order/size/etc.; treat it as a product hypothesis.

### 14.3 Refined thesis: Submission Ready

Generic Scan→Edit→Sign/Compress toolbar is established. More specific product: **choose a target task → scan/import → specify or retrieve verified requirements → assemble and prepare → run technical checks → human review → export**.

Examples of *verifiable* checks: file type, file size against explicitly specified maximum, page count, portrait/landscape heuristic, OCR text layer where available. **Human review** for correct content, signature appropriateness, correct person, completeness. **Cannot guarantee** recipient acceptance, agency processing, or legal sufficiency.

**Important:** don't require “choose a task” for someone who merely needs immediate scanning. Keep prominent quick-scan path.

### 14.4 Proposed storefront

1. **“Your PDF. Ready for the next step.”** Prepared file with checklist.
2. **“Scan, sign and organize in one flow.”** Guided document preparation.
3. **“Check the file before you send it.”** MB limit/format/readability with proper caveats.
4. “Fit the file-size limit.”
5. “Catch pages that need attention.”
6. “Save and share with confidence.”

**Visual:** paper/ink/teal status/amber review. UI mockup steps: choose document job, checklist distinguishes auto-verifiable and review-required, output “technical checks passed / your confirmation required / recipient not verified.”

### 14.5 Meta, pricing, unit economics and KPIs

**Meta A/control:** “Turn your iPhone into a document scanner.” **B/favorite:** “Your PDF is too large to upload?” → fit stated MB limit. **C:** “Three documents. One PDF. Ready to share.” → multi-stage completion.

Public US examples in previous audit: Adobe Scan ~$9.99 monthly/$49.99 premium; Genius Scan ~$4.99 and $39.99 Ultra products; Scanner Pro ~$7.99/$29.99/$59.99 Plus products; SwiftScan ~$5.99 monthly VIP/$34.99 annual; CamScanner ~$9.99 monthly/$59.99 annual products; Scan Hero ~$7.99 weekly trial/$14.99 monthly; PDFgear free. Public IAP listing does **not** establish which is live.

Possible test: free basic scanning, **one-time premium preparation ~$6.99–$9.99**, monthly ~$9.99 or annual ~$59.99 for frequent pro use. One-time $9.99 purchase at **4% install→purchase** nets about **$0.32 RPI** with illustrative .8075 factor. Subscription case **6% trial × 35% paid =2.1%**, annual mix 70% at $59.99 + monthly 30% at $9.99 ⇒ **~$0.76 RPI**. Both are modeled scenarios.

**MVP:** scan; import PDF; merge/reorder; compress to explicit limit; signature/form placement; human-accessible quality preview; file format/page count checks; export/share. **Defer:** full Adobe-style editing, AI chat across all docs, fax stack, generalized secure cloud storage, broad document summaries. Default to local processing where technically possible and disclose cloud processing accurately.

**Activation/North Star:** percentage starting document preparation that **successfully export a file satisfying their stated technical conditions**. Track scan/import→task chosen→checks→review→export, task time, correction rate, return visits, refunds, paid conversion, D30 net RPI. Test scanner-first versus readiness-first storefront and scan-user acquisition versus existing-PDF-repair audiences. **Do not misrepresent a prepared file as already submitted or accepted.**

**Starting sources:** [Adobe Scan](https://apps.apple.com/us/app/adobe-scan-pdf-ocr-scanner/id1199564834), [CamScanner](https://apps.apple.com/us/app/camscanner-pdf-scanner-app/id388627783), [iScanner](https://apps.apple.com/us/app/iscanner-pdf-document-scanner/id1040093707), [Genius Scan](https://apps.apple.com/us/app/scanner-app-genius-scan/id377672876), [Scanner Pro](https://apps.apple.com/us/app/scanner-pro-scan-pdf-documents/id333710667), [SwiftScan](https://apps.apple.com/us/app/swiftscan-ai-document-scanner/id834854351), [PDF Expert](https://apps.apple.com/us/app/pdf-expert-editor-reader/id743974925), [PDFgear](https://apps.apple.com/us/app/pdf-gear-pdf-editor-reader/id6465897558), [Apple scan support](https://support.apple.com/guide/iphone/scan-text-and-documents-iph653f28965/ios).

---

## 15. Category 11 — AI Resume Builder — partial audit

**Status: PARTIAL.** The user requested the next category and a short executive conclusion was delivered, **but no completed 20-app roster, pricing table, review analysis, UI storyboard, ad tests or D30 model were delivered before the request to compile this knowledge base.** Do not infer those from a generic industry view.

### 15.1 What was established

**[PUBLIC, via earlier storefront research]** Competition exists for all obvious features:

- **Kickresume:** templates, AI-generated/tailored bullets, resume feedback.
- **AI Resume Tailor:** resume versus job-description comparisons, before/after changes, missing keywords and claim verification prompts.
- **CVpop:** tailoring, application tracking and interview preparation.
- **Resume Builder – AI CV Maker:** bullets, job-description matching and ATS scores.

**[THESIS]** A plain resume-template creator, ATS score, job match comparison, rewrite button and AI claim verifier are **not** independently differentiated.

### 15.2 Preferred early hypothesis — ProofPoint

**Working name:** ProofPoint.  
**Proposition:** *Show the evidence that you're a match.*  
**Mental model:** A job's requirements mapped to **truthful evidence from the applicant's own history**.

Example conceptual layout:

| Job requirement | Evidence supplied by user | State |
|---|---|---|
| Paid acquisition at scale | Managed $X campaigns, supported by user's resume/work history | **Supported** |
| Team leadership | Led Y-person team, user-supplied | **Supported** |
| B2B enterprise sales | No supplied evidence | **Not demonstrated** |
| New domain experience | Partial evidence from adjacent work | **Explain carefully** |

**Never invent employment dates, revenue, credentials, titles, achievements or results to satisfy a job posting.** The value proposition is transparent evidence mapping and useful gap identification, not falsely promising a certain ATS outcome or interview.

Prior ideation also considered: recruiter 10-second view, evidence-first AI bullets, resume versions treated as campaigns, interview response preparation. These are ideas, not a completed competitive study.

### 15.3 Work still required

1. Verify a defensible **20-app US iPhone cohort** (include Kickresume, Teal's relevant mobile experience if available, Rezi, Resume.io, Zety/Resume Genius mobile offerings *only if an actual matching app is confirmed*, job-tailoring specialists, and resume-template producers). Do not claim nonexistent apps.
2. Capture exact first three US screenshots, public offers, review patterns on billing, ATS claims, editing limits and output portability.
3. Contrast mobile-specific user needs with web-first builders.
4. Test evidence-map versus traditional ATS-score concept on product-page conversion, free-to-paid, application completion and refund rates.
5. Model D30 economics for one-time interview/job-search utility versus annual subscription. Job search is episodic; annual plan may be a poor user fit.
6. Consider accuracy, job-market regulations, candidate privacy, and accessibility of exported documents.

**Starting storefront references:** [Kickresume](https://apps.apple.com/us/app/kickresume-ai-resume-builder/id1523618695). Additional app identifiers require verification in the follow-up audit.

---

## 16. Category 12 — Immigration Case Tracker — concept only

**Status: CONCEPT ONLY.** Immigration tracking was explored in the initial 12-category differentiation exercise, **but not given its separate 20-app US storefront audit, price benchmarking, review-by-review synthesis, or financial model**.

### 16.1 Early competing mental model and insight

**Known concept-level competitors:** Lawfully and numerous USCIS case-status apps. The earlier discussion described Lawfully as a large established participant, including community estimates and case predictions. Those publisher claims, user counts, prediction methodologies and current prices should be independently verified before reuse.

**Customer emotion:** uncertainty and repetitive checking. A user may check status many times a day even when no action is possible. The product should reduce uncertainty **without pretending to control government timelines**.

### 16.2 Proposed concept: Stop Checking / Case Flight Tracker

**Primary promise:** *Stop checking constantly. Know when something actually changes.*

Visual language modeled after **flight/parcel tracking**, with a crucial split:

1. **Official status:** Exact government status and last verifiable update, fetched through a lawful supported source.
2. **Informational context:** General process milestones, possible next steps, public processing-time information.
3. **Model/estimate (if included):** Clearly labeled predictions with methods, cohort definitions, uncertainty and no false precision.
4. **Action required:** Only flag a required action when grounded in a verified notice or user-provided official document; avoid fabricated legal deadlines.

Possible home screen:

```text
I-485  |  UNDER REVIEW
Last confirmed official change: [verified date]
Action required from you: [only if verified]

No new official change detected since last check.
Estimated timing (if any): separate, clearly labeled, not guaranteed.
```

Features explored: optional “no change” digest, official-versus-estimate separation, practical next-step education, case cohort comparisons where data is legitimate. **Do not present this as legal advice or guarantee prediction accuracy.** Secure immigration-case identifiers; verify source refresh rates, consent, and whether data access is supported/allowed.

### 16.3 Proposed early App Store narrative (untested)

1. **“Stop checking your case 20 times a day.”** Clear official status.
2. **“Know when your official status changes.”** Notification only on confirmed updates.
3. **“Understand what comes next.”** Plain-language explanation, explicit source/uncertainty.

Possible Meta creative: anxious repeated refresh → user turns on trusted change notifications → gets a clear confirmed update. Avoid assuming a “nothing changed” notification can be sent without verified source refresh, or claiming real-time tracking where it does not exist.

### 16.4 Work still required

- Research the actual **20-app competitor set** and ownership, public IAP, current reviews and the first-three screenshots of each live US storefront.
- Verify lawful access and accuracy of USCIS status sources, rate limitations, availability, latency and maintenance burden.
- Understand privacy/security requirements for case data and user identifiers; avoid unnecessary retention.
- Separate lawful general information from regulated immigration/legal advice, and verify jurisdiction-specific constraints.
- Evaluate annual vs monthly vs transaction fees for an intrinsically **long-duration but low-frequency** need.
- Test whether the calm notification positioning converts sufficiently and retains users compared with free official USCIS tracking.

**Starting sources:** [USCIS Case Status Online](https://egov.uscis.gov/), [USCIS case-processing-times information](https://egov.uscis.gov/processing-times/), [Lawfully](https://www.lawfully.com/). Confirm these sites' present APIs/services and terms before developing a product around them.

---

## 17. Portfolio comparison and next actions

### 17.1 Comparative evaluation — hypotheses, not validated rankings

The comparisons below are **qualitative operating hypotheses derived from the completed audits**. No common Meta cohort, CPI, conversion, retention, or user research was collected to validate relative attractiveness.

| Category | Immediate acquisition trigger | Potential returning job | Key risk to D30 payback | Most decisive product test |
|---|---|---|---|---|
| Storage Cleaner | Phone full / messy photos | Ongoing declutter | Low CPI tolerance; free tools | Recover honest storage without scary deletion |
| Calorie Counter | Need daily nutritional clarity | Multiple meal decisions/day | Slow trust/behavioral value | Decision-first vs camera-first cohort |
| Plant Identifier | Sick plant | Multiple plants and recovery | Episodic identification | Guided assessment→follow-up rate |
| Habit Tracker | Can't maintain routines | Daily/weekly logging and recovery | Cheap alternatives; intangible value | Real return after missed sessions |
| Fax | Important fax needed today | Repeat business transactions | One-time users, refunds, API cost | Accurate send/failure recovery + payment mix |
| Baby Tracker | Newborn tracking / parental handoff | Many daily family events | Finite newborn lifecycle, free collaboration | Handoff adoption by real families |
| Sleep Tracker | Poor night / confusing wearable data | Tonight's experiment and trend | Apple native + one-time competitors | Second personal experiment rate |
| Universal TV Remote | Lost remote / remote failed | Daily household TV control | Official free apps; device failures | First verified command and D1 reconnect |
| Recipe Importer | Saved Reels / dinner indecision | Cook again, evolving personal recipes | Cheap perpetual alternatives | First and second recipe cooked |
| Scanner / PDF | Need a PDF prepared now | Recurring paperwork | Native and free PDF editors | Technical-criteria export completion |
| AI Resume Builder | Applying to a particular job | Tailor successive applications | Episodic search, crowded ATS claims | Evidence map's real application value [TODO] |
| Immigration Tracker | Waiting / status anxiety | Passive confirmed updates | Legal/privacy/source trust and free official status | Confirmed-status alert reliability [TODO] |

### 17.2 Suggested decision gates for the app factory

**Gate 0 — Evidence:** Does a precise complaint appear across independent sources, and does the competitor genuinely fail to solve it? Could the iPhone already do it for free?

**Gate 1 — Prototype:** Can the proposed experience demonstrate a tangible advantage in a <30-second product video or in the first 3 store screenshots?

**Gate 2 — Activation:** Is the critical task demonstrably successful (e.g., television responds, fax transmit confirmed, PDF prepared, caregiver sees handoff, imported recipe cooked)?

**Gate 3 — Paid funnel:** Can the user perceive a clear paid benefit after the first successful interaction? Is price presented transparently?

**Gate 4 — D30 cash:** Is **observed** D30 net RPI at/above **observed** CPI by a sustainable margin after refunds, commission and service costs? Use actual *paid install cohort*, not category-wide app-store estimates.

**Gate 5 — Scale reliability:** Does the product work in repeat use, across device/OS/vendor scenarios? Are support issues or platform dependency eroding returns?

### 17.3 Cross-category brand and UX guidelines

- Use a **single hero outcome** in the first screenshot and one concrete proof screenshot second.
- Don't show nonexistent data in actual marketing. Concept mocks in this KB use fictitious names, photos and values.
- Show familiar functionality by screenshot 4–6 if hero screenshot is unconventional; don't force users to guess product category.
- Preserve a **direct fast path** for power users (scan now, send fax directly, connect TV, log meal).
- Turn warnings into actionable recovery—not generic red errors.
- Use a visual system suited to the problem: warm/editorial for recipe/food/habit; trusted/structured for fax/PDF; dark/high contrast for sleep and remote; calm but efficient for baby; real-user photographs for cleaner.
- Separate product proof from social proof. A startup cannot make unsupported “millions of users” claims.
- Keep source provenance visible where AI transforms data: extracted vs inferred ingredients; original vs suggested resume bullet; actual vs predicted sleep/case status; generated caregiver summary vs source logs.
- Test channel-specific **Custom Product Pages** and make creative→page→onboarding consistent. Respect platform limits, actual features and trademark rules.
- Maintain high compliance/trust standards in health, baby, immigration and sensitive-document categories.

### 17.4 Recommended next research tasks, in order

1. **Finish AI Resume Builder properly:** 20 verified current US storefronts, reviews, exact paywalls and Job Match Evidence Map validation.
2. **Audit Immigration Case Tracker properly:** regulatory/source access first, then 20 storefronts, customer pain and monetization.
3. For first build candidates, **capture exact live current US App Store screenshots** from 20 competitors each; code every first-three sequence to avoid qualitative overgeneralization.
4. Use a third-party competitive-paywall database only as a supplement; acquire a small set of first-hand device/onboarding observations where lawful and practical.
5. Build **ad concept test cells** for 3 messages × 2 first screenshots × 1 coherent onboarding each; measure post-install activation, not just CTR/CPI.
6. Implement a common **D30 net-revenue cohort dashboard** across apps with precise definitions for direct purchase, trial, monthly/yearly payers, commissions, refunds, fees and actual payout dates.
7. Run reliability/permission tests tailored to category (TV hardware lab; PDF source and format testing; plant image ambiguity; baby offline sync; fax transmission failure). Consider a category dead if its basic task cannot be dependable.
8. Maintain this Markdown file as a living knowledge base; date changes, source new evidence, distinguish hypothesis revisions, and replace modeled conversion rates with **observed cohorts**.

---

## 18. Source and verification index

### 18.1 High-priority platform documentation

- [Apple App Store Connect — Custom Product Pages](https://developer.apple.com/app-store/custom-product-pages/): campaign-specific screenshots and product pages; feature limits and requirements may change.
- [Apple Small Business Program](https://developer.apple.com/app-store/small-business-program/): eligibility-dependent 15% commission, not universally applicable.
- [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/): control accessibility, transparency and interface standards.
- [Apple Photos support](https://support.apple.com/guide/iphone/delete-or-hide-photos-and-videos-iphb4defbde9/ios): deletion and Recently Deleted behavior; check exact iOS version and iCloud settings.
- [Apple TV Remote support](https://support.apple.com/en-us/108778): supported hardware and native capabilities.
- [Apple iPhone local-network permissions](https://support.apple.com/en-us/102229): user authorization to discover/control local devices.
- [Apple iPhone document scanning](https://support.apple.com/guide/iphone/scan-text-and-documents-iph653f28965/ios): native alternatives.
- [USCIS official case status](https://egov.uscis.gov/): confirm permitted access and freshness of official information.

### 18.2 Subscription analytics and competitive paywalls

- [RevenueCat — State of Subscription Apps](https://www.revenuecat.com/state-of-subscription-apps): cohort benchmarks; verify methodology and geography.
- [RevenueCat Utilities-specific report](https://www.revenuecat.com/state-of-subscription-apps-2026-utilities): check the current working URL and release-date context.
- [Adapty — Utilities benchmarks](https://adapty.io/blog/utilities-app-subscription-benchmarks/).
- [Adapty — Productivity benchmarks](https://adapty.io/blog/productivity-app-subscription-benchmarks/).
- [Adapty — Apple Ads subscription benchmarks](https://adapty.io/apple-ads-for-subscription-apps/).
- [Superwall — paywall analytics](https://superwall.com/features/paywall-analytics).
- [Superwall Paywall Screens](https://www.paywallscreens.com/).
- [MWM Intelligence](https://mwm.ai/mwm-intelligence).

### 18.3 Competitor storefront anchors

The category sections above contain primary-app and product links. **Many additional competitor names came from earlier research but do not have an independently re-opened URL inside this knowledge base**. Re-verify exact App Store app ID, country, publisher and current IAP for diligence.

### 18.4 Suggested source-record template for future updates

```yaml
category: universal_tv_remote
competitor: Example App
storefront_country: US
platform: iPhone
observed_at: YYYY-MM-DD
app_store_url: https://apps.apple.com/us/app/.../id...
publisher: "..."
source_type: apple_app_store  # app_store | developer | review | third_party | model
first_3_screenshot_exact_copy: []
screenshot_capture_location: null
visual_classification: []
main_promise: "..."
other_claims: []
list_price_public_iaps: []
trial_offer_verified_in_app: null
reviews_positive_short_themes: []
reviews_negative_short_themes: []
measurement_confidence: qualitative
notes: "A public IAP does not prove a specific user's paywall."
```

### 18.5 Proposed internal experiment-record template

```yaml
app: Remote Ready
experiment: compatibility_before_paywall
country: US
channel: Meta
audience: verified_tv_device_segment
start_date: YYYY-MM-DD
end_date: YYYY-MM-DD
randomization_unit: install
control: paywall_first
challenger: device_test_first
primary_metric: d30_net_proceeds_per_paid_install
secondary_metrics:
  - install_to_verified_command
  - verified_to_paywall
  - paid_conversion
  - d1_reconnect_success
  - refunds
  - support_cost_per_paid_install
cash_revenue_basis: realized_receipts_by_d30
commission_basis: actual_apple_settlement
refund_basis: actual_cohort_loss
status: hypothesis
```

---

## One-page conclusion

Across the app categories examined, the promising opening move is usually **not inventing a category or adding another AI feature**. It is finding an already-familiar customer job that incumbents solve with too much friction, poor transparency or weak follow-through—and designing the entire product, App Store page, advertisement, onboarding and paid offer around a **more useful outcome**.

For Storage Cleaner, prove the deletion decision; for Calorie Counter, support the next food choice; for Plant, follow the assessment into care; for Habits, make returning possible; for Fax, make transmission understandable; for Baby, enable a real caregiver handoff; for Sleep, test one practical change; for TV Remote, prove first-command compatibility; for Recipes, turn saved links into meals; for PDF, check the file against stated technical conditions; for Resume, ground claims in evidence; for Immigration, separate verified official status from estimates.

**The portfolio discipline:** Treat every such idea as a falsifiable hypothesis. The final selection should depend on **observed** acquisition and D30 contribution, real recurring behavior, the product's ability to do its core job reliably, and the operational/compliance burden—not on aesthetic novelty alone.
