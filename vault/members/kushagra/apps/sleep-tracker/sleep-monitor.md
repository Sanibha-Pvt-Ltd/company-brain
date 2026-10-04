---
type: app
category: sleep-tracker
app: Sleep Monitor
app_store_id: unknown
member: kushagra
updated: 2026-10-04
status: draft
sources: [screens:49]
---

# Sleep Monitor — screenshot teardown

**Scope.** Screens-only review of team capture `sleep monitor.pdf` (PDF created 2026-10-03; 49 pages). Each page is covered by a screen-span row below; adjacent pages are grouped only when they belong to the same visible flow. Companion analysis PDF is secondary and was not used as evidence. Listing, reviews and App Store ID are unavailable. [UNKNOWN]

## Per-screen table

| Screen(s) | What user sees | Visible ask | What it gives | Verbatim copy (representative) | Lever | Friction / dark pattern | Source |
|---:|---|---|---|---|---|---|---|
| 1–3 | Welcome/social-proof pages and goal prompt. | Start and select desired outcome. | No tracked-night outcome can be concluded from stills. | `“What are you hoping to achieve with Sleep Monitor?”` (representative copy visible in this span) | onboarding / report / offer | Taps, delay, hard gating and outcome remain unverified from stills. | `sleep monitor.pdf`, pp. 1–3 |
| 4–9 | Sleep-duration, sleep-quality, continuity questions and social-proof/results claims. | Repeated answer selections. | No tracked-night outcome can be concluded from stills. | `“How much sleep do you usually get at night?”` (representative copy visible in this span) | onboarding / report / offer | Taps, delay, hard gating and outcome remain unverified from stills. | `sleep monitor.pdf`, pp. 4–9 |
| 10–14 | Snoring/apnea-risk, early wake, daytime feeling and demographic questions; notification prompt shown. | Notification permission plus sleep/health answers and gender/age. | No tracked-night outcome can be concluded from stills. | `“Detect your snoring & sleep apnea risks.”` (representative copy visible in this span) | onboarding / report / offer | Taps, delay, hard gating and outcome remain unverified from stills. | `sleep monitor.pdf`, pp. 10–14 |
| 15–22 | Benefit and pseudo-personalized report/progress screens: score, action plan, recordings, sleep health, sounds, and testimonials. | Continue through benefit carousel. | No tracked-night outcome can be concluded from stills. | `“Here is Your Sleep Wellness Score.”` (representative copy visible in this span) | onboarding / report / offer | Taps, delay, hard gating and outcome remain unverified from stills. | `sleep monitor.pdf`, pp. 15–22 |
| 23–28 | Premium offer, Apple purchase sheet, discounted one-time offer, luck game, prize and email ask. | Choose a plan, continue/close, play offer interaction, enter email. | No tracked-night outcome can be concluded from stills. | `“Sleep better With Premium.”` (representative copy visible in this span) | onboarding / report / offer | Taps, delay, hard gating and outcome remain unverified from stills. | `sleep monitor.pdf`, pp. 23–28 |
| 29–33 | Home screen and soundscape/sleep-tip browsing. | Browse content; no completed sleep result shown here. | No tracked-night outcome can be concluded from stills. | `“No Data.”` (representative copy visible in this span) | onboarding / report / offer | Taps, delay, hard gating and outcome remain unverified from stills. | `sleep monitor.pdf`, pp. 29–33 |
| 34–40 | Journal/trends report pages, sample sleep score, sleep stages, recordings, risk and notes. | Open reports and tracking prompts. | No tracked-night outcome can be concluded from stills. | `“Well done! You had a good rest.”` (representative copy visible in this span) | onboarding / report / offer | Taps, delay, hard gating and outcome remain unverified from stills. | `sleep monitor.pdf`, pp. 34–40 |
| 41–49 | Sleep factor editing, phone placement instructions, smart alarm/tutorial, program and settings pages. | Edit factors, place phone, start tutorial or open profile. | No tracked-night outcome can be concluded from stills. | `“What is a Smart Alarm?”` (representative copy visible in this span) | onboarding / report / offer | Taps, delay, hard gating and outcome remain unverified from stills. | `sleep monitor.pdf`, pp. 41–49 |

## Eight screen lenses

1. **First win.** A wellness score 69 is shown p. 17 and journal score 89 p. 34, after a long quiz and paywall p. 23. [OBSERVED] Data provenance is not visible, so first verified sleep benefit and taps are [UNKNOWN].
2. **Ask ledger.** Goal p. 3; sleep duration p. 4; quality p. 6; continuity p. 8; snoring p. 9; notification p. 10; apnea p. 11; early wake p. 12; daytime energy p. 13; gender/age p. 14. Premium begins p. 23.
3. **Abstractions.** “Sleep Wellness Score,” risks, sleep debt, sleep stages, sleep score and program appear p. 10–22 and p. 34–46. [OBSERVED] [INFERRED] A simple recording and measured duration can precede score/health framing.
4. **Feel-good moments.** Score and personalized action plan cards p. 17–18 look like a tailored payoff. [OBSERVED] The screenshot does not reveal whether personal sleep data underlies them.
5. **Feel-bad moments.** Risk presentation and a “Try Your Luck!” offer/game appear p. 10–11 and p. 27–28. [OBSERVED] [INFERRED] Health-risk framing and chance-based discounts may distract from sleep tracking.
6. **Paywall.** P. 23 shows ₹124.91/month (₹1,499/year) highlighted, plus ₹1,499/month; p. 25 shows one-time offer ₹243.25 with a countdown; Apple sheets p. 24 and 26. [OBSERVED] India storefront, captured 2026-10-03. Do not infer delay/hard gate from stills.
7. **Repeat cost.** Pages 29–49 show a sleep-home, sound library, journal, reports, and tracking instructions. [OBSERVED] Actual tracking success and repeat taps are [UNKNOWN].
8. **Feature map.** [INFERRED] Table stakes: record sleep and make the morning report legible. Differentiator: journal, soundscapes and sleep-factor coaching. Bloat risk: multiple score frameworks, several premium offers and a prize game before any verified sleep record.

## Keep / Kill / Different

- **Keep.** Score and personalized action plan cards p. 17–18 look like a tailored payoff. [OBSERVED] The screenshot does not reveal whether personal sleep data underlies them.
- **Kill.** Risk presentation and a “Try Your Luck!” offer/game appear p. 10–11 and p. 27–28. [OBSERVED] [INFERRED] Health-risk framing and chance-based discounts may distract from sleep tracking. [INFERRED] Remove steps or claims here that precede a verified result/command; test the precise step against a fresh install before shipping a similar flow.
- **Different.** A wellness score 69 is shown p. 17 and journal score 89 p. 34, after a long quiz and paywall p. 23. [OBSERVED] Data provenance is not visible, so first verified sleep benefit and taps are [UNKNOWN]. [INFERRED] Make the first successful sleep report/TV command visible, identify whether it is measured or a preview, and put optional permissions/account/payment after that first outcome.

## Open questions and verification

- [UNKNOWN] Exact launch-to-benefit taps/time, whether PDF pages form one continuous path, soft versus hard gating, close delays, trial defaults in action, checkout and successful result.
- [UNKNOWN] Repeat-session taps, retention, notification behavior, US storefront prices, listing/review evidence and App Store ID.
- **Checked:** all 49 pages of `sleep monitor.pdf` were visually inspected from rendered contact sheets. High-resolution offer pages were separately checked when cited above. Every numeric offer reported in this note is tied to an individual screenshot page and the India storefront shown in the capture; prices are not US estimates.
