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
| BitePal | ~26 | pet at #10 (emotional); BMI/plan at ~#36–42 | 7: hearts, streak, shop, fasting window, activity mode, burn goal, "metabolism" | soft; -50% → gift → -60% with a 59:59 timer; no trial | yes, after paywall and account; **macros locked** | ~3–4 [INFERRED] |
| Appediet | 6, then value at asks 6, 8, 12 (13 total) | editable baseline maths at #9 (1663) | 1–2: recommended diet type, "Smart Reminders" | soft; **weekly ₹999 trial pre-selected**, reminder off; fake "Lucky" screen | yes, after paywall | ~2–4 [INFERRED] |
| MyFitnessPal | ~11 screens / ~16 fields incl. an email account | 2,500 kcal at #15 (1651) | 2: net calories, streak | soft; 7-day trial; honest terms | **yes, free manual logging** (with ads) | ~4 + typing [INFERRED] |
| Healthify (returning) | ~10 incl. phone account on screen 1 | setup summary #11; "Eat 1,450 Cal" #16 | heavy: product menu (Coach, SNAP, GLP-1, IF…), two tiers, Ria, 4 goal domains | soft; no trial; **3 prices in ~60 s** | logging yes; Snap is Healthify+ | `[UNKNOWN]` |

All counts come from the screens [OBSERVED], except where marked. The ₹ prices are India storefront only; the US prices for all five are `[UNKNOWN]`.

**What the table says:**
- The category median is about 13–20 asks before the user is handed anything.
- 4 of 5 apps gate the photo log, which is the thing every one of them advertises on its welcome or paywall screen (Cal AI 1819/1844, Appediet 1670, BitePal 1776, MFP 1652, Healthify 1633).
- The only app that lets a non-payer log is the 2009 incumbent, and only by typing.

**Quiz length vs payoff.** On screen, the calorie number depends on about 6 inputs: sex, age, height, weight, activity and goal. Appediet's own maths shows this: 1,663 × 1.2 = 1,996 (1663) [OBSERVED]. Everything else (where you heard of us, tried other apps, barriers, accomplishments, meal-plan appetite, fasting, water, where you eat) **changes nothing visible in the plan**. The quiz is mostly a sales funnel dressed up as personalisation [INFERRED from OBSERVED plan screens].

The one exception: Appediet's health-concern answer does produce a diet card (1666), and Healthify echoes "Enabling Hypertension care" (1631).

## 2. Hypothesis verdict

The starting hypothesis: *"Logging friction is the whole game. Photo logging cut it; the next friction is correcting wrong estimates and repeat logging. Long quizzes may be investment or pure friction."*

| Claim | Verdict | Evidence |
|---|---|---|
| Logging friction is the whole game | **Partly confirmed, but aimed at the wrong moment.** In the first session, the friction is everything *before* the first log: 10–26 asks, an account, and a paywall. No captured flow reaches a log. | all 5 journeys |
| Photo logging cut friction | **Confirmed as the pitch; killed as a first-session reality.** It is gated in 4 of 5: Cal AI hard wall (1845), MFP premium (1652), Healthify+ Snap (1633), BitePal "unlimited" paid (xlsx). | screens + [DATA:ganesh-benchmark-xlsx] |
| Correction is the next friction | **Untested.** Zero correction screens were captured. The only signal is the xlsx review lines: Cal AI "fix this … never adjust macros or calories"; 8 grapes at 700+ cal; BitePal popcorn at 775 cal. These are [DATA:ganesh-benchmark-xlsx], not verified, with n=3. | gap |
| Long quizzes: investment or friction? | **Friction, unless value is interleaved.** Appediet (value at asks 6, 8, 12) and BitePal (pet at ask ~9, tone choice) earn their questions. Cal AI asks about 20 and hands back a loading bar. It works because TikTok traffic has already *seen* the scan [INFERRED from 1823]. | 1663, 1780, 1786 vs 1834–1845 |

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

**Asks before the first win: 1** (camera). **Total asks in the first five minutes: about 6–7** (camera, 4 profile inputs, tone, payment). The current apps ask 10–26.

The free/paid line is a proposal: free manual and barcode logging plus a small daily photo allowance; paid for unlimited photo, macros and insights [INFERRED]. It has to be priced with stage B/C data; the screens cannot settle it.

## 4. Differentiators (max 3, each tied to evidence)

1. **The first scan is the first screen, and it's free.**
   - Evidence: no captured app lets a new user see their own meal analysed before paying or completing a quiz. Cal AI puts it behind a hard wall (1845); BitePal after paywall and account (1816–1817); Appediet after paywall (1676); MFP and Healthify gate photo logging (1652, 1633).
   - It also neutralises the trust problem: the user verifies accuracy before paying.
   - This is a **gap no shortlisted app fills** [OBSERVED].
2. **Show the maths, fix in place.**
   - Every estimate is itemised with its portion and a per-item "how we got this", and corrections happen on the result card. There is no separate "fix" flow.
   - Evidence: Appediet's editable baseline (1663) is the single most trust-building screen in the set. Appediet also shows how fast trust breaks: three on-screen arithmetic errors (1661 BMI, 1667 stats, 1673 the hero 143 + 160 + 293 ≠ 248.8).
   - Correction complaints appear in Ganesh's notes for Cal AI and BitePal [DATA:ganesh-benchmark-xlsx, unverified].
   - **Needs hands-on validation** of how each app corrects today.
3. **Gentle in the mechanics, not just the copy.**
   - Tone choice (BitePal 1786) with none of the pressure: no draining hearts (1787), no countdowns (1815), no "Lucky Ones Only" (1675), no "You Won't See This Offer Again!" followed by a cheaper price (1634 → 1636).
   - ED-safe defaults:
     - Never suggest a deficit or "move now!" when BMI is under 18.5. Appediet 1661 does exactly that.
     - An "I'd rather not see numbers" mode. A BitePal user with an ED praised this [DATA:ganesh-benchmark-xlsx].
     - Burn-back and rollover are off.
   - Evidence: BitePal's 55.7K US ratings in about 2 years show emotion sells [DATA:itunes-lookup-us]. Its mechanics contradict its brand, and nobody in the set is gentle in both.

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
| Rating prompt before use | Appediet 1667 | asks for praise before any experience |
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
