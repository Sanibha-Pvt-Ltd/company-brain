---
type: app
category: sleep-tracker
app: Sleep Cycle
app_store_id: unknown
member: kushagra
updated: 2026-10-04
status: draft
sources: [screens:11]
---

# Sleep Cycle — screenshot teardown

**Scope.** Screens-only review of team capture `sleepcycle sleeptracker.pdf` (PDF created 2026-10-03; 11 pages). Each page is covered by a screen-span row below; adjacent pages are grouped only when they belong to the same visible flow. Companion analysis PDF is secondary and was not used as evidence. Listing, reviews and App Store ID are unavailable. [UNKNOWN]

## Per-screen table

| Screen(s) | What user sees | Visible ask | What it gives | Verbatim copy (representative) | Lever | Friction / dark pattern | Source |
|---:|---|---|---|---|---|---|---|
| 1–4 | Welcome and consent prompts for health-data processing and tracking. | Accept health-data terms; optional tracking/marketing permission with skip. | [OBSERVED] Welcome and consent prompts for health-data processing and tracking. | `“We classify our users’ data as health data.”` (representative copy visible in this span) | feature discovery | [INFERRED] Asks user to accept health-data terms; optional tracking/marketing permission with skip. Still images cannot establish timing, hard gating or action success. | `sleepcycle sleeptracker.pdf`, pp. 1–4 |
| 5–8 | Discovery-source question, account creation/login, and sleep goal selection. | Answer referral question, create/sign in account, choose sleep goal. | [OBSERVED] Discovery-source question, account creation/login, and sleep goal selection. | `“Join a community of sleep enthusiasts.”` (representative copy visible in this span) | profile/question burden | [INFERRED] Asks user to answer referral question, create/sign in account, choose sleep goal. Still images cannot establish timing, hard gating or action success. | `sleepcycle sleeptracker.pdf`, pp. 5–8 |
| 9–11 | Notification explanation, subscription explainer and Apple purchase confirmation. | Continue toward a 7-day free trial; iOS purchase sheet. | [OBSERVED] Notification explanation, subscription explainer and Apple purchase confirmation. | `“How your subscription works.”` (representative copy visible in this span) | feature discovery | [INFERRED] Asks user to continue toward a 7-day free trial; iOS purchase sheet. Still images cannot establish timing, hard gating or action success. | `sleepcycle sleeptracker.pdf`, pp. 9–11 |

## Eight screen lenses

1. **First win.** No first sleep result is present. Consent, referral question, login, goal, notifications and a subscription explanation precede any visible tracking screen. [UNKNOWN] First-win/taps.
2. **Ask ledger.** Health-data consent p. 3; optional tracking/marketing p. 4; discovery source p. 5; sign-in/account p. 6–7; goal p. 8; notifications explanation p. 9; offer p. 10; Apple purchase sheet p. 11.
3. **Abstractions.** Health-data consent and sleep goals are understandable concepts; account is introduced before showing sleep value. [OBSERVED] [INFERRED] Invite account creation after the first report.
4. **Feel-good moments.** Privacy explanation (p. 3) and optional tracking skip (p. 4) are user-respecting moments. [OBSERVED] No earned progress appears.
5. **Feel-bad moments.** Account creation and consent precede a usable screen. [OBSERVED] No fear copy or hidden control is established by these pages.
6. **Paywall.** P. 10 says 7 days free then ₹2,050/year and “Recurring billing. Cancel anytime.” Apple sheet p. 11. [OBSERVED] India storefront, captured 2026-10-03. Close delay/hard gate unknown.
7. **Repeat cost.** No core tracking screen is captured; repeat cost is [UNKNOWN].
8. **Feature map.** [INFERRED] Table stakes: easy start and clear sleep summary. Differentiator/bloat cannot be established from 11 pages; onboarding is the only evidence.

## Keep / Kill / Different

- **Keep.** [OBSERVED] Keep the explicit health-data explanation and optional tracking skip (pp. 3–4).
- **Kill.** Remove account creation and subscription before showing a first tracked night (pp. 6–11). [INFERRED]
- **Different.** Allow local setup and first report without login; explain the paid tier after the report. [INFERRED]

## Open questions and verification

- [UNKNOWN] Exact launch-to-benefit taps/time, whether PDF pages form one continuous path, soft versus hard gating, close delays, trial defaults in action, checkout and successful result.
- [UNKNOWN] Repeat-session taps, retention, notification behavior, US storefront prices, listing/review evidence and App Store ID.
- **Checked:** all 11 pages of `sleepcycle sleeptracker.pdf` were visually inspected from rendered contact sheets. High-resolution offer pages were separately checked when cited above. Every numeric offer reported in this note is tied to an individual screenshot page and the India storefront shown in the capture; prices are not US estimates.
