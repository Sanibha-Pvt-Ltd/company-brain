---
type: app
category: calorie-tracker
app: AI Calorie Counter - Appediet
app_store_id: 6450329545
member: ganesh
run_by: harshil
updated: 2026-10-04
status: draft
scope: screens-only
screens_analysed: 23
reviews_analysed: 0
sources: [screenshots:23 (IMG_1655–1677, India storefront), itunes-lookup-us, ganesh-benchmark-xlsx]
---

# Appediet: screens-only teardown

Related: [[members/ganesh/drafts/calorie-tracker/screens-synthesis]]

**Capture caveat.** The capture runs from launch to the meal-log search screen (1677). No meal was logged and no scan result was captured. The plan on 1672 shows "Goal 64.7 kg" after 55.0 kg was entered on 1661. Either a target screen was not captured, or the plan does not reflect the input `[UNKNOWN]`.

## A1 Snapshot (US, short)

| Field | Value | Tag |
|---|---|---|
| Developer | Appediet Information PTE. LTD (same in xlsx) | [DATA:itunes-lookup-us; ganesh-benchmark-xlsx] |
| US rating | 4.78 from 47,333 ratings | [DATA:itunes-lookup-us 2026-10-04] |
| First release / latest | 2023-08-21 / v1.67.1 on 2026-09-29 | [DATA:itunes-lookup-us] |
| Age rating | 12+ | [DATA:itunes-lookup-us] |
| Positioning | "Smart Insights Hit Goals" and "Make diet tracking easy with AI" | [OBSERVED 1655, 1670] |

- **A2 Business performance:** not in this run (screens-only).
- **A4 Acquisition:** not in this run (screens-only).
- **A6 Failure mining:** not in this run (screens-only).

## A3 Monetization (from screens, India storefront ₹)

- **Banner and hero (1673):** the banner reads "Get a 3-Day FREE Trial Enjoy all the benefits!". The X is faint, top-left.
  - The hero plate lists Poached Egg 143 Cal, Avocado 160 Cal and Toast 293 Cal under "248.8 Cal Total calories".
  - The items add up to **596**, not 248.8. **The paywall's own hero shows broken arithmetic** [OBSERVED numbers; sum INFERRED].
- **Plans (visible dimmed behind the banner on 1673; in full on 1674):**
  - "₹76.90 Per Week": unselected, and likely the annual plan shown as a weekly price [INFERRED].
  - "Free Trial" with a "Most Popular" tag: **pre-selected** (checked on both 1673 and 1674).
  - The price line "Free for 3-Day, then **₹999.00 per week.**" appears only on 1674, under the heading "Fast Food Tracking" above the plans (on 1673 the banner covers that area). 1674's hero is a "Calorie Intake" bar chart, not the plate.
  - A "Remind me before free trial ends" toggle, **OFF** by default.
  - Button: "Try For Free". Subline: "No payment now".
  - ₹76.90 × 52 = ₹3,998.80, which matches the xlsx's ₹3,999/yr [INFERRED].
- **"Lucky" screen (1675):** "Lucky Ones Only" / "Congratulations !" / "Limited Time Offer ₹999" / "Free for 3-Day, then ₹999.00 per week." It is **the same ₹999/week price, reframed as luck**.
- **Disagreement with Ganesh's notes:** the xlsx says "₹699/week" [DATA:ganesh-benchmark-xlsx]. The screens show ₹999/week. The screens are primary.
- **Why this matters:** a pre-selected weekly trial converts at **₹999 a week**: ₹999 × 52 = ₹51,948 a year, about 13× the ₹3,999 annual plan [INFERRED]. It is the only weekly-renewing default among the five apps captured here [INFERRED from the five notes].
- **US price:** `[UNKNOWN]`.

## A5 Screens lens

### Journey (capture order; matches content)

| # | stage | what user sees | asks | gives | verbatim copy | lever | friction / dark pattern | tag |
|---|---|---|---|---|---|---|---|---|
| 1655 | first-launch | meal card: 25 g carb / 11 g protein / 14 g fat; Food 267 kcal vs Goal 320 kcal | Get Started | the promise | "Smart Insights Hit Goals" | — | none | [OBSERVED] |
| 1656 | onboarding | goal | pick | — | "What's your goal?" Lose weight / Stay in shape / Gain muscle | — | — | [OBSERVED] |
| 1657 | permission (pre) | Health diagram | Continue (no skip visible) | a promise | "Connect to Apple Health and get your personalized plan instantly" | speed promise | **broken promise**: 9 more quiz questions follow (1658–1662, 1664–1665, 1668–1669); no skip on screen | [OBSERVED] |
| 1658–1660 | onboarding | gender, birth year 2001, height 176 cm | 3 asks | — | "What's your birth year?" | — | — | [OBSERVED] |
| 1661 | onboarding | weight 55.0 kg, live BMI | weight | BMI | "Your BMI: 16.1 Underweight  **You have a great potential to get in better shape, move now!**" | push to act | **ED red flag**: an underweight user is told to "move now!"; also 55 kg at 176 cm = BMI 17.8, not 16.1 | [OBSERVED; calc INFERRED] |
| 1662 | onboarding | activity | pick | — | "Not Very Active  I get winded while climbing stairs" | — | — | [OBSERVED] |
| 1663 | result | baseline maths: 1,663 × 1.2 = 1,996, with a ✏️ to edit the activity factor | Continue | **a transparent, editable number** | "How we got this number" / "This is your daily maintenance energy" | trust via transparency | none; **best plan screen in the set** | [OBSERVED] |
| 1664 | onboarding | allergies | multi | a promise | "We'll point out allergens as we track your meals." | — | — | [OBSERVED] |
| 1665 | onboarding | health concerns | multi | — | "Do you have any health concerns?" Cholesterol / Blood Pressure / Blood Sugar … | — | — | [OBSERVED] |
| 1666 | result | "Mediterranean Diet" card for Blood Sugar: nutrients, foods to eat, foods to avoid | Continue | **advice** | "Based on your answers, we recommend Mediterranean Diet" / "Sources of recommendation" | authority | "Foods to Avoid" list is moralising-adjacent | [OBSERVED] |
| 1667 | social proof / rating | 5 stars, user stats | Continue (no rating dialog captured) | — | "Share Your Thoughts" / "1,000,000 Users" / "80% of Appediet Users" / "Over 100,000 users have hit their target weight with Appediet" | social proof | five stars under "Share Your Thoughts" before any use; "80% of Appediet Users" has no stated predicate, so it cannot be checked against the 100,000 figure | [OBSERVED; rating-ask intent INFERRED] |
| 1668 | onboarding | attribution + referral code | pick | — | "How did you first hear about Appediet?" | — | a marketing question for the app | [OBSERVED] |
| 1669 | onboarding | tracking habit | pick | — | "Do you track your diet?" | — | — | [OBSERVED] |
| 1670 | explainer | scan demo | Continue | — | "Make diet tracking easy with AI" | — | — | [OBSERVED] |
| 1671 | permission (pre) | Smart Reminders toggle **on** in the capture; meal / water / weight reminders | Continue / Skip | — | "Let me send you notifications and be your guide for diet tracking!" / "Follows you, not the clock" | — | toggle on (whether it was pre-set is [UNKNOWN]) | [OBSERVED] |
| 1672 | result | plan: 1,996 kcal; Carb 274 g 55% / Protein 100 g 20% / Fat 55 g 25% | Let's get started | **the plan, before the paywall** | "Congratulations Your custom plan is ready!" / "Your Goal : maintain your current weight" Goal 64.7 kg | commitment | goal weight ≠ entered weight | [OBSERVED] |
| 1673 | paywall | plate hero, trial banner | — | — | "Get a 3-Day FREE Trial" / "248.8 Cal Total calories" | — | faint X; **wrong sum in the hero** | [OBSERVED] |
| 1674 | paywall | "Calorie Intake" chart hero; "Fast Food Tracking"; ₹76.90/week vs Free Trial (pre-selected) | Try For Free | — | "Free for 3-Day, then ₹999.00 per week." / "Remind me before free trial ends" (off) | default bias | **weekly trial pre-selected; reminder off** | [OBSERVED] |
| 1675 | downsell (fake) | "Lucky Ones Only" | Claim Now | — | "Congratulations !" / "Limited Time Offer ₹999" | false scarcity | same price framed as a lucky offer | [OBSERVED] |
| 1676 | core-task | meal picker | pick a meal | a first-log prompt | "What was your last meal?" / "Logging is the first step to your health journey" / "Talk about it later" | — | none; a good prompt | [OBSERVED] |
| 1677 | core-task | lunch log: search; tabs For you / History / My Food / My Meal; Scan Food / Barcode / Say Food / Quick Log; suggestions | log | **4 input modes** | Egg 71 kcal 1 medium; Rice Jasmine 194 kcal 1 cup; Chicken Grilled 100 kcal 4 oz … | — | US-centric suggestions (oz, cup) on the IN storefront; a crown icon marks premium | [OBSERVED] |

### The 8 measures

1. **First win.** Personal value comes **before** the paywall: the baseline maths (1663) at about screen 9, plus diet advice (1666) and the plan (1672). The first logged meal comes **after** the paywall. Launch to the log screen is 23 captured screens [OBSERVED]; tap count [UNKNOWN].
2. **Ask ledger.** Goal → Health permission (before anything is given) → gender → birth year → height → weight → activity → *(given: baseline 1,996, editable)* → allergies → health concerns → *(given: diet advice)* → rating → source → tracking habit → notifications → *(given: plan)* → payment. That is **14 asks** counting the rating screen (the xlsx says "16 questions") [OBSERVED count]. Value lands after asks 7, 9 and 13; this is the most interleaved give/ask rhythm of the five notes [INFERRED].
3. **Abstractions.** Calories, macros with % split (needed). **"Baseline" / activity multiplier** (needed, and taught well). **Diet type** recommended by the app (invented). **"Smart Reminders"** (invented label). **4 log modes plus "My Food" and "My Meal"** (partly needed).
4. **Feel-good moments.** The editable baseline (1663) is earned: the user sees how the number is built. "Congratulations Your custom plan is ready!" is half-earned, because the plan is real. "Lucky Ones Only" is manufactured.
5. **Feel-bad moments.**
   - The underweight BMI → "move now!" (1661). This is the worst ED copy in the set.
   - A "Foods to Avoid" list (1666).
   - A star-rating screen before use (1667).
   - Wrong maths on the BMI (1661) and on the paywall hero (1673); an unverifiable "80%" stat (1667).
   - A weekly-trial default with the reminder off (1674).
   - Fake luck (1675).
6. **Paywall.** Soft, with a faint X. Three screens: hero, plans, fake luck. A 3-day trial that converts to **weekly ₹999** by default. The annual price is shown as weekly.
7. **Repeat cost.** Meal picker → search screen with 4 modes. A quick-log from "For you" suggestions is likely about 2–3 taps (meal → item → add) [INFERRED]. A scan is likely meal → Scan Food → shutter → confirm, about 4 taps [INFERRED]. Return hooks: smart reminders (meal / water / weight).
8. **Feature map.**
   - Table stakes: scan, barcode, search, macros, reminders.
   - Differentiators: **transparent baseline maths**; "Say Food" voice log; health-concern-aware advice.
   - Bloat: the diet-type recommendation, the rating ask, attribution.

### Keep / Kill / Different

- **Keep:**
  - "How we got this number" with an editable activity factor (1663). Copy this nearly verbatim.
  - The give/ask rhythm (value after asks 7, 9, 13).
  - "What was your last meal?" (1676).
  - The 4 log modes on one screen (1677).
- **Kill:**
  - The BMI-push copy (1661).
  - Rating screen before use (1667).
  - The predicate-less "80%" stat (1667).
  - The weekly-trial default with the reminder off (1674).
  - Fake luck (1675).
  - Hero arithmetic that doesn't add up (1673).
  - A Health permission promising "instantly" with no skip (1657).
- **Different:** Show the maths for *every* number, including AI meal estimates: "Rice 1 cup ≈ 205 kcal × your portion", with the portion editable in place. If a user's BMI is under 18.5, never suggest a deficit or "move now". Default to maintenance, with neutral copy.

## A8 Verdict (short)

Appediet has the most *honest-feeling* plan screen in the category: transparent baseline maths, editable. It then undoes the trust with careless numbers (two arithmetic errors visible on screen: BMI 1661, hero sum 1673) and the most aggressive billing default (a weekly ₹999 trial pre-selected, reminder off). **Most exploitable weakness:** trust. A user who notices 143 + 160 + 293 ≠ 248.8 on the paywall has reason to doubt every AI estimate after it.

- **Copy:** transparent, editable baseline; value-interleaved quiz; multi-mode log screen.
- **Beat:** numeric correctness, billing honesty, ED-safe BMI copy.
- **Evidence strength:** onboarding/paywall strong; core loop medium (log screen seen, no log completed).
