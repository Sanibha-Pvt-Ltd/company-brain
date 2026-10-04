---
type: app
category: sleep-tracker
app: Sleep Sounds and Alarm by Leap Health
app_store_id: unknown
member: kushagra
updated: 2026-10-04
status: draft
sources: [screens:54]
---

# Sleep Sounds and Alarm by Leap Health — screenshot teardown

**Scope.** Screens-only review of team capture `sleeptracker_sounds and alarm by leap health.pdf` (PDF created 2026-10-03; 54 pages). Each page is covered by a screen-span row below; adjacent pages are grouped only when they belong to the same visible flow. Companion analysis PDF is secondary and was not used as evidence. Listing, reviews and App Store ID are unavailable. [UNKNOWN]

## Per-screen table

| Screen(s) | What user sees | Visible ask | What it gives | Verbatim copy (representative) | Lever | Friction / dark pattern | Source |
|---:|---|---|---|---|---|---|---|
| 1–5 | Welcome, sleep questionnaire, and promised sleep-tracker outputs. | Choose sleep duration and other answers; accept prompt/continue. | [OBSERVED] Welcome, sleep questionnaire, and promised sleep-tracker outputs. | `“How much sleep do you usually get at night?”` (representative copy visible in this span) | profile/question burden | [INFERRED] Asks user to choose sleep duration and other answers; accept prompt/continue. Still images cannot establish timing, hard gating or action success. | `sleeptracker_sounds and alarm by leap health.pdf`, pp. 1–5 |
| 6–14 | Personalization questions, health-risk content and demographic inputs. | Answer sleep/health questions and select profile information. | [OBSERVED] Personalization questions, health-risk content and demographic inputs. | `“100+ Risks Analyzed.”` (representative copy visible in this span) | profile/question burden | [INFERRED] Asks user to answer sleep/health questions and select profile information. Still images cannot establish timing, hard gating or action success. | `sleeptracker_sounds and alarm by leap health.pdf`, pp. 6–14 |
| 15–21 | Premium benefit carousel, then store purchase confirmation. | Free-trial/premium CTA and Apple purchase confirmation. | [OBSERVED] Premium benefit carousel, then store purchase confirmation. | `“Find Your Best Sleep With PREMIUM.”` (representative copy visible in this span) | trial conversion | [INFERRED] Asks user to free-trial/premium CTA and Apple purchase confirmation. Still images cannot establish timing, hard gating or action success. | `sleeptracker_sounds and alarm by leap health.pdf`, pp. 15–21 |
| 22–29 | Home/sleep tracking start, microphone permission, sample/no-data report and sleep sound browsing. | Start tracking; microphone permission is requested. | [OBSERVED] Home/sleep tracking start, microphone permission, sample/no-data report and sleep sound browsing. | `“Start Sleep Tracking.”` (representative copy visible in this span) | result preview | [INFERRED] Asks user to start tracking; microphone permission is requested. Still images cannot establish timing, hard gating or action success. | `sleeptracker_sounds and alarm by leap health.pdf`, pp. 22–29 |
| 30–33 | Sleep schedule, activity/wellness and notes surfaces. | Set/track routines; add notes and activity. | [OBSERVED] Sleep schedule, activity/wellness and notes surfaces. | `“Sleep goal.”` (representative copy visible in this span) | feature discovery | [INFERRED] Asks user to set/track routines; add notes and activity. Still images cannot establish timing, hard gating or action success. | `sleeptracker_sounds and alarm by leap health.pdf`, pp. 30–33 |
| 34–40 | Journal/trend and sleep-score reports, sleep analysis, health-risk and dream-note surfaces. | Open report and analysis controls; some screens prompt for monitoring time. | [OBSERVED] Journal/trend and sleep-score reports, sleep analysis, health-risk and dream-note surfaces. | `“89” (sleep score displayed in the journal screenshot).` (representative copy visible in this span) | result preview | [INFERRED] Asks user to open report and analysis controls; some screens prompt for monitoring time. Still images cannot establish timing, hard gating or action success. | `sleeptracker_sounds and alarm by leap health.pdf`, pp. 34–40 |
| 41–46 | Sleep-factor editing and tutorials for phone placement/alarm; program feature card. | Add/remove factors, follow tutorials, start program. | [OBSERVED] Sleep-factor editing and tutorials for phone placement/alarm; program feature card. | `“Tap to add/remove sleep factors.”` (representative copy visible in this span) | feature discovery | [INFERRED] Asks user to add/remove factors, follow tutorials, start program. Still images cannot establish timing, hard gating or action success. | `sleeptracker_sounds and alarm by leap health.pdf`, pp. 41–46 |
| 47–54 | Profile/settings pages, premium promotion, sleep setup and tracking/recording prompts. | Configure settings, create/access account, activate trial or continue tracking. | [OBSERVED] Profile/settings pages, premium promotion, sleep setup and tracking/recording prompts. | `“Sweet dreams!”` (representative copy visible in this span) | trial conversion | [INFERRED] Asks user to configure settings, create/access account, activate trial or continue tracking. Still images cannot establish timing, hard gating or action success. | `sleeptracker_sounds and alarm by leap health.pdf`, pp. 47–54 |

## Eight screen lenses

1. **First win.** Journal p. 34 shows a score of 89 and report pages continue through p. 40, after onboarding and premium pages p. 15–21. [OBSERVED] Whether these screens reflect a recorded night is [UNKNOWN].
2. **Ask ledger.** Quiz answers p. 3–14; paywall p. 15–21; microphone permission p. 23; first start-tracking CTA p. 22/28. [OBSERVED] Individual question topics are recorded in page index.
3. **Abstractions.** Sleep score, sleep stages, sleep apnea risk, dream analysis, activity and sleep factors all appear. [OBSERVED] [INFERRED] The score/report bundle should be layered after raw sleep duration and recording.
4. **Feel-good moments.** Journal reports and “Well done! You had a good rest.” p. 34 provide a concrete positive feedback loop. [OBSERVED] Provenance of score 89 is [UNKNOWN].
5. **Feel-bad moments.** “100+ Risks Analyzed” and disease-risk framing p. 13 arrive before tracking. [OBSERVED] [INFERRED] This may overstate what a consumer sleep recorder can diagnose.
6. **Paywall.** Premium carousel p. 15–20 advertises a 7-day trial then ₹3,599/year; Apple purchase modal p. 21. [OBSERVED] INR is displayed; US pricing is unknown. PDF metadata creation date is 2026-10-03; screenshot capture date is unknown. Confirm terms/close behavior in hands-on test.
7. **Repeat cost.** P. 22/28 show “Start Sleep Tracking”; p. 34–40 show report screens. [OBSERVED] Repeat taps, overnight recording and report-generation path are [UNKNOWN].
8. **Feature map.** [INFERRED] Table stakes: start recording and show a morning sleep summary. Differentiator: a trend journal and editable sleep factors (p. 34–43). Bloat risk: health-risk carousel plus sounds, meditation, dreams and exercise modules before one verified report.

## Keep / Kill / Different

- **Keep.** [INFERRED] Keep the journal score/trend screens and editable sleep factors (pp. 34–43), with measurement provenance.
- **Kill.** Remove the “100+ Risks Analyzed” claim before a recording and defer unrelated content modules (pp. 13, 31–40). [INFERRED]
- **Different.** Start one recording, then present a sourced overnight timeline and only then optional risk/coaching content. [INFERRED]

## Open questions and verification

- [UNKNOWN] Exact launch-to-benefit taps/time, whether PDF pages form one continuous path, soft versus hard gating, close delays, trial defaults in action, checkout and successful result.
- [UNKNOWN] Repeat-session taps, retention, notification behavior, US storefront prices, listing/review evidence and App Store ID.
- **Checked:** all 54 pages of `sleeptracker_sounds and alarm by leap health.pdf` were visually inspected from rendered contact sheets. High-resolution offer pages were separately checked when cited above. Every numeric offer reported in this note is tied to an individual screenshot page and the India storefront shown in the capture; prices are not US estimates.
