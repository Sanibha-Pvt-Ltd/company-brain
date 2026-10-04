---
type: app
category: baby-tracker
app: Nara Baby
member: kushagra
updated: 2026-10-04
status: draft
sources: [screenshots:28]
---
# Nara Baby — screenshot teardown

Source: `kushagra screenshots/Baby tracker/screenshots/narababy_app.pdf`, 28 pages. Each page below was visually checked against the rendered source. “Asks” records visible user questions, permissions, profile inputs, or payment choices; it does not estimate taps. A static capture cannot prove that an event was saved, a control was tapped, or a displayed promise works. Prices are displayed in INR (₹); the storefront is not independently verified, and US pricing is unknown. The `updated` date is the analysis date; screenshot capture dates were not verified.

## Per-screen table

| # | What is on screen | Asks of user | Gives before / alongside ask | Lever / friction / copy | Evidence |
|---:|---|---|---|---|---|
| 1 | iOS tracking permission | Ask App Not to Track / Allow | Privacy choice only | [OBSERVED] Permission, account, or sharing choice is presented; completion is not captured. | [OBSERVED] `narababy_app.pdf` p.1 |
| 2 | Welcome | Get Started / login | Wellness tracker framing | [OBSERVED] Navigation or continue control is visible; requirement to proceed is UNKNOWN. | [OBSERVED] `narababy_app.pdf` p.2 |
| 3 | Account path | I’m new to Nara / joining family / login | Account route selection | [OBSERVED] Navigation or continue control is visible; requirement to proceed is UNKNOWN. | [OBSERVED] `narababy_app.pdf` p.3 |
| 4 | Create account | Name/email/password/relationship; create | Terms/privacy acceptance | [OBSERVED] Input or preference options are visible; whether required is UNKNOWN. | [OBSERVED] `narababy_app.pdf` p.4 |
| 5 | Baby profile | Name/birthdate/sex/first child | Baby data needed for setup | [OBSERVED] Input or preference options are visible; whether required is UNKNOWN. | [OBSERVED] `narababy_app.pdf` p.5 |
| 6 | Activity selection 1 | Toggle feeding/pumping/diaper/sleep/routines | Select categories | [OBSERVED] Input or preference options are visible; whether required is UNKNOWN. | [OBSERVED] `narababy_app.pdf` p.6 |
| 7 | Activity selection 2 | Toggle growth/milestones/medical/vaccines | More category choices | [OBSERVED] Input or preference options are visible; whether required is UNKNOWN. | [OBSERVED] `narababy_app.pdf` p.7 |
| 8 | Postpartum health question | Yes/no | Optional health tracking context | [OBSERVED] Input or preference options are visible; whether required is UNKNOWN. | [OBSERVED] `narababy_app.pdf` p.8 |
| 9 | Health categories | Toggle hydration/nutrition/health/mood/journal/sleep | Category selection | [OBSERVED] Input or preference options are visible; whether required is UNKNOWN. | [OBSERVED] `narababy_app.pdf` p.9 |
| 10 | Notifications | Enable / Not now | Timer reminders explained | [OBSERVED] Navigation or continue control is visible; requirement to proceed is UNKNOWN. | [OBSERVED] `narababy_app.pdf` p.10 |
| 11 | Invite caregiver | Invite caregiver / Not now | Shared tracking offered | [OBSERVED] Permission, account, or sharing choice is presented; completion is not captured. | [OBSERVED] `narababy_app.pdf` p.11 |
| 12 | Welcome story | Start now | Narrative onboarding; no tracked event | [OBSERVED] Navigation or continue control is visible; requirement to proceed is UNKNOWN. | [OBSERVED] `narababy_app.pdf` p.12 |
| 13 | Home/feed dashboard | Got it | Track session button and categories | [OBSERVED] Navigation or continue control is visible; requirement to proceed is UNKNOWN. | [OBSERVED] `narababy_app.pdf` p.13 |
| 14 | Pump/diaper dashboard | Tap + on category | Event cards | [OBSERVED] Navigation or continue control is visible; requirement to proceed is UNKNOWN. | [OBSERVED] `narababy_app.pdf` p.14 |
| 15 | Sleep/routine/growth dashboard | Tap + | Event types | [OBSERVED] Navigation or continue control is visible; requirement to proceed is UNKNOWN. | [OBSERVED] `narababy_app.pdf` p.15 |
| 16 | No entries state | Start tracking | No data shown | [OBSERVED] Navigation or continue control is visible; requirement to proceed is UNKNOWN. | [OBSERVED] `narababy_app.pdf` p.16 |
| 17 | Trends | Select feed/sleep/diaper trend | Zero or empty event stats | [OBSERVED] Input or preference options are visible; whether required is UNKNOWN. | [OBSERVED] `narababy_app.pdf` p.17 |
| 18 | Category menu | Choose category | Activity list | [OBSERVED] Input or preference options are visible; whether required is UNKNOWN. | [OBSERVED] `narababy_app.pdf` p.18 |
| 19 | Sleep trend detail | Select day/range | Sleep totals and day/night breakdown; no entries | [OBSERVED] Input or preference options are visible; whether required is UNKNOWN. | [OBSERVED] `narababy_app.pdf` p.19 |
| 20 | Guides | Open guide | Article library | [OBSERVED] Navigation or continue control is visible; requirement to proceed is UNKNOWN. | [OBSERVED] `narababy_app.pdf` p.20 |
| 21 | Guide detail | Read/scroll | Feeding article | [OBSERVED] Navigation or continue control is visible; requirement to proceed is UNKNOWN. | [OBSERVED] `narababy_app.pdf` p.21 |
| 22 | Guide detail | Read/scroll | Sleep guide/article | [OBSERVED] Navigation or continue control is visible; requirement to proceed is UNKNOWN. | [OBSERVED] `narababy_app.pdf` p.22 |
| 23 | Account | Choose account/subscription/settings | Menu options | [OBSERVED] Input or preference options are visible; whether required is UNKNOWN. | [OBSERVED] `narababy_app.pdf` p.23 |
| 24 | Subscription sheet | Choose lifetime/monthly; Continue/restore | ₹7,900 lifetime, ₹799 monthly; claims listed | [OBSERVED] Paid-tier/trial controls appear here; behavior after selection or close is UNKNOWN. | [OBSERVED] `narababy_app.pdf` p.24 |
| 25 | Settings | Set email/password/preferences | Account preferences | [OBSERVED] Input or preference options are visible; whether required is UNKNOWN. | [OBSERVED] `narababy_app.pdf` p.25 |
| 26 | Children/family | Add child/caregiver | Family management | [OBSERVED] Navigation or continue control is visible; requirement to proceed is UNKNOWN. | [OBSERVED] `narababy_app.pdf` p.26 |
| 27 | Dashboard overflow | Set reminders/edit activities | Shortcuts | [OBSERVED] Navigation or continue control is visible; requirement to proceed is UNKNOWN. | [OBSERVED] `narababy_app.pdf` p.27 |
| 28 | Summary sheet | Today/last 24h | No activity | [OBSERVED] Navigation or continue control is visible; requirement to proceed is UNKNOWN. | [OBSERVED] `narababy_app.pdf` p.28 |

## Eight dimensions

1. **First win:** Home event cards shown p.13 after setup; no event completion until p.16 says no entries, with Start tracking.
2. **Ask ledger:** Tracking permission dialog, account route/create, baby data, category choices, postpartum health, notification ask, caregiver invite (pp.1-11) [OBSERVED].
3. **Abstractions:** Broad reproductive/postpartum health categories in addition to baby logging; guides and routines [OBSERVED pp.8-9,20-22].
4. **Feel-good moments:** Narrative welcome and organized categories [OBSERVED]; first log outcome is absent.
5. **Feel-bad moments:** Many category and account asks before dashboard [OBSERVED pp.2-12]; likely setup burden [INFERRED].
6. **Paywall:** Account section paywall p.24 after dashboard; full-res shows INR pricing; whether core log remains free UNKNOWN.
7. **Repeat cost:** Category card + buttons for starting event (pp.13-15); taps unknown.
8. **Feature map:** Must match: caregiving categories and family access. Differentiator: content guides and postpartum tracking. Bloat: health scope can obscure core baby log [INFERRED].

## Keep / Kill / Different

- **Keep:** Keep optional postpartum switch and “Not Now” for caregiver invite (p.11).
- **Kill:** Kill: tracking-permission request before user sees benefit (p.1) and extensive category selection as prerequisite.
- **Different:** start with Feed/Sleep/Diaper; defer postpartum and extra categories until user asks.

## Limits

These are screenshot observations, not a live usability test. Tap count/time-to-value, conditional branches, saved-state confirmation unless captured, purchase success, reminder delivery, sync behavior, and free access after closing a paywall are UNKNOWN. Any recommendation above is tagged as inference.
