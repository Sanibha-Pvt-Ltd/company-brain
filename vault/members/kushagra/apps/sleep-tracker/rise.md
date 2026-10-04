---
type: app
category: sleep-tracker
app: RISE
app_store_id: unknown
member: kushagra
updated: 2026-10-04
status: draft
sources: [screens:53]
---

# RISE — screenshot teardown

**Scope.** Screens-only review of team capture `Rise_sleeptracker.pdf` (PDF created 2026-10-03; 53 pages). Each page is covered by a screen-span row below; adjacent pages are grouped only when they belong to the same visible flow. Companion analysis PDF is secondary and was not used as evidence. Listing, reviews and App Store ID are unavailable. [UNKNOWN]

## Per-screen table

| Screen(s) | What user sees | Visible ask | What it gives | Verbatim copy (representative) | Lever | Friction / dark pattern | Source |
|---:|---|---|---|---|---|---|---|
| 1–6 | Opening benefit story and claim about sleep; introduction to profile setup. | Continue/Next; the pages do not show a sleep result. | [OBSERVED] Opening benefit story and claim about sleep; introduction to profile setup. | `“That drug is Sleep.”` (representative copy visible in this span) | profile/question burden | [INFERRED] Asks user to continue/Next; the pages do not show a sleep result. Still images cannot establish timing, hard gating or action success. | `Rise_sleeptracker.pdf`, pp. 1–6 |
| 7–21 | Profile quiz: name, discovery source, gender/age/student status, goals, challenges, tracking, sleep practices, and energy habits. | Name entry and repeated selections; Skip appears on several profile pages. | [OBSERVED] Profile quiz: name, discovery source, gender/age/student status, goals, challenges, tracking, sleep practices, and energy habits. | `“Let’s get to know each other better.”` (representative copy visible in this span) | profile/question burden | [INFERRED] Asks user to name entry and repeated selections; Skip appears on several profile pages. Still images cannot establish timing, hard gating or action success. | `Rise_sleeptracker.pdf`, pp. 7–21 |
| 22 | Preview of a sleep-pattern/energy result and request to discover patterns. | Continue into onboarding. | [OBSERVED] Preview of a sleep-pattern/energy result and request to discover patterns. | `“Now, let’s discover your sleep and energy patterns.”` (representative copy visible in this span) | feature discovery | [INFERRED] Asks user to continue into onboarding. Still images cannot establish timing, hard gating or action success. | `Rise_sleeptracker.pdf`, pp. 22 |
| 23–28 | Phone Motion and Apple Health explanations, Health data selection, and iOS permission prompts. | Motion/Health permissions; choices include allowing or declining. | [OBSERVED] Phone Motion and Apple Health explanations, Health data selection, and iOS permission prompts. | `“First, let’s enable Phone Motion Data.”` (representative copy visible in this span) | permission cost | [INFERRED] Asks user to motion/Health permissions; choices include allowing or declining. Still images cannot establish timing, hard gating or action success. | `Rise_sleeptracker.pdf`, pp. 23–28 |
| 29–30 | Building profile/data insights; sleep-need claims and a continue action. | Wait/continue; inputs include phone motion and Apple Health. | [OBSERVED] Building profile/data insights; sleep-need claims and a continue action. | `“Building K’s Profile.”` (representative copy visible in this span) | profile/question burden | [INFERRED] Asks user to wait/continue; inputs include phone motion and Apple Health. Still images cannot establish timing, hard gating or action success. | `Rise_sleeptracker.pdf`, pp. 29–30 |
| 31–34 | Sleep pattern questionnaire for weekday/weekend bed and wake times. | Choose or adjust bed and wake times. | [OBSERVED] Sleep pattern questionnaire for weekday/weekend bed and wake times. | `“On a normal weekday, what is your approximate sleep schedule?”` (representative copy visible in this span) | profile/question burden | [INFERRED] Asks user to choose or adjust bed and wake times. Still images cannot establish timing, hard gating or action success. | `Rise_sleeptracker.pdf`, pp. 31–34 |
| 35–40 | Sleep-need and sleep-debt explanation followed by energy result screens. | Continue, adjust sleep need, view sleep debt/energy. | [OBSERVED] Sleep-need and sleep-debt explanation followed by energy result screens. | `“When you sleep less than your sleep need, you build up sleep debt.”` (representative copy visible in this span) | feature discovery | [INFERRED] Asks user to continue, adjust sleep need, view sleep debt/energy. Still images cannot establish timing, hard gating or action success. | `Rise_sleeptracker.pdf`, pp. 35–40 |
| 41–46 | Energy schedule graph and recommendations for planning bedtime and daytime activity. | Continue, optimize day, sleep easier, start today. | [OBSERVED] Energy schedule graph and recommendations for planning bedtime and daytime activity. | `“This is your Energy Schedule today.”` (representative copy visible in this span) | feature discovery | [INFERRED] Asks user to continue, optimize day, sleep easier, start today. Still images cannot establish timing, hard gating or action success. | `Rise_sleeptracker.pdf`, pp. 41–46 |
| 47–49 | Feature/benefit cards about changing biology, optimizing the day, and discovering a better you. | Continue through the feature carousel. | [OBSERVED] Feature/benefit cards about changing biology, optimizing the day, and discovering a better you. | `“Discover a better you.”` (representative copy visible in this span) | feature discovery | [INFERRED] Asks user to continue through the feature carousel. Still images cannot establish timing, hard gating or action success. | `Rise_sleeptracker.pdf`, pp. 47–49 |
| 50–53 | Premium/trial offer, Apple purchase confirmation, and satisfaction guarantee overlay. | Select plan/start trial; Apple side-button confirmation; an overlay offers a “NO READY TO TRY” exit. | [OBSERVED] Premium/trial offer, Apple purchase confirmation, and satisfaction guarantee overlay. | `“Try RISE.”` (representative copy visible in this span) | trial conversion | [INFERRED] Asks user to select plan/start trial; Apple side-button confirmation; an overlay offers a “NO READY TO TRY” exit. Still images cannot establish timing, hard gating or action success. | `Rise_sleeptracker.pdf`, pp. 50–53 |

## Eight screen lenses

1. **First win.** A tailored sleep/energy profile first appears on p. 29, before the paywall at p. 50, but no completed sleep night is shown. [OBSERVED] First verified sleep benefit and taps to it: [UNKNOWN].
2. **Ask ledger.** Observed in PDF order: name p. 7; discovery source p. 9; gender p. 11; age p. 12; student status p. 13; goal p. 14; challenges p. 16; sleep tracking p. 17; sleep practices p. 19; energy strategies p. 20; phone motion and Health access p. 23–28; sleep schedule p. 32–34. This is page order, not a proven tap path.
3. **Abstractions.** “Sleep need,” “sleep debt,” and “Energy Schedule” dominate p. 35–46. [OBSERVED] [INFERRED] A plain sleep-hours result could precede these derived ideas.
4. **Feel-good moments.** Profile completion and explanatory energy-curve screens (p. 29–46) make the result feel personalized. [OBSERVED] Whether the output reflects a real night is [UNKNOWN].
5. **Feel-bad moments.** On p. 2 the benefit list includes “Reduced anxiety and depression”; this is health-claim framing before setup. [OBSERVED] The capture cannot show coercion or delayed exits.
6. **Paywall.** Offer p. 50: 7 days free then ₹6,900/year (also says ₹575/month); monthly option ₹99.00. [OBSERVED] India storefront; source PDF metadata creation date 2026-10-03; screenshot capture date unknown. Apple sheet p. 52; no visible close control on p. 50, but hardness/exit delay is [UNKNOWN].
7. **Repeat cost.** No repeat-session path or real nightly report. [UNKNOWN] P. 22–49 describe schedule, energy and features; exact repeat action count is not shown.
8. **Feature map.** [INFERRED] Table stakes: personalized bedtime guidance tied to measured sleep. Differentiator: energy schedule (p. 41–46). Bloat risk: extensive demographics, goals and strategy categories before any recorded sleep.

## Keep / Kill / Different

- **Keep.** [INFERRED] Keep the tangible weekday/weekend schedule and Energy Schedule walkthrough (pp. 31–46), while labeling predictions.
- **Kill.** Remove the pre-recording demographics/challenge cascade and the anxiety/depression benefit claim (pp. 2, 7–21) from the critical path. [INFERRED]
- **Different.** Let the user set bedtime, record a night, then show measured sleep duration before optional Health access and a trial. [INFERRED]

## Open questions and verification

- [UNKNOWN] Exact launch-to-benefit taps/time, whether PDF pages form one continuous path, soft versus hard gating, close delays, trial defaults in action, checkout and successful result.
- [UNKNOWN] Repeat-session taps, retention, notification behavior, US storefront prices, listing/review evidence and App Store ID.
- **Checked:** all 53 pages of `Rise_sleeptracker.pdf` were visually inspected from rendered contact sheets. High-resolution offer pages were separately checked when cited above. Every numeric offer reported in this note is tied to an individual screenshot page and the India storefront shown in the capture; prices are not US estimates.
