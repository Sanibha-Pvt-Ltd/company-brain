---
type: app
category: baby-tracker
app: Baby Daybook
member: kushagra
updated: 2026-10-04
status: draft
sources: [screenshots:16]
---
# Baby Daybook — screenshot teardown

Source: `kushagra screenshots/Baby tracker/screenshots/babydaybook_app.pdf`, 16 pages. Each page below was visually checked against the rendered source. “Asks” records visible user questions, permissions, profile inputs, or payment choices; it does not estimate taps. A static capture cannot prove that an event was saved, a control was tapped, or a displayed promise works. Pricing with ₹ is the India storefront.

## Per-screen table

| # | What is on screen | Asks of user | Gives before / alongside ask | Lever / friction / copy | Evidence |
|---:|---|---|---|---|---|
| 1 | Welcome screen | Add baby or sign in | Basic app positioning | [OBSERVED] Permission, account, or sharing choice is presented; completion is not captured. | [OBSERVED] `babydaybook_app.pdf` p.1 |
| 2 | Add baby onboarding form | Sex, name, birthday, prematurity, sleep predictions, day start/end | States sleep schedule prediction purpose | [OBSERVED] Input or preference options are visible; whether required is UNKNOWN. | [OBSERVED] `babydaybook_app.pdf` p.2 |
| 3 | Protect and sync | Sign in with Google/Facebook/Apple | Sync/account benefit explained | [OBSERVED] Permission, account, or sharing choice is presented; completion is not captured. | [OBSERVED] `babydaybook_app.pdf` p.3 |
| 4 | Settings during onboarding | Choose units for temp/volume/weight/height/head size | Unit preferences | [OBSERVED] Input or preference options are visible; whether required is UNKNOWN. | [OBSERVED] `babydaybook_app.pdf` p.4 |
| 5 | Permissions | Allow notifications | Permission rationale only | [OBSERVED] Permission, account, or sharing choice is presented; completion is not captured. | [OBSERVED] `babydaybook_app.pdf` p.5 |
| 6 | Premium upsell | Try for free; choose monthly/yearly/lifetime | Premium feature list, prices, annual trial disclosed | [OBSERVED] Paid-tier/trial controls appear here; behavior after selection or close is UNKNOWN. | [OBSERVED] `babydaybook_app.pdf` p.6 |
| 7 | Premium detail | Try for free | Family sync, sleep predictions, statistics, timeline, growth, reminders described | [OBSERVED] Paid-tier/trial controls appear here; behavior after selection or close is UNKNOWN. | [OBSERVED] `babydaybook_app.pdf` p.7 |
| 8 | Dashboard | Choose event icon | Today’s event categories and sleep-prediction panel; no entries | [OBSERVED] Input or preference options are visible; whether required is UNKNOWN. | [OBSERVED] `babydaybook_app.pdf` p.8 |
| 9 | Dashboard categories | Choose Breastfeeding or other event | Events are directly available | [OBSERVED] Input or preference options are visible; whether required is UNKNOWN. | [OBSERVED] `babydaybook_app.pdf` p.9 |
| 10 | Breastfeeding detail/statistics | Select period/side | Summary empty state for selected event | [OBSERVED] Input or preference options are visible; whether required is UNKNOWN. | [OBSERVED] `babydaybook_app.pdf` p.10 |
| 11 | Timeline | Choose timeline icon/date | Timeline overview shown | [OBSERVED] Input or preference options are visible; whether required is UNKNOWN. | [OBSERVED] `babydaybook_app.pdf` p.11 |
| 12 | Development | Choose growth/teething/moments | Development categories shown | [OBSERVED] Input or preference options are visible; whether required is UNKNOWN. | [OBSERVED] `babydaybook_app.pdf` p.12 |
| 13 | Account/sync status | Unlock premium; grant notifications | Sync status and family list | [OBSERVED] Navigation or continue control is visible; requirement to proceed is UNKNOWN. | [OBSERVED] `babydaybook_app.pdf` p.13 |
| 14 | Settings | Toggle timeline/daily activity/resume; permissions | App configuration | [OBSERVED] Permission, account, or sharing choice is presented; completion is not captured. | [OBSERVED] `babydaybook_app.pdf` p.14 |
| 15 | Settings lower section | Set units; allow analytics | Preferences are editable | [OBSERVED] Permission, account, or sharing choice is presented; completion is not captured. | [OBSERVED] `babydaybook_app.pdf` p.15 |
| 16 | Settings support | Rate/recommend/FAQ/feedback | Support links | [OBSERVED] Navigation or continue control is visible; requirement to proceed is UNKNOWN. | [OBSERVED] `babydaybook_app.pdf` p.16 |

## Eight dimensions

1. **First win:** Baby profile and prediction preferences precede dashboard (p.2); actual first event not shown.
2. **Ask ledger:** Baby name/birthday/prematurity/sleep prediction/day schedule (p.2), sync login (p.3), notification permission (p.5), then Premium (p.6) [OBSERVED].
3. **Abstractions:** Sleep predictions, timeline/development and Premium bundles introduce extra concepts [OBSERVED pp.2,6-7].
4. **Feel-good moments:** Baby profile setup and event categories give concrete orientation [OBSERVED pp.2,8]; no completed log visible.
5. **Feel-bad moments:** Premium before first tracker use imposes an interruption [OBSERVED p.6; friction INFERRED].
6. **Paywall:** Full-res p.6 shows monthly/yearly/lifetime, annual trial and renewal copy; X visible. Interaction after close UNKNOWN.
7. **Repeat cost:** Event categories are directly visible on dashboard (p.8); tap count unknown.
8. **Feature map:** Must match: direct feed/sleep logging and summary. Differentiator: configurable units and development timeline. Bloat: broad premium bundle before any event [INFERRED from pp.6-7].

## Keep / Kill / Different

- **Keep:** Keep clear settings and visible activity categories (pp.8,14-16).
- **Kill:** Kill: account/sign-in before any tracker screen is shown (p.3); whether a guest route exists is UNKNOWN, notification ask before value (p.5), pre-use paywall (p.6).
- **Different:** allow local profile and first log before sync, permissions, or Premium.

## Limits

These are screenshot observations, not a live usability test. Tap count/time-to-value, conditional branches, saved-state confirmation unless captured, purchase success, reminder delivery, sync behavior, and free access after closing a paywall are UNKNOWN. Any recommendation above is tagged as inference.
