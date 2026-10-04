---
type: app
category: baby-tracker
app: Pebbi
member: kushagra
updated: 2026-10-04
status: draft
sources: [screenshots:30]
---
# Pebbi — screenshot teardown

Source: `kushagra screenshots/Baby tracker/screenshots/pebbi_app.pdf`, 30 pages. Each page below was visually checked against the rendered source. “Asks” records visible user questions, permissions, profile inputs, or payment choices; it does not estimate taps. A static capture cannot prove that an event was saved, a control was tapped, or a displayed promise works. Pricing with ₹ is the India storefront.

## Per-screen table

| # | What is on screen | Asks of user | Gives before / alongside ask | Lever / friction / copy | Evidence |
|---:|---|---|---|---|---|
| 1 | Welcome | Start logging / set preferences | Simple private shared timeline claim | [OBSERVED] Navigation or continue control is visible; requirement to proceed is UNKNOWN. | [OBSERVED] `pebbi_app.pdf` p.1 |
| 2 | Add baby | Name, DOB/time, sex, preterm | Profile data form | [OBSERVED] Input or preference options are visible; whether required is UNKNOWN. | [OBSERVED] `pebbi_app.pdf` p.2 |
| 3 | Profile complete | Start Tracking + | Personal birth facts and profile celebration | [OBSERVED] Navigation or continue control is visible; requirement to proceed is UNKNOWN. | [OBSERVED] `pebbi_app.pdf` p.3 |
| 4 | Dashboard intro | Skip / Got it | Dashboard explained | [OBSERVED] Navigation or continue control is visible; requirement to proceed is UNKNOWN. | [OBSERVED] `pebbi_app.pdf` p.4 |
| 5 | Sync intro | Skip / Got it | Household sharing explained | [OBSERVED] Navigation or continue control is visible; requirement to proceed is UNKNOWN. | [OBSERVED] `pebbi_app.pdf` p.5 |
| 6 | Insights intro | Skip / Got it | Patterns/routine / missed events explanation | [OBSERVED] Navigation or continue control is visible; requirement to proceed is UNKNOWN. | [OBSERVED] `pebbi_app.pdf` p.6 |
| 7 | Alarms intro | Skip / Got it | Reminders explained | [OBSERVED] Navigation or continue control is visible; requirement to proceed is UNKNOWN. | [OBSERVED] `pebbi_app.pdf` p.7 |
| 8 | More intro | Skip / Got it | Data export/settings/FAQ options | [OBSERVED] Navigation or continue control is visible; requirement to proceed is UNKNOWN. | [OBSERVED] `pebbi_app.pdf` p.8 |
| 9 | Timeline intro | Skip / Got it | Events organized by day/week | [OBSERVED] Navigation or continue control is visible; requirement to proceed is UNKNOWN. | [OBSERVED] `pebbi_app.pdf` p.9 |
| 10 | Overview intro | Skip / Got it | Daily overview widget explained | [OBSERVED] Navigation or continue control is visible; requirement to proceed is UNKNOWN. | [OBSERVED] `pebbi_app.pdf` p.10 |
| 11 | Event card intro | Skip / Got it | Growth/medication add entry explained | [OBSERVED] Navigation or continue control is visible; requirement to proceed is UNKNOWN. | [OBSERVED] `pebbi_app.pdf` p.11 |
| 12 | Finish tour | Skip / Got it | Tour completion | [OBSERVED] Navigation or continue control is visible; requirement to proceed is UNKNOWN. | [OBSERVED] `pebbi_app.pdf` p.12 |
| 13 | Choose events | Select feeds/sleep/happy/growth/milestone/medication/symptoms/activity | Tracking options | [OBSERVED] Input or preference options are visible; whether required is UNKNOWN. | [OBSERVED] `pebbi_app.pdf` p.13 |
| 14 | Dashboard | Let’s go / skip for now | Ready to begin; no log yet | [OBSERVED] Navigation or continue control is visible; requirement to proceed is UNKNOWN. | [OBSERVED] `pebbi_app.pdf` p.14 |
| 15 | Dashboard cards | Add event | Empty feed/sleep card; Premium prediction prompt | [OBSERVED] Navigation or continue control is visible; requirement to proceed is UNKNOWN. | [OBSERVED] `pebbi_app.pdf` p.15 |
| 16 | Dashboard lower widgets | Add growth/milestone | Growth/milestone counters at zero | [OBSERVED] Navigation or continue control is visible; requirement to proceed is UNKNOWN. | [OBSERVED] `pebbi_app.pdf` p.16 |
| 17 | Sync and households | Set device name/create/join household | Data-sync explanation | [OBSERVED] Permission, account, or sharing choice is presented; completion is not captured. | [OBSERVED] `pebbi_app.pdf` p.17 |
| 18 | Insights empty state | No action visible | Not enough history yet | [OBSERVED] No setup, permission, account, or payment ask is visible on this screen. | [OBSERVED] `pebbi_app.pdf` p.18 |
| 19 | Reminders disabled | Enable notifications | Permission required for alerts | [OBSERVED] Permission, account, or sharing choice is presented; completion is not captured. | [OBSERVED] `pebbi_app.pdf` p.19 |
| 20 | Options menu | Choose settings/sync/insights/export/help | Navigation list | [OBSERVED] Input or preference options are visible; whether required is UNKNOWN. | [OBSERVED] `pebbi_app.pdf` p.20 |
| 21 | Options lower | Choose menu item | Settings and account options | [OBSERVED] Input or preference options are visible; whether required is UNKNOWN. | [OBSERVED] `pebbi_app.pdf` p.21 |
| 22 | Add new data sheet | Choose feeding/sleep/nappy/growth | Quick entry picker | [OBSERVED] Input or preference options are visible; whether required is UNKNOWN. | [OBSERVED] `pebbi_app.pdf` p.22 |
| 23 | Timeline | Choose day/week/list | Empty day timeline | [OBSERVED] Input or preference options are visible; whether required is UNKNOWN. | [OBSERVED] `pebbi_app.pdf` p.23 |
| 24 | Go Premium | Upgrade to Premium | Premium benefit list, no price on this page | [OBSERVED] Paid-tier/trial controls appear here; behavior after selection or close is UNKNOWN. | [OBSERVED] `pebbi_app.pdf` p.24 |
| 25 | Premium feature detail | Scroll/upgrade | Long-term check-ins and household sharing | [OBSERVED] Paid-tier/trial controls appear here; behavior after selection or close is UNKNOWN. | [OBSERVED] `pebbi_app.pdf` p.25 |
| 26 | Premium feature detail | Scroll/upgrade | Milestones/symptom photos/PDF export | [OBSERVED] Paid-tier/trial controls appear here; behavior after selection or close is UNKNOWN. | [OBSERVED] `pebbi_app.pdf` p.26 |
| 27 | Premium feature detail | Upgrade to Premium | Feature summary and restore purchases | [OBSERVED] Paid-tier/trial controls appear here; behavior after selection or close is UNKNOWN. | [OBSERVED] `pebbi_app.pdf` p.27 |
| 28 | Choose a plan | Choose monthly/annual/lifetime | Trial and renewal terms; see following screens | [OBSERVED] Input or preference options are visible; whether required is UNKNOWN. | [OBSERVED] `pebbi_app.pdf` p.28 |
| 29 | Annual choice | Choose plan | 14-day trial then ₹1,999/year | [OBSERVED] Input or preference options are visible; whether required is UNKNOWN. | [OBSERVED] `pebbi_app.pdf` p.29 |
| 30 | Lifetime choice | Choose plan / enter promo | ₹5,900 lifetime; promo code | [OBSERVED] Input or preference options are visible; whether required is UNKNOWN. | [OBSERVED] `pebbi_app.pdf` p.30 |

## Eight dimensions

1. **First win:** Dashboard “ready to track” after profile/tour (pp.3-14); no first event shown.
2. **Ask ledger:** Profile fields and multi-screen tour; event selection; later sync/notification permissions (pp.2-19) [OBSERVED].
3. **Abstractions:** Sync & Households, Insights, alarms, predictions, AI summaries, long-term check-ins [OBSERVED pp.4-19,24-27].
4. **Feel-good moments:** Profile completion screen “All Set!” and onboarding tour descriptions [OBSERVED pp.3-12]; no recorded event.
5. **Feel-bad moments:** 10 successive tour screens each ask Skip/Got it [OBSERVED pp.4-12]; cost is tutorial repetition [INFERRED].
6. **Paywall:** Premium from dashboard cards p.15 and full-screen paywall pp.24-30; prices/trial clear in plan chooser; close X visible on p.24.
7. **Repeat cost:** Add Event button and Add New Data sheet (pp.4,22); taps unknown.
8. **Feature map:** Must match: family sync, timeline, multiple record types. Differentiator: visible empty-state Insights status (“Not enough history yet”, p.18). Bloat: predictive/AI features before data exists [INFERRED].

## Keep / Kill / Different

- **Keep:** Keep honest “Not enough history yet” state and skippable tour (pp.4-12).
- **Kill:** Kill: predictive upsell from empty data (p.15) and repetitive tour prompts.
- **Different:** limit tour to one optional card; offer insight upgrade only after meaningful history has accumulated.

## Limits

These are screenshot observations, not a live usability test. Tap count/time-to-value, conditional branches, saved-state confirmation unless captured, purchase success, reminder delivery, sync behavior, and free access after closing a paywall are UNKNOWN. Any recommendation above is tagged as inference.
