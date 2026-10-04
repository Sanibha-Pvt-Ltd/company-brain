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

Source: `kushagra screenshots/Baby tracker/screenshots/babytrackerbynighp.pdf`, 14 pages. Each page below was visually checked against the rendered source. “Asks” records visible user questions, permissions, profile inputs, or payment choices; it does not estimate taps. A static capture cannot prove that an event was saved, a control was tapped, or a displayed promise works. Prices are displayed in INR (₹); the storefront is not independently verified, and US pricing is unknown. The `updated` date is the analysis date; screenshot capture dates were not verified.

## Per-screen table

| # | What is on screen | Asks of user | Gives before / alongside ask | Lever / friction / copy | Evidence |
|---:|---|---|---|---|---|
| 1 | Baby info form | Name, gender, birth date/time, due date | No value beyond profile setup | [OBSERVED] Input or preference options are visible; whether required is UNKNOWN. | [OBSERVED] `babytrackerbynighp.pdf` p.1 |
| 2 | Home dashboard | Tap Feeding/Nappy change/Sleep/Pumping/Other | Categories available; greeting/personalized baby header | [OBSERVED] Navigation or continue control is visible; requirement to proceed is UNKNOWN. | [OBSERVED] `babytrackerbynighp.pdf` p.2 |
| 3 | Expanded Feed choices | Nursing, expressed, formula, supplement | Feed subtypes shown | [OBSERVED] Navigation or continue control is visible; requirement to proceed is UNKNOWN. | [OBSERVED] `babytrackerbynighp.pdf` p.3 |
| 4 | Feeding log form | Time, amount, note; save/checkmark | 100 ml amount control | [OBSERVED] Navigation or continue control is visible; requirement to proceed is UNKNOWN. | [OBSERVED] `babytrackerbynighp.pdf` p.4 |
| 5 | Supplement log form | Supplement, amount, unit, note | Entry fields available | [OBSERVED] Navigation or continue control is visible; requirement to proceed is UNKNOWN. | [OBSERVED] `babytrackerbynighp.pdf` p.5 |
| 6 | Today list | Choose date/category | No events visible | [OBSERVED] Input or preference options are visible; whether required is UNKNOWN. | [OBSERVED] `babytrackerbynighp.pdf` p.6 |
| 7 | Weekly charts | Choose week/category | Chart templates, zeros/no records | [OBSERVED] Input or preference options are visible; whether required is UNKNOWN. | [OBSERVED] `babytrackerbynighp.pdf` p.7 |
| 8 | Empty state | No action visible | No information available | [OBSERVED] No setup, permission, account, or payment ask is visible on this screen. | [OBSERVED] `babytrackerbynighp.pdf` p.8 |
| 9 | Settings list | Choose data backup/sync/export/photo copy | Export and backup controls | [OBSERVED] Input or preference options are visible; whether required is UNKNOWN. | [OBSERVED] `babytrackerbynighp.pdf` p.9 |
| 10 | Settings support | FAQ, rate/share/about | Support options | [OBSERVED] Navigation or continue control is visible; requirement to proceed is UNKNOWN. | [OBSERVED] `babytrackerbynighp.pdf` p.10 |
| 11 | Settings continuation | Explore Plus/remove ads | Plus and ads route | [OBSERVED] Navigation or continue control is visible; requirement to proceed is UNKNOWN. | [OBSERVED] `babytrackerbynighp.pdf` p.11 |
| 12 | Plus paywall | Subscribe to Plus; select annual/monthly | Sleep tracking, alerts, ad-free benefits and INR prices | [OBSERVED] Paid-tier/trial controls appear here; behavior after selection or close is UNKNOWN. | [OBSERVED] `babytrackerbynighp.pdf` p.12 |
| 13 | Remove ads offer | Remove Ads one-time purchase | ₹499 one-off; no ads promise | [OBSERVED] Navigation or continue control is visible; requirement to proceed is UNKNOWN. | [OBSERVED] `babytrackerbynighp.pdf` p.13 |
| 14 | Baby info card | Edit profile/add another | Current child record shown | [OBSERVED] Navigation or continue control is visible; requirement to proceed is UNKNOWN. | [OBSERVED] `babytrackerbynighp.pdf` p.14 |

## Eight dimensions

1. **First win:** Baby profile p.1 then dashboard category cards p.2; screenshots do not show a completed saved event.
2. **Ask ledger:** Name/gender/dates on p.1. Later subscription is reached in settings (pp.9-13); no account/notification ask visible.
3. **Abstractions:** Feed subtype list and broad event types (pp.2-5); plus and ad removal are distinct paid concepts (pp.12-13).
4. **Feel-good moments:** Baby profile card and color-coded category dashboard [OBSERVED pp.1-3]; no event completion.
5. **Feel-bad moments:** Blank charts/empty state (pp.6-8) may feel unrewarding before any data; [INFERRED].
6. **Paywall:** Plus plans appear from settings (p.12), and ₹499 Remove Ads offer (p.13). No upfront wall is shown.
7. **Repeat cost:** Select a category, fill fields, save (pp.2-5); exact repeat taps unknown.
8. **Feature map:** Must match: timer/amount/nursing events. Differentiator: export/backup and one-time ad removal. Bloat: many categories/settings can overwhelm [INFERRED].

## Keep / Kill / Different

- **Keep:** Keep fast category cards and simple amount entry (pp.2-5).
- **Kill:** Kill: blank charts presented without guidance (pp.6-8) and any forced paywall; none shown at launch.
- **Different:** show a proposed “first event saved” confirmation and show a useful same-day timeline; keep subscription under settings.

## Limits

These are screenshot observations, not a live usability test. Tap count/time-to-value, conditional branches, saved-state confirmation unless captured, purchase success, reminder delivery, sync behavior, and free access after closing a paywall are UNKNOWN. Any recommendation above is tagged as inference.
