---
type: category-product-strategy
category: habit-tracker
member: harshil
updated: 2026-10-06
status: draft
sources: [context.md, screenshots:269 across 15 apps, knowledge:us_ios_app_factory_knowledge_base_2026-10-04.md + organic-growth-knowledge-base.md + sanibha-app-factory-knowledge-base.md, web:0]
---

# Habit Tracker — final recommendations (v1)

Context: [[research/categories/habit-tracker/context]]

## Positioning

**Statement.** For people who have started and quit habit trackers before, Again is the habit tracker that helps you start again. When you miss days, it offers a smaller version of the habit to do today instead of showing a broken streak.

**Promise order.**
1. Missed a few days? Your history stays, and there is a smaller way back in.
2. Every habit has a normal size and a small "backup" size. Either one counts as done.
3. Check in with one tap.
4. A weekly view that shows which days work for you, once there is enough data to say so.

**Proof points we can show.** Check-in before any paywall. A history that shows gaps and returns, with nothing erased. A paywall that states the renewal date and promises a reminder before the trial ends.

**Never claim.** "Science shows" or "research proves" without a named source; user counts or ratings we cannot source; "no failure" or "you can't fail"; any mental-health, mindfulness or medical benefit; any date by which a habit will "stick"; "free" if a card is needed.

**Naming and storefront.** Working name Again; confirm clearance before brand work. Screenshot order: (1) "Missed a few days? Your progress isn't gone.", (2) "Get back on track in two minutes.", (3) "Learn what helps you stay consistent.", (4) "Track progress without starting over.", (5) "Make your goals fit real life.", (6) "Check in with one tap." Also run one conventional first screen as the control. Palette: warm cream, forest, terracotta, charcoal. No mascot, no pet, no game.

## UI/UX

**Principles.** Check in before any question. Never reset or hide history. One action per screen. Plain, calm words after a miss. No guilt copy, no countdown timers, no fake urgency.

**Information architecture.** Three tabs: Today, History, Settings. The comeback card lives on Today.

**First five minutes.**
1. Open and pick one habit from templates or type your own.
2. Choose the normal size, then choose a backup size.
3. Choose days: set days, or a number of times per week.
4. Choose a reminder time.
5. Land on Today and check in once.
Design target (not measured): first check-in within 8 taps of launch. No quiz, no account, no sample-data screens.

**Permissions.** Notifications are asked once, right after the first check-in, using only the real iOS dialog and a one-line reason. Apple Health is not asked in v1. No tracking prompt.

**Core loop.** Open Today, check in (normal or backup), see this week's count. After 3 missed scheduled days, the Today screen swaps to the comeback card.

**Key screens and states.**
- Today, state 1, on track: "3 of 4 this week", with one more to go.
- Today, state 2, missed days: "It's been 5 days." Button: "Try the small version today." Link: "Change my goal."
- Today, state 3, restarted: "You're back. Your earlier progress still counts."
- Check-in sheet: normal size, backup size, "skip today" (visible, never hidden); states: done, backup done, skipped.
- Reason question (after repeated misses, one tap, five answers): ran out of time, forgot, was exhausted, schedule changed, goal too big. Always skippable.
- History: all days, with gaps and returns shown honestly; no streak counter as the hero.
- Paywall: shown after the first check-in; see below.

**Paywall.** One screen, X visible immediately. Show price per year and per month in the same unit, the renewal date, and a promised reminder before the trial ends. A lifetime option sits beside the annual plan. No countdown timer, no "you lose this offer if you exit" line, no weekly plan, no repeated downsell.

**Visual language.** Cream background, charcoal text, forest for done, terracotta for the comeback card. Calm motion only.

**Voice.** Plain and kind. "Life happened. Start small today." Never "you failed" or "you broke your streak".

**Accessibility.** Dynamic Type, VoiceOver labels on check-in and the week count, no colour-only states.

**Refuse list.** Quiz screens before first check-in; sample data presented as the user's own; "reset the counter" copy that guilts; fake system dialogs; unsourced research claims; discount wheels and countdown timers; a paywall before the first check-in.

## v1 product features

| # | Feature | Free / paid |
|---|---|---|
| 1 | Five-step onboarding ending in a first check-in | Free |
| 2 | Habit with a normal size and a backup size; either counts as done | Free |
| 3 | Flexible schedule: set days, or X times per week, plus skip day | Free |
| 4 | One-tap check-in | Free |
| 5 | Today screen with three states (on track, missed days, restarted) | Free |
| 6 | Comeback card after 3 missed scheduled days: offers the small version | Free |
| 7 | One-tap reason question and a suggested change (smaller goal or different day) | Paid |
| 8 | History view showing gaps and returns | Free |
| 9 | Weekly pattern view: best and hardest days, only when there is enough data | Paid |
| 10 | One reminder per habit at a user-set time, with at most one comeback nudge per run of misses | Free |
| 11 | Paywall with annual, monthly and lifetime | n/a |

**6-week cap.** All 11 fit in six weeks if features 7 and 9 ship in their simplest form: fixed rules and fixed wording, no generated text.

**Cut list.** Calendar-grid home screen, pets or game, RPG, social or buddy features, coach chat or AI chat, automatic Apple Health check-ins, Apple Watch, quit-habit counters, home-screen widgets, templates library beyond ten, journaling and mood, weekly plan, community.

**Free/paid line.** Free: up to 3 habits, backup size, flexible schedules, the comeback card and history. Paid: unlimited habits, reason-based suggestions, weekly pattern view. The free habit count is set by the first experiment.

**Success metrics (no targets yet).**
1. Habit recovery rate: of users who miss 3 or more scheduled opportunities, the share who resume within 7 days (operating definition from context.md, not an industry benchmark).
2. Install to first check-in, and time to first check-in.
3. Share of comeback cards acted on.
4. D7 and D30 active retention.
5. Trial to paid, and net proceeds per install at day 30.

## New recommendations

1. **Check-in before any paywall.** In the screenshots, no app shows a completed check-in before its paywall; ours comes after the first check-in.
2. **Honest trial timeline.** State the renewal date and promise a day-5 reminder (Routine Planner and Days Since show this); drop countdowns and "you lose this offer" lines.
3. **Test lifetime as a first-class plan.** Seven of the fifteen paywalls show a lifetime option.
4. **Backup size as the core mechanic.** Make the small version count as done in history, so the user is never "at zero".
5. **Quit-habit type with a non-destructive reset (v1.1).** Five of the fifteen apps offer a quit or limit habit; slips are the same comeback moment, and an existing app guilts here ("You don't want to reset that counter, do you?").
6. **Short onboarding as a visible edge.** Fabulous, Finch and Grit need 34 to 36 screens before first value; ours takes five.
7. **Source or drop every claim.** Grit shows an unsourced "Research shows..." line; we will not copy that.

## Before build

1. Capture the missing screens by hand on at least five competitors (Streaks in-app, (Not Boring) Habits, Finch, Habitify, Everyday): create a habit, skip several days, return. No set shows what happens after a miss.
2. Capture US-storefront prices; the screens are India (₹) and cannot be converted.
3. Prototype the comeback card and test it with people who have quit a tracker before.
4. Decide the free habit count and test it.
5. Confirm the name Again is clear.
6. Re-test whether first-time users understand the "start again" storefront against "Build better habits".
