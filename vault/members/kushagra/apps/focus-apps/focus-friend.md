---
type: app
category: focus-apps
app: Focus Friend
member: kushagra
updated: 2026-10-04
status: draft
sources: [screenshots:28]
---

# Focus Friend — screens-only teardown

Source: `kushagra screenshots/Focus_Apps/screenshots/focusfriendapp.pdf` (28 pages). This is a highly illustrated narrative and focus-timer experience; Pro prices are displayed in ₹, with storefront context unverified.

## Screen map

| Pages | Stage / what user sees | Asks and copy | Friction / evidence |
|---|---|---|---|
| 1–2 | iOS notification prompt, then title “Focus Friend / Timer for work & study” and “Meet your bean.” | Allow/Don’t Allow notification; “MEET YOUR BEAN.” | Push prompt is first capture, before stated focus benefit; no explanation beyond iOS default. [OBSERVED] |
| 3–8 | Bean greets user, asks name, tells comic story: cosmic ray zapped a bean; user ate the bean; asks “A BEAN?” | Name the bean, tap story dialogue/Next. | Narrative engagement precedes timer. Naming character is optional only if app supports skipping; screenshots don’t show a skip. [OBSERVED] |
| 9–15 | Bean knits; tells user that picking up the phone makes it drop stitches; longer focus completes a scarf, which can decorate a room; subscribe to Focus Friend Pro for cooler decorations. | Continue through story; premium pitch is tied to cosmetics. | Story explains distraction trade-off in character voice; introduces Pro before visible first timer. [OBSERVED] |
| 16–18 | Room with FOCUS button; timer default 15:00, Deep Focus Mode toggle, 3x socks optional; running screen shows Cancel (8) and time 14:58. | Start session; optional deep-focus mode. | Timer is actionable and cancellation is explicit. The displayed value is not independently measured elapsed time. [OBSERVED] |
| 19–20 | Room/world preview; Focus Stats card (“Summary / last 28 days”) shows zero total minutes and zero sessions. | Inspect world and stats. | No completed session in those stats. [OBSERVED] |
| 21 | Shop: Focus Friend Pro; “Longer sessions / focus up to 6 hours in a row,” earn scarves, 3x socks optional, allow list for selected apps in deep focus. Plans: ₹399/month, ₹1,999/year (₹166.58/month, 58% off), ₹3,999 lifetime; Continue. | Select plan. | Paid affordances; X close at bottom and Restore Purchases. ₹ is displayed; storefront is not independently verified. [OBSERVED] |
| 22–25 | Shop tabs for Beans and Outfits; item prices in beans; decorate room; bean editor; settings panels for deep focus and notifications, backup/import. | Spend earned currency/customize; adjust settings. | Lots of customization after core session. [OBSERVED] |
| 26–28 | Basic login, then announcement/settings and Daily check-in panel with current/best streak 0 days and milestones. | Username/password; check in. | Account path appears in settings, separate from timer; Daily check-in is an additional streak mechanism. [OBSERVED] |

## Eight lens dimensions

1. **First win:** Timer screen provides a first clear focus action (p.16–18); no successful session is visible in stats (p.20), which show 0 minutes and 0 sessions. Exact taps/outcome are [UNKNOWN].
2. **Ask ledger:** notification prompt (p.1), story and bean naming (p.3–15), Pro narrative/purchase exposure (p.15, shop p.21), session setup (p.17), account credentials in settings (p.26), streak check-in p.28. The precise path is not proven; timer is accessible in the supplied captures without a signup form.
3. **Abstractions:** bean narrative, room decorations, knitting/scarf, beans and socks currencies/rewards, Pro, deep-focus allow list, daily check-in/streaks (p.3–28). Character and scarf map directly to focus duration; separate currency/store/streak systems add concepts. [INFERRED]
4. **Feel-good:** A cute focus companion and tangible knitted scarf reflect time spent (p.9–15). The bean introduction “A BEAN? I like it!” (p.6) develops the character before the timer; it is not a session reward. [OBSERVED]
5. **Feel-bad:** Notification request comes first (p.1); the bean says work “unravels” when user returns to phone (p.11–12), which could evoke guilt. The timer explicitly exposes cancellation (p.18) and no miss/broken-streak guilt is visible in the selected screenshots.
6. **Paywall:** Focus Friend Pro shop (p.21) lists ₹399/month, ₹1,999/year, ₹3,999 lifetime; no trial copy on this screen. Close and Restore are visible. The paywall is tied to longer sessions, cosmetics and app allow list; whether features are gated elsewhere is [UNKNOWN]. US price is [UNKNOWN]; storefront is not independently verified.
7. **Repeat cost:** Exact taps unknown. Timer defaults to 15 minutes and Start is visible (p.17). The visible completion reward (p.6) shows 30 study minutes, which is a different captured state; don’t assume exact default/completion consistency. Return hooks include room customization, daily check-in, rewards and focus stats (p.20–28).
8. **Feature map:** Table stakes: focus timer, session stop, session totals. Differentiator: character-driven distraction story and room/scarf artifact; intentional cancel and optional app allow list (p.9–18, p.21). Bloat risk: several currencies/customization screens, separate check-in/streak and early notification ask. [INFERRED]

## Keep / Kill / Different

- **Keep:** Story makes distraction consequences legible in the bean’s own terms (p.11–15); timer offers clear Start/Cancel and optional blocking (p.17–18). The p.6 bean introduction gives the character a memorable voice before the timer.
- **Kill:** Do not ask for notifications before explaining their value (p.1). Avoid guilt copy around lost stitches (p.11–12) as a daily penalty; do not introduce store currencies before first focus.
- **Different:** Put a no-account, no-notification timer up front, then let users opt into the bean story/rewards. Celebrate attended focus time without implying that leaving the app or missing a day harmed the companion. [INFERRED]

## Verification and unknowns

Reviewed all 28 pages; enlarged timer, shop, and settings captures. Confirmed 15:00 timer setup, p.21 ₹ plan amounts (storefront unverified), and that p.6 is the bean introduction. Study Bunny’s separate `studybunny.pdf` p.6 contains the “Great Work! 30 study mins +3” screen; it does not belong to this app. US prices, paid gating, live reward behavior, exact taps, and session success are [UNKNOWN].
