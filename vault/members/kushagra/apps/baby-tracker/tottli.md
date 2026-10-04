---
type: app
category: baby-tracker
app: Tottli
member: kushagra
updated: 2026-10-04
status: draft
sources: [screenshots:29]
---
# Tottli — screenshot teardown

Source: `kushagra screenshots/Baby tracker/screenshots/tottli.pdf`, 29 pages. Each page below was visually checked against the rendered source. “Asks” records visible user questions, permissions, profile inputs, or payment choices; it does not estimate taps. A static capture cannot prove that an event was saved, a control was tapped, or a displayed promise works. Prices are displayed in INR (₹); the storefront is not independently verified, and US pricing is unknown. The `updated` date is the analysis date; screenshot capture dates were not verified.

## Per-screen table

| # | What is on screen | Asks of user | Gives before / alongside ask | Lever / friction / copy | Evidence |
|---:|---|---|---|---|---|
| 1 | Sign-in welcome | Apple/Google/email/invite code | “Less time logging. More time with your baby.” | [OBSERVED] Permission, account, or sharing choice is presented; completion is not captured. | [OBSERVED] `tottli.pdf` p.1 |
| 2 | Analytics consent | Allow analytics / Not now | Usage analytics rationale | [OBSERVED] Permission, account, or sharing choice is presented; completion is not captured. | [OBSERVED] `tottli.pdf` p.2 |
| 3 | Recent activity placeholders | No ask visible | Recent list skeleton; category tiles | [OBSERVED] No setup, permission, account, or payment ask is visible on this screen. | [OBSERVED] `tottli.pdf` p.3 |
| 4 | Care stage selection | Select baby here / arriving soon | Stage-specific benefit framing | [OBSERVED] Input or preference options are visible; whether required is UNKNOWN. | [OBSERVED] `tottli.pdf` p.4 |
| 5 | Reminder setup | Turn on notifications / Not now | Feed/diaper reminders based on logs | [OBSERVED] Navigation or continue control is visible; requirement to proceed is UNKNOWN. | [OBSERVED] `tottli.pdf` p.5 |
| 6 | Baby/caregiver profile | Enter name, baby name, birth date | Profile context | [OBSERVED] Input or preference options are visible; whether required is UNKNOWN. | [OBSERVED] `tottli.pdf` p.6 |
| 7 | Challenge selection | Choose hardest part | Sleep/feeding/time-to-next/nap challenge | [OBSERVED] Input or preference options are visible; whether required is UNKNOWN. | [OBSERVED] `tottli.pdf` p.7 |
| 8 | First timeline log | Choose feed/diaper; set time/amount; log feed | Log form offers first useful record | [OBSERVED] Input or preference options are visible; whether required is UNKNOWN. | [OBSERVED] `tottli.pdf` p.8 |
| 9 | Invite co-caregiver | Share invite / copy code | Caregiver access offered | [OBSERVED] Permission, account, or sharing choice is presented; completion is not captured. | [OBSERVED] `tottli.pdf` p.9 |
| 10 | First week checklist | Continue | Timeline ready; suggested setup tasks | [OBSERVED] Navigation or continue control is visible; requirement to proceed is UNKNOWN. | [OBSERVED] `tottli.pdf` p.10 |
| 11 | Premium trial explainer | Try it free | Unlocks and trial/cancel details | [OBSERVED] Paid-tier/trial controls appear here; behavior after selection or close is UNKNOWN. | [OBSERVED] `tottli.pdf` p.11 |
| 12 | Premium carousel: patterns | Swipe | Sleep pattern insight preview | [OBSERVED] Paid-tier/trial controls appear here; behavior after selection or close is UNKNOWN. | [OBSERVED] `tottli.pdf` p.12 |
| 13 | Premium carousel: food journey | Swipe | Food tracking insight preview | [OBSERVED] Paid-tier/trial controls appear here; behavior after selection or close is UNKNOWN. | [OBSERVED] `tottli.pdf` p.13 |
| 14 | Premium carousel: reminders | Swipe | Reminder capability preview | [OBSERVED] Paid-tier/trial controls appear here; behavior after selection or close is UNKNOWN. | [OBSERVED] `tottli.pdf` p.14 |
| 15 | Premium carousel: watch log | Swipe | Watch logging preview | [OBSERVED] Paid-tier/trial controls appear here; behavior after selection or close is UNKNOWN. | [OBSERVED] `tottli.pdf` p.15 |
| 16 | Premium carousel: timeline | Swipe | Time-saving claim | [OBSERVED] Paid-tier/trial controls appear here; behavior after selection or close is UNKNOWN. | [OBSERVED] `tottli.pdf` p.16 |
| 17 | Premium carousel: family | Swipe | Sharing claim | [OBSERVED] Paid-tier/trial controls appear here; behavior after selection or close is UNKNOWN. | [OBSERVED] `tottli.pdf` p.17 |
| 18 | Premium carousel: care notes | Swipe/close | AI-generated summary preview | [OBSERVED] Paid-tier/trial controls appear here; behavior after selection or close is UNKNOWN. | [OBSERVED] `tottli.pdf` p.18 |
| 19 | Timeline empty state | Log a feed | No activity yet; primary action | [OBSERVED] Navigation or continue control is visible; requirement to proceed is UNKNOWN. | [OBSERVED] `tottli.pdf` p.19 |
| 20 | Timeline day view | Select date | Empty feed/food/pump/diaper lists | [OBSERVED] Input or preference options are visible; whether required is UNKNOWN. | [OBSERVED] `tottli.pdf` p.20 |
| 21 | Settings/profile | Manage household/Premium | Profile and tier | [OBSERVED] Navigation or continue control is visible; requirement to proceed is UNKNOWN. | [OBSERVED] `tottli.pdf` p.21 |
| 22 | Restore subscriptions sheet | Restore past purchases/contact support | No subscriptions found | [OBSERVED] Paid-tier/trial controls appear here; behavior after selection or close is UNKNOWN. | [OBSERVED] `tottli.pdf` p.22 |
| 23 | Smart reminders settings | Open reminder options | Smart reminders section | [OBSERVED] Navigation or continue control is visible; requirement to proceed is UNKNOWN. | [OBSERVED] `tottli.pdf` p.23 |
| 24 | Smart stash settings | Open stash | Pumped milk inventory feature | [OBSERVED] Navigation or continue control is visible; requirement to proceed is UNKNOWN. | [OBSERVED] `tottli.pdf` p.24 |
| 25 | Live activities setting | Enable/upgrade | Feature access state | [OBSERVED] Navigation or continue control is visible; requirement to proceed is UNKNOWN. | [OBSERVED] `tottli.pdf` p.25 |
| 26 | Settings lower | Open handoff/milestones/onboarding | Settings options | [OBSERVED] Navigation or continue control is visible; requirement to proceed is UNKNOWN. | [OBSERVED] `tottli.pdf` p.26 |
| 27 | Onboarding settings | Replay setup/open premium setup | Replay option | [OBSERVED] Navigation or continue control is visible; requirement to proceed is UNKNOWN. | [OBSERVED] `tottli.pdf` p.27 |
| 28 | Privacy/account | Toggle analytics/open policy/delete | Privacy controls; destructive deletion warning | [OBSERVED] Input or preference options are visible; whether required is UNKNOWN. | [OBSERVED] `tottli.pdf` p.28 |
| 29 | Privacy details/data export | Open transfer | Import/export option | [OBSERVED] Navigation or continue control is visible; requirement to proceed is UNKNOWN. | [OBSERVED] `tottli.pdf` p.29 |

## Eight dimensions

1. **First win:** First recorded feed form is presented at p.8, where user selects category, time and amount; that screen offers “Log feed.” A saved confirmation is not in the captured set.
2. **Ask ledger:** Analytics consent p.2, child stage p.4, reminder permission p.5, baby/caregiver details p.6, challenge choice p.7, caregiver invite p.9, then trial p.11 [OBSERVED].
3. **Abstractions:** The onboarding uses a staged “who are we setting up for,” timeline, smart stash, handoff and Premium concepts [OBSERVED pp.4-19,22-29].
4. **Feel-good moments:** The first-week checklist and empty timeline [OBSERVED pp.10,20] orient the user; no saved event or feedback shown.
5. **Feel-bad moments:** Account ask before dashboard? No account form is visible in these pages. Setup still collects several preferences before the first feed form [OBSERVED pp.4-8].
6. **Paywall:** Trial education carousel starts p.11; plans/prices are not visible in these screenshots. Trial payment terms/prices [UNKNOWN].
7. **Repeat cost:** Feed card opens time/amount logger with one prominent “Log feed” CTA (p.8); exact saving flow UNKNOWN.
8. **Feature map:** Must match: simple feed/sleep/diaper records. Differentiator: smart stash/care handoff. Bloat: multiple carousel concepts before a first event [INFERRED].

## Keep / Kill / Different

- **Keep:** Keep the feed log p.8 and checklist p.10; both communicate a concrete next action.
- **Kill:** Kill: trial carousel before a saved-feed confirmation (pp.11 onward); this capture does not establish whether the p.8 log can be saved without starting a trial. Keep caregiver sharing optional.
- **Different:** let the user save the p.8 log first; introduce premium features one at a time when relevant.

## Limits

These are screenshot observations, not a live usability test. Tap count/time-to-value, conditional branches, saved-state confirmation unless captured, purchase success, reminder delivery, sync behavior, and free access after closing a paywall are UNKNOWN. Any recommendation above is tagged as inference.
