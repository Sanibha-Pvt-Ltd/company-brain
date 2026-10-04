---
type: app
category: calorie-tracker
app: "Healthify: AI Calorie Tracker"
app_store_id: 943712366
member: ganesh
run_by: harshil
updated: 2026-10-04
status: draft
scope: screens-only
screens_analysed: 16
reviews_analysed: 0
sources: [screenshots:16 (IMG_1621–1636, India storefront), itunes-lookup-us, ganesh-benchmark-xlsx]
---

# Healthify: screens-only teardown

Related: [[members/ganesh/drafts/calorie-tracker/screens-synthesis]]

**Capture caveat (important).** This is **not a new-user flow**. After the account screen, the app says "Welcome back Ganesh!" (1622), so an earlier account existed.
- Height was never asked; the BMI on 1628 uses stored data [INFERRED].
- The new-user quiz may be longer.
- The xlsx says 15 onboarding screens and 13 questions [DATA:ganesh-benchmark-xlsx].
- No meal log or Snap result was captured.

## A1 Snapshot (US, short)

| Field | Value | Tag |
|---|---|---|
| Developer | HealthifyMe Wellness Private Limited | [DATA:itunes-lookup-us 2026-10-04] |
| US rating | 4.57 from **5,977** ratings | [DATA:itunes-lookup-us] |
| First release / latest | 2014-12-17 / v12.0.1 on 2026-09-28 | [DATA:itunes-lookup-us] |
| Age rating | 12+ | [DATA:itunes-lookup-us] |
| Positioning | a broad health platform: coach, Snap, diet plan, GLP-1, fasting, calorie tracker, workouts | [OBSERVED 1623–1624] |

The xlsx names Healthify the category winner [DATA:ganesh-benchmark-xlsx]. With 5,977 US ratings, against 368,153 for Cal AI and 2,370,589 for MFP [DATA:itunes-lookup-us], it reads as **an India winner, not a US benchmark** [INFERRED].

- **A2 Business performance:** not in this run (screens-only).
- **A4 Acquisition:** not in this run (screens-only).
- **A6 Failure mining:** not in this run (screens-only).

## A3 Monetization (from screens, India storefront ₹)

- **Paywall 1632:** comes right after setup. The X is visible immediately.
  - "Healthify+" / "Starting at just ~~₹399~~ ₹125/mo" / "Limited Time Offer!"
  - 12 Months "Save 70%" at **₹125 /mo**, ~~₹4,799~~ ₹1499 (pre-selected).
  - 1 Month at ₹399 /mo.
  - **No trial.**
  - 1633 lists the benefits: Macro & Micro Nutrient Analysis, **Snap - Photo-based Meal Tracking**, Detailed Meal Insights & Reports, AI Coach Ria, Edit Calorie Budgets, Custom Meals, Recipes.
- **Downsell 1634 (on close):**
  - "68% + Extra 20% OFF — Only For Today!"
  - "Lifetime of good health, at the cost of cutting chai."
  - "You Won't See This Offer Again!"
  - ~~₹4,788~~ **₹1,199 For The Whole Year!**
- **Home banner 1636:** "TRACKPLUS ₹49 PER MONTH ~~₹125/month~~ LOWEST PRICE EVER".
- **Three prices within about a minute** (status-bar clock 12:46 on 1632 → 12:47 on 1636): ₹1,499/yr, then ₹1,199/yr, then ₹49/mo for a "TrackPlus" tier (₹49 × 12 = ₹588/yr if billed monthly [INFERRED]). The anchors also disagree: ₹4,799 vs ₹4,788 (₹4,788 = ₹399 × 12 [INFERRED]). "You Won't See This Offer Again!" (1634) is followed two screens later (1636) by a lower-priced offer, though for a differently named tier (TrackPlus, not Healthify+) [OBSERVED].
- **Ganesh's notes:** they agree on ₹1,499 / ₹1,199 / ₹399 [DATA:ganesh-benchmark-xlsx]. The xlsx does not mention the ₹49 TrackPlus banner.
- **"3 days left" chip on home (1636):** suggests a trial or grace period. Its meaning is `[UNKNOWN]`.

## A5 Screens lens

### Journey (capture order; matches content)

| # | stage | what user sees | asks | gives | verbatim copy | lever | friction / dark pattern | tag |
|---|---|---|---|---|---|---|---|---|
| 1621 | account (wall) | +91 phone (field empty); WhatsApp opt-in **ticked**; Email / Apple / Google / Facebook | phone or SSO | — | "Let's Create Your Account" / "Receive updates and reminders on Whatsapp" | — | **account wall on screen 1**; WhatsApp opt-in ticked while the phone field is still empty, so likely pre-ticked [INFERRED] | [OBSERVED] |
| 1622 | interstitial | confetti | — | recognition | "Welcome back Ganesh!" | — | — | [OBSERVED] |
| 1623–1624 | onboarding | 10+ product lines as checkboxes | multi | — | "What are you looking for?" Coach Guidance / SNAP / Diet Plan / Weight Loss / GLP-1 / Intermittent Fasting / Calorie Tracker / Muscle Gain / Workouts and Yoga / HEALTHY FOODS … | — | **product-menu-as-question**: the user must learn the app's SKUs | [OBSERVED] |
| 1625 | onboarding | typed age | age | — | "Your age determines how much you should consume." | — | — | [OBSERVED] |
| 1626 | onboarding | city + coach language (8 Indian languages plus English and Other) | 2 asks | — | "Where are you from?" / "What language do you prefer to speak in?" / "This does not affect your app language." | — | **India-specific** (coach language) | [OBSERVED] |
| 1627–1628 | onboarding | weight 70 kg, target 69.5 kg; BMI 20.9 note | 2 asks | BMI context | "Set a realistic weight goal for yourself." / "Your current BMI is 20.9 which is in the normal range" | reassurance | none; a calm BMI line | [OBSERVED] |
| 1629 | onboarding | medical conditions | multi | — | "Any Medical Condition we should be aware of?" Diabetes / Pre-Diabetes / Cholesterol / Hypertension / PCOS / Thyroid / Physical Injury | care | none; PCOS and Thyroid fit the India mix | [OBSERVED] |
| 1630 | permission (pre) | Apple Health | Sync / manual | — | "More access = faster path to your fitness goal!" / "On the next screen, tap "All categories on"" | — | coaches the user to grant all; offers "No, I'll Track Everything Manually" | [OBSERVED] |
| 1631 | loading | 3 setup steps | wait | **a plan summary** | "Setting-up Healthify for Ganesh..." / "Setting Goal: Lose 0.5 kg" / "Enabling Hypertension care" | personalization | none; short, and specific to the inputs | [OBSERVED] |
| 1632–1633 | paywall | 12 mo vs 1 mo, benefits | pay / X | — | "Starting at just ₹399 ₹125/mo" / "Limited Time Offer!" | anchor | Snap (photo log) is paywalled | [OBSERVED] |
| 1634 | downsell | chai photo, ₹1,199/yr | Avail / X | — | "Lifetime of good health, at the cost of cutting chai." / "You Won't See This Offer Again!" | false scarcity, local metaphor | **false finality**: a lower ₹49/mo TrackPlus offer appears on 1636 (different tier) | [OBSERVED] |
| 1635 | onboarding | Ria intro | View My Daily Goals | — | "I'm Ria, your personal fitness AI… nutrition, hydration, sleep, and exercise" | — | four goal domains to learn | [OBSERVED] |
| 1636 | home | TrackPlus ₹49 banner; "3 days left"; Track Food "Eat 1,450 Cal" with camera and +; IF prompt; Protein / Fats / Carbs / Fibre 0%; "Click to Unlock Your New Year Gift"; Weight "0 kg lost"; tabs Home / Snap / + / Plans / Streaks | — | **a calorie target** | "Eat 1,450 Cal" / "LOWEST PRICE EVER" | — | a third price; a "New Year Gift" in October; a busy home | [OBSERVED] |

### The 8 measures

1. **First win.** The calorie target ("Eat 1,450 Cal") appears on home at screen 16, **after** the paywall and downsell (both closable) [OBSERVED]. No meal was logged. A first log from home is camera or + on the Track Food card. Whether Snap works on free is `[UNKNOWN]`: the paywall lists it as a Healthify+ benefit.
2. **Ask ledger (returning user).** Account (phone / SSO, with WhatsApp opt-in ticked) → product lines → age → city → language → weight → target → medical → Health → *(given: setup summary)* → payment ×2 → *(given: 1,450 Cal)*. That is **about 10 asks**, with the plan only after payment screens. A new user likely faces more (height, sex, activity) `[UNKNOWN]`.
3. **Abstractions.** The product menu (Coach, SNAP, Diet Plan, GLP-1, IF, TrackPlus vs Healthify+) is **invented, and the heaviest load in the set**. Ria (AI coach). 4 goal domains (nutrition, hydration, sleep, exercise). Streaks. Fibre as a tracked macro (useful). **Two subscription tiers with different names** (Healthify+, TrackPlus).
4. **Feel-good moments.** "Welcome back Ganesh!" with confetti is earned recognition. The calm BMI line (1628) and the specific setup summary (1631) are earned.
5. **Feel-bad moments.**
   - An account wall with the WhatsApp opt-in already ticked (1621).
   - "You Won't See This Offer Again!", followed two screens later by a cheaper (differently named) TrackPlus offer (1634 → 1636).
   - A New Year gift in October (1636).
   - "0 kg lost" as a home metric (1636). It is weight-loss framing on day 0 for a normal-BMI user who chose a 0.5 kg goal.
   - ED: the goal was set to "Lose 0.5 kg" and 1,450 Cal for a 70 kg, BMI 20.9 user [OBSERVED]. The maths is not shown, so it can't be checked. A 1,450 target for that profile looks aggressive [INFERRED].
6. **Paywall.** Soft. The X is immediate. No trial. Three price points across paywall, downsell and home banner. A local, warm metaphor ("cutting chai").
7. **Repeat cost.** Track Food card → camera or + is likely 1 tap to the logger [INFERRED from 1636]. The rest is `[UNKNOWN]`. Hooks: Streaks tab, WhatsApp reminders (opt-in ticked), coach, Ria.
8. **Feature map.**
   - Table stakes: calorie target, macros, food logging, Apple Health.
   - Differentiators: **human coaches**, Indian food database, regional-language coaching, medical-condition plans (the xlsx reviews praise the coach and Indian food [DATA:ganesh-benchmark-xlsx]).
   - Bloat for a calorie-tracker job: GLP-1, workouts / yoga, IF, sleep, recipes, New Year gift.

### India-specific vs transferable to the US

| India-specific (do not copy for the US) | Transferable |
|---|---|
| +91 phone-first signup with a WhatsApp opt-in (1621) | Medical-condition question feeding a visible line in the setup summary, "Enabling Hypertension care" (1629, 1631) |
| Regional coach language (1626) | Short, specific setup summary instead of a fake percentage bar (1631) |
| The "cutting chai" price metaphor (1634); the US equivalent would be a coffee comparison, which is still a dark-ish anchor | Calm BMI context line (1628) |
| Human dietitian coaching at ₹ prices; US labour costs make this a different business [INFERRED] | Fibre as a first-class nutrient (1636) |
| Indian food database (xlsx reviews) [DATA:ganesh-benchmark-xlsx] | "No, I'll Track Everything Manually" as an equal-weight escape from the Health permission (1630) |

### Keep / Kill / Different

- **Keep:**
  - The setup summary that echoes the user's inputs (1631).
  - The calm BMI line (1628).
  - The medical-condition question, *if* it visibly changes something.
  - The manual escape on the Health prompt (1630).
- **Kill:**
  - The account wall on screen 1 (1621).
  - The ticked-by-default WhatsApp opt-in (1621) [default state INFERRED].
  - The product-menu question (1623–1624).
  - Three prices plus false finality (1632 → 1634 → 1636).
  - "0 kg lost" on day 0 (1636).
  - Two tier names.
- **Different:** One product, one price, one tier. If we ask about a condition, show exactly what it changed ("Sodium line added to your day because you said hypertension"). Otherwise don't ask.

## A8 Verdict (short)

Healthify wins in India on coaches, Indian food data and regional language. Those moats are local, labour-heavy, and don't transfer to the US, which matches its 5,977 US ratings [DATA:itunes-lookup-us]. For Sanibha it is a **pattern source, not a benchmark**.
- **Worth taking:** the input-echoing setup summary and condition-aware care.
- **Worth avoiding:** the platform sprawl and price whiplash.

**Evidence strength:** paywall strong; onboarding medium (returning-user flow); core loop none.

## Verification (2026-10-04)

**Checked:** all 16 screenshots (IMG_1621–1636) opened; ~30 verbatim quotes, ~20 numbers/prices, 16 IMG refs and order, capture date (EXIF 2026-10-03, so "New Year gift in October" holds), 4 [INFERRED] calculations (₹49×12 = ₹588; ₹399×12 = ₹4,788; ₹1,499 vs ₹4,799 ≈ 69% off vs "Save 70%"; ₹125×12 = ₹1,500), 5 xlsx claims (D5 15 screens, E5 13 questions, H5 prices, I5 Top Pick, J5/K5 coach and Indian-food reviews) and 6 US listing fields (plus Cal AI and MFP rating counts).

**Corrections:**
- Developer "HealthifyMe Wellness" → "HealthifyMe Wellness Private Limited".
- Cal AI / MFP rating counts 368K / 2.37M → exact 368,153 / 2,370,589; "an India winner, not a US benchmark" → [INFERRED].
- "Three prices in about 60 seconds" → within about a minute (clock 12:46 → 12:47).
- "'You Won't See This Offer Again!' contradicted one screen later by a cheaper offer" → two screens later (1636), and the ₹49 offer is a differently named tier (TrackPlus), so "contradicted" is softened throughout.
- 1621 WhatsApp "pre-ticked" → ticked with the phone field empty, so default [INFERRED] (all mentions).
- 1626 "9 Indian languages" → 8 Indian languages plus English and Other.

**Not verifiable:** new-user flow; meaning of the "3 days left" chip; whether Snap works free; the maths behind 1,450 Cal; US price.
