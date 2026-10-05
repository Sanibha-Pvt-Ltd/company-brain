---
type: category-product-strategy
category: sleep-tracker
member: harshil
updated: 2026-10-05
status: draft
sources: [context.md, screenshots:279 across 8 apps, team research:Sleep_App_Analysis.pdf, knowledge:sanibha-app-factory-knowledge-base.md, organic-growth-knowledge-base.md, web:0]
---

# Sleep Tracker — final recommendations (v1)

Built on [[research/categories/sleep-tracker/context]]. Decision-only. Prices, name and the paywall timing test are open until the items under "Before build" are closed. All competitor prices seen in captures are India storefront (₹) and are not US prices.

## Positioning

**Positioning statement**
For adults who already own an Apple Watch (or will log two times a day) and wake up tired after a night their tracker called "fine", Tonight (working name) is the sleep-experiment app that turns the sleep data already in Apple Health into one small change to try tonight, then shows honestly what changed over seven nights. Unlike Sleep Cycle, ShutEye, Sleep Monitor and Leap's Sleep Tracker, it starts from your real past nights, not from a quiz, and it never gives you a score or a "risk" it can't stand behind. Unlike RISE and SleepWatch, it runs one planned test at a time against your own baseline instead of passively tagging habits.

**Messaging**

| Layer | Message |
|---|---|
| Line | Stop tracking bad sleep. Start testing what helps. |
| Acquisition hook | "You know you slept badly. What will you try tonight?" |
| Differentiator | One 7-night experiment at a time, compared with your own past nights, with the night count and the limits shown on the result. |
| Emotional benefit | Less worry about the numbers; a clear next thing to do tonight. |
| Retention reason | The next experiment, and a running log of what has and hasn't helped you. |

**Target user**
- Primary: Apple Watch owner, 25–45, who already has weeks or months of sleep in Apple Health and still feels tired.
- Secondary: no-Watch user willing to log bedtime and wake time (manual path, clearly labelled as more limited before purchase).
- Not v1: snorers wanting audio evidence, people wanting a sound machine, people seeking a diagnosis, shift workers needing schedule planning.
- Searches: "sleep tracker", "sleep tracker apple watch", "improve sleep", "sleep habits".
- Fears: another number to feel bad about, a tracker that is wrong about their night, being charged after a "free" start, health data leaving the phone.

**Name:** "Tonight" is a placeholder until cleared. Stay in the "tonight / next step / experiment / notebook" territory. Never use "doctor", "clinic", "diagnose", "AI" or "score" in the name.

**Proof the user sees in the product**
1. Before any paywall, the app shows the user's own imported nights: how many nights were found, average recorded sleep, bedtime range, and where each night came from (Watch, iPhone, manual).
2. Every experiment result shows the number of baseline nights and experiment nights used.
3. Every result carries the line "Other changes could also explain the difference."
4. "Not enough nights to tell" is a real result state, shown when it's true.
5. Every night is editable, and edited nights are marked "Edited".
6. The morning check-in asks how rested you feel before it shows any number.
7. The paywall states price, period, trial end date and renewal; the X is visible from the first frame; the trial reminder is on by default.
8. A "Not a medical device" line is on the onboarding safety screen and in Settings.

**App Store screenshots.** Shots 1–3 tell one story; every shot uses real app UI with clearly sample data.

| # | Headline | Content |
|---|---|---|
| 1 | "You know you slept badly. What will you try tonight?" | Home: last night's recorded sleep, "How rested do you feel?", Tonight card "Caffeine cutoff: 2 PM" |
| 2 | "Test one change for seven nights." | Experiment in progress: 7 night dots, 3 filled, one yes/no question |
| 3 | "See what changed — honestly." | Result: baseline vs experiment nights, night counts, caveat line |
| 4 | "Starts with the nights already in Apple Health." | Import screen: "We found 186 nights" (sample), sources listed |
| 5 | "No sleep score. No scare screens." | Night detail with plain observations |
| 6 | "Your first experiment is free." | Experiment library with five experiments |

- Store shots never show user counts, star laurels, "#1", "clinically proven", percentage improvement claims or before/after sleep claims.

**Ad angles (Meta, in test order)**
1. **Experiment (lead):** user sees a sleep score, shrugs, opens Tonight, picks "Earlier caffeine cutoff", day 7 result appears. Store line: "Stop tracking bad sleep. Start testing what helps."
2. **Apple Watch owners:** "Your Watch already knows how you slept. Put it to work." Watch → import → baseline → experiment.
3. **Control:** conventional "See how you really slept" summary creative, to benchmark the category promise.
4. **Honest-app angle (test once 1–3 have data):** "Most sleep apps start with a quiz. We start with your real nights." No competitor names or screenshots in the ad.

**We will never claim**
- That the app improves sleep, or any percentage of users improved, until a designed study supports it.
- That a change *caused* a result. Only "your recorded sleep was longer/shorter during the experiment".
- Sleep apnea, snoring, breathing, disease or "health risk" detection of any kind.
- CBT-I, therapy, or "programme" language implying treatment.
- Sleep stage accuracy beyond what Apple Health provides; we show it as recorded by the source.
- "Free" anywhere a trial converts to paid without the full terms beside it.

## UI/UX

**Design principles (tie-breakers)**
1. Real nights before anything else: show the user's own imported data before any quiz, account or paywall.
2. Feeling first, number second: the morning screen asks how rested you feel before it shows duration.
3. One change at a time: the app never runs two experiments at once or shows more than one action for tonight.
4. Say what we don't know: sample size and the caveat are part of every result, not a footnote.
5. Every ask earns its place: no permission or question is asked before the screen that needs it, and every one can be skipped except Health for the Watch path.
6. Calm, not alarming: no red warnings, no "needs attention", no countdowns, no sad mascots.
7. One tap a day: the daily cost of using the app is one morning tap and one evening tap.

**Structure (3 tabs)**

| Tab | Holds |
|---|---|
| Tonight (home) | Last night summary + rested check-in; tonight's one action; current experiment progress; empty/connect states |
| Experiments | Library of 5 experiments; current experiment detail; completed experiments log with results |
| Nights | Calendar/list of nights with source labels; night detail (duration, in-bed window, awakenings and stages only if the source provides them); edit/add night; 30-night trend |

Settings (gear on Tonight): Apple Health connection, reminders, pause mode, subscription & manage, restore, privacy & data deletion, "Not a medical device" note, support.

**First five minutes** (Watch path; first win marked)

| # | Screen | What's on it | Primary action | Asks | Given so far |
|---|---|---|---|---|---|
| 1 | Welcome | Line "Find out what helps you sleep — starting tonight." Illustration of the Tonight card. "Not a medical device. All numbers are estimates." | Get started | Nothing | Promise |
| 2 | Your frustration | "What bothers you most about your sleep?" Falling asleep / Waking at night / Not enough sleep / Waking up tired / Irregular schedule | Pick one (Skip visible) | 1 tap, skippable | — |
| 3 | Bring in your nights | Pre-prompt: "Tonight reads your sleep from Apple Health. It stays on this iPhone. Choose 'All Recorded Data' so we can find your usual pattern." Secondary: "I don't wear a watch" | Connect Apple Health | Health (sleep read only) | — |
| 4 | System Health sheet + history range | iOS sheets | Allow | Health | — |
| 5 | **FIRST WIN — Your nights** | "We found 186 nights." Avg recorded sleep, usual bedtime range, nights per source, one plain observation ("Your bedtime varied by more than an hour on 9 of the last 14 nights.") | See what to try | Nothing | Own data, real observation |
| 6 | Pick tonight's experiment | 2–3 suggested experiments ranked by frustration + data, each with one line on why; "See all 5" | Choose | 1 tap + target (e.g. cutoff time) | Personal suggestion |
| 7 | Your 7-night plan | Night dots, "One question each evening", "Result on <date>", baseline nights count | Start tonight | Nothing | Plan |
| 8 | Paywall (soft) | "Your first experiment is free." What Premium adds; plans; trial terms; reminder toggle on; X visible at once | Start free trial / X | Payment (optional) | — |
| 9 | Evening reminder pre-prompt | "One reminder at 8 PM for tonight's question. Nothing else." | Turn on | Notifications | — |
| 10 | Tonight (home) | Experiment night 1 card, tonight's action, morning check-in waiting | — | — | Running experiment |

- Taps to first win: 4 (Get started → Skip/answer → Connect → Allow). None of the eight captured apps showed a result built from the user's real sleep data before its first paywall; RISE's first personal number (sleep need) arrived around 34 screens in and came from self-reported times.
- No-Watch path: screen 3 "I don't wear a watch" → "When did you go to bed and wake up last night?" (two time pickers) → screen 5 becomes "Your first night" plus "We need 3 nights to build your baseline. Your experiment starts on <date>." → screens 6–10 as above. The paywall on this path states "Manual logging: no automatic sleep stages or awakenings."
- No account, no ATT prompt, no name, age, sex, height or weight in onboarding.

**Permissions**

| Permission | When | Pre-prompt | On deny / limited |
|---|---|---|---|
| Apple Health — read Sleep only | Screen 3 | "Reads your sleep from Apple Health. Stays on this iPhone." | Switch to manual path; Tonight shows "Connect Apple Health" card with Settings deep link; never blocks |
| Health history range | System sheet after read access | Pre-prompt recommends "All Recorded Data" | 30 days still works; baseline shows nights found |
| Notifications | Screen 9, after an experiment exists | "One reminder at 8 PM for tonight's question." | Question waits on home; morning card reminds once |
| ATT | Not in v1 first session | — | Decision with s4-analytics |
| Microphone, motion, location, contacts | Never in v1 | — | — |

**Core loop and repeat use**
- Morning (from Health sync or first open after wake): "Last night: 7h 18m recorded. How rested do you feel?" Tired / Okay / Rested — one tap, then the number and one observation.
- Evening: one notification with action buttons ("Caffeine after 2 PM today?" Yes / No) — answerable from the notification.
- Day 7–8: result screen, then "Keep it / Go back / Try another" (next experiment is the Premium moment for free users).
- Missed days are shown as gray dots, never as failure; experiment extends by the missed nights automatically.
- Pause mode: one switch pauses experiments, check-ins and reminders.
- No streaks, no mascots, no badges.

**Key screens and states**

*Tonight (home)*
```
Good morning.
Last night (Apple Watch)         7h 18m recorded
How rested do you feel?   [Tired] [Okay] [Rested]
----------------------------------------------
TONIGHT  Caffeine cutoff: 2 PM          Night 3 of 7
● ● ● ○ ○ ○ ○
----------------------------------------------
One observation: bedtime within 30 min of usual on 5 of 7 nights.
```
- Most important element: the rested check-in.
- States: no Health data yet ("Your watch hasn't sent last night yet" + Refresh + Add manually); night missing ("No night found. Add it?"); permission denied (connect card); first morning before any experiment; experiment complete (result card replaces progress); paused.

*Your nights (import / first win)*
- Most important: nights-found count with sources.
- States: importing (progress with real count, no fake percentages); 0 nights found ("No sleep in Apple Health yet — log tonight manually or wear your watch to bed"); fewer than 7 nights ("Enough to start; baseline will grow"); mixed sources listed per source.

*Experiment setup*
- Most important: the single target (time or yes/no rule).
- States: suggested list; full library; target picker; already running ("Finish or stop your current experiment first").

*Experiment in progress*
- Most important: night dots with today's question.
- States: on track; missed answer (gray dot, "Answer for yesterday?"); missing night data (night excluded, end date moves); stopped early (saved as "Stopped", no result).

*Result*
```
YOUR 7-NIGHT EXPERIMENT: Caffeine cutoff 2 PM
Baseline (21 nights)        6h 42m recorded
Experiment (7 nights)       7h 10m recorded
Felt rested                 2 of 7  →  5 of 7 mornings
Your recorded sleep was longer during this experiment.
Other changes could also explain the difference.
[Keep this habit]  [Go back]  [Try another]
```
- Most important: the two-row comparison with night counts.
- States: longer / shorter / about the same (within a fixed band) / "Not enough nights to tell" (fewer than 5 experiment nights); watch-vs-feeling disagreement shown as its own line ("Recorded sleep was similar, but you felt rested more often").

*Paywall*
- Most important: what the free user keeps, stated above the plans.
- States: first-time (onboarding); result-moment ("Start your next experiment"); trial active (shows end date); lapsed (history and past results stay visible).

**Paywall rules**
- Placement: soft paywall at onboarding screen 8 after the first win and experiment choice; second placement at "Try another" after the first result.
- Run a test from launch: A = onboarding soft paywall + result paywall vs B = result paywall only.
- X visible from the first frame on every paywall; no close delay; no downsell, spin, timer or "one-time offer" after close.
- Plans: annual (default highlighted) and monthly; lifetime as a later test. Price points are set by s5-monetization; starting points to test are the ones proposed in context §10. No weekly plan; never show a weekly or daily breakdown of an annual price.
- Trial: 7 days, reminder toggle on by default, reminder sent 2 days before charge; copy states "Free for 7 days, then <price>/year. Cancel any time in Settings."
- Free users keep: Health import, all nights and edits, morning check-in, trends, the first full experiment including its result, and all past results forever.
- Premium unlocks: every experiment after the first, full-history baselines, experiment log comparisons, and later features below.
- Price shown on the paywall must equal the price on Apple's sheet. Restore, Terms, Privacy and "Manage subscription" on every paywall and in Settings; meets App Review Guideline 3.1.2 disclosure.

**Visual language**
- Dark night interface stays (it's used at bedtime), but move off the category's neon blue/purple glow: midnight base, warm cream as the accent, sage for positive change, slate for neutral.
- Editorial serif for headlines, system sans for data; numbers in tabular figures.
- Real app UI and plain shapes only — no stock photos of tired people, no glowing brains, body scans, 3D avatars, laurels or mascots.
- Charts: dot strips and two-row comparisons; no gauges, no 0–100 dials.
- Motion: slow fades only; respects Reduce Motion.
- Final tokens belong to brand-designer.

**Voice and copy**
Tone: calm, plain, precise; a thoughtful friend with a notebook, not a coach or a doctor.

Lines we ship:
- "We found 186 nights in Apple Health."
- "How rested do you feel?"
- "Your recorded sleep was longer during this experiment. Other changes could also explain the difference."
- "Not enough nights to tell yet. We'll add the missed nights to the end."
- "Your first experiment is free."

Lines we never ship (seen in captures):
- "Diagnosis: High-risk sleep problems" — Sleep Monitor, p11 (generated from quiz answers)
- "Oops — Payment Issue … Your Free Trial may disappear soon — try again to keep it!" — ShutEye, p28 (shown after the user cancelled Apple's sheet)
- "Advance warning about 100 diseases!" — Leap Sleep Tracker, p13
- "Microphone permission is indispensable to track and analyze your sleep quality." — Leap Sleep Tracker, p24
- "Super Prize! Congrats! You are so lucky" — Sleep Monitor, p28

**Accessibility**
- Dynamic Type to the largest accessibility sizes on all screens; night dots get text equivalents ("Night 3 of 7, answered").
- VoiceOver labels on every chart row, dot and check-in button; results read as sentences.
- Contrast ≥ 4.5:1 for text on the midnight background; never colour-only meaning (sage vs slate also labelled).
- Reduce Motion removes all transitions beyond crossfade.
- Notification actions usable without opening the app.

**Refuse list (seen in captures)**

| Pattern | Where seen |
|---|---|
| Fake error after cancelling purchase ("Payment Issue", "99.9% complete") | ShutEye p28 |
| Quiz-generated diagnosis / health-risk score before any data | Sleep Monitor p11, p17; ShutEye p19 |
| Disease / apnea / choking-risk claims | Leap p13, p29; Sleep Monitor p10, p33, p38; ShutEye p38 |
| Fake "Creating your report… %" loaders | ShutEye p20; Sleep Monitor p16; Leap p26 |
| Countdown timers, slot machine, "Super Prize", one-time offer chains | Sleep Monitor p23–p28 |
| Paywall price different from Apple sheet price | Leap p30 (₹2,499/yr) vs p33 (₹3,999/yr) |
| Close button appearing late on paywall | Leap p30 → p31 |
| No visible close on onboarding paywall | Pillow p15–p16; Sleep Cycle p10; Sleep Monitor p23 |
| Required-sounding permission screens with no skip | Leap p24; Pillow p7; RISE p23 |
| Notification permission as the very first screen | ShutEye p1 |
| ATT prompt as the first screen | Remly p1 |
| Pre-checked consent boxes | Sleep Cycle p3 |
| Third-party ads in a paid sleep app | Leap p35–p48 |
| Demo/sample reports dressed as the user's own | ShutEye p44–p45; Sleep Monitor p34–p39; Leap p44 |
| Unverifiable mass-user and percentage claims | ShutEye p4, p12; Sleep Monitor p7; Leap p18 |
| Sad mascot when a session is too short | Leap p54 |
| Account wall before value | Sleep Cycle p6 |

## v1 product features

| # | Feature | What it does | Free / Paid |
|---|---|---|---|
| 1 | Apple Health sleep import | Reads Sleep Analysis (all history the user grants); labels each night by source; background refresh each morning | Free |
| 2 | Manual nights | Add or edit bedtime/wake time; edited nights marked "Edited"; full no-Watch path | Free |
| 3 | Your nights (first win) | Nights found, average recorded sleep, bedtime range, one plain observation | Free |
| 4 | Morning check-in | Tired / Okay / Rested before any number; stored per night | Free |
| 5 | Tonight home | Last night summary, tonight's one action, experiment progress | Free |
| 6 | Night detail & 30-night trend | Duration, in-bed window, awakenings/stages only when the source provides them; dot-strip trend | Free |
| 7 | Experiment engine | Baseline from past nights, 7-night plan, one daily yes/no question, auto-extends for missed nights | Free (first experiment) / Paid after |
| 8 | Five experiments | Bedtime consistency, caffeine cutoff, evening screens off, bedroom (dark/cool/quiet checklist), wind-down routine — each with a one-paragraph explanation and its limits | First free / rest Paid |
| 9 | Result screen | Baseline vs experiment, night counts, rested mornings, caveat, "Not enough nights" state, Keep / Go back / Try another | Free (first) / Paid after |
| 10 | Experiment log | All past experiments and results, kept forever | Free to view |
| 11 | Evening reminder | One local notification with Yes/No actions for the day's question | Free |
| 12 | Pause mode | Pauses experiments, check-ins, reminders | Free |
| 13 | Subscription | StoreKit 2 annual + monthly, 7-day trial, reminder, restore, manage link, 3-step cancel guidance | — |
| 14 | Privacy & safety | On-device storage, delete all data, "Not a medical device" note, "talk to a doctor if…" page | Free |

**Paid unlocks:** every experiment after the first; baselines using full history instead of the last 30 nights; side-by-side comparison of past experiments; Premium items added later (below).

**Later (v1.1 / v2) — with the trigger that brings each in**

| Feature | Bring in when |
|---|---|
| Home/lock-screen widget with check-in | D7 retention known and morning check-in rate below the evening answer rate |
| Custom experiment ("test your own change") | ≥ 30% of completers start a second experiment |
| More experiments (alcohol timing, exercise timing, nap cutoff, light in the morning) | Users exhaust the five; requests in feedback |
| Apple Watch app (answer question on wrist) | Evening answer rate is the main drop-off |
| PDF/summary export to share with a doctor | Repeated support requests |
| Lifetime purchase | Paywall test shows annual resistance in review mining |
| Write manual nights to Apple Health | Manual-path users ≥ 20% of active users |
| Sleep sounds | Never as core; only if wind-down experiment users ask for it |

**Not building**

| Competitor feature | Why not |
|---|---|
| Proprietary sleep score | Apple already provides one; score anxiety is the problem we position against |
| Microphone snore/sleep-talk recording | Battery, privacy and accuracy cost; SnoreLab/ShutEye own it; not our job |
| Sleep apnea / breathing / disease risk | Medical claim risk; we can't support it |
| Smart alarm | Reliability is a trust killer; iOS alarm stays the alarm |
| Sound/music/story library | Content cost; different job (help me fall asleep) |
| AI dream analysis | Distraction, no evidence value |
| Phone-on-mattress motion tracking | Accuracy and battery; Health-first instead |
| Accounts, family plans, social | No need for v1; data stays on device |
| Ads | Paid sleep app; trust |
| CBT-I "programme" | Treatment claim; refer out instead |

**Free vs paid line**
A free user can connect Apple Health (or log manually), see every night they have, check in each morning, and run one complete experiment through to its result — they finish knowing whether one change seemed to help. Payment unlocks the ongoing part: every experiment after the first, comparisons across experiments, and full-history baselines. Nothing a free user has recorded or learned is ever locked, so the paywall sells "keep finding out what helps" rather than ransoming their own data.

**Success metrics for v1**

| Metric | Target |
|---|---|
| Install → Health authorized (Watch path) or first manual night | UNKNOWN — set after first cohort |
| Install → first experiment started | UNKNOWN — set after first cohort |
| Experiment completion (≥ 5 of 7 nights answered) | UNKNOWN — set after first cohort |
| Second-experiment adoption among completers (North Star) | UNKNOWN — set after first cohort |
| Trial → paid | Third-party Health & Fitness benchmark 35.0% (estimate, not a target until our cohort exists) |

## New recommendations

1. Sharpen the differentiator against SleepWatch, not just RISE: SleepWatch's premium already sells "Discover Which Actions May Help You Sleep Better" habit tagging; our claim must be "one planned change, tested against your own baseline", never "find what affects your sleep".
2. Make "Not enough nights to tell" and "Watch and how you felt disagree" first-class result states, designed and copy-tested before launch.
3. Guide the iOS history-range sheet with a pre-prompt recommending "All Recorded Data", and track which option users pick; it decides whether the first-win screen works.
4. Ship a no-Watch path with a 3-night manual baseline from day one, and measure the Watch/no-Watch split in the first cohort; if most installs have under 7 nights in Health, re-cut the ad audience to Watch owners only.
5. Run the paywall-placement test (onboarding soft paywall + result paywall vs result paywall only) from the first cohort.
6. Test an "honest app" creative ("Most sleep apps start with a quiz. We start with your real nights.") once the lead angles have baseline data.
7. Retire the "can we read enough history?" risk in week 1 of build: a HealthKit spike on 5 team/friend devices reading full sleep history and per-source labels.

## Before build

**Missing captures / checks**
- No captured app showed a real morning report from an actual night; capture one completed night in Sleep Cycle, ShutEye and SleepWatch.
- No app showed imported Apple Health history in the captured flow; capture AutoSleep, Sleep++, Bevel and Athlytic (the Health-first competitors closest to us — none captured).
- Apple's own Sleep Score screen in the Health app on a Watch-wearing device.
- Free/limited version after closing the paywall in Pillow and Sleep Cycle (not reached in captures).
- Whether Pillow, Sleep Cycle and Sleep Monitor onboarding paywalls have a close control outside the captured frames.
- US storefront prices and paywalls for all eight apps (all captures are ₹).
- Cancellation flows and trial reminders actually delivered on day 5.
- RISE, SleepWatch and Pillow 1–2★ US reviews on experiment/insight accuracy.

**Next agents**
- brand-designer: midnight/cream/sage direction, name territory.
- ux-designer: screens above, all states, Mobbin references for editorial dark UI.
- s1-spec: experiment engine rules (baseline window, minimum nights, comparison band), free/paid gating.
- s5-monetization: price points and paywall test design.
- s6-legal: health-claim review of every copy line and store screenshot; privacy labels for HealthKit.
