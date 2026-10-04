---
type: category-screens
category: calorie-tracker
member: ganesh
run_by: harshil
updated: 2026-10-04
status: draft
scope: screens-only
sources: [screenshots:132 (5 apps, India storefront), itunes-lookup-us, ganesh-benchmark-xlsx]
---

# Calorie tracker: screens synthesis

**Apps:**
- [[members/ganesh/apps/calorie-tracker/cal-ai]] (27 screens)
- [[members/ganesh/apps/calorie-tracker/myfitnesspal]] (18)
- [[members/ganesh/apps/calorie-tracker/appediet]] (23)
- [[members/ganesh/apps/calorie-tracker/bitepal]] (48)
- [[members/ganesh/apps/calorie-tracker/healthify]] (16, a returning-user flow)

**Method:** `skills/app-researcher/prompts/a5-screens-lens.md`. This run used team screenshots only. Reviews were not mined; a few review lines are cited from Ganesh's xlsx notes and marked unverified.

**The biggest gap in the evidence.** Across all 132 screenshots, **no app shows a logged meal, an AI estimate, or a correction**. Every capture stops at the paywall, the log screen, or an empty home. So the part of the hypothesis about correction and repeat logging **cannot be tested from these screens**. See the open questions.

## 1. Pattern table

| App | Asks before first value | First value (screen #) | Invented concepts before first log | Paywall | First log reachable without paying? | Day-2 log taps |
|---|---|---|---|---|---|---|
| Cal AI | ~18 observed + gap (xlsx: 23) | none captured; plan reveal not seen | 3: Health Score, rollover, burn-back | **hard**, after quiz; 3-day trial; no X | **no** | `[UNKNOWN]` |
| BitePal | 25 before the plan | pet at #10 (emotional); BMI at #37 (1807), plan at #42 (1812) | 6: hearts, streak, shop, activity mode, burn goal, "metabolism"; plus a fasting window (not needed) | soft; -50% → gift → -60% with a 59:59 timer; no trial | yes, after paywall and account; **macros locked** | ~3–4 [INFERRED] |
| Appediet | 7, then value after asks 7, 9, 13 (14 total) | editable baseline maths at #9 (1663) | 1–2: recommended diet type, "Smart Reminders" | soft; **weekly ₹999 trial pre-selected**, reminder off; fake "Lucky" screen | yes, after paywall | ~2–4 [INFERRED] |
| MyFitnessPal | ~11 screens / ~16 fields incl. an email account | 2,500 kcal at #15 (1651) | 2: net calories, streak | soft; 7-day trial; honest terms | **yes, free manual logging** (with ads) | ~4 + typing [INFERRED] |
| Healthify (returning) | ~10 incl. phone account on screen 1 | setup summary #11; "Eat 1,450 Cal" #16 | heavy: product menu (Coach, SNAP, GLP-1, IF…), two tiers, Ria, 4 goal domains | soft; no trial; **3 prices within ~1 min** (clock 12:46 → 12:47) | logging yes; Snap is Healthify+ | `[UNKNOWN]` |

All counts come from the screens [OBSERVED], except where marked. The ₹ prices are India storefront only; the US prices for all five are `[UNKNOWN]`.

**What the table says:**
- Asks before the plan range from about 10 (Healthify, returning user) to 25 (BitePal); the median of the five is about 14 [INFERRED from the counts above].
- 4 of 5 apps put the photo log on the paid side (Cal AI: whole app behind a hard wall, 1845; MFP 1652; Healthify 1633; BitePal "Unlimited AI food photo recognition" per xlsx, free allowance `[UNKNOWN]`). Appediet's gating is `[UNKNOWN]`. Every one of them advertises photo logging on a welcome, explainer or paywall screen (Cal AI 1819/1844, Appediet 1670, BitePal 1776, MFP 1652, Healthify 1633).
- Only Cal AI blocks a non-payer from any log entry point. The other four reach a log screen or a home with log controls after closing the paywall, and the xlsx lists manual/text logging as free for all four [DATA:ganesh-benchmark-xlsx]. No capture completed a free log.

**Quiz length vs payoff.** On screen, the calorie number depends on about 6 inputs: sex, age, height, weight, activity and goal. Appediet's own maths shows this: 1,663 × 1.2 = 1,996 (1663) [OBSERVED]. Everything else (where you heard of us, tried other apps, barriers, accomplishments, meal-plan appetite, fasting, water, where you eat) **changes nothing visible in the plan**. The quiz is mostly a sales funnel dressed up as personalisation [INFERRED from OBSERVED plan screens].

The one exception: Appediet's health-concern answer does produce a diet card (1666), and Healthify echoes "Enabling Hypertension care" (1631).

## 2. Hypothesis verdict

The starting hypothesis: *"Logging friction is the whole game. Photo logging cut it; the next friction is correcting wrong estimates and repeat logging. Long quizzes may be investment or pure friction."*

| Claim | Verdict | Evidence |
|---|---|---|
| Logging friction is the whole game | **Partly confirmed, but aimed at the wrong moment.** In the first session, the friction is everything *before* the first log: 10–25 asks, an account in some apps, and a paywall. No captured flow reaches a log. | all 5 journeys |
| Photo logging cut friction | **Confirmed as the pitch; killed as a first-session reality.** It is gated in 4 of 5: Cal AI hard wall (1845), MFP premium (1652), Healthify+ Snap (1633), BitePal "unlimited" paid (xlsx). | screens + [DATA:ganesh-benchmark-xlsx] |
| Correction is the next friction | **Untested.** Zero correction screens were captured. The only signal is the xlsx review lines: Cal AI "fix this … never adjust macros or calories"; 8 grapes at 700+ cal; BitePal popcorn at 775 cal. These are [DATA:ganesh-benchmark-xlsx], not verified, with n=3. | gap |
| Long quizzes: investment or friction? | **Friction, unless value is interleaved.** Appediet (value after asks 7, 9, 13) and BitePal (pet after 4 asks, tone choice) earn their questions. Cal AI asks about 20 and hands back a loading bar. It may work because video-ad traffic has already *seen* the scan [INFERRED; 1823 only shows TikTok listed first]. | 1663, 1780, 1786 vs 1834–1845 |

**Net:** keep the hypothesis, but move its centre. Our edge is not a better scanner first. It is **letting the scanner be the first screen and free**, and then making a correction visible and trustworthy. The correction half needs a hands-on test before we bet on it.

## 3. Our first five minutes (screen by screen)

Our target is **one log in about 3 taps, about 6 asks in total, and the paywall after the first log**.

| # | Screen | Ask | Gives | Copy direction |
|---|---|---|---|---|
| 1 | Welcome | tap | the promise | "Snap your meal. See what's in it." Primary: **Scan a meal**. Secondary: "Type it instead". No account, no quiz. |
| 2 | Camera | system camera permission (in context, because the user just tapped Scan) | — | No pre-prompt screen. |
| 3 | Result | none | **the first win**: itemised list (item, portion, kcal), a total, and "how we got this" per item | Every portion is editable in place (a slider or chips such as ½, 1, 1½). "Looks off? Tap any line." Save says "Logged." Nothing more. |
| 4 | Your number (optional) | 4 inputs on one screen: sex/age, height, weight, goal. "It's OK to estimate" (borrowed from MFP 1649) | a daily target | The maths is shown and editable (borrowed from Appediet 1663). The first meal is drawn against it. **"Just let me log, no target"** is an equal-weight option. |
| 5 | How should I talk to you? (optional, 1 tap) | tone | voice control | Borrowed from BitePal 1786. Gentle is the default. |
| 6 | Paywall | payment (closable) | clarity | Says what stays free and what's paid. Annual plus monthly. The trial reminder is **ON by default**. The X is visible at once. One price, no downsell ladder, no timers. The logged meal stays visible behind the sheet. |
| later | after the 2nd log | notifications | — | "Want a nudge around lunch?" Asked only once the user has shown a habit. |
| later | after ~3 logged days | account / iCloud | — | "Keep your history safe across phones?" |

**Asks before the first win: 1** (camera). **Total asks in the first five minutes: about 6–7** (camera, 4 profile inputs, tone, payment). The current apps ask 10–25.

The free/paid line is a proposal: free manual and barcode logging plus a small daily photo allowance; paid for unlimited photo, macros and insights [INFERRED]. It has to be priced with stage B/C data; the screens cannot settle it.

## 4. Differentiators (max 3, each tied to evidence)

1. **The first scan is the first screen, and it's free.**
   - Evidence: no captured app lets a new user see their own meal analysed before paying or completing a quiz. Cal AI puts it behind a hard wall (1845); BitePal after paywall and account (1816–1817); Appediet after paywall (1676); MFP and Healthify gate photo logging (1652, 1633).
   - It also neutralises the trust problem: the user verifies accuracy before paying.
   - This is a **gap no shortlisted app fills in these India-storefront captures** [OBSERVED]; US flows are `[UNKNOWN]`.
2. **Show the maths, fix in place.**
   - Every estimate is itemised with its portion and a per-item "how we got this", and corrections happen on the result card. There is no separate "fix" flow.
   - Evidence: Appediet's editable baseline (1663) is the single most trust-building screen in the set. Appediet also shows how fast trust breaks: two on-screen arithmetic errors (1661 BMI 16.1 where 55 kg / 1.76² = 17.8; 1673 the hero 143 + 160 + 293 = 596 ≠ 248.8) [INFERRED arithmetic on OBSERVED numbers].
   - A correction complaint (Cal AI) and over-estimate complaints (Cal AI, BitePal) appear in Ganesh's notes [DATA:ganesh-benchmark-xlsx, unverified].
   - **Needs hands-on validation** of how each app corrects today.
3. **Gentle in the mechanics, not just the copy.**
   - Tone choice (BitePal 1786) with none of the pressure: no draining hearts (1787), no countdowns (1815), no "Lucky Ones Only" (1675), no "You Won't See This Offer Again!" followed by a cheaper offer on a differently named tier (1634 → 1636).
   - ED-safe defaults:
     - Never suggest a deficit or "move now!" when BMI is under 18.5. Appediet 1661 does exactly that.
     - An "I'd rather not see numbers" mode. A BitePal user with an ED praised this [DATA:ganesh-benchmark-xlsx].
     - Burn-back and rollover are off.
   - Evidence: BitePal has 55,700 US ratings since its 2024-06-10 release [DATA:itunes-lookup-us]; that its pet and tone drive this is [INFERRED]. Its mechanics contradict its brand, and nobody in the set is gentle in both.

## 5. Concepts we refuse to add

| Concept | Seen in | Why we refuse |
|---|---|---|
| Health Score | Cal AI 1843 | an invented number on top of calories; the user must learn it, and it adds nothing to the job |
| Rollover calories / burned-calories-back by default | Cal AI 1835, 1839; BitePal 1805; MFP "net" 1651 | teaches compensation ("earn" or "bank" food); an ED risk; available as an opt-in setting at most |
| Pet hearts that drain / streak loss | BitePal 1787, 1818; MFP ⚡ 1654; Healthify Streaks tab | guilt as retention; we use "You showed up" forgiveness instead |
| Fasting windows in onboarding | BitePal 1777–1792; Healthify 1636 | a different job; nudges restriction |
| "Metabolism type", recommended diet type | BitePal 1808; Appediet 1666 | pseudo-diagnosis; not needed to log |
| Product-menu question / multiple tiers | Healthify 1623–1624, 1632 vs 1636 | the user must learn our SKUs; one product, one price |
| Shop / in-app currency | BitePal 1818 | not needed for the job |
| "Calories left to burn" goal | BitePal 1818 | an exercise quota shown by default |
| Attribution and "tried other apps" before value | Cal AI 1823–1824; Appediet 1668 | serve us, not the user; ask after day 3 or use install attribution instead |
| Star-rating ("Share Your Thoughts") screen before use | Appediet 1667 | asks for praise before any experience |
| BMI category push copy | Appediet 1661 | shame and an ED risk; we show BMI only on request, with neutral copy |

## 6. Open questions (the screens cannot answer these)

1. **Correction flow** in all 5: what happens when the AI is wrong? How many taps does a fix take? Does a fix change kcal and macros? (Cal AI's "fix this" is reported as not adjusting [DATA:xlsx].) This needs **a hands-on test**: log the same 5 meals in each app, including Indian and US plates, and record the taps to correct.
2. **Day-2 taps to log** for each app: no repeat-log screens were captured. Hands-on test.
3. **Free photo allowance** in BitePal, Healthify and Appediet: what does a non-payer get? Hands-on test.
4. **US paywall prices and trial terms** for all 5: capture them on a US Apple ID.
5. **Cal AI:** is the plan number shown before the hard wall? (There is a gap between 1843 and 1844.) Is there a downsell on back-navigation? Recapture.
6. **Cal AI / BitePal BMI copy for an underweight input:** do they push a deficit like Appediet does? Re-run onboarding with BMI 17.
7. **BitePal:** does a "no calorie numbers" mode exist (xlsx ED review vs the 1818 home)? Hands-on test.
8. **Healthify new-user flow** (this capture is a returning user): recapture on a fresh Apple ID if Healthify stays in scope.
9. **Review mining (A6)** on all 5 to size the correction and accuracy clusters before differentiator 2 is committed.

## What would change the call

- **If** hands-on testing shows Cal AI's correction is already fast and accurate, differentiator 2 weakens. Lead harder on 1 and 3.
- **If** US paywalls show a free first scan, differentiator 1 is not a gap. The India storefront may differ.
- **If** review mining shows that churn is driven by price or billing rather than accuracy, move honest pricing up from a rule to the headline.

**Next stage:** run review mining (A6) on Cal AI, BitePal and Appediet, plus a hands-on correction and day-2 test. Then run stage B (market) for calorie-tracker. No `research/categories/calorie-tracker/lens.md` exists yet, so stage 0 should run first or in parallel.

## Verification (2026-10-04)

**Checked:** every claim traced to the five app notes (each verified against all 132 screenshots on 2026-10-04), the xlsx, or iTunes lookup. ~60 claims checked: ~25 numbers/counts, ~30 IMG refs, 5 xlsx claims, 2 US listing numbers.

**Corrections:**
- BitePal asks "~26" → 25 before the plan; "BMI/plan at ~#36–42" → BMI #37, plan #42; invented concepts 7 → 6 plus a fasting window.
- Appediet asks "6, value at 6/8/12 (13 total)" → "7, value after 7/9/13 (14 total)".
- Healthify "3 prices in ~60 s" → within ~1 min.
- "Category median about 13–20 asks" → range 10–25, median ≈ 14; "10–26 asks" → 10–25 (twice).
- "4 of 5 gate the photo log" → now says what each gate is; BitePal's free allowance and Appediet's gating are [UNKNOWN].
- **"The only app that lets a non-payer log is the 2009 incumbent" → removed.** Four of the five reach a log entry point after closing the paywall, and the xlsx lists manual logging as free for all four; only Cal AI blocks.
- BitePal "pet at ask ~9" → after 4 asks.
- Cal AI "works because TikTok traffic has already seen the scan" → "may work" [INFERRED].
- Differentiator 1 gap scoped to the India-storefront captures.
- Appediet "three on-screen arithmetic errors" → two (BMI, hero); the 1667 stat is ambiguous, not wrong.
- "Correction complaints for Cal AI and BitePal" → one correction complaint (Cal AI) and over-estimate complaints (Cal AI, BitePal).
- "BitePal's 55.7K ratings show emotion sells" → the causal link marked [INFERRED].
- "Rating prompt before use" → star-rating screen (no rating dialog captured).

**Not verifiable:** all US prices; any correction or day-2 flow; free photo allowances.
