---
type: app
category: habit-tracker
app: "Habit Tracker (Inner Grow)"
app_store_id: 1438388363
member: ganesh
run_by: harshil
updated: 2026-10-04
status: draft
scope: screens-only
screens_analysed: 20
reviews_analysed: 0
sources: [screenshots:20, ganesh-benchmark-xlsx, itunes-lookup-us]
---

# Habit Tracker (Inner Grow Limited)

Screens: `ganesh_screenshots/Habit Trackers/Habit Tracker/` IMG_2052–2071 (20 files, contiguous). India storefront, captured on 2026-10-03 `[INFERRED: the home calendar highlights Sa 3]`. The journey ends on an empty home screen, so **no habit creation or check-in was captured**. Context: [[members/ganesh/drafts/habit-tracker/screens-synthesis]]

## A1 Snapshot (short)

| Field | Value |
|---|---|
| Developer | Inner Grow Limited `[DATA:itunes-lookup-us 2026-10-04]` |
| US price | Free with IAP `[DATA:itunes-lookup-us]` |
| US rating | 4.79 from 147,537 ratings `[DATA:itunes-lookup-us 2026-10-04]` |
| Version | 2.14.23, released 2026-08-15. First release 2019-01-31. Genre Productivity `[DATA:itunes-lookup-us]` |
| Last notes | "add shortcut supports / add custom repeat interval / fix bugs" `[DATA:itunes-lookup-us]` |
| Lead promise | splash "More Happier" `[OBSERVED #1]`, then "Record small steps of progress and cultivate good habits" `[OBSERVED #2]` |

## A2 Business performance
Not in this run (screens-only).

## A3 Monetization (from screens)

- **Plans (India storefront):** "Lifetime, Best Deal, One-Time payment, unlock pro forever ₹999 ~~₹2,497.5~~" and "Annual, Popular, 3 Days Free Trial, no paym[ent…] Only ₹49.92/month ₹599 ~~₹1,497.5~~" `[OBSERVED #17]`. The US price is `[UNKNOWN]`.
- **Placement:** after the quiz, the "I promise" screen and a reviews screen, and before home. It is dismissible with a ✕ top-left `[OBSERVED #17]`.
- **Default:** the Lifetime tile has the highlighted pink border `[OBSERVED]`.
- **Downsell:** closing leads to "Limited-Time Offer ✨ 70% OFF", a **countdown 23:59:58** and "Only ₹799 ~~₹2,663.33~~ One-Time Purchase", with "Claim Offer" and a faint "Discard" `[OBSERVED #18]`. The struck ₹2,663.33 matches nothing on the previous screen (lifetime was ₹999 struck from ₹2,497.5); it is exactly ₹799 ÷ 0.30, i.e. back-calculated from the "70% OFF" claim. The #17 anchors are likewise exactly price ÷ 0.4 (999 ÷ 0.4 = 2,497.5; 599 ÷ 0.4 = 1,497.5). The anchors look derived, not real former prices `[INFERRED]`.
- **Pressure copy:** "Limited-time offer, price rising soon." `[OBSERVED #17]`.
- **Paid features shown:** "Unlimited habits / Quit Habit / Habit reminders" (list continues below the fold) `[OBSERVED #17]`. Reminders behind the paywall is notable for a habit app.
- **Disagreement with Ganesh's xlsx:** the xlsx says "₹1,499/yr or ₹1,999 Lifetime", "5 onboarding screens" and "Gentle Flow" `[DATA:ganesh-benchmark-xlsx]`. The screens show ₹599/yr and ₹999 lifetime, a ₹799 timed downsell, and **19 screens before home** (16 before the paywall). "Gentle" does not fit a countdown downsell. Ganesh, please correct the row. Prices may have changed since the xlsx was made.

## A4 Acquisition
Not in this run (screens-only).

## A5 Screens lens

### Per-screen table (capture order = journey order; no gaps)

| # | file | stage | what user sees | asks of user | gives to user | verbatim copy | lever | friction / dark pattern | tag |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 2052 | first-launch | splash | — | — | "More Happier" | — | — | [OBSERVED] |
| 2 | 2053 | onboarding | product mock: colourful habit list with streak counts | Continue | preview | "Record small steps of progress and cultivate good habits" | aspiration | — | [OBSERVED] |
| 3 | 2054 | onboarding | weekly grid mock | Continue | preview | "Review your habit progress and savor the joy of success" | progress | — | [OBSERVED] |
| 4 | 2055 | onboarding | group mock with "Girlfriend" | Continue | preview | "Track together with your bestie / Get better together" | social | — | [OBSERVED] |
| 5 | 2056 | onboarding | meditating woman, 2 habit cards | Continue | — | "Journey with Habit / Let growth leave its mark" | — | 4 intro screens before any action | [OBSERVED] |
| 6 | 2057 | quiz | multi-select, progress bar, "Skip" | struggles | — | "Which of these often happens to you? No clear goals / Procrastinate before tasks / Often feel stressed or anxious / Hard to stick to plans / Hard to finish tasks on time" | problem priming | skippable (good) | [OBSERVED] |
| 7 | 2058 | quiz | — | procrastination | — | "Do you often procrastinate?" | — | — | [OBSERVED] |
| 8 | 2059 | quiz | — | action timing | — | "When do you act after setting a goal?" | — | — | [OBSERVED] |
| 9 | 2060 | quiz | — | reason | — | "If you don't act right away, why? … Fear of failure / … Low motivation" | — | — | [OBSERVED] |
| 10 | 2061 | quiz | — | motive | — | "What drives you to build good habits?" | — | — | [OBSERVED] |
| 11 | 2062 | education | near-empty chart, "5%" | Continue | pseudo-science | "Building good habits boosts happiness!" "Habit Formation Curve and Trajectory of Subjective Well-being (SWB) Evolution" "Studies show habit building increases happiness…" | authority | uncited "studies"; the chart barely renders | [OBSERVED] |
| 12 | 2063 | yes-ladder | grey sad woman vs colourful woman at desk | "Yes 💪" (only button) | — | "Want to better plan your day?" | yes-ladder | single-option question | [OBSERVED] |
| 13 | 2064 | yes-ladder | overweight woman with junk food (grey) vs yoga woman | "Yes 💪" | — | "Want to feel happier and healthier?" | shame contrast | **body-shaming before/after imagery** | [OBSERVED] |
| 14 | 2065 | yes-ladder | crying woman under cloud vs sunny woman | "Yes 💪" | — | "Want to become a better you?" | shame contrast | single-option | [OBSERVED] |
| 15 | 2066 | commitment | checklist of 5 pledges | "I promise!" | — | "「I promise I will」 Greet the Morning with a Smile! / Sip the Day's Refreshment! / Wave Goodbye to Heavy Drinks! / Drift Away from the Screen! / Walk in the Sunset's Glow!" | commitment device | the pledges never become habits (see #20) | [OBSERVED] |
| 16 | 2067 | social proof | 5★ review cards | Continue | — | "Some habit tracking apps … can create guilt from not finishing everything that day." / "…I lost the streak so I started some new ones…" | proof | its own showcased reviews name streak guilt | [OBSERVED] |
| 17 | 2068 | paywall | Lifetime vs Annual tiles, features | buy / ✕ | — | "Unlock Pro now / Become better every day!" "Lifetime Best Deal ₹999 ~~₹2,497.5~~" "Annual Popular 3 Days Free Trial … Only ₹49.92/month ₹599 ~~₹1,497.5~~" "Limited-time offer, price rising soon." | anchoring, urgency | fake anchors, "price rising soon" | [OBSERVED] |
| 18 | 2069 | downsell | gift box, timer | claim / Discard | — | "Limited-Time Offer 70% OFF 23:59:58 Only ₹799 ~~₹2,663.33~~ One-Time Purchase" "Claim Offer" / "Discard" | scarcity | **countdown downsell**, faint decline | [OBSERVED] |
| 19 | 2070 | settings | sheet over empty home | choose tap vs swipe | — | "Check-in Method / Please choose your preferred check-in method. Swipe right to check in / Tap to check in" | — | **invented concept** asked before the user has a habit | [OBSERVED] |
| 20 | 2071 | core-task | empty state, 5-tab bar, gift icon, lightbulb | add a habit | nothing | "No Habits / Tap "+" to add your first habit." | — | **screen 20, zero habits**; the promises from #15 were not carried over | [OBSERVED] |

### The 8 measures

1. **First win.** Not reached in the capture. The user lands on "No Habits" on screen 20 `[OBSERVED #20]`. The first check-in needs the add-habit flow, which was not captured `[UNKNOWN taps]`. That makes ≥25 taps from launch, after the paywall `[INFERRED]`: 4 Continue (#2–#5) + 2 per quiz screen (select + Continue, #6–#10) = 10 + 1 (#11) + 3 (#12–#14) + 1 (#15) + 1 (#16) + 1 ✕ (#17) + 1 Discard (#18) + 1 Confirm (#19) + 1 "+" + 1 check-in, plus the uncaptured add-habit flow.
2. **Ask ledger.** 5 quiz questions (#6–#10), 3 single-button "Yes" questions (#12–#14), a pledge (#15), the paywall (#17), the downsell (#18) and the check-in method (#19): **12 asks**. Gives back: 4 product mocks, an uncited chart and reviews. Nothing personal comes back. The quiz answers visibly change nothing, because the user still lands on an empty list `[OBSERVED #20]`.
3. **Abstractions:** habits, categories ("Habit Formation / Exercise / Control Habits", #2), quantitative goals ("2400/2000 ml", #2), Quit Habit (#17, paid), groups with friends (#4), "BestDay" (#3), check-in method (#19), a gift box and a lightbulb icon (#20), Pro. That makes **9** as listed (gift box and lightbulb counted as one; 10 if counted separately). The job needs habit + check-in. The check-in method is pure invention.
4. **Feel-good:** only previews of other people's progress (#2–#5). Nothing earned. Manufactured: "Studies show…" (#11) and the yes-ladder (#12–#14).
5. **Feel-bad:** before/after shame imagery (#13–#14); fake anchors and "price rising soon" (#17); a 24-hour countdown downsell (#18); arriving empty after making promises (#15 → #20). Missed-day behaviour: `[UNKNOWN]`. The app's own showcased reviews mention "lost the streak" and "guilt" (#16) `[OBSERVED]`.
6. **Paywall:** pre-home, dismissible with ✕, lifetime highlighted, then a timed downsell. See A3.
7. **Repeat cost:** 1 tap or 1 swipe per habit, by the user's choice (#19) `[OBSERVED]`. Home has a 7-day strip and an "All" filter. Widgets: the release notes mention widgets (`[DATA:itunes-lookup-us]` "If your widget is not working…"); none were captured.
8. **Feature map.** Table stakes: list, check-in, weekly grid. Differentiators: the colourful grid "Habit Tracker" journal look (#3), quantitative habits, groups. Bloat: check-in method, BestDay, gift-box upsell icon.

## Keep / Kill / Different

**Keep**
- "Skip" on every quiz screen (#6–#10).
- The visual weekly grid as a reward artefact (#3). It looks like a paper journal page people would screenshot.

**Kill**
- Single-button "Yes" questions and before/after shame imagery (#12–#14).
- Pledges that are not turned into habits (#15 → #20).
- Invented anchors, "price rising soon" and countdown downsells (#17–#18).
- Asking for a check-in method before the user owns a habit (#19).
- Landing on an empty state on screen 20 (#20).

**Different**
- Whatever the user picks or promises in onboarding **is** their habit list. Never land on an empty list.
- No quiz before the first check-in. If we ask a question, its answer must change something visible on the next screen.
- One way to check in (tap), chosen by us.

## A6 Failure mining
Not in this run (screens-only).

## A8 Verdict (short)

A solid, simple tracker (4.79★, 147k US ratings) hidden behind a conversion-funnel onboarding copied from the quiz-app playbook. That onboarding has 4 previews, 5 quiz questions, a 3-step yes-ladder with shame imagery, a pledge, a paywall and a countdown downsell, and the payoff is an **empty screen**. **Copy:** skippable questions and the journal-grid look. **Beat:** everything before the first habit. **Most exploitable weakness:** the onboarding promises ("I promise I will…") that silently vanish. It is the clearest case in the set of asks with nothing given back.

Evidence strength: A1 strong · A3 strong (India) · A5 strong for onboarding, weak for the core loop (not captured).

## Verification (2026-10-04)

Checked against all 20 screenshots (IMG_2052–2071), opened visually and OCR'd; xlsx "5 Parameters Benchmark" row 30; iTunes lookup US (id 1438388363) on 2026-10-04.
- Checked: ≈25 verbatim quotes, ≈15 numbers/prices (₹999/₹2,497.5, ₹599/₹1,497.5, ₹49.92, 70%, 23:59:58, ₹799/₹2,663.33, 2400/2000 ml, 5%), 20 per-screen IMG refs + ≈30 in-text #refs, 3 xlsx claims (₹1,499/yr or ₹1,999 lifetime; 5 screens; "Gentle Flow": all match the cell), 7 API fields (incl. release notes and the widget line: all match).
- Corrections:
  - Downsell anchor "matches nothing… invented" → kept, plus the arithmetic: ₹2,663.33 = 799 ÷ 0.30, and both #17 anchors = price ÷ 0.4 `[INFERRED]`.
  - xlsx comparison "16 screens before home" → 19 before home (16 before the paywall).
  - "18 screens later, zero habits" / "after 20 screens" → on screen 20.
  - Taps "≥22" → ≥25 (sum now shown), plus the uncaptured add-habit flow.
  - Concepts "≈8" → 9 (10 if the gift box and lightbulb are counted separately).
- Could not verify: the add-habit flow and first check-in; the paid-feature list below the fold on #17; US prices.
