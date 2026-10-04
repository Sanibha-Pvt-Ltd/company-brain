---
type: app
category: baby-tracker
app: Baby Tracker by Nighp
member: kushagra
updated: 2026-10-04
status: draft
sources: [screenshots:14]
---
# Baby Tracker by Nighp — screenshot teardown

Source: `kushagra screenshots/Baby tracker/screenshots/babytrackerbynighp.pdf`, 14 pages. Each page below was visually checked against the rendered source. “Asks” records visible user questions, permissions, profile inputs, or payment choices; it does not estimate taps. A static capture cannot prove that an event was saved, a control was tapped, or a displayed promise works. Pricing with ₹ is the India storefront.

## Per-screen table

| # | What is on screen | Asks of user | Gives before / alongside ask | Lever / friction / copy | Evidence |
|---:|---|---|---|---|---|
| 1 | Baby info form | Name, gender, birth date/time, due date | No value beyond profile setup | [OBSERVED] Input or preference choice requested; whether it is mandatory is UNKNOWN. | [OBSERVED] `babytrackerbynighp.pdf` p.1 |
| 2 | Home dashboard | Tap Feeding/Nappy change/Sleep/Pumping/Other | Categories available; greeting/personalized baby header | [OBSERVED] Navigation or continue choice is visible; requirement to proceed is UNKNOWN. | [OBSERVED] `babytrackerbynighp.pdf` p.2 |
| 3 | Expanded Feed choices | Nursing, expressed, formula, supplement | Feed subtypes shown | [OBSERVED] Navigation or continue choice is visible; requirement to proceed is UNKNOWN. | [OBSERVED] `babytrackerbynighp.pdf` p.3 |
| 4 | Feeding log form | Time, amount, note; save/checkmark | 100 ml amount control | [OBSERVED] Navigation or continue choice is visible; requirement to proceed is UNKNOWN. | [OBSERVED] `babytrackerbynighp.pdf` p.4 |
| 5 | Supplement log form | Supplement, amount, unit, note | Entry fields available | [OBSERVED] Navigation or continue choice is visible; requirement to proceed is UNKNOWN. | [OBSERVED] `babytrackerbynighp.pdf` p.5 |
| 6 | Today list | Choose date/category | No events visible | [OBSERVED] Input or preference choice requested; whether it is mandatory is UNKNOWN. | [OBSERVED] `babytrackerbynighp.pdf` p.6 |
| 7 | Weekly charts | Choose week/category | Chart templates, zeros/no records | [OBSERVED] Input or preference choice requested; whether it is mandatory is UNKNOWN. | [OBSERVED] `babytrackerbynighp.pdf` p.7 |
| 8 | Empty state | No action visible | No information available | [OBSERVED] No direct data/permission/payment ask is apparent on this captured screen. | [OBSERVED] `babytrackerbynighp.pdf` p.8 |
| 9 | Settings list | Choose data backup/sync/export/photo copy | Export and backup controls | [OBSERVED] Input or preference choice requested; whether it is mandatory is UNKNOWN. | [OBSERVED] `babytrackerbynighp.pdf` p.9 |
| 10 | Settings support | FAQ, rate/share/about | Support options | [OBSERVED] Navigation or continue choice is visible; requirement to proceed is UNKNOWN. | [OBSERVED] `babytrackerbynighp.pdf` p.10 |
| 11 | Settings continuation | Explore Plus/remove ads | Plus and ads route | [OBSERVED] Navigation or continue choice is visible; requirement to proceed is UNKNOWN. | [OBSERVED] `babytrackerbynighp.pdf` p.11 |
| 12 | Plus paywall | Subscribe to Plus; select annual/monthly | Sleep tracking, alerts, ad-free benefits and INR prices | [OBSERVED] Paid tier/trial control is on this page; visibility of dismiss/close is noted only when shown. | [OBSERVED] `babytrackerbynighp.pdf` p.12 |
| 13 | Remove ads offer | Remove Ads one-time purchase | ₹499 one-off; no ads promise | [OBSERVED] Navigation or continue choice is visible; requirement to proceed is UNKNOWN. | [OBSERVED] `babytrackerbynighp.pdf` p.13 |
| 14 | Baby info card | Edit profile/add another | Current child record shown | [OBSERVED] Navigation or continue choice is visible; requirement to proceed is UNKNOWN. | [OBSERVED] `babytrackerbynighp.pdf` p.14 |

## Eight dimensions

1. **First win:** Baby profile p.1 then dashboard category cards p.2; screenshots do not show a completed saved event.
2. **Ask ledger:** {lens[1]}
3. **Abstractions:** {lens[2]}
4. **Feel-good moments:** {lens[3]}
5. **Feel-bad moments:** {lens[4]}
6. **Paywall:** {lens[5]}
7. **Repeat cost:** {lens[6]}
8. **Feature map:** {lens[7]}

## Keep / Kill / Different

- **Keep:** Keep fast category cards and simple amount entry (pp.2-5).
- **Kill:** Kill: blank charts presented without guidance (pp.6-8) and any forced paywall; none shown at launch.
- **Different:** show a proposed “first event saved” confirmation and show a useful same-day timeline; keep subscription under settings.

## Limits

These are screenshot observations, not a live usability test. Tap count/time-to-value, conditional branches, saved-state confirmation unless captured, purchase success, reminder delivery, sync behavior, and free access after closing a paywall are UNKNOWN. Any recommendation above is tagged as inference.
