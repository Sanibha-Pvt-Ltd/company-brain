---
type: app
category: baby-tracker
app: The Wonder Weeks
member: kushagra
updated: 2026-10-04
status: draft
sources: [screenshots:13]
---
# The Wonder Weeks — screenshot teardown

Source: `kushagra screenshots/Baby tracker/screenshots/wonderweek_apps.pdf`, 13 pages. Each page below was visually checked against the rendered source. “Asks” records visible user questions, permissions, profile inputs, or payment choices; it does not estimate taps. A static capture cannot prove that an event was saved, a control was tapped, or a displayed promise works. Prices are displayed in INR (₹); the storefront is not independently verified, and US pricing is unknown. The `updated` date is the analysis date; screenshot capture dates were not verified.

## Per-screen table

| # | What is on screen | Asks of user | Gives before / alongside ask | Lever / friction / copy | Evidence |
|---:|---|---|---|---|---|
| 1 | Launch/loading | Wait | Brand mark only | [OBSERVED] No setup, permission, account, or payment ask is visible on this screen. | [OBSERVED] `wonderweek_apps.pdf` p.1 |
| 2 | Language selection | Select language | Language choices | [OBSERVED] Input or preference options are visible; whether required is UNKNOWN. | [OBSERVED] `wonderweek_apps.pdf` p.2 |
| 3 | 10 Leaps intro | Start / partner code | Development-leap positioning | [OBSERVED] Navigation or continue control is visible; requirement to proceed is UNKNOWN. | [OBSERVED] `wonderweek_apps.pdf` p.3 |
| 4 | Baby name | Enter baby name / Login | Baby profile begins | [OBSERVED] Input or preference options are visible; whether required is UNKNOWN. | [OBSERVED] `wonderweek_apps.pdf` p.4 |
| 5 | Gender selection | Choose boy/girl or skip | Profile field | [OBSERVED] Input or preference options are visible; whether required is UNKNOWN. | [OBSERVED] `wonderweek_apps.pdf` p.5 |
| 6 | Profile photo | Add photo or skip | Photo optional | [OBSERVED] Navigation or continue control is visible; requirement to proceed is UNKNOWN. | [OBSERVED] `wonderweek_apps.pdf` p.6 |
| 7 | Calculation progress | Wait | “Calculating your leap!” | [OBSERVED] No setup, permission, account, or payment ask is visible on this screen. | [OBSERVED] `wonderweek_apps.pdf` p.7 |
| 8 | Notification education | Next | Notification value proposition | [OBSERVED] Navigation or continue control is visible; requirement to proceed is UNKNOWN. | [OBSERVED] `wonderweek_apps.pdf` p.8 |
| 9 | Subscription chooser | Select duration / Purchase / restore | 1,3,24 month plans and prices; 24-month highlighted | [OBSERVED] Paid-tier/trial controls appear here; behavior after selection or close is UNKNOWN. | [OBSERVED] `wonderweek_apps.pdf` p.9 |
| 10 | Login form | Email/password / create account | Account requirement | [OBSERVED] Permission, account, or sharing choice is presented; completion is not captured. | [OBSERVED] `wonderweek_apps.pdf` p.10 |
| 11 | Email verification | Check email / next / resend | Email OTP required | [OBSERVED] Input or preference options are visible; whether required is UNKNOWN. | [OBSERVED] `wonderweek_apps.pdf` p.11 |
| 12 | Feature preview 1 | Next | Diary feature promo | [OBSERVED] Navigation or continue control is visible; requirement to proceed is UNKNOWN. | [OBSERVED] `wonderweek_apps.pdf` p.12 |
| 13 | Repeat plan chooser | Select duration / Purchase | Same subscription options; purchase CTA | [OBSERVED] Input or preference options are visible; whether required is UNKNOWN. | [OBSERVED] `wonderweek_apps.pdf` p.13 |

## Eight dimensions

1. **First win:** No first diary entry or tracking dashboard is shown in this 13-page set. First win UNKNOWN.
2. **Ask ledger:** Language, infant name, gender/photo, notification education, sign-in/email verification, then payment choice [OBSERVED pp.2-11].
3. **Abstractions:** The proprietary “10 Leaps” framework is the dominant explanatory model [OBSERVED p.3].
4. **Feel-good moments:** Baby avatar/photo and diary preview [OBSERVED pp.5-6,12] create identity/anticipation; no recorded developmental milestone is shown.
5. **Feel-bad moments:** Login/email verification and paywall happen before a usable diary screen in the provided capture [OBSERVED]; exact user path conditionality UNKNOWN.
6. **Paywall:** Plan selector appears p.9 and p.13; INR amounts are displayed; storefront is not independently verified. Trial terms and close behavior are not visible on the screenshot [UNKNOWN].
7. **Repeat cost:** Repeat cost UNKNOWN because no tracker/dashboard is captured.
8. **Feature map:** Must match: age-organized guidance if users need it. Differentiator: leap-timed guidance. Bloat: jargon/framework before first useful diary record [INFERRED].

## Keep / Kill / Different

- **Keep:** Keep optional profile photo and feature preview (pp.6,12).
- **Kill:** Kill: subscription before demonstrating a useful diary entry; avoid presenting leap labels as necessary concepts.
- **Different:** open a sample diary/age view before account or payment, explain any development terms in ordinary language.

## Limits

These are screenshot observations, not a live usability test. Tap count/time-to-value, conditional branches, saved-state confirmation unless captured, purchase success, reminder delivery, sync behavior, and free access after closing a paywall are UNKNOWN. Any recommendation above is tagged as inference.
