---
type: app
category: sleep-tracker
app: ShutEye
app_store_id: unknown
member: kushagra
updated: 2026-10-04
status: draft
sources: [screens:49]
---

# ShutEye — screenshot teardown

**Scope.** Screens-only review of team capture `shuteye_sleeptracker.pdf` (PDF created 2026-10-03; 49 pages). Each page is covered by a screen-span row below; adjacent pages are grouped only when they belong to the same visible flow. Companion analysis PDF is secondary and was not used as evidence. Listing, reviews and App Store ID are unavailable. [UNKNOWN]

## Per-screen table

| Screen(s) | What user sees | Visible ask | What it gives | Verbatim copy (representative) | Lever | Friction / dark pattern | Source |
|---:|---|---|---|---|---|---|---|
| 1–4 | Notification prompt, welcome, social-proof claims and “upgrade” framing. | System notification permission appears first. | No tracked-night outcome can be concluded from stills. | `“It’s time to upgrade your sleep!”` (representative copy visible in this span) | onboarding / report / offer | Taps, delay, hard gating and outcome remain unverified from stills. | `shuteye_sleeptracker.pdf`, pp. 1–4 |
| 5–11 | Sleep duration, satisfaction, sleep latency, snoring/breathing, wake-up and morning-fatigue quiz. | Repeated single-choice answers. | No tracked-night outcome can be concluded from stills. | `“How much sleep do you usually get at night?”` (representative copy visible in this span) | onboarding / report / offer | Taps, delay, hard gating and outcome remain unverified from stills. | `shuteye_sleeptracker.pdf`, pp. 5–11 |
| 12–19 | Sleep quiz continues: claimed improvement, sleep position, habits, life impact, diagnoses, and health-risk framing. | More health and habit answers. | No tracked-night outcome can be concluded from stills. | `“Identify your health risks through sleep tracker.”` (representative copy visible in this span) | onboarding / report / offer | Taps, delay, hard gating and outcome remain unverified from stills. | `shuteye_sleeptracker.pdf`, pp. 12–19 |
| 20–24 | Report-generation animation, sleep-recorder examples, feature and review claims. | Wait/continue through promotional screens. | No tracked-night outcome can be concluded from stills. | `“Creating your sleep report…”` (representative copy visible in this span) | onboarding / report / offer | Taps, delay, hard gating and outcome remain unverified from stills. | `shuteye_sleeptracker.pdf`, pp. 20–24 |
| 25–28 | Free-trial activation and premium purchase flow; payment issue screen follows. | Trial toggle/start, Apple purchase confirmation, retry/cancel. | No tracked-night outcome can be concluded from stills. | `“7-day FREE trial is enabled!”` (representative copy visible in this span) | onboarding / report / offer | Taps, delay, hard gating and outcome remain unverified from stills. | `shuteye_sleeptracker.pdf`, pp. 25–28 |
| 29–34 | Sleep score explainer, an open-ended sleep concern prompt, wake-time selection and all-set screen. | Enter/select concern and wake time; skip offered for wake time. | No tracked-night outcome can be concluded from stills. | `“One Score to Understand Your Sleep.”` (representative copy visible in this span) | onboarding / report / offer | Taps, delay, hard gating and outcome remain unverified from stills. | `shuteye_sleeptracker.pdf`, pp. 29–34 |
| 35–40 | Home/insights, sleep-note, dream, sound and sleep-tracker feature surfaces. | Explore feature cards; sleep-tracking CTA is visible. | No tracked-night outcome can be concluded from stills. | `“The Journey Begins.”` (representative copy visible in this span) | onboarding / report / offer | Taps, delay, hard gating and outcome remain unverified from stills. | `shuteye_sleeptracker.pdf`, pp. 35–40 |
| 41–49 | Sleep tracker onboarding/instructions, demo report and profile/premium surfaces. | Set up or start a tracker; account/premium actions appear in later screens. | No tracked-night outcome can be concluded from stills. | `“Start Sleep Tracker.”` (representative copy visible in this span) | onboarding / report / offer | Taps, delay, hard gating and outcome remain unverified from stills. | `shuteye_sleeptracker.pdf`, pp. 41–49 |

## Eight screen lenses

1. **First win.** First visible score is 96 on p. 31, after a long quiz and paywall (p. 25–28). [OBSERVED] Screenshot does not establish that score came from a recorded night; first verified sleep benefit/taps [UNKNOWN].
2. **Ask ledger.** Notification prompt p. 1; sleep duration p. 5; satisfaction p. 6; latency p. 8; snoring p. 9; waking p. 10; fatigue p. 11; sleep position p. 13; habits p. 14–15; daily impact p. 17; diagnosis p. 18. Paywall begins p. 25.
3. **Abstractions.** Score, CBT-I, sleep position, “sleep quality,” health risks, “sleep report,” sleep stages and sleep debt appear across p. 7–24. [OBSERVED] [INFERRED] Much of the quiz could be collapsed to one optional sleep goal.
4. **Feel-good moments.** An “All Set!” screen p. 34 and score explainer p. 31 offer reassurance. [OBSERVED] Claimed 93% improvement and other social proof on p. 12 are not individual progress.
5. **Feel-bad moments.** P. 19 says “Identify your health risks through sleep tracker” before the report; this could raise anxiety. [OBSERVED] The images cannot verify medical accuracy or user distress.
6. **Paywall.** Paywall p. 26 shows enabled 7-day trial, reminder on day 5, and ₹5,900/year on day 7; Apple confirmation follows p. 27. [OBSERVED] India storefront, captured 2026-10-03. Payment issue is shown p. 28. Exact trial-default behavior/exit is [UNKNOWN].
7. **Repeat cost.** Home p. 35–40 and tracker guide p. 41–45 show starting and revisiting reports. Actual overnight completion and number of repeat taps are [UNKNOWN].
8. **Feature map.** [INFERRED] Table stakes: start a sleep recording and see morning summary. Differentiator: dream/sound library and CBT-I framing (p. 7, 22–23, 39–40). Bloat risk: a long health questionnaire and unverified risk claims before the first measured result.

## Keep / Kill / Different

- **Keep.** An “All Set!” screen p. 34 and score explainer p. 31 offer reassurance. [OBSERVED] Claimed 93% improvement and other social proof on p. 12 are not individual progress.
- **Kill.** P. 19 says “Identify your health risks through sleep tracker” before the report; this could raise anxiety. [OBSERVED] The images cannot verify medical accuracy or user distress. [INFERRED] Remove steps or claims here that precede a verified result/command; test the precise step against a fresh install before shipping a similar flow.
- **Different.** First visible score is 96 on p. 31, after a long quiz and paywall (p. 25–28). [OBSERVED] Screenshot does not establish that score came from a recorded night; first verified sleep benefit/taps [UNKNOWN]. [INFERRED] Make the first successful sleep report/TV command visible, identify whether it is measured or a preview, and put optional permissions/account/payment after that first outcome.

## Open questions and verification

- [UNKNOWN] Exact launch-to-benefit taps/time, whether PDF pages form one continuous path, soft versus hard gating, close delays, trial defaults in action, checkout and successful result.
- [UNKNOWN] Repeat-session taps, retention, notification behavior, US storefront prices, listing/review evidence and App Store ID.
- **Checked:** all 49 pages of `shuteye_sleeptracker.pdf` were visually inspected from rendered contact sheets. High-resolution offer pages were separately checked when cited above. Every numeric offer reported in this note is tied to an individual screenshot page and the India storefront shown in the capture; prices are not US estimates.
