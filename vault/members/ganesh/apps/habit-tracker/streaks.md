---
type: app
category: habit-tracker
app: "Streaks"
app_store_id: 963034692
member: ganesh
run_by: harshil
updated: 2026-10-04
status: draft
scope: screens-only
screens_analysed: 0
reviews_analysed: 0
sources: [screenshots:12 (11 App Store preview images + 1 listing page; 0 in-app), ganesh-benchmark-xlsx, itunes-lookup-us]
---

# Streaks (Crunchy Bagel), design-led, paid upfront

Screens folder: `ganesh_screenshots/Habit Trackers/Streaks/` IMG_2111–2122 (12 files). Context: [[members/ganesh/drafts/habit-tracker/screens-synthesis]]

**No A5 teardown is possible.** All 12 files are App Store captures, not in-app screens `[OBSERVED]`:
- IMG_2111–2121 are the App Store **preview images** viewed full screen. They have the App Store ✕ top-right, neighbouring preview cards at the edges and the marketing "09:41" status bar inside a device frame. IMG_2112 and IMG_2113 are identical.
- IMG_2122 is the **App Store listing page** (India): "Streaks / The habit-forming to-do list / ₹599 / 701 RATINGS 4.8 / No.11 Health & Fitness".

Under the screens-lens source rule, listing images are marketing, not the product. That makes **screens_analysed: 0** `[UNKNOWN] no team in-app screenshots`. The app is paid upfront (₹599 in India), so it was most likely not bought for capture `[INFERRED]`.

**What to capture** (needs a purchase, $5.99 US / ₹599 IN): first launch → any onboarding → empty state → add first task → first completion → a missed day (day 2/3) → settings → widget setup. Ideally also a US-storefront run.

## A1 Snapshot (short)

| Field | Value |
|---|---|
| Developer | Crunchy Bagel Pty Ltd `[DATA:itunes-lookup-us 2026-10-04]` |
| US price | **$5.99 paid upfront** `[DATA:itunes-lookup-us 2026-10-04]`. India: ₹599 `[OBSERVED IMG_2122 listing]` |
| US rating | 4.81 from 27,347 ratings `[DATA:itunes-lookup-us 2026-10-04]`. India: 4.8 from 701 `[OBSERVED IMG_2122]` |
| Version | 11.4.2, released 2026-09-27. First release 2015-06-01. Genre Health & Fitness `[DATA:itunes-lookup-us]` |
| Last notes | "Improved Health task processing / Faster setup when adding Health tasks / Improvements to app launch speed" `[DATA:itunes-lookup-us]` |
| Positioning | "STREAKS. The to-do list that helps you form good habits. Apple Design Award winner. Track up to 24 tasks you want to complete each day. Your goal is to build a streak of consecutive days." `[DATA:itunes-lookup-us description]` |

## A2 Business performance
Not in this run (screens-only).

## A3 Monetization
Paid upfront: $5.99 US `[DATA:itunes-lookup-us]` and ₹599 India `[OBSERVED IMG_2122]`. No paywall, by model. Whether any IAP exists: `[UNKNOWN]`. Check the listing's IAP section. Ganesh's xlsx says "₹599 One-Time Purchase… 12 daily tasks" `[DATA:ganesh-benchmark-xlsx]`. The US description says "up to 24 tasks" `[DATA:itunes-lookup-us]`. The spread may be per-page versus total, or an old limit `[UNKNOWN]`.

## A4 Acquisition
Not in this run. Listing claims "Apple Design Award winner" `[DATA:itunes-lookup-us]`.

## A5 Screens lens
`[UNKNOWN]` no team in-app screenshots (see above). For reference only, **not** as screen evidence: the preview images advertise Health-linked auto-completing tasks, negative tasks ("DON'T SMOKE"), timers, shared tasks, many widgets and a Live Activity timer. These are listing claims `[DATA:app-store-listing-images]`, not observed flows.

One positioning fact is relevant to the hypothesis. The product is literally named after the consecutive-day streak, and the description states "Your goal is to build a streak of consecutive days" `[DATA:itunes-lookup-us]`. It is the purest streak-mechanic app in the set. Whether a missed day resets to 0 is `[UNKNOWN]` until captured or mined from reviews.

## Keep / Kill / Different
Cannot be grounded in screens this run. The one listing-level lesson: **automatic completion from Apple Health** removes the check-in tap altogether for health habits `[DATA:itunes-lookup-us release notes + description]`. That is worth testing as a "zero-tap check-in" idea once we capture it in-app.

## A6 Failure mining
Not in this run (screens-only).

## A8 Verdict (short)
No screen verdict. As positioning, Streaks is the benchmark for "small, paid once, beautiful, no funnel". It is proof that a habit tracker can hold 4.8★ across 27k US ratings without a quiz or a paywall. Evidence strength: A1 strong · A3 strong · A5 none.
