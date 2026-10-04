---
type: app
category: habit-tracker
app: "Grit: Daily Habit Tracker"
app_store_id: 6446997766
member: ganesh
run_by: harshil
updated: 2026-10-04
status: draft
scope: screens-only
screens_analysed: 40
reviews_analysed: 0
sources: [screenshots:40, ganesh-benchmark-xlsx, itunes-lookup-us]
---

# Grit: Daily Habit Tracker (GrittyApps)

Screens: `ganesh_screenshots/Habit Trackers/Grit: Daily Habit Tracker/` IMG_2012–2051 (40 files, contiguous). India storefront, captured on 2026-10-03 `[INFERRED: home shows Sat 3]`. Ends on home with 3 habits, **none completed**. The system notification dialog was not captured. Context: [[members/ganesh/drafts/habit-tracker/screens-synthesis]]

## A1 Snapshot (short)

| Field | Value |
|---|---|
| Developer | GrittyApps `[DATA:itunes-lookup-us 2026-10-04]` |
| US price | Free with IAP `[DATA:itunes-lookup-us]` |
| US rating | 4.78 from 15,958 ratings `[DATA:itunes-lookup-us 2026-10-04]` |
| Version | 6.0.1, released 2026-09-18. First release 2023-05-17. Genre Productivity `[DATA:itunes-lookup-us]` |
| Last notes | "Redesigned statistics screen… Multicolumn layouts… New widgets…" `[DATA:itunes-lookup-us]` |
| Lead promise | "Welcome to Grit / Discover a better self, one habit at a time." with "4M+ Users / 90K+ Ratings / 4.8 Top Rated" `[OBSERVED #1]` |

Note: the in-app "90K+ Ratings" and "4M+ Users" claims (#1) are not US numbers. The US count is 15,958 `[DATA:itunes-lookup-us]`, so "90K+" must be worldwide or `[UNKNOWN]`.

## A2 Business performance
Not in this run (screens-only).

## A3 Monetization (from screens)

- **Plans (India storefront):** "Not sure? Enable free trial" (toggle **off**). "Most popular / Yearly ₹108.25 / mo / Start your journey for ₹1,299 / ~~₹299.00 / mo~~". "Monthly ₹299.00 / mo". "Lifetime ₹2,499". Plus "Cancel at any time" and "Get Full Access" `[OBSERVED #38]`. The US price is `[UNKNOWN]`.
- **Framing:** the yearly price leads as a monthly equivalent, with the monthly price struck through as the anchor. That is a real comparison, not an invented one `[OBSERVED]`. The trial is opt-in and its length is not shown `[UNKNOWN]`.
- **Placement:** pre-home, after 37 onboarding screens (#1–#37), personalised ("Hey Ganesh Varma, it's time to get full access to Grit"). Dismissible ✕ top-right `[OBSERVED #38]`.
- **After closing:** a permanent "Unlock everything / With Grit Premium" card in the habit list `[OBSERVED #40]`.
- **Disagreement with Ganesh's xlsx:** the xlsx says "₹1,499/yr (3-day trial) or ₹1,999 Lifetime", "6 onboarding screens" and "Gentle Flow" `[DATA:ganesh-benchmark-xlsx]`. The screens show ₹1,299/yr, ₹299/mo and ₹2,499 lifetime, with **37 screens before the paywall**. The tone is gentle; the length is not. Ganesh, please correct the row.

## A4 Acquisition
Not in this run (screens-only).

## A5 Screens lens

### Per-screen table (capture order = journey order; no gaps)

| # | file | stage | what user sees | asks | gives | verbatim copy | lever | friction / dark pattern | tag |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 2012 | first-launch | owl mascot, laurels | start | proof | "4M+ Users / 90K+ Ratings / 4.8 Top Rated / Welcome to Grit / Discover a better self, one habit at a time." | social proof | — | [OBSERVED] |
| 2 | 2013 | onboarding | product mock of colourful habits with streak flames | Continue | preview | "Feel calmer and more in control / Create simple routines that help you move through your day with clarity." | aspiration | — | [OBSERVED] |
| 3 | 2014 | onboarding | habit config form mock | Continue | preview | "Make time for what matters" fields "Color / Icon / Description / Type Good / Groups No group / Goal 30 minutes / Repeat Every day" | — | shows a 7-field form as a selling point | [OBSERVED] |
| 4 | 2015 | onboarding | illustration | Continue | reassurance | "Gently become your best self / Progress doesn't have to be extreme. Small, consistent steps lead to real change." | low bar | — | [OBSERVED] |
| 5 | 2016 | proof | 3 review cards | Continue | — | "Loved by people just like you" | social proof | — | [OBSERVED] |
| 6 | 2017 | quiz | — | mood | — | "How are you feeling today? Take a breath, let's start simple." | care | — | [OBSERVED] |
| 7 | 2018 | interstitial | owl with heart balloon | Continue | warmth | "A little better each day / Let's build habits that help you feel even better." | — | — | [OBSERVED] |
| 8 | 2019 | input | name field + keyboard | type name | — | "What should we call you? We'll personalize your journey." | — | typed input | [OBSERVED] |
| 9 | 2020 | interstitial | owl, heart eyes | Continue | recognition | "Glad to have you here, Ganesh Varma 👋 We'll create a plan that fits your lifestyle…" | personalisation | — | [OBSERVED] |
| 10 | 2021 | quiz | — | sleep | — | "How much sleep do you usually get?" | — | — | [OBSERVED] |
| 11 | 2022 | quiz | — | out of bed | — | "How long does it usually take you to get out of bed?" | — | — | [OBSERVED] |
| 12 | 2023 | quiz | — | chronotype | — | "When do you usually feel your best?" | — | — | [OBSERVED] |
| 13 | 2024 | quiz | — | routine | — | "How do you feel about your current routine?" | — | — | [OBSERVED] |
| 14 | 2025 | quiz | — | motivation | — | "What's motivating you right now?" | — | — | [OBSERVED] |
| 15 | 2026 | quiz | 10 chips | biggest difference | — | "What would make the biggest difference in your life today?" | — | — | [OBSERVED] |
| 16 | 2027 | interstitial | illustration | Continue | — | "Imagine your days feeling lighter" | future pacing | — | [OBSERVED] |
| 17 | 2028 | interstitial | illustration | Continue | — | "You're closer than you think / … And you don't have to do it alone." | — | — | [OBSERVED] |
| 18 | 2029 | quiz | — | distraction | — | "How easily do you get distracted?" | — | — | [OBSERVED] |
| 19 | 2030 | quiz | — | procrastination | — | "How often do you procrastinate?" | — | — | [OBSERVED] |
| 20 | 2031 | quiz | — | support | — | "Do you feel supported in your daily life? … I often feel alone" | — | sensitive | [OBSERVED] |
| 21 | 2032 | quiz | multi-select | blockers | — | "What usually gets in your way? Select all that apply." | — | — | [OBSERVED] |
| 22 | 2033 | quiz | one selected | Continue | — | "I don't know where to begin" | — | — | [OBSERVED] |
| 23 | 2034 | education | rising curve | Continue | promise | "Small habits can change a lot / Our users report feeling more energized… within a few weeks." "Now / Week 1 / Week 2 / After 3 weeks" | future pacing | an unlabelled y-axis is a **manufactured** promise | [OBSERVED] |
| 24 | 2035 | quiz | yes/no card | — | — | "Does this sound like you? I feel overwhelmed when I have too much to do" | self-recognition | — | [OBSERVED] |
| 25 | 2036 | quiz | yes/no | — | — | "I always feel like there's not enough time" | — | — | [OBSERVED] |
| 26 | 2037 | quiz | yes/no | — | — | "I struggle to stay focused on what matters" | — | — | [OBSERVED] |
| 27 | 2038 | quiz | yes/no, sad emoji | — | — | "At the end of the day, I wish I had done more for myself" | pain priming | — | [OBSERVED] |
| 28 | 2039 | interstitial | illustration | Continue | — | "Life can be easier" | — | — | [OBSERVED] |
| 29 | 2040 | interstitial | "+ Happiness / + Energy / − Stress / + Calmness" | Continue | — | "Real progress people can feel" | — | — | [OBSERVED] |
| 30 | 2041 | loading | ring + review | wait | — | "Creating your personalized journey…" "APPS WE LOVE" "4.8/5" | labour illusion | **manufactured** | [OBSERVED] |
| 31 | 2042 | result | 4 scores | Continue | diagnosis | "Here's where you are today / Focus / Productivity / Self-control / Well-being — Could be better" "There's room to grow, and that's completely okay." | gap framing | **every score is "Could be better"**; likely a generic verdict presented as personal `[INFERRED]` | [OBSERVED] |
| 32 | 2043 | result | 4 scores → "Good" | Continue | promise | "Here's where we're heading in just a few weeks" | future pacing | manufactured | [OBSERVED] |
| 33 | 2044 | interstitial | owl in sunglasses | "I'm ready for change" | — | "Ganesh Varma, ready to build a routine you actually enjoy?" | commitment | — | [OBSERVED] |
| 34 | 2045 | permission | 3 toggles, all **on** | Continue | — | "Hard time getting started? Gentle reminders can help you keep going / Evening energy / Start small / Helpful updates — Get personalized recommendations and special offers." | defaults | **marketing opt-in pre-ticked** next to the reminder toggles | [OBSERVED] |
| 35 | 2046 | interstitial | footprints | Continue | — | "Every big change starts small / … Let's start with one simple step." | low bar | — | [OBSERVED] |
| 36 | 2047 | core setup | habit chips, 3 selected | pick first steps | habits | "Choose your first small step / Pick something simple…" Get Out of Bed / Stretch / Wash Your Face selected, "Continue (3)" | micro-habits | "first small step" allows many | [OBSERVED] |
| 37 | 2048 | commitment | 4 pledges + hold button | hold to agree | — | "Ganesh Varma, let's make a promise to yourself 💜 … I will stay consistent, not perfect / Hold to agree / Research shows that committing to contracts like this one makes you more likely to achieve your goals." | commitment device | uncited "research" | [OBSERVED] |
| 38 | 2049 | paywall | personalised plans | buy / ✕ | — | see A3 | personalisation, anchor | ✕ top-right; trial off by default | [OBSERVED] |
| 39 | 2050 | celebration | owl | "Start my journey" | — | "Congratulations! Your journey starts now ✨ You don't need to change your whole life overnight." | celebration | congratulates nothing yet | [OBSERVED] |
| 40 | 2051 | core-task | 3 habits + premium card | check in | habit list | "Wash Your Face Every day ⊕ / Stretch Every day, 0/5 minutes ▶ / Get Out of Bed Every day ⊕ / Unlock everything With Grit Premium / Synced with iCloud" tabs "Habits / Statistics / Settings" | — | — | [OBSERVED] |

### The 8 measures

1. **First win.** 1 tap past #40 (⊕ on "Get Out of Bed"), so ≈**41 taps** from launch, approximate: 38 screens with one action each (#1–#39 minus the #30 loader) + 2 extra for name typing and the multi-select + 1 check-in = 41, **after the paywall** `[INFERRED]`. Not captured `[UNKNOWN]`. The longest path in the set.
2. **Ask ledger.** Name, 11 quiz questions (#6, #10–#15, #18–#21), 4 "Does this sound like you?" cards, reminders (with a pre-ticked marketing toggle), the first steps, the pledge and the paywall: **20 asks**. Gives: 8 interstitials of encouragement (#7, #9, #16, #17, #28, #29, #33, #35), a fake diagnosis (#31), a fake forecast (#32) and the user's name repeated back 4 times. In this capture the quiz answers led to "Could be better" on every axis `[OBSERVED #31]`; whether every user gets the same verdict is `[INFERRED]`.
3. **Abstractions:** habit type (Good/Bad), groups, goal (count/duration), repeat, colour/icon/description (#3), timer habits (0/5 min ▶, #40), streak flames (#2), to-do items ("Plan Tomorrow To-do", #2), statistics and Premium. That makes **10** as listed (colour/icon/description counted as one). The home screen is clean (3 rows). The concepts live in creation and settings.
4. **Feel-good:** good copy that lowers the bar: "Progress doesn't have to be extreme" (#4), "There's room to grow, and that's completely okay." (#31), "I will stay consistent, not perfect" (#37), "You don't need to change your whole life overnight." (#39). Manufactured: the forecast curve (#23), the diagnosis (#31–#32), the loader (#30) and "Congratulations!" before any action (#39).
5. **Feel-bad:** 4 pain-priming cards (#24–#27); a pre-ticked "special offers" toggle (#34); uncited "Research shows…" (#37). Missed-day behaviour: `[UNKNOWN]`. The "consistent, not perfect" pledge suggests forgiveness, but the streak-flame counts on the mock (#2) suggest consecutive-day streaks `[INFERRED]`.
6. **Paywall:** pre-home, after 37 screens, personalised, ✕ visible, yearly default, opt-in trial, a persistent premium card afterwards. The cleanest price framing in the set.
7. **Repeat cost:** 1 tap (⊕) for a yes/no habit; ▶ starts a timer for duration habits `[OBSERVED #40]`. Hooks: reminders (#34), widgets (per release notes `[DATA]`), statistics.
8. **Feature map.** Table stakes: list, one-tap check, reminders, stats, iCloud sync. Differentiators: timer habits, Apple Health, strong statistics (the current release focus). Bloat in onboarding: 8 interstitials, 4 yes/no cards, the diagnosis and the forecast.

## Keep / Kill / Different

**Keep**
- Forgiving copy: "consistent, not perfect" (#37) and "room to grow, and that's completely okay" (#31).
- Micro-habit chips as the first step: "Get Out of Bed / Stretch / Wash Your Face" (#36).
- Yearly-as-monthly framing anchored on a *real* monthly price (#38).
- A home screen that is just the list (#40).

**Kill**
- 37 screens before the paywall and 39 before the list. Every interstitial (#7, #16, #17, #28, #29, #35) and the yes/no pain cards (#24–#27).
- The fake diagnosis and forecast (#31–#32) and the forecast curve (#23).
- Marketing consent pre-ticked among reminder toggles (#34).
- "Hold to agree" contracts with uncited research (#37); "Congratulations!" for nothing (#39).

**Different**
- Grit's #36 becomes our screen 1, and its #40 our screen 2. Its warm copy moves to the moments it is earned: after a check-in, after a missed day.
- Reminders: one toggle, one time, no marketing bundled in.

## A6 Failure mining
Not in this run (screens-only).

## A8 Verdict (short)

Grit is a good, actively developed tracker with the kindest copy in the set. Its onboarding is the longest in the set: 39 screens before the list and about 41 taps before the first check-in. It copies the quiz-funnel pattern wholesale, down to a diagnosis that said "Could be better" on all four axes (likely for everyone `[INFERRED]`). **Copy:** forgiving language, micro-habit chips, honest plan framing. **Beat:** time to first check-in (about 41 taps for Grit; our target is 2). **Most exploitable weakness:** the gap between "gently become your best self" and a 40-screen funnel that ends in a paywall.

Evidence strength: A1 strong · A3 strong (India) · A5 strong for onboarding, weak for the core loop.

## Verification (2026-10-04)

Checked against all 40 screenshots (IMG_2012–2051), opened visually and OCR'd; xlsx "5 Parameters Benchmark" row 31; iTunes lookup US (id 6446997766) on 2026-10-04.
- Checked: ≈40 verbatim quotes, ≈15 numbers/prices (₹108.25, ₹1,299, ₹299.00, ₹2,499, 4M+/90K+/4.8, 0/5 minutes, Sat 3), 40 per-screen IMG refs + ≈35 in-text #refs, 3 xlsx claims (₹1,499/yr 3-day trial or ₹1,999 lifetime; 6 screens; "Gentle Flow": all match the cell), 7 API fields (incl. release notes: all match).
- Corrections:
  - Paywall cited as #37 (×2 in A3) → #38 (IMG_2049); #37 is the pledge.
  - "after 36 onboarding screens" / "36 screens before the paywall" → 37.
  - Kill list "40 before the list" → 39; verdict "40 screens" → 39 screens before the list.
  - "13 quiz questions" → 11 (#6, #10–#15, #18–#21; #22 is a re-capture); asks "≈22" → 20.
  - "9 interstitials" (×2) → 8, as tagged in the table.
  - Taps "≈42" → ≈41 (sum now shown).
  - Concepts "≈8–9" → 10 (the items listed).
  - "says 'Could be better' to everyone" / "a generic verdict" → observed on all four axes in this run; generic-for-everyone tagged `[INFERRED]` (one capture).
- Could not verify: the system notification dialog; trial length; whether the diagnosis varies by answers.
