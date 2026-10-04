---
type: category-screens
category: habit-tracker
member: ganesh
run_by: harshil
updated: 2026-10-04
status: draft
scope: screens-only
sources: [screenshots:112 in-app (Finch 35, Inner Grow 20, Productive 17, Grit 40) + Streaks 12 listing captures excluded, ganesh-benchmark-xlsx, itunes-lookup-us]
---

# Habit tracker: screens synthesis

Apps: [[members/ganesh/apps/habit-tracker/finch]] · [[members/ganesh/apps/habit-tracker/habit-tracker-inner-grow]] · [[members/ganesh/apps/habit-tracker/productive]] · [[members/ganesh/apps/habit-tracker/grit]] · [[members/ganesh/apps/habit-tracker/streaks]]

All captures are from the India storefront on 2026-10-03 `[INFERRED from ₹ prices and on-screen dates]`. Prices are ₹ and India-only. **None of the four captured journeys shows a completed check-in or a missed day.** Every capture stops at, or before, the first habit list.

## 1. Pattern table

| | Finch | Inner Grow | Productive | Grit | Streaks |
|---|---|---|---|---|---|
| In-app screens captured | 35 (IMG_2000 missing) | 20 | 17 | 40 | 0 (listing only) |
| Screens before the habit list | 34 | 19 (lands **empty**) | 15 | 39 | [UNKNOWN] |
| Taps to first check-in (approx.) | ≈38 | ≥25 + add-habit flow [UNKNOWN] | ≈15 | ≈41 | [UNKNOWN] |
| First check-in before or after paywall | after | after | after | after | no paywall (paid upfront) |
| Asks before first check-in | 23 | 12 | 12 | 20 | [UNKNOWN] |
| Quiz questions | 11 on 13 screens (+4 pet-setup choices) | 5 + 3 single-button "Yes" | 6 | 11 + 4 yes/no cards | [UNKNOWN] |
| Concepts visible by day-1 home | 16 | 9–10 | 7 | 10 | [UNKNOWN] |
| Concepts *required* for first check-in | 0 (✓ button) | check-in method (asked) | 0 (swipe, coached) | 0 (⊕) | [UNKNOWN] |
| Manufactured rewards | stat toast, app-open streak, loader, "-401%" | uncited "studies" chart | "program" loader | forecast curve, diagnosis, loader, "Congratulations!" | — |
| Paywall | soft, 4 screens, pre-home; ✕ only as a skip link on the last | pre-home ✕ + 24-hour countdown downsell | pre-first-habit ✕, **weekly default** | pre-home ✕, yearly default, opt-in trial | ₹599 / $5.99 upfront |
| Price (India) | ₹3,499/yr, 7-day trial | ₹599/yr (3-day trial) · ₹999 lifetime · ₹799 downsell | ₹599/wk · ₹9,900/yr | ₹1,299/yr · ₹299/mo · ₹2,499 lifetime | ₹599 |
| Repeat cost per habit | 1 tap | 1 tap or swipe | 1 swipe | 1 tap (▶ for timers) | [UNKNOWN] |
| Missed-day handling seen | none | none | none | none | none |

All cells are `[OBSERVED]` in the app notes unless marked; tap counts are `[INFERRED]` (method in each note). Ganesh's xlsx disagrees on price or onboarding length for all four subscription apps. Each note says how.

**Five patterns the screens show:**
1. **Every subscription app runs the same quiz funnel:** questions → fake loader → paywall → list. The questions are nearly identical across apps: sleep (Finch #14, Grit #10), getting out of bed (Finch #15, Grit #11), procrastination (Inner Grow #7, Productive #10, Grit #19) and focus (Productive #11, Grit #18) `[OBSERVED]`. In none of the captured runs does a quiz answer visibly change what the user gets (Finch's quiz only branches to a follow-up question, #24). Inner Grow lands on an empty list, Productive offers a 6-option picker, and Grit showed "Could be better" on all four axes `[OBSERVED]`. Each app was captured once, so whether answers change anything on other paths is `[INFERRED]`.
2. **The paywall always comes before the first check-in.** 4 of 4 `[OBSERVED]`.
3. **Micro-habits are the category's default first step.** "Get out of bed / Brush teeth / Wash my face" (Finch #35) and "Get Out of Bed / Stretch / Wash Your Face" (Grit #36) `[OBSERVED]`. The winner and the newest challenger converged on the same lowest-possible bar.
4. **Commitment contracts are everywhere:** "I promise!" (Inner Grow #15), "Hold to agree" (Grit #37) and "How many days in a row will you take care of Rainbow?" (Finch #34) `[OBSERVED]`. Inner Grow's promises are never turned into habits.
5. **Warm, forgiving copy coexists with manipulative pricing in the same funnel.** Grit's "consistent, not perfect" sits next to a pre-ticked "special offers" toggle. Finch's "doing what you can" sits next to "-401% OFF / Offer expires when you exit this screen!" `[OBSERVED]`.

## 2. Our first five minutes (screen by screen)

Target: **first check-in at about 15 seconds and 2 taps**, no account, no quiz, no price before value. One concept: *a habit you tick*. Copy is draft.

| # | Screen | User does | User gets | Asks | Why (evidence) |
|---|---|---|---|---|---|
| 1 | "Pick one small thing for today." 6 micro-habit chips: Get out of bed · Drink a glass of water · Brush teeth · Stretch 2 min · Step outside · Write one line. "+ Your own" | tap one chip | it is now their habit | 0 (a choice, not a question) | Finch #35 and Grit #36 defaults; Productive #15 "Let's start with one of these" |
| 2 | Today: that one habit, a big ring, a hint: "Done already? Tap it." | tap the ring | **first check-in.** Soft haptic, ring fills, "That's today. Nice." | 0 | No app reaches a check-in before ~15 taps (table) |
| 3 | "Add another? (you can skip)" with the same chips plus "That's enough for now" as an equal-weight button | 0–2 taps | a list of 1–3 | 0 | Grit #36 lets users pick several; capping at 3 keeps the day-1 bar low `[INFERRED]` |
| 4 | "Want a nudge tomorrow?" The time is prefilled from when they just checked in (e.g. 8:40). Buttons "Remind me" / "No thanks". iOS prompt only after "Remind me". One toggle; nothing bundled. | 1 tap | a reminder they chose | 1 (notifications) | Finch #10 persona ask with equal "Maybe later"; Grit #34 bundled marketing is what we refuse |
| 5 | Back on Today; done. **No paywall in session 1.** Paywall appears only when the user reaches for a paid feature (4th habit, history beyond 7 days, widgets themes) or on day 3 after a check-in: one yearly plan as default, monthly secondary, trial timeline with charge date, ✕ visible from frame 1. | — | — | 0 | Finch #29 timeline (keep); Productive #14 weekly default, Inner Grow #18 countdown, Finch "-401%" (kill) |

**Missed day (day 2+):** the habit shows "Rested yesterday" in neutral grey, never red, with no sad face. The headline count is **"days this week"** (e.g. "4 of 7"), not consecutive days, so one miss costs one dot, not the whole chain. Optional second line: "Longest run: 12 days" (it never resets, it is just history). Users who want a classic streak can turn it on in settings; it stays off by default `[INFERRED]`. This must be validated by review mining (open question 1).

Monetisation honesty check: free = up to 3 habits, check-ins, reminders, a 7-day view. Paid = unlimited habits, full history and stats, widgets, Health auto-check. That matches the free/paid line in Ganesh's xlsx, where Inner Grow, Grit and Productive keep core tracking free `[DATA:ganesh-benchmark-xlsx]`. Caveat: the xlsx is wrong on price for all four apps, and Inner Grow's own paywall lists "Unlimited habits" as a Pro feature (#17), contradicting the xlsx's "Track unlimited habits… free". Paywall conversion without an onboarding paywall is unproven `[UNKNOWN]` (open question 4).

## 3. Differentiators (max 3)

1. **The 15-second first check-in.** We pick a micro-habit on screen 1 and the user ticks it on screen 2. There is no quiz and no paywall first.
   *Evidence:* screens before the list are 34, 19, 15 and 39 (table). All 4 put the paywall first. Inner Grow ends on "No Habits / Tap "+" to add your first habit." after a pledge (#15 → #20) `[OBSERVED]`. In each captured run the quiz led to an outcome with no visible link to the answers `[OBSERVED]`; that it ignores answers in general is `[INFERRED]` (one capture per app).
2. **Week-based progress instead of a consecutive streak, so a missed day costs one dot, not the chain.** Copy reacts with rest, not failure.
   *Evidence:* Inner Grow chose to showcase reviews saying "I lost the streak" and that other apps "create guilt from not finishing everything that day" (#16) `[OBSERVED]`. Grit's own pledge is "I will stay consistent, not perfect" (#37), yet its mock UI counts consecutive flames (#2) `[OBSERVED]`. Finch's streak is earned by opening the app, and its commitment screen asks "How many days in a row will you take care of Rainbow?" (#32–#34) `[OBSERVED]`. Streaks' whole positioning is "a streak of consecutive days" `[DATA:itunes-lookup-us]`. **No app in the set shows a forgiving missed-day mechanic on screen.** This is the gap, but it is still `[INFERRED]` from screens. Review mining must confirm streak-loss as a 1–2★ cluster.
3. **Earned-only delight.** Every celebration is caused by a real check-in: a companion or visual that grows from actual completions. There are no stats for answering questions, no "1 DAY STREAK" for opening the app, no fake loaders and no fake diagnoses.
   *Evidence:* Finch's emotional pull comes from giving first (pet at tap 2, #5) and from reciprocity ("When you take care of yourself, you take care of me, too!", #9). Its manufactured moments are separable and add nothing to the job: "+5.6 Compassion" (#9), "1 DAY STREAK" (#32), "Generating your self-care goals…" (#25). Grit's "Could be better" ×4 (#31) and Productive's "Building up your personalized program…" (#13) look like theatre: the screens are `[OBSERVED]`, the reading is `[INFERRED]`. Whether we ship a character at all (the Finch route) or a quieter visual (the Streaks route) is a design call. The rule is the same either way: it only moves when the user does something.

## 4. Concepts we refuse to add

| Concept | Seen in | Why we refuse |
|---|---|---|
| Currencies / reward tokens per habit | Finch #35 (≥3 icons) | Turns self-care into an economy; needs a Shop and a Bag to spend; the job doesn't need it |
| Pet stats / traits ("+5.6 Compassion") | Finch #7, #9 | Manufactured numbers with no meaning |
| Adventures / quests / challenges | Finch #35, Productive #17 | A second progress system competing with the real one |
| Habit type, groups, colour, icon, description at creation | Grit #3 | 7 fields before the first tick; we give defaults and let users edit later |
| Check-in method choice | Inner Grow #19 | A decision with no value; we choose tap |
| Time-of-day sections on day 1 | Productive #17, Finch #35 | Meaningless with 1–3 habits; can appear automatically later |
| Commitment contracts / pledges / "days in a row" goals | Inner Grow #15, Grit #37, Finch #34 | Turn a miss into a broken promise, the very guilt we design against |
| Diagnosis scores ("Could be better") | Grit #31 | Generic verdicts dressed as personal ones |
| Social groups at v1 | Inner Grow #4, Finch "Friends" tab | Adds accounts and a network; not needed for the first win |
| Mental-health condition intake | Finch #20 | Sensitive data before value; not needed to tick "Drink water" |

## 5. Hypothesis verdict

Prior (lens): *"Concept bloat (habits, routines, goals, areas, points) and streak guilt drive churn. Finch wins on emotion, not mechanics. Our edge is probably fewer concepts, forgiveness instead of guilt, and a first check-in within 30 seconds."*

| Part | Verdict | Why |
|---|---|---|
| Concept bloat drives churn | **Partly killed** | Finch, the winner, shows the *most* concepts (16 on day 1). None of them block the first check-in, because they are dressed as the pet's world. What the screens actually show is that **concepts required *before* the first check-in** are the cost, and **total concepts** are not. Churn itself cannot be seen in screens. |
| Streak guilt drives churn | **Unverified** | No screen in any app shows a missed day. The indirect signals all point the same way: Inner Grow's own showcased reviews mention "lost the streak" and "guilt"; Finch ("1 DAY STREAK", "days in a row"), Grit (streak flames on its mock, #2) and Inner Grow (day counts with flame icons on its mocks, #2) show consecutive-day framing, while Grit and Finch use forgiving copy. Productive's capture shows no streak framing. Send this to review mining. |
| Finch wins on emotion, not mechanics | **Confirmed, with a correction** | Finch's mechanics are *heavier* than anyone's (currencies, adventure, shop, quests). Emotion is the wrapper that makes them feel like play. The emotion that matters is reciprocity: it gives a pet first, and caring for the pet means caring for yourself. The manufactured bits are separable. |
| First check-in within 30 s is our edge | **Confirmed, and wider than expected** | The fastest competitor needs about 15 taps, and all four need ≥15 screens and put the paywall first. The gap is not 30 s versus 60 s; it is about 2 taps versus about 15–41 (Productive ≈15, Finch ≈38, Grit ≈41; Inner Grow ≥25 plus an uncaptured add-habit flow). |
| Forgiveness instead of guilt is our edge | **Plausible, not yet evidenced** | The copy already uses forgiveness (Grit #4, #31, #37; Finch #8). No **mechanic** in the screens does. The edge is a mechanic that matches the copy. |

**Biggest surprise:** the category's winner is the most concept-heavy app, not the lightest. And every subscription competitor, including the "gentle" ones, runs the same quiz → fake loader → paywall funnel before the user can tick anything.

## 6. Open questions (send to review mining or a hands-on test)

1. **What happens on a missed day** in Finch, Grit, Productive, Inner Grow and Streaks? Does the streak reset, and is there a freeze or repair item, and is it paid? Hands-on: install, check in on day 1, skip day 2, capture day 3. Reviews: search 1–2★ for "streak", "lost", "reset", "guilt".
2. Finch's IMG_2000 is missing, and the user-name entry screen was not captured. Do they hide another ask or paywall screen?
3. Streaks: buy it ($5.99 US) and capture first launch → first task → completion → missed day → widgets. It is our only no-funnel benchmark.
4. Does dropping the onboarding paywall cost too much conversion? Screens cannot answer this. Look for public benchmarks on onboarding versus contextual paywalls, or A/B test it ourselves.
5. US pricing for all four. Every price here is ₹ (India). A US-storefront capture of each paywall is needed before stage C pricing.
6. Finch's free tier after the trial is skipped: how many goals, and is the pet gated? It was not captured.
7. Repeat-day hooks: notification copy on days 2–7 for each app (pet-voiced versus generic), and whether guilt appears in notifications rather than in-app.
8. Ganesh's xlsx disagrees with the screens on price and onboarding length for Finch, Inner Grow, Productive and Grit (see each note). Re-check the xlsx before anyone quotes it.

## Verification (2026-10-04)

Every claim was traced to the four app notes (verified the same day against all 112 in-app screenshots, the xlsx and the iTunes API) or to the screenshots directly. Streaks' 12 listing captures were confirmed as App Store images, not in-app screens.
- Checked: pattern table (13 rows × 5 apps), ≈30 IMG/# refs, ≈20 quotes, 1 xlsx claim, 1 API claim, all tap/ask/concept/quiz counts recomputed from the notes.
- Corrections:
  - Taps: Inner Grow "≥22" → ≥25; Productive "≈16" → ≈15; Grit "≈42" → ≈41. Ranges "~16 taps" → ~15 and "16–42" → 15–41, with per-app values shown.
  - Asks: Finch "≈21" → 23; Grit "≈22" → 20.
  - Quiz questions: Finch "13" → 11 on 13 screens; Grit "13" → 11.
  - Concepts: Finch "≈15" → 16 (table and verdict); Inner Grow "≈8" → 9–10; Productive "≈6" → 7; Grit "≈8–9" → 10.
  - "In no app does a quiz answer change…", "Grit tells everyone", "every competitor's quiz… ignores the answers" → limited to the captured runs; the generalisation is tagged `[INFERRED]` (one capture per app; Finch's quiz does branch, #24).
  - "pure theatre `[OBSERVED]`" → screens observed, reading `[INFERRED]`.
  - "all four apps sell consecutive-day framing while using forgiving copy" → Finch, Grit and Inner Grow show consecutive-day framing; Productive's capture shows none.
  - xlsx free/paid match: caveat added, because Inner Grow's paywall (#17) lists "Unlimited habits" as Pro, contradicting the xlsx.
  - Capture date tagged `[INFERRED]`.
- No conclusion in §5 changes: the gap is still about 2 taps versus about 15 to 41, and the paywall is first in 4 of 4.
- Could not verify: missed-day behaviour, any first check-in, US prices (none captured).
