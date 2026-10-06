---
type: category-product-strategy
category: calorie-counter
member: harshil
updated: 2026-10-06
status: draft
sources: [context.md, screenshots:253 across 9 apps, knowledge:us_ios_app_factory_knowledge_base_2026-10-04.md + sanibha-app-factory-knowledge-base.md, web:0]
---

# Calorie Counter — final recommendations (v1)

Context: [[research/categories/calorie-counter/context]]

## Positioning

**Statement.** For US adults who want to eat well without logging being a chore, NextPlate (working name) is the calorie app that tells you what fits your day before you eat, and logs the meal in one tap or one photo. It shows an honest range, not fake exactness.

**Promise order.**
1. Know what fits today: remaining calories and protein, with a few meals that fit.
2. Snap a meal and get an editable estimate shown as a range, labelled "photo estimate" or "label-checked".
3. Log your usual meals in one tap.
4. See progress without guilt: no streak shaming.

**Proof points we can show.** The first scan happens before any quiz. One price, shown in the same unit for annual and monthly. A close button on the paywall from the first second. Every number in the plan matches every other screen.

**Never claim.** Any accuracy percentage; user counts or star ratings we cannot source; "free" when a card is needed; a weight-by-date promise; medical or clinical wording; "guaranteed" anything; before/after body imagery.

**Name and storefront.** Keep NextPlate for now; confirm the name is clear before brand work. Storefront order: (1) "Know what fits your day", (2) "Snap it. See the range. Log it.", (3) "Your usual meals, one tap away", (4) "Plan dinner in seconds", (5) "Progress without the pressure". Palette: warm cream, dark olive, tomato, sage; real food photography; no mascot.

## UI/UX

**Principles.** Value before questions. Four inputs only. Show ranges, not false precision. One screen, one job. Honest money screens. Nothing that makes the user feel guilty.

**Information architecture.** Four tabs: Today, Scan, Meals (repeat and saved), Progress. Settings sit under Progress.

**First five minutes.**
1. Open on the camera, with a "skip, set up first" option.
2. First photo gives a result with a calorie range and editable portions.
3. Ask only goal, height, weight and age, with units set from the phone's region. Nothing is pre-filled silently.
4. Show the user's own daily target and "what's left" on one screen.
5. Log the meal, then show Today.
Design target (not measured): first logged meal within 10 taps of launch.

**Permissions.** Camera: asked at the first scan with a one-line reason. Notifications: asked once, after the first logged meal, using only the real iOS dialog. Apple Health: optional, in Progress, one ask, weight only in v1. No tracking prompt in onboarding. No fake system dialogs and no pointing hands.

**Core loop.** Open Today, see what's left, pick a suggested or saved meal or snap a new one, log, see what's left update.

**Key screens and states.**
- Today: remaining calories and protein, three "fits now" meals; states: empty, over budget (neutral wording, no red), offline.
- Scan result: photo, item list, range, edit portion; states: low confidence ("not sure, tap to fix"), nothing detected, no network.
- Meals: usual meals, one tap to log; empty until the first log.
- Progress: weekly average and weight trend; no streak counter.
- Paywall: see below.

**Paywall.** One screen, shown after the first logged meal, with an X visible immediately. Annual and monthly in the same unit; show the full price, renewal date and a reminder promise next to the trial. No downsell chain, no spin wheel, no countdown, no "to continue" wording.

**Visual language.** Cream background, olive text, tomato for one accent, sage for success. Large type; few numbers per screen.

**Voice.** Plain, kind, specific. "Dinner fits." Never "you failed" or "cheat".

**Accessibility.** Dynamic Type, VoiceOver labels on the camera and the range, no colour-only meaning.

**Refuse list.** Quiz over 5 screens; fake loaders; fake system alerts; invented social proof; pre-ticked consents; multiple prices for the same plan; body-shaming imagery; streak guilt; a tracking prompt before value.

## v1 product features

| # | Feature | Free / paid |
|---|---|---|
| 1 | Camera-first onboarding with 4 inputs and a personal daily target | Free |
| 2 | Photo scan with editable portions and a range; label-checked vs photo-estimate marker | Free first scans; paid beyond a daily limit set by test |
| 3 | Barcode scan | Free |
| 4 | Today screen: remaining calories and protein | Free |
| 5 | "What fits now": 3 meals from the user's own saved and frequent foods that fit what's left | Paid |
| 6 | One-tap repeat meals | Free |
| 7 | Manual search and quick add | Free |
| 8 | Weekly progress and weight trend, no streaks | Free |
| 9 | Optional Apple Health weight read | Free |
| 10 | One paywall with restore and plain cancel instructions | n/a |

**6-week cap.** Features 1–4, 6–8 and 10 ship in six weeks; feature 5 ships only in its simplest form (saved meals that fit the remaining budget, no generated recipes).

**Cut list.** Exercise burn-back, rollover calories, health score, fasting, community, referral, recipe import, AI persona or pet, meal planner, GLP-1 mode, regional-language pack, widgets (after v1).

**Free/paid line.** Basic logging stays free (manual, barcode, repeat). Paid unlocks unlimited photo scans and "what fits now". The daily free scan limit is set in the first experiment.

**Success metrics (no targets yet).**
1. Install → first logged meal.
2. Time to first logged meal.
3. Share of users logging on 3+ days in week 1.
4. Share of photo estimates the user edits.
5. Install → trial → paid, and net proceeds per install at day 30.

## New recommendations

1. **First scan before the quiz.** None of the nine apps lets the user try the core job before the questions.
2. **Plan-consistency check.** Build an automated check that every number (target, weight, goal) matches on every screen.
3. **Locale-aware defaults.** Units and currency come from the phone's region; never preset the wrong unit.
4. **Range plus source label.** Show every estimate as a range and mark it "photo estimate" or "label-checked".
5. **Weekend and dinner-out budget.** A one-tap "eating out tonight" that reserves part of the day's budget (the idea behind Yazio's weekend flex).
6. **Truthful comparison creative.** Test an ad that counts the screens before a competitor lets you log, after legal review.
7. **Free barcode scan as a trust signal.** The knowledge base notes MyFitnessPal's move of barcode scanning to paid upset users.

## Before build

1. Capture the missing screens (home, a scan result, correction, log, settings) from at least MyFitnessPal, Cal AI and one more, in the US storefront; none were captured, so taps-to-log and day-2 behaviour are unknown.
2. Confirm US prices of the competitors in the US App Store; the screens are India (₹).
3. Decide the free-scan limit and test it.
4. Legal review of the comparison creative and of all trial wording.
5. Confirm the name NextPlate is clear.
6. Test whether "what fits now" changes behaviour; no screenshot shows any competitor doing it.
