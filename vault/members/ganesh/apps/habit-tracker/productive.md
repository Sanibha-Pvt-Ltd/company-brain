---
type: app
category: habit-tracker
app: "Productive - Habit Tracker"
app_store_id: 983826477
member: ganesh
run_by: harshil
updated: 2026-10-04
status: draft
scope: screens-only
screens_analysed: 17
reviews_analysed: 0
sources: [screenshots:17, ganesh-benchmark-xlsx, itunes-lookup-us]
---

# Productive - Habit Tracker (Mosaic S.r.l.)

Screens: `ganesh_screenshots/Habit Trackers/Productive - Habit Tracker/` IMG_2082–2098 (17 files, contiguous). India storefront, captured on 2026-10-03 `[INFERRED: Today = SA 3]`. The journey ends at the first habit **before** it was completed. Context: [[members/ganesh/drafts/habit-tracker/screens-synthesis]]

## A1 Snapshot (short)

| Field | Value |
|---|---|
| Developer | Mosaic S.r.l. `[DATA:itunes-lookup-us 2026-10-04]` |
| US price | Free with IAP `[DATA:itunes-lookup-us]` |
| US rating | 4.60 from 91,069 ratings `[DATA:itunes-lookup-us 2026-10-04]` |
| Version | 3.26.39, released 2026-03-19 (≈6.5 months without an update). First release 2015-06-02. Genre Productivity `[DATA:itunes-lookup-us]` |
| Last notes | "Hello readers! In this update we've fixed few bugs and polished the app." `[DATA:itunes-lookup-us]` |
| Lead promise | "The best time to start is now!" `[OBSERVED #2, #4]` |

## A2 Business performance
Not in this run (screens-only).

## A3 Monetization (from screens)

- **Plans (India storefront):** "Not sure yet? Enable Free Trial" (an unticked radio), "MOST POPULAR Weekly ₹599.00/week" and "Yearly ₹9,900.00/year" `[OBSERVED #13]`. The US price is `[UNKNOWN]`.
- **Default and framing:** **Weekly** is the highlighted, badged tile. Weekly costs about ₹31,148 a year at that rate, about 3× the yearly plan `[INFERRED: 599 × 52]`. Defaulting to weekly is the costliest-plan trap. The trial is opt-in, which is honest, but it is worded "Not sure yet?" so taking the trial reads as doubt `[INFERRED]`.
- **Placement:** after the quiz and the "Building up your personalized program…" loader, and **before the user picks a first habit** `[OBSERVED #12–#14]`. A ✕ shows top-left with "Already purchased?" `[OBSERVED #13]`. No downsell was captured after closing.
- **Disagreement with Ganesh's xlsx:** the xlsx says "₹2,499/yr (7-day trial) or ₹599/mo" and "Up to 5 active habits" free `[DATA:ganesh-benchmark-xlsx]`. The screens show **₹599/week** and **₹9,900/yr**, with no trial length shown `[OBSERVED #13]`. The free-habit cap was not visible on screen `[UNKNOWN]`. Ganesh, please correct the row.

## A4 Acquisition
Not in this run. On-screen data point: the ATT pre-prompt says tracking will "Create a better community by bringing more users like you to Productive" `[OBSERVED #5]`. That means paid user acquisition depends on ATT opt-in `[INFERRED]`.

## A5 Screens lens

### Per-screen table (capture order = journey order; the system ATT dialog was not captured)

| # | file | stage | what user sees | asks of user | gives to user | verbatim copy | lever | friction / dark pattern | tag |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 2082 | first-launch | dark loader | wait | — | "Update in progress… This may take a moment" | — | a wait on first launch | [OBSERVED] |
| 2 | 2083 | consent | app icon | accept terms | — | "The best time to start is now!" "By continuing you accept our Terms of Service…" "Accept and Continue" | — | — | [OBSERVED] |
| 3 | 2084 | consent | privacy wall | accept tracking | — | "We value your privacy. … To give your consent, tap Accept All and Continue. … If you prefer that we only use essential technologies … tap X in the top corner of the screen." "Accept All and Continue" / "Customize Preferences" | default bias | **reject is a small ✕, accept is the big button** | [OBSERVED] |
| 4 | 2085 | onboarding | hiker illustration | "Let's do it" | — | "You're about to take the first step in changing your life! Let us guide you through it." | journey | — | [OBSERVED] |
| 5 | 2086 | permission | ATT pre-prompt | Continue (to system ATT) | — | "Get a personalized experience / By allowing tracking … Improve your experience with the help of bug reports and analytics / Create a better community by bringing more users like you to Productive" "Your privacy is always paramount" | euphemism | frames ad tracking as "community" | [OBSERVED] |
| 6 | 2087 | quiz | time wheel | wake time | — | "What time do you usually wake up?" | — | — | [OBSERVED] |
| 7 | 2088 | quiz | — | energy | — | "What is your energy level throughout the day?" | — | — | [OBSERVED] |
| 8 | 2089 | quiz | options animating in | — | — | "How satisfied are you with your current lifestyle?" | — | duplicate capture of #9 mid-animation | [OBSERVED] |
| 9 | 2090 | quiz | — | satisfaction | — | "Completely — I feel very active and energized / Somewhat … / Not at all — I'm sedentary and would like to see a major change" | — | — | [OBSERVED] |
| 10 | 2091 | quiz | — | procrastination | — | "Do you often procrastinate?" | — | — | [OBSERVED] |
| 11 | 2092 | quiz | — | focus | — | "Do you find it hard to focus?" | — | — | [OBSERVED] |
| 12 | 2093 | quiz | — | goal | — | "What do you expect to achieve with Productive?" | — | — | [OBSERVED] |
| 13 | 2094 | loading | animated shapes | wait | — | "Building up your personalized program…" | labour illusion | **manufactured**; the "program" turns out to be one habit the user picks | [OBSERVED] |
| 14 | 2095 | paywall | 3 tiles | buy / ✕ | — | "Get access to Productive Pro with no limits!" "Not sure yet? Enable Free Trial" "MOST POPULAR Weekly ₹599.00/week" "Yearly ₹9,900.00/year" | default, social proof | **weekly default**, paywall before first habit | [OBSERVED] |
| 15 | 2096 | core setup | 6 habit options | pick first habit | a habit | "Choose your first habit / Let's start with one of these. You can add more habits later." Exercise / Drink water / Study online / Focus with Pomodoro / Read / Eat a healthy meal | one-thing focus | good: one choice, no config | [OBSERVED] |
| 16 | 2097 | core-task | coach mark over habit card | swipe right | first-check-in guidance | "This is your first habit. Swipe right 👉 to complete it" "Study online ★ New 25m" | guided first action | — | [OBSERVED] |
| 17 | 2098 | core-task | home: time-of-day tabs, 4-tab bar | — | — | "Evening / All Day / Morning / Afte[rnoon]" tabs "Today / Challenges / Stats / Explore" | — | the coach mark was dismissed without completing; first check-in not captured | [OBSERVED] |

### The 8 measures

1. **First win.** One swipe past #16, so ≈16 taps/swipes from launch (approximate: 1 per screen, +1 for the system ATT dialog), **after the paywall** `[INFERRED]`. The completion itself was not captured `[UNKNOWN]`.
2. **Ask ledger.** Terms, the cookie/tracking consent, the ATT pre-prompt plus the system ATT, wake time, energy, satisfaction, procrastination, focus, goal, the paywall and the first habit: **12 asks** before a check-in. Gives before the paywall: an illustration and a fake loader. The first real give (a habit) comes **after** the price.
3. **Abstractions:** habits, time-of-day sections (Morning/Afternoon/Evening/All Day, #17), timer habits ("25m", #16), Challenges, Stats, Explore and Pro. That makes **≈6**. Light on day 1; the time-of-day tabs are the one invented layer.
4. **Feel-good:** the "Choose your first habit… You can add more habits later" restraint (#15) and the guided first swipe (#16). Manufactured: "Building up your personalized program…" (#13), whose output is a 6-option picker that ignores the quiz `[INFERRED]`.
5. **Feel-bad:** a big Accept-All against a small ✕ to reject (#3); "community" framing for ad tracking (#5); weekly-as-default (#14); "Update in progress…" on first launch (#1). Missed-day behaviour: `[UNKNOWN]`.
6. **Paywall:** pre-value, dismissible ✕, weekly default, opt-in trial, no downsell seen. See A3.
7. **Repeat cost:** 1 swipe per habit `[OBSERVED #16]`. Return hooks seen: none in the capture. Notifications were never asked for in the captured flow `[OBSERVED]`, so the reminder ask probably comes later `[UNKNOWN]`.
8. **Feature map.** Table stakes: list, swipe check, stats. Differentiators: built-in timer habits, Challenges, Explore content. Bloat on day 1: time-of-day tabs before the user has more than one habit.

## Keep / Kill / Different

**Keep**
- "Choose your first habit" with 6 options and nothing else (#15). It is the lightest habit-creation step in the set.
- The coach mark that names the single action: "Swipe right 👉 to complete it" (#16).

**Kill**
- The cookie wall where reject is a corner ✕ (#3) and the euphemistic ATT copy (#5).
- A quiz whose answers do not change the outcome, plus the fake "program" loader (#6–#13).
- Paywall before the first habit, with weekly as default (#14).

**Different**
- Habit picker on screen 1 (Productive's #15 moved to the front). First check-in on screen 2.
- If we show a paywall at all in onboarding: yearly is the default, the weekly-equivalent price is never the hero, and it comes after the first check-in.
- No ATT on first launch. Ask only if and when we run paid UA, and say plainly "to measure our ads".

## A6 Failure mining
Not in this run (screens-only).

## A8 Verdict (short)

Productive has the right instinct buried at screen 15 ("Let's start with one of these"). In front of it sit a consent wall, ATT, a 6-question quiz, a fake loader and a weekly-default paywall. The app has not shipped an update since March 2026 `[DATA:itunes-lookup-us]`. **Copy:** single first-habit picker and guided first swipe. **Beat:** order of operations, so value comes before the price. **Most exploitable weakness:** the ₹599/week default, about 3× the yearly price, on a habit app whose job lasts months.

Evidence strength: A1 strong · A3 strong (India) · A5 strong for onboarding, weak for the core loop.
