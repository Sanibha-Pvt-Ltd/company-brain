---
type: app
category: baby-tracker
app: nappi
member: kushagra
updated: 2026-10-04
status: draft
sources: [screenshots:28]
---
# nappi — screenshot teardown

Source: `kushagra screenshots/Baby tracker/screenshots/nappi_app.pdf`, 28 pages. Each page below was visually checked against the rendered source. “Asks” records visible user questions, permissions, profile inputs, or payment choices; it does not estimate taps. A static capture cannot prove that an event was saved, a control was tapped, or a displayed promise works. Pricing with ₹ is the India storefront.

## Per-screen table

| # | What is on screen | Asks of user | Gives before / alongside ask | Lever / friction / copy | Evidence |
|---:|---|---|---|---|---|
| 1 | Welcome slide 1 | Next | Log everything in seconds | [OBSERVED] Navigation or continue choice is visible; requirement to proceed is UNKNOWN. | [OBSERVED] `nappi_app.pdf` p.1 |
| 2 | Welcome slide 2 | Next | Watch/voice/Alexa benefits | [OBSERVED] Navigation or continue choice is visible; requirement to proceed is UNKNOWN. | [OBSERVED] `nappi_app.pdf` p.2 |
| 3 | Welcome slide 3 | Get Started | Share with family promise | [OBSERVED] Navigation or continue choice is visible; requirement to proceed is UNKNOWN. | [OBSERVED] `nappi_app.pdf` p.3 |
| 4 | Sign in | Sign in or create account | Google/Apple/email available | [OBSERVED] Permission/account/sharing choice requested before the user can proceed from this captured state. | [OBSERVED] `nappi_app.pdf` p.4 |
| 5 | Parent name | Enter name | Personal greeting | [OBSERVED] Input or preference choice requested; whether it is mandatory is UNKNOWN. | [OBSERVED] `nappi_app.pdf` p.5 |
| 6 | Family setup | Create/join family or enter code | Family sharing framed as tracking with others | [OBSERVED] Permission/account/sharing choice requested before the user can proceed from this captured state. | [OBSERVED] `nappi_app.pdf` p.6 |
| 7 | Invite family | Enter email / skip | Caregiver invitation; optional skip | [OBSERVED] Input or preference choice requested; whether it is mandatory is UNKNOWN. | [OBSERVED] `nappi_app.pdf` p.7 |
| 8 | Notification explainer | Enable notifications or Not now | Reminders, feeds, live timers described | [OBSERVED] Permission/account/sharing choice requested before the user can proceed from this captured state. | [OBSERVED] `nappi_app.pdf` p.8 |
| 9 | Feature summary | Start tracking | What’s included list | [OBSERVED] Navigation or continue choice is visible; requirement to proceed is UNKNOWN. | [OBSERVED] `nappi_app.pdf` p.9 |
| 10 | Dashboard | Tap a category to start | SleepSense and quick log; no event shown | [OBSERVED] Navigation or continue choice is visible; requirement to proceed is UNKNOWN. | [OBSERVED] `nappi_app.pdf` p.10 |
| 11 | Sleep timer | Start | Start sleep event | [OBSERVED] Navigation or continue choice is visible; requirement to proceed is UNKNOWN. | [OBSERVED] `nappi_app.pdf` p.11 |
| 12 | Dashboard after timer entry | Choose another category | Event categories shown | [OBSERVED] Input or preference choice requested; whether it is mandatory is UNKNOWN. | [OBSERVED] `nappi_app.pdf` p.12 |
| 13 | More categories | Add photo / choose activity | Additional tracking options | [OBSERVED] Input or preference choice requested; whether it is mandatory is UNKNOWN. | [OBSERVED] `nappi_app.pdf` p.13 |
| 14 | Lumi assistant | Ask a question / prompt | Assistant intro; data guidance offers | [OBSERVED] Navigation or continue choice is visible; requirement to proceed is UNKNOWN. | [OBSERVED] `nappi_app.pdf` p.14 |
| 15 | Premium paywall preview | Try one week free / close | Feature list and close option | [OBSERVED] Paid tier/trial control is on this page; visibility of dismiss/close is noted only when shown. | [OBSERVED] `nappi_app.pdf` p.15 |
| 16 | SleepSense | Open sleep insight | Sleep guidance and expected range positioning | [OBSERVED] Navigation or continue choice is visible; requirement to proceed is UNKNOWN. | [OBSERVED] `nappi_app.pdf` p.16 |
| 17 | Reports tab | Choose date/range | Empty calendar, no records | [OBSERVED] Input or preference choice requested; whether it is mandatory is UNKNOWN. | [OBSERVED] `nappi_app.pdf` p.17 |
| 18 | Memories | Add memory | Empty memory prompt | [OBSERVED] Navigation or continue choice is visible; requirement to proceed is UNKNOWN. | [OBSERVED] `nappi_app.pdf` p.18 |
| 19 | Child profile | Add another baby | Profile card | [OBSERVED] Navigation or continue choice is visible; requirement to proceed is UNKNOWN. | [OBSERVED] `nappi_app.pdf` p.19 |
| 20 | Family menu | Open category | Family calendar/health/milestones/reminders/sleep/guidance | [OBSERVED] Navigation or continue choice is visible; requirement to proceed is UNKNOWN. | [OBSERVED] `nappi_app.pdf` p.20 |
| 21 | Settings | Choose setting | Subscription/account/referrals | [OBSERVED] Input or preference choice requested; whether it is mandatory is UNKNOWN. | [OBSERVED] `nappi_app.pdf` p.21 |
| 22 | Settings preferences | Change units/notifications/shortcuts | Preferences | [OBSERVED] Navigation or continue choice is visible; requirement to proceed is UNKNOWN. | [OBSERVED] `nappi_app.pdf` p.22 |
| 23 | Settings support | Open help/rate/share | Support links | [OBSERVED] Navigation or continue choice is visible; requirement to proceed is UNKNOWN. | [OBSERVED] `nappi_app.pdf` p.23 |
| 24 | Premium benefits sheet | Try one week free / close | Benefit list including predictions, sounds, reporting, Lumi | [OBSERVED] Paid tier/trial control is on this page; visibility of dismiss/close is noted only when shown. | [OBSERVED] `nappi_app.pdf` p.24 |
| 25 | Premium terms/plans | Choose yearly/monthly; trial CTA | ₹3,999/year, ₹399/month, free week details | [OBSERVED] Paid tier/trial control is on this page; visibility of dismiss/close is noted only when shown. | [OBSERVED] `nappi_app.pdf` p.25 |
| 26 | Apple purchase sheet | Double-click to subscribe | Trial and renewal terms visible | [OBSERVED] Paid tier/trial control is on this page; visibility of dismiss/close is noted only when shown. | [OBSERVED] `nappi_app.pdf` p.26 |
| 27 | SleepSense detail | No action visible | Sleep tracking guidance/expected age-range summary | [OBSERVED] No direct data/permission/payment ask is apparent on this captured screen. | [OBSERVED] `nappi_app.pdf` p.27 |
| 28 | More category sheet | Choose potty/pumping/medical | Additional event categories | [OBSERVED] Input or preference choice requested; whether it is mandatory is UNKNOWN. | [OBSERVED] `nappi_app.pdf` p.28 |

## Eight dimensions

1. **First win:** Dashboard and event buttons shown p.10; sleep timer start screen p.11. No stop/save confirmation captured.
2. **Ask ledger:** {lens[1]}
3. **Abstractions:** {lens[2]}
4. **Feel-good moments:** {lens[3]}
5. **Feel-bad moments:** {lens[4]}
6. **Paywall:** {lens[5]}
7. **Repeat cost:** {lens[6]}
8. **Feature map:** {lens[7]}

## Keep / Kill / Different

- **Keep:** Keep clear category tiles and optional “Not now” on notification ask (p.8).
- **Kill:** Kill: requiring family creation/invite before first log; avoid assistant presenting itself as medical authority.
- **Different:** make sign-in and family invite optional until after a local entry; expose timer and save confirmation immediately.

## Limits

These are screenshot observations, not a live usability test. Tap count/time-to-value, conditional branches, saved-state confirmation unless captured, purchase success, reminder delivery, sync behavior, and free access after closing a paywall are UNKNOWN. Any recommendation above is tagged as inference.
