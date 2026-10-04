---
type: app
category: focus-apps
app: Study Bunny
member: kushagra
updated: 2026-10-04
status: draft
sources: [screenshots:28]
---

# Study Bunny — screens-only teardown

Source: `kushagra screenshots/Focus_Apps/screenshots/studybunny.pdf` (28 pages). The set includes a tutorial, timer/reward page, shop and settings; Google Gemini banner ads appear beneath several screens.

## Screen map

| Pages | Stage / what user sees | Asks and value | Friction / evidence |
|---|---|---|---|
| 1–5 | Notification prompt; bunny home with “Meet your Study Bunny!”; tracking prompt asks user to allow tracking to keep app free/personalize ads; menu tutorial; 30-minute countdown selected. | Allow push; allow tracking; Start. | Two permissions precede any focus reward, though tutorial navigation provides explanation. [OBSERVED] |
| 6–8 | “Great Work!” reward: “30 study mins +3,” pause minutes 0; double coin with video ad; “Limit 10 bonus coins per day / You redeemed 0/10 today”; bunny home has 3 coins; store. | Optional rewarded ad to double currency; return home; spend coins. | Focus is counted in study minutes; reward and daily ad cap are explicit. [OBSERVED] |
| 9–15 | Announcements, language chooser, promo, limited edition item, “Name your bunny?”, Happy Meter explanation, blank timer/chart screen. | Optional product/language and pet naming. | Announcement/promo dialogs take attention from study; “Happy Meter” adds emotional score mechanic. [OBSERVED] |
| 16–20 | Monthly daily-study-hours calendar; optional carry-over prompt; To Do panel; flashcards; music list. | Create tasks/cards or choose music. | Useful study support is secondary to timer; screenshots don’t show a task being completed. [OBSERVED] |
| 21–25 | Announcements; Basic Login and Premium Login forms; settings with Bunny Name, Happy Meter, Challenge Mode, Power Save, Honesty Mode; ad rewards; daily check-in panel. | Optional account login, mode toggles and check-in. | Account surfaces exist after focus screens; honesty mode, challenge mode, and daily streak are extra rules. [OBSERVED] |
| 26 | In-app purchases list: 1 gold crown $0.99 USD; currency packs $1.99, $4.99, $14.99, $19.99, $69.99 USD. Crown text says 30 days of No Ads, Offline Use, and Wearable Crown. | Buy currency/crown. | Currency bundle and multi-benefit unlock require interpretation. USD is shown in the supplied screen. [OBSERVED] |
| 27–28 | Study Tips videos; Daily check-in with current/best streak 0 days and milestones. | Watch videos / check in. | Study-tip external video and streak surface add optional modules. [OBSERVED] |

## Eight lens dimensions

1. **First win:** The timer is configured at 30 minutes on p.5; completion-style “Great Work!” screen says “30 study mins +3” on p.6. The screenshots show these states, but do not verify they are the same real session or that focus occurred. Exact taps/outcome are [UNKNOWN].
2. **Ask ledger:** notification request (p.1); tutorial and tracking prompt (p.2–5); timer setup (p.5); reward/ad choice (p.6); optional name, account and check-in later (p.13, p.22–25, p.28). Pages do not establish the mandatory sequence. No payment ask is visible before the first timer screenshots.
3. **Abstractions:** Study minutes, coins, carrots, ad doubling, 10-per-day reward limit, store skins, gold crown, Happy Meter, streaks, flashcards, challenges and honesty mode (p.6–28). Minutes map directly to study; coins/carrots/stores and multiple modes are extra. [INFERRED]
4. **Feel-good:** “Great Work!” awards coins based on displayed study minutes (p.6); bunny/room decoration can reflect earned play (p.7–8, p.24–25). This is a concrete game reward, but the static screenshot cannot validate it was earned.
5. **Feel-bad:** Notification permission first (p.1); tracking explainer says “Please allow tracking to keep the app free” and references personalized ads (p.3). “Honesty Mode” and streak count (p.24, p.28) could shame users if focused on cheating/misses; exact behavior is not shown. No hidden-close paywall is evident.
6. **Paywall:** No full-screen subscription wall in this set. One-time in-app purchase list (p.26) prices USD $0.99 crown, $1.99/$4.99/$14.99/$19.99/$69.99 currency/item bundles. The capture itself labels USD. No recurring plan or trial displayed.
7. **Repeat cost:** Exact taps unknown. Home exposes countdown, menu, and start (p.4–5); completion-style reward returns to home (p.6–7). Return hooks include daily study log, room, daily check-in, progress history and bonus ads (p.8, p.16–17, p.28). Need a live repeated session to measure.
8. **Feature map:** Table stakes: configurable focus countdown, study-time record, break/pause adjustment. Differentiators: low-friction timer, hand-drawn bunny, reward tied to study minutes, task list/flashcards (p.5–6, p.18–20). Bloat/cost: permission-first, dual soft currency, daily reward cap, streak/happiness meters, promos and external ad banner modules (p.1–3, p.6, p.9–15, p.21–28). [INFERRED]

## Keep / Kill / Different

- **Keep:** Simple countdown; show elapsed study and pause minutes separately (p.5–6); reward ad is optional and the daily limit is visible (p.6); daily-hours history may help show consistency (p.16–17).
- **Kill:** Don’t request notifications before a user has a study schedule (p.1); avoid making app access feel conditional on ad tracking (p.3). Keep honesty/challenge modes away from the core session unless users seek them.
- **Different:** Offer the timer immediately with an optional reminder after the first focus. Reward elapsed effort without requiring currency conversion; clearly label any ad multiplier and keep the non-ad reward intact. [INFERRED]

## Verification and unknowns

Reviewed all 28 pages; enlarged p.5–8 and p.26. Confirmed the 30-minute timer selection, reward screen text, 10-bonus-coin limit, and USD one-time purchase amounts. Actual timer completion, ad exposure, purchase eligibility, repeat taps, and US availability remain [UNKNOWN].
