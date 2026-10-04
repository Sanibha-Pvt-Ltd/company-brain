---
type: app
category: calorie-tracker
app: MyFitnessPal
app_store_id: 341232718
member: ganesh
run_by: harshil
updated: 2026-10-04
status: draft
scope: screens-only
screens_analysed: 18
reviews_analysed: 0
sources: [screenshots:18 (IMG_1637–1654, India storefront), itunes-lookup-us, ganesh-benchmark-xlsx]
---

# MyFitnessPal: screens-only teardown

Related: [[members/ganesh/drafts/calorie-tracker/screens-synthesis]]

**Capture caveat.** The capture runs from launch to the free home screen. No meal was logged. One onboarding step is missing between 1649 and 1650: the progress bar jumps from segment 4 to segment 6. It is likely the goal weight / weekly pace step `[INFERRED]`. The copy is en-GB ("customise", "fibre", "Prioritise"), consistent with the India storefront localisation. US copy will differ.

## A1 Snapshot (US, short)

| Field | Value | Tag |
|---|---|---|
| Developer | MyFitnessPal, Inc. | [DATA:itunes-lookup-us 2026-10-04] |
| US rating | 4.71 from 2,370,589 ratings | [DATA:itunes-lookup-us] |
| First release / latest | 2009-12-08 / v26.39.0 on 2026-09-29 | [DATA:itunes-lookup-us] |
| Age rating | 17+ | [DATA:itunes-lookup-us] |
| Positioning | "Ready for some wins? Start tracking, it's easy!" | [OBSERVED 1637] |

- **A2 Business performance:** not in this run (screens-only).
- **A4 Acquisition:** not in this run (screens-only).
- **A6 Failure mining:** not in this run (screens-only).

## A3 Monetization (from screens, India storefront ₹)

- **Model:** freemium plus ads. The free home shows an **amazon.in banner ad** and "Get ad-free tracking in Premium—upgrade now" [OBSERVED 1654].
- **Upsell 1652:** "Stay on it with tools that turn habits into results". It sells barcode, voice and photo logging as premium. An X is visible.
- **Paywall 1653:** visible X. "Your first week is free".
  - Annual Plan "Save 58%" at **₹258.25 / month, ₹3,099 billed annually** (pre-selected).
  - Monthly Plan at ₹619 / month.
  - "Try it free for 7 days. Trust the process."
  - Footer: "Billing starts at the end of your 7-day free trial unless you cancel. Plans renew automatically. Cancel via the App Store."
- **Saving check:** ₹619 × 12 = ₹7,428, and ₹3,099 is 42% of that, so "Save 58%" is accurate [INFERRED].
- **Ganesh's notes:** the xlsx agrees on prices and lists the barcode scanner and photo scan as paid [DATA:ganesh-benchmark-xlsx]. The xlsx does not mention the 7-day trial; the screens show it.
- **Downsell:** none captured.
- **US price:** `[UNKNOWN]`.

## A5 Screens lens

### Journey

| # | stage | what user sees | asks | gives | verbatim copy | lever | friction / dark pattern | tag |
|---|---|---|---|---|---|---|---|---|
| 1637 | first-launch | photo carousel, protein chart | Sign Up For Free / Log In | the promise | "Ready for some wins? Start tracking, it's easy!" | aspiration | none | [OBSERVED] |
| 1638 | account (method) | Continue / Google / Apple | pick a method | — | "Welcome! Let's customise MyFitnessPal for your goals." / "We will collect personal information from and about you…" | — | an account path chosen before any value | [OBSERVED] |
| 1639 | onboarding | name field | typed name | — | "First, what can we call you?" | warmth | typing | [OBSERVED] |
| 1640 | onboarding | goals (up to 3) | multi | — | "Hey, G. 👋 Let's start with your goals." | personalization | none | [OBSERVED] |
| 1641 | interstitial | blue card | Next | praise | "Great! You've just taken a big step on your journey." | praise | manufactured (one tap = "big step") | [OBSERVED] |
| 1642 | onboarding | 18 habit chips | multi | — | "Which healthy habits are most important to you?" | — | a long list | [OBSERVED] |
| 1643 | interstitial | — | Next | — | "Your goals, your way." / "customisable–from nutrients, to macros, to meal plans." | — | filler | [OBSERVED] |
| 1644 | onboarding | meal-planning frequency | pick | — | "How often do you plan your meals in advance?" | — | — | [OBSERVED] |
| 1645 | interstitial | — | Next | praise | "Nice! You have a solid system." | praise | manufactured | [OBSERVED] |
| 1646 | onboarding | meal plans | pick | — | "Do you want us to help you build weekly meal plans?" | — | serves the upsell | [OBSERVED] |
| 1647 | onboarding | activity, with job examples | pick | clarity | "Not including workouts - we count that separately." / "(e.g. bank clerk, desk job)" | — | none; the clearest activity screen | [OBSERVED] |
| 1648 | onboarding | sex, age, country, postcode on one form | 4 fields | — | "We use sex at birth and age to calculate an accurate goal for you." | — | **postcode** is not needed for the job | [OBSERVED] |
| 1649 | onboarding | height + weight on one form | 2 fields | reassurance | "It's OK to estimate, you can update this later." | permission to be imperfect | none; kind copy | [OBSERVED] |
| gap | — | progress segment 5 not captured | — | — | — | — | likely goal weight / pace | [INFERRED] |
| 1650 | account | email + password + T&C | 3 fields | — | "Almost done! Create your account." / "10 characters minimum" | — | **mandatory email account** before the plan | [OBSERVED] |
| 1651 | result | **2,500 net calories**, plus 3 opt-ins shown **ticked** | Next | **the plan** | "Congratulations, G!" / "Your daily net calorie goal is: 2,500" / ✓ Keep me on track with reminders / ✓ Use my phone to track my steps / ✓ Would you like to receive our emails? | — | **marketing email opt-in ticked** on arrival (pre-ticked by default is [INFERRED]; no user action on this screen is visible) | [OBSERVED] |
| 1652 | upsell | barcode / voice / photo | Next / X | — | "Scan a barcode to log lightning fast" … "Take a photo to log your entire meal" | — | the fast log methods are premium | [OBSERVED] |
| 1653 | paywall | annual vs monthly | Try it free / X | — | "Your first week is free" / "Trust the process." | anchor | soft; honest terms | [OBSERVED] |
| 1654 | home (free) | calories 0 / 2,500; macros 0/312 C, 0/83 F, 0/125 P; ad; Breakfast / Lunch / Dinner / Snacks with Log buttons; streak 0 ⚡ | Log | **a usable free diary** | "Get ad-free tracking in Premium—upgrade now" | — | a banner ad on home | [OBSERVED] |

### The 8 measures

1. **First win.** The plan number arrives at 1651, after account creation. The first log comes **after a soft paywall the user can close**, on a free home [OBSERVED]. Launch to the free home is 18 captured screens plus typing (name, age, postcode, height, weight, email, password); tap count [UNKNOWN]. Free manual diary logging is stated in the xlsx ("Manual food search & diary logging" under What's FREE) [DATA:ganesh-benchmark-xlsx]; a first free log was not performed in the capture.
2. **Ask ledger.** Account method → name → goals → habits → planning frequency → meal plans → activity → sex/age/country/postcode → height/weight → [gap] → email/password → *(given: 2,500 kcal)* → 3 ticked opt-ins → paywall. That is **about 11 screens and about 16 fields before the number**. The typing is heavy (7 typed fields). Three praise interstitials (1641, 1643, 1645) give nothing.
3. **Abstractions.** **"Net calories"** (the job needs calories; "net" adds exercise maths). Macros (needed). Meal plans (upsell). The **streak ⚡** (invented). "Healthy habits" chips (invented framing).
4. **Feel-good moments.** "It's OK to estimate, you can update this later." (1649) is earned kindness. The praise cards are manufactured. "Congratulations, G!" is half-earned.
5. **Feel-bad moments.**
   - Email opt-in already ticked (1651) [default state INFERRED].
   - A postcode asked before value (1648).
   - The banner ad on home (1654).
   - The fast log methods shown, then gated (1652).
   - ED: "net calorie goal" implies exercise offsets food [INFERRED]. Otherwise MFP's copy is neutral.
6. **Paywall.** Soft, with an X. A 7-day trial with honest terms. Two touchpoints (upsell, then plans). No downsell captured.
7. **Repeat cost.** Home → "Log" on a meal → search → pick → add is about **4 taps plus typing** for a free user [INFERRED from 1654]. The faster methods (photo, barcode, voice) are premium [OBSERVED 1652; DATA:xlsx]. Hooks: a streak, reminders (ticked on 1651), emails (ticked on 1651), the week strip.
8. **Feature map.**
   - Table stakes: database search, diary by meal, macros, steps.
   - Differentiators: the database size and brand trust (the xlsx says 20M+ foods [DATA:ganesh-benchmark-xlsx]).
   - Bloat: the habit chips, the meal-plan questions, the praise interstitials, the postcode.

### Keep / Kill / Different

- **Keep:**
  - "It's OK to estimate, you can update this later." (1649)
  - Activity options with job examples (1647).
  - Free manual logging (1654).
  - Honest 7-day trial terms (1653).
- **Kill:**
  - The account before the plan (1650).
  - The postcode (1648).
  - Three praise interstitials (1641, 1643, 1645).
  - Ticked-by-default marketing emails (1651) [default state INFERRED].
  - Ads on the home screen (1654).
- **Different:** Free manual logging, like MFP, but **without ads and without an account up front**. Use local storage first, and offer iCloud / Sign in with Apple only when the user has something to lose (for example after 3 logged days).

## A8 Verdict (short)

MFP wins on habit, database and a free diary. Its onboarding is the most "form-like": typed fields, an account wall, a postcode. And the fast log methods that new apps lead with are premium here. **Most exploitable weakness:** on free, logging a meal means searching and typing. Every AI challenger's welcome screen exists to say "you don't have to do that anymore".

- **Copy:** estimate-is-OK copy; job-example activity levels; honest trial terms.
- **Beat:** a free fast log; no account wall; no ads.
- **Evidence strength:** onboarding/paywall strong; repeat cost medium (home seen, log not done).

## Verification (2026-10-04)

**Checked:** all 18 screenshots (IMG_1637–1654) opened; ~35 verbatim quotes, ~20 numbers/prices, 18 IMG refs and order, the progress-segment gap (1649 at 4 of 7 → 1650 at 6 of 7), 3 [INFERRED] calculations (₹619×12 = ₹7,428 and ₹3,099/₹7,428 = 41.7% → "Save 58%" accurate; ₹258.25×12 = ₹3,099; macros 312×4+83×9+125×4 = 2,495 ≈ 2,500), field counts (16 fields, 7 typed, 18 habit chips), 4 xlsx claims (H6 prices, G6 paid barcode/photo, F6 20M+ database, no trial mentioned) and 5 US listing fields.

**Corrections:**
- 1651 opt-ins "pre-ticked" → shown ticked; default state [INFERRED] (all mentions).
- "about 25 taps [OBSERVED]" → tap count [UNKNOWN].
- "The only incumbent where logging is free" → removed; the xlsx lists manual logging as free for MFP (and for Healthify, Appediet and BitePal), and no free log was performed in the capture.

**Not verifiable:** the missing segment-5 screen; US price and copy; free logging tap count.
