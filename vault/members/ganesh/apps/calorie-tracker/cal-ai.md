---
type: app
category: calorie-tracker
app: Cal AI - Calorie Tracker
app_store_id: 6480417616
member: ganesh
run_by: harshil
updated: 2026-10-04
status: draft
scope: screens-only
screens_analysed: 27
reviews_analysed: 0
sources: [screenshots:27 (IMG_1819–1845, India storefront), itunes-lookup-us, ganesh-benchmark-xlsx]
---

# Cal AI: screens-only teardown

Related: [[members/ganesh/drafts/calorie-tracker/screens-synthesis]] · lens: none yet for calorie-tracker (no `research/categories/calorie-tracker/lens.md`), so the starting hypothesis in `prompts/a5-screens-lens.md` is used as the lens.

**Capture caveat.** The 27 screens run from launch to the paywall and stop there. Nothing after the paywall was captured: no scan, no AI result, no correction, no home screen. So for the US benchmark app, the core loop is `[UNKNOWN]`.

## A1 Snapshot (US, short)

| Field | Value | Tag |
|---|---|---|
| Developer | Viral Development LLC | [DATA:itunes-lookup-us 2026-10-04] |
| Price model | Free download (US price 0.0), subscription | [DATA:itunes-lookup-us for price; subscription OBSERVED 1845] |
| US rating | 4.80 from 368,153 ratings | [DATA:itunes-lookup-us 2026-10-04] |
| First release / latest | 2024-04-08 / v26.39.0 on 2026-09-29 | [DATA:itunes-lookup-us] |
| Age rating | 4+ | [DATA:itunes-lookup-us] |
| Positioning | "Calorie tracking made easy", with a camera-scan demo on the first screen | [OBSERVED 1819] |

The in-app social proof says "4.8 avg rating", "250K+ App Ratings" and "10M+ Cal AI Users" [OBSERVED 1840]. The US rating count is 368,153 [DATA], so the in-app number is conservative or out of date [INFERRED].

- **A2 Business performance:** not in this run (screens-only).
- **A4 Acquisition:** not in this run (screens-only). The only on-screen signal is the source question, which lists TikTok first, then Instagram, then YouTube [OBSERVED 1823].
- **A6 Failure mining:** not in this run (screens-only).

## A3 Monetization (from screens, India storefront ₹)

- **Placement:** after 25 onboarding screens and before any use of the product [OBSERVED 1819–1845].
- **Hard or soft:** the paywall (1845) has a back arrow (←) and no X. The headline is "Start your 3-day FREE trial to continue". Ganesh's notes say "Hard Wall … App is locked without authorizing subscription trial" [DATA:ganesh-benchmark-xlsx]. The screens are consistent with that (no X, capture stops here); whether anything is reachable without starting a trial is `[UNKNOWN]` from screens alone.
- **Plans:** "Start for free & save 75%" at ₹2,999.00 billed annually, shown as ₹249.91/mo and pre-selected, or Monthly at ₹999.00/mo [OBSERVED 1845]. The 75% saving checks out: ₹999 × 12 = ₹11,988, and ₹2,999 is 25% of that [INFERRED]. This matches the xlsx (₹2,999/yr, 3-day trial, ₹999/mo) [DATA:ganesh-benchmark-xlsx].
- **Trial terms:** the terms are honestly stated: "3 days free, then ₹2,999.00 per year. Billed annually and renews automatically unless canceled in the App Store." [OBSERVED 1845]
- **Pre-paywall framing:** "We want you to try Cal AI for free", plus "No Payment Due Now" and a "Try Now" button [OBSERVED 1844]. It frames the trial as a gift one screen before the price.
- **Downsell / exit offer:** none captured. Whether one appears on back-navigation is `[UNKNOWN]`.
- **US price:** `[UNKNOWN]`. Do not convert the ₹ figures. Capture the paywall on a US Apple ID.

## A5 Screens lens

### Journey (capture order IMG_1819 → 1845; order matches content)

| # | stage | what user sees | asks of user | gives to user | verbatim copy | lever | friction / dark pattern | tag |
|---|---|---|---|---|---|---|---|---|
| 1819 | first-launch | camera-scan demo video of a sandwich and chips | tap Get Started | the promise | "Calorie tracking made easy" | simplicity promise | none; the clearest promise in the category | [OBSERVED] |
| 1820 | onboarding | sex picker | sex | nothing | "Choose your sex" / "This helps personalize your experience." | personalization | none | [OBSERVED] |
| 1821 | onboarding | workouts per week | 0-2 / 3-5 / 6+ | nothing | "This will be used to calibrate your custom plan." | personalization | none | [OBSERVED] |
| 1822 | onboarding | date-of-birth wheel | DOB | nothing | "When were you born?" | — | shows **January 1 2024** with Continue already enabled (so likely the default [INFERRED]); an 18-year-old would have to scroll back at least 6 years | [OBSERVED] |
| 1823 | onboarding | attribution list | where heard | nothing | "Where did you hear about us?" TikTok, Instagram, Youtube, App Store… | — | a marketing question for the app, worth nothing to the user | [OBSERVED] |
| 1824 | onboarding | yes/no | tried other apps | nothing | "Have you tried other calorie tracking apps?" | — | marketing question for the app | [OBSERVED] |
| 1825 | onboarding | chart: Cal AI line goes down; "Without a plan" line rebounds up | Continue | a claim | "Designed to help you stay on track" / "Without a plan" | fear of regain | unlabelled y-axis, no source; a manufactured "you'll fail without us" | [OBSERVED] |
| 1826 | onboarding | height, ft/in default 5 ft 6 in | height | nothing | "This will be taken into account when calculating your daily nutrition goals." | — | imperial default even on the IN storefront (good for US) | [OBSERVED] |
| 1827 | onboarding | weight ruler, lbs, 123.4 lbs | weight | nothing | "What is your weight?" | — | none | [OBSERVED] |
| 1828 | onboarding | yes/no | trainer/dietitian | nothing | "Do you currently work with a personal trainer or registered dietitian?" | — | the screens never show it being used | [OBSERVED] |
| 1829 | onboarding | lose / maintain / gain | goal | nothing | "This helps us generate a plan for your calorie intake." | — | none | [OBSERVED] |
| gap | — | the progress bar jumps from about 30% to about 47% between 1829 and 1830 | — | — | — | — | likely target weight, pace and similar screens **not captured** (the xlsx says 23 questions) | [INFERRED] |
| 1830 | onboarding | barriers list | pick barrier | nothing | "What's stopping you from reaching your goals?" Lack of consistency / Unhealthy eating habits / … | self-diagnosis | mild self-blame framing | [OBSERVED] |
| 1831–1832 | onboarding | diet list animating in | diet | nothing | "Do you follow a specific diet?" Balanced, Whole-food focus, Mediterranean, … Low-carb | — | none | [OBSERVED] |
| 1833 | onboarding | aspirations | pick one | nothing | "What would you like to accomplish?" … "Feel better about my body" | identity | body-image option; harmless as a choice, but the app never uses it on screen | [OBSERVED] |
| 1834 | onboarding | thank-you interstitial | Continue | praise only | "Thank you for trusting us!" / "Now let's personalize Cal AI for you..." | reciprocity | it promises personalisation is starting, after 10+ questions | [OBSERVED] |
| 1835 | onboarding | burned-calories example (+490 cal) | Yes / No | an explained feature | "Add calories burned back to your daily goal?" / "Daily Calorie Budget 2,500 → 2,990" | earn-more-food | introduces the "earn food with exercise" concept; ED risk (see Feel-bad) | [OBSERVED] |
| 1836 | permission (pre) | Apple Health pitch | Yes / No | — | "Sync workouts from Apple Health?" | — | none | [OBSERVED] |
| 1837 | permission (pre) | Health diagram | Connect Apple Health | — | "Sync your daily activity between Cal AI and the Health app to have the most thorough data." | — | none | [OBSERVED] |
| 1838 | permission (coach) | mock iOS sheet with "Turn On All" circled | Continue | — | "Tap "Turn On All" to sync workouts" / "workouts can't raise your calorie budget without it." | loss framing | coaches the user to grant every category | [OBSERVED] |
| 1839 | onboarding | rollover example | Yes / No | an explained feature | "Rollover extra calories to the next day?" / "Rollover up to 200 cals" | banking | a third concept: calorie rollover | [OBSERVED] |
| 1840 | social proof | 4.8 stars, 10M+ users, two 5★ reviews | Continue | reassurance | "Join over 10 million people like you" | social proof | the reviews are curated in-app, not live [INFERRED] | [OBSERVED] |
| 1841 | permission (pre) | fake notification dialog with a 👆 pointing at Allow | Allow / Don't Allow | — | "Stay on track with Cal AI notifications" | nudge | a pointing finger steers the choice | [OBSERVED] |
| 1842 | interstitial | "All done!" | Continue | — | "Time to generate your custom plan!" | anticipation | none | [OBSERVED] |
| 1843 | loading | 19% progress bar | wait | — | "We're setting everything up for you" / "Customizing health plan..." Daily recommendation for Calories, Carbs, Protein, Fats, Health Score | labour illusion | a manufactured progress bar | [OBSERVED] |
| gap | — | no plan reveal captured between 1843 and 1844 | — | — | — | — | whether the user sees their calorie number **before** the paywall is `[UNKNOWN]` | [INFERRED] |
| 1844 | pre-paywall | scan demo again | Try Now | a free framing | "We want you to try Cal AI for free" / "No Payment Due Now" | gift framing | the trial is framed as a gift; the price arrives on the next screen | [OBSERVED] |
| 1845 | paywall | annual (pre-selected) vs monthly | start trial | nothing new | "Start your 3-day FREE trial to continue" | anchoring, "save 75%" | hard wall; no X, only a back arrow | [OBSERVED] |

### The 8 measures

1. **First win.** Not reached in 27 screens. The first win (a scanned meal with numbers) comes **after** the hard paywall and a trial start [OBSERVED 1845; INFERRED]. Launch to paywall takes 27 captured screens; tap count [UNKNOWN]. The only "value" before the paywall is three explanatory feature cards (1835, 1838, 1839) and a demo video.
2. **Ask ledger.** Everything below was asked before the user got anything: sex → workouts → DOB → source → other apps → height → weight → trainer → goal → [about 3–5 uncaptured] → barriers → diet → accomplish → burn-back Y/N → Health Y/N → Health permission → rollover Y/N → notifications → trial/payment. That is **18 observed asks**, plus the gap (the xlsx counts 23). Received by the end: a "Thank you for trusting us!" and a loading bar. Two of the asks (source, other apps) serve the company only. **This is the main finding: about 20 asks, then a payment ask, with zero product value in between.**
3. **Abstractions.** Calories and the "daily calorie budget" (the job needs these). Macros (Carbs, Protein, Fats; the job partly needs them). **"Health Score"** (invented) [1843]. **Burned-calories-added-back** (optional; the app invented the framing) [1835]. **Rollover calories** (invented) [1839]. That is three extra concepts to learn before a single log.
4. **Feel-good moments.** "Thank you for trusting us!" is manufactured. The 10M-users proof is borrowed. The 1835 example (+490 cal, "Daily Calorie Budget 2,500 → 2,990") gives a little feel-good, but about hypothetical food, not the user's own. **No earned feel-good moment appears in the capture.**
5. **Feel-bad moments.** The "Without a plan" rebound curve is a fear claim with no source [1825]. The pointing finger on the notification prompt [1841]. "workouts can't raise your calorie budget without it" is loss framing [1838]. **ED flag:** burn-back and rollover teach "earn food by exercising / bank calories". For users with disordered eating, compensatory logic is a known risk pattern [INFERRED]. Both are opt-in Yes/No screens, which softens it.
6. **Paywall.** Hard, after the full quiz. No X. A 3-day trial, with honest terms. "save 75%" is accurate. The annual plan is pre-selected. A gift-framing screen precedes it. No downsell was captured.
7. **Repeat cost.** `[UNKNOWN]`: no post-paywall screens. Retention hooks were set up in onboarding: notifications [1841], Apple Health [1837], rollover [1839].
8. **Feature map.**
   - Table stakes: photo scan, calorie target, macros, Apple Health.
   - Differentiators: speed of the photo log, as promised [1819, 1844]. The screens cannot verify it.
   - Bloat: Health Score, rollover, the attribution and "tried other apps" questions, the trainer question.

### Keep / Kill / Different

- **Keep:** The first screen promises one job and shows it working (1819). The neutral, clean question design with one question per screen and a "why we ask" subline (1821, 1822, 1826). The honest trial terms (1845). The imperial-first units for the US (1826).
- **Kill:**
  - The hard paywall before any scan (1845).
  - The DOB default of 2024 (1822).
  - The attribution and other-apps questions inside the core quiz (1823, 1824). Move them after the first win, or drop them.
  - The unlabelled fear chart (1825).
  - The pointing-finger notification pre-prompt (1841).
  - The fake progress bar (1843).
  - Rollover and burn-back as onboarding concepts (1835, 1839).
- **Different:** **Scan first, ask later.** Screen 2 is the camera. The user scans a real meal and sees calories within about 3 taps. Then we ask only what the number needs (sex, age, height, weight, goal: 5 asks) and show *their* daily target next to the meal they just logged. The paywall comes after that, with the logged meal visible behind it. Rollover and burn-back become settings, off by default.

## A8 Verdict (short)

Cal AI leads on a single, legible promise. TikTok is listed first in its "Where did you hear about us?" question [OBSERVED 1823]; its real channel mix is `[UNKNOWN]`. Its onboarding is not short: about 20 asks and a hard wall before the product is touched. That plausibly works on high-intent traffic from video ads, where the user has already *seen* the scan [INFERRED]. **Most exploitable weakness:** the user pays (starts a trial) before verifying the one thing being sold, scan accuracy. Ganesh's notes include a 2★ review of an 8-grape photo logged at over 700 calories, and a 4★ review saying the "fix this" feature never adjusts calories [DATA:ganesh-benchmark-xlsx; not verified in this run]. A free first scan plus a visible, working correction would attack that directly.

- **Copy:** the one-job first screen; one-question-per-screen with a "why"; honest trial copy.
- **Beat:** value before the paywall; ask count; post-scan correction (to be verified in review mining).
- **Evidence strength:** onboarding/paywall strong; core loop **none** (not captured); monetization strong for IN, US `[UNKNOWN]`.

## Verification (2026-10-04)

**Checked:** all 27 screenshots (IMG_1819–1845) opened; ~35 verbatim quotes, ~20 numbers/prices, 27 IMG refs and order, the progress-bar gap (1829 ≈ 32% → 1830 ≈ 47%), 4 [INFERRED] calculations (₹999×12 = ₹11,988 and ₹2,999 = 25% of it; ₹249.91×12 = ₹2,998.92; 320+90+80 = 490 and 2,500+490 = 2,990), 6 xlsx claims (B7 developer, E7 "Hard Wall (After 23 questions)", F7 locked, H7 prices, K7 8-grapes review, L7 "fix this" review) and 6 US listing fields.

**Corrections:**
- Price-model tag: "subscription" was attributed to iTunes lookup → lookup gives only price 0.0; subscription is from 1845.
- In-app vs US rating count: "conservative or out of date" → tagged [INFERRED].
- Hard wall: "nothing after it was reachable" → capture just stops; reachability [UNKNOWN].
- 1822: "defaults to January 1 2024, adult must scroll 25+ years" → shows that date with Continue enabled (default [INFERRED]); an 18-year-old scrolls back ≥6 years.
- 1840 "curated, not live" → [INFERRED].
- "about 30+ taps" → tap count [UNKNOWN].
- Verdict "TikTok-first acquisition [OBSERVED 1823]" → TikTok is only listed first in the source question; channel mix [UNKNOWN]. "Works on video-ad traffic" → [INFERRED].

**Not verifiable:** US price; whether a plan reveal or downsell exists outside the capture; anything after the paywall.
