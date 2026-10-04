---
type: reference
updated: 2026-10-04
---

# App shortlist for screenshot analysis

Input: `ganesh_screenshots/`, with 38 apps across 4 categories (660 screenshots, India storefront) plus `app_benchmark_report.xlsx`. We analyse only the category winner plus the best 4 apps per category, using the lens in `skills/app-researcher/prompts/a5-screens-lens.md`.

Screen analysis uses **only our own screenshots** (team-captured), never App Store listing images or web walkthroughs.

## Weights

US App Store data comes from the iTunes Search API, pulled 2026-10-04 `[DATA:itunes-search]`. We don't have revenue data yet, so ratings are the demand proxy.

| Factor | Weight | Measure |
|---|---|---|
| Demand | 35% | log(US rating count), relative to the category max |
| Momentum | 25% | log(US ratings per year since launch), relative to the category max; favours breakouts |
| Quality | 15% | US average rating; 4.0 scores 0, 5.0 scores 1 |
| Coverage | 25% | screenshots available (12 or more = full); nothing to analyse means no value here |

**Forced in:** the xlsx category winners. **Excluded:** US rating below 4.45, fewer than 6 screenshots, or a different job than the category.

## Shortlist (20 apps, about 345 screenshots)

| Category | App | Score | US rating | US ratings | Screens | Note |
|---|---|---|---|---|---|---|
| Calorie | Healthify | 67 | 4.57 | 5,977 | 16 | xlsx winner, but a **weak US presence** (India-first); kept as a winner, not as a US benchmark |
| Calorie | Cal AI | 93 | 4.80 | 368,234 | 27 | US breakout (launched 2024); the real US benchmark |
| Calorie | MyFitnessPal | 96 | 4.71 | 2,370,943 | 18 | incumbent |
| Calorie | Appediet | 83 | 4.78 | 47,333 | 23 | AI challenger |
| Calorie | BitePal | 82 | 4.66 | 55,700 | 48 | AI challenger, fast growth |
| Habit | Finch | 99 | 4.95 | 759,175 | 35 | winner |
| Habit | Habit Tracker (Davetech) | 88 | 4.79 | 147,561 | 20 | |
| Habit | Productive | 82 | 4.60 | 91,069 | 17 | |
| Habit | Grit | 80 | 4.78 | 15,958 | 40 | |
| Habit | Streaks | 80 | 4.81 | 27,347 | 12 | design-led, paid upfront |
| Plant | PictureThis | 72 | 4.80 | 1,117,651 | **0** | winner; **no team screenshots, so no screen analysis** until Ganesh captures the flow (onboarding → first ID → paywall → care) |
| Plant | PlantIn | 87 | 4.56 | 229,609 | 12 | |
| Plant | Plantum | 84 | 4.59 | 119,334 | 15 | |
| Plant | Plant App | 83 | 4.70 | 55,488 | 13 | |
| Plant | Plantiary | 79 | 4.66 | 28,301 | 13 | |
| Storage | Cleanup | 91 | 4.65 | 728,978 | 10 | winner |
| Storage | Phone Storage Cleaner | 83 | 4.52 | 73,211 | 12 | |
| Storage | Clever Cleaner | 79 | 4.78 | 83,019 | 7 | fastest challenger (launched 2025) |
| Storage | Cleaner Kit | 77 | 4.44 | 351,373 | 7 | 0.01 under the rating cut; kept as the large incumbent bundle, so treat it as a failure-mining source |

## Excluded

| App | Reason |
|---|---|
| Yazio (58 screens), FoodPilot, WiseMeal, NubCal | lower demand and momentum; NubCal has 105 US ratings |
| Fabulous | US rating 4.43 |
| TickTick | to-do app, not a habit tracker |
| Days Since | quit counter, a different job; 6 screenshots |
| Atoms, Routine Planner, (Not Boring) Habits, Everyday, Tangerine, Habitify, HabitKit | below the top 4; HabitKit has 4 screenshots and Habitify 6. Atoms and (Not Boring) are worth one look later as design references |
| Plantaria, PlantNet, Botan, LeafSnap | lower score; Botan rated 4.37; LeafSnap has 2 screenshots |
| Darksy, Clean Manager | US ratings 4.39 and 4.24 |

Note: the "Plant App" folder is Plant App by ScaleUp (id 1595795215), and "Tangerine" is Tangerine: Self-care & Goals (id 1468882685), not the bank app the name search returns first.
