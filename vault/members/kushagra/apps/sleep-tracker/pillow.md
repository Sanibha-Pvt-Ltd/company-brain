---
type: app
category: sleep-tracker
app: Pillow
app_store_id: unknown
member: kushagra
updated: 2026-10-04
status: draft
sources: [screens:18]
---

# Pillow — screenshot teardown

**Scope.** Screens-only review of team capture `pillow_sleeptracker.pdf` (PDF created 2026-10-03; 18 pages). Each page is covered by a screen-span row below; adjacent pages are grouped only when they belong to the same visible flow. Companion analysis PDF is secondary and was not used as evidence. Listing, reviews and App Store ID are unavailable. [UNKNOWN]

## Per-screen table

| Screen(s) | What user sees | Visible ask | What it gives | Verbatim copy (representative) | Lever | Friction / dark pattern | Source |
|---:|---|---|---|---|---|---|---|
| 1–2 | Welcome and privacy explanation. | Accept privacy notice. | [OBSERVED] Welcome and privacy explanation. | `“We Respect Your Privacy.”` (representative copy visible in this span) | feature discovery | [INFERRED] Asks user to accept privacy notice. Still images cannot establish timing, hard gating or action success. | `pillow_sleeptracker.pdf`, pp. 1–2 |
| 3–4 | Personalized-analysis profile fields and bedtime setup. | Select birth year, sex, weight, height, and bedtime. | [OBSERVED] Personalized-analysis profile fields and bedtime setup. | `“Personalised Analysis.”` (representative copy visible in this span) | profile/question burden | [INFERRED] Asks user to select birth year, sex, weight, height, and bedtime. Still images cannot establish timing, hard gating or action success. | `pillow_sleeptracker.pdf`, pp. 3–4 |
| 5–10 | Notification and wearable prompts, Motion/Apple Health permissions, Health data scope and sharing. | Notification, wearable data, motion, Health read/write and sharing permissions. | [OBSERVED] Notification and wearable prompts, Motion/Apple Health permissions, Health data scope and sharing. | `“Don’t Miss Important Reports and Insights.”` (representative copy visible in this span) | permission cost | [INFERRED] Asks user to notification, wearable data, motion, Health read/write and sharing permissions. Still images cannot establish timing, hard gating or action success. | `pillow_sleeptracker.pdf`, pp. 5–10 |
| 11–13 | Microphone/sleep-sounds and iCloud-upload explanations; health safety notice. | Microphone access, optional iCloud upload, acknowledge safety notice. | [OBSERVED] Microphone/sleep-sounds and iCloud-upload explanations; health safety notice. | `“Your Safety Matters.”` (representative copy visible in this span) | feature discovery | [INFERRED] Asks user to microphone access, optional iCloud upload, acknowledge safety notice. Still images cannot establish timing, hard gating or action success. | `pillow_sleeptracker.pdf`, pp. 11–13 |
| 14 | Congratulations screen. | Tap “Let’s begin!” | [OBSERVED] Congratulations screen. | `“Congratulations!”` (representative copy visible in this span) | feature discovery | [INFERRED] Asks user to tap “Let’s begin!” Still images cannot establish timing, hard gating or action success. | `pillow_sleeptracker.pdf`, pp. 14 |
| 15–18 | Premium benefits and trial price screen; later pages in this capture are not established as a successful tracking session. | Start free trial or continue toward premium. | [OBSERVED] Premium benefits and trial price screen; later pages in this capture are not established as a successful tracking session. | `“Pillow Premium Your free 7-day trial.”` (representative copy visible in this span) | trial conversion | [INFERRED] Asks user to start free trial or continue toward premium. Still images cannot establish timing, hard gating or action success. | `pillow_sleeptracker.pdf`, pp. 15–18 |

## Eight screen lenses

1. **First win.** No actual tracked-night report appears in p. 1–18; first visible benefit is premium access. [UNKNOWN] First win/taps and whether a real result is available before trial.
2. **Ask ledger.** Profile birth year/sex/weight/height p. 3; bedtime p. 4; notification p. 5; wearable p. 6; motion p. 7; Apple Health p. 8–10; sleep-sound microphone p. 11; optional iCloud p. 12; acknowledge medical disclaimer p. 13; premium p. 15–16.
3. **Abstractions.** Health data permissions, wearable model, iCloud upload and sleep sounds are introduced before a tracked result (p. 6–12). [OBSERVED] [INFERRED] Only the chosen capture method is needed to begin.
4. **Feel-good moments.** Privacy and safety explanations (p. 2, 12–13) offer context before permissions. [OBSERVED] A first result or earned progress moment is absent.
5. **Feel-bad moments.** Health and microphone permissions stack before tracking. [OBSERVED] Copy at p. 13 says “Pillow is not a medical app.” Permission necessity is [UNKNOWN] without hands-on test.
6. **Paywall.** Paywall p. 16: 7 days free, then ₹1,999/year / ₹166.58 per month. [OBSERVED] INR is displayed; US pricing is unknown. PDF metadata creation date is 2026-10-03; screenshot capture date is unknown. The capture includes no proof of checkout or close delay.
7. **Repeat cost.** No overnight tracking/result or next-day repeat path shown. [UNKNOWN] Setup asks for notifications and health access, but the ongoing tap count is not shown.
8. **Feature map.** [INFERRED] Table stakes: bedtime and sleep recording. Differentiator: Apple Watch/Health and sleep-sound context. Bloat risk: iCloud upload explanation and wearable setup before demonstrating core tracking.

## Keep / Kill / Different

- **Keep.** [INFERRED] Keep the privacy explanation and explicit medical-safety caveat (pp. 2, 13).
- **Kill.** Remove the sequence of wearable, motion, Health, microphone and iCloud asks before first tracking (pp. 6–12). [INFERRED]
- **Different.** Start with local phone tracking; ask for Watch, Health, sounds and cloud one at a time when needed. [INFERRED]

## Open questions and verification

- [UNKNOWN] Exact launch-to-benefit taps/time, whether PDF pages form one continuous path, soft versus hard gating, close delays, trial defaults in action, checkout and successful result.
- [UNKNOWN] Repeat-session taps, retention, notification behavior, US storefront prices, listing/review evidence and App Store ID.
- **Checked:** all 18 pages of `pillow_sleeptracker.pdf` were visually inspected from rendered contact sheets. High-resolution offer pages were separately checked when cited above. Every numeric offer reported in this note is tied to an individual screenshot page and the India storefront shown in the capture; prices are not US estimates.
