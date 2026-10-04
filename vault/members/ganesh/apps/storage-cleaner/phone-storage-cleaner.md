---
type: app
category: storage-cleaner
app: "Phone Storage Cleaner: Free up"
app_store_id: 6449484412
member: ganesh
run_by: harshil
updated: 2026-10-04
status: draft
scope: screens-only
screens_analysed: 12
reviews_analysed: 0
sources: [screenshots:12, ganesh-benchmark-xlsx, itunes-lookup-us]
---

# Phone Storage Cleaner: Free up ("FreeUp Cleaner")

Screens: `ganesh_screenshots/Storage Cleaners/Phone Storage Cleaner: Free up/` IMG_2252–2263, India storefront, captured on or about 2026-10-03 `[INFERRED: the Apple sheet says the ₹699/week plan starts "6 Oct 2026" after a 3-day trial]`. The app calls itself "FreeUp Cleaner" in the tracking prompt and "Free Up" in its copy `[OBSERVED #3, #4]`. Context: [[research/categories/storage-cleaner/overview]] · [[members/ganesh/drafts/storage-cleaner/screens-synthesis]]

## A1 Snapshot (short)

| Field | Value |
|---|---|
| Developer | LUNAPARK MEDYA INTERNET TEKNOLOJILERI… (Ganesh lists it as "Must Have Apps") `[DATA:itunes-lookup-us 2026-10-04]` `[DATA:ganesh-benchmark-xlsx]` |
| US price | Free with IAP `[DATA:itunes-lookup-us]` |
| US rating | 4.52 from 73,211 ratings `[DATA:itunes-lookup-us 2026-10-04]` |
| Version | 2.10.1, released 2026-10-02. First release 2023-10-19 `[DATA:itunes-lookup-us]` |
| Lead promise | "Let's Clean Your Storage!" / "1 Million+ devices cleaned up!" `[OBSERVED #2]` |

## A2 Business performance
Not in this run (screens-only).

## A3 Monetization (from screens)

- **Model on screen:** one weekly plan with a 3-day trial. "Free for 3 days then ₹ 699/weekly" `[OBSERVED #9]`. The Apple sheet reads "3-day free trial · Starting today · ₹ 699 per week · Starting on 6 Oct 2026" `[OBSERVED #10]`. No annual or lifetime plan was visible in the captures. These are **India storefront** prices; the US price is `[UNKNOWN]`.
- **Disagreement with Ganesh's xlsx:** the xlsx lists "₹999/yr or ₹1,999 Lifetime" `[DATA:ganesh-benchmark-xlsx]`. The screens show **₹699/week** only. Either the plans vary by experiment, or the row is wrong. Re-check with one more capture.
- **Touchpoints:** a pre-paywall interstitial ("3 day free trial is enabled!", #8), the onboarding paywall (#9), the Apple purchase sheet (#10, after tapping "Try free"), and an "Unlock" gate on Contacts on home (#11). The same paywall appears again (IMG_2263).
- **Dismissability:** "Skip trial" in small grey text, top-right, is visible as soon as the paywall loads `[OBSERVED #9]`. The Apple sheet has a ✕ `[OBSERVED #10]`.
- **Live counter:** "2558 people have joined today!" `[OBSERVED]`, manufactured social proof `[INFERRED]`.

## A4 Acquisition
Not in this run.

## A5 Screens lens

### Per-screen table (reordered where the content says so)

Order note: IMG_2260 (the Apple purchase sheet) is filed before IMG_2261/2263 (the paywall), but it can only appear after tapping "Try free". IMG_2261 is the paywall still loading, and IMG_2263 is the same paywall loaded. Journey order used: 2252 → 2253 → 2254 → 2255 → 2256 → 2257 → 2258 → 2259 → 2261/2263 → 2260 → 2262. IMG_2263 may instead be the paywall re-shown from home (the battery reads 76 on both 2262 and 2263) `[INFERRED]`.

| # | file | stage | what user sees | asks of user | gives to user | verbatim copy | lever | friction / dark pattern | tag |
|---|---|---|---|---|---|---|---|---|---|
| 1 | IMG_2252 | launch | Blue splash with a broom icon and a loading bar | Wait | — | — | — | — | `[OBSERVED]` |
| 2 | IMG_2253 | welcome | iCloud icon with a red ✕; a red bar "62 of 64 GB used" | Tap Continue (and accept the terms) | A canned crisis | "Let's Clean Your Storage!" / "1 Million+ devices cleaned up!" / "62 of 64 GB used" / "Clean your storage easily!" / "By continuing, you agree to Terms of Use and Privacy Policy" | Fear plus a laurel of social proof | **"62 of 64 GB" is not this phone or this iCloud**: the device is 255 GB with 120 GB used (#11), and 64 GB is not an iCloud tier `[INFERRED]` | `[OBSERVED]` |
| 3 | IMG_2254 | permission | iOS App Tracking Transparency (ATT) prompt over "More Storage Space" | Allow tracking | Nothing | "Allow \"FreeUp Cleaner\" to track your activity across other companies' apps and websites? This data will be used to gather performance statistics for personalizing your cleaning experience and fixing errors and crashes." | Vague justification | Tracking asked on screen 3, before any value. The purpose copy hides the ad-attribution use `[INFERRED]` | `[OBSERVED]` |
| 4 | IMG_2255 | onboarding | Bar chart "Without Free Up" vs "With Free Up 86%" | Continue | A claim | "More Storage Space" / "+86%" / "extra space for all your media with Free Up" / "*Based on Free Up internal data" | Big-number authority | Unverifiable and meaningless (86% of what?) | `[OBSERVED]` |
| 5 | IMG_2256 | onboarding | A line graph "Now → Goal" | Continue | A claim | "Eliminate Duplicates" / "160" / "duplicate contacts removed on average" | Goal-gradient framing | Contacts is introduced as a second job. "Goal" is a made-up abstraction | `[OBSERVED]` |
| 6 | IMG_2257 | onboarding | A clock face | Continue | A claim | "Save Hours" / "8h" / "gained per month with automated Free Up" | Time saved | "8h per month" is implausible for photo cleanup. "Automated" is not shown anywhere in the app | `[OBSERVED]` |
| 7 | IMG_2258 | onboarding | A speedometer | Continue | A claim | "Boost Performance" / "50%" / "faster response times with regular Free Up" | Performance myth | **A false claim**: deleting photos does not make an iPhone respond 50% faster `[INFERRED]`. The overview §9 already flags "faster" claims as unsupported | `[OBSERVED]` |
| 8 | IMG_2259 | pre-paywall | A toggle switched on | Nothing; auto-advances `[INFERRED]` | Primes "free" | "3 day free trial is enabled!" | Default effect | The trial is **pre-enabled** before the user has seen a price | `[OBSERVED]` |
| 9 | IMG_2261 → IMG_2263 | paywall | Photos badge 200 and iCloud badge 120; a green bar "25 from 100% used"; plan card; trial row with a ✓ | Try free | Counts of unknown origin | "Clean your Storage" / "Get rid of what you don't need." / "25 from 100% used" / "2558 people have joined today!" / "FreeUp Pro: Quick Clean, Large Files Clean, Photo Cleaning, Manage Contacts, No Ads and Limits." / "Free for 3 days then ₹ 699/weekly" / "3-day free trial ✓" / "Try Free" / "Skip trial" / "Secured with Apple" | Social proof, live counter, a "free" CTA | The badge counts animate (200/120 here, 343/278 on #10), so they are counters, not scan results `[INFERRED]`. The "25 from 100%" bar contradicts screen #2's "62 of 64 GB". "Skip trial" is low-contrast | `[OBSERVED]` |
| 10 | IMG_2260 | Apple sheet | The iOS in-app purchase sheet over the paywall | Confirm the subscription | — | "Storage Cleaner Pro · Subscription · 3-day free trial · Starting today · ₹ 699 per week · Starting on 6 Oct 2026 · No commitment. Cancel at any time in Settings…" | — | Fine; this is Apple's own sheet | `[OBSERVED]` |
| 11 | IMG_2262 | home / core | "Storage Used: 120 GB / 255 GB · 424 items"; "Ready to clean!"; Similar Photos "46 items · 427 MB"; Screenshots "138 items · 281 MB"; Contacts "Unlock"; "Save more space — View Guide"; tabs: Home, Photo, Video; PRO | Pick a category | **First real scan: about 708 MB found in two categories, plus a true storage reading** | as listed | Real numbers (earned); "Ready to clean!" is positive framing | Contacts is locked. Whether free users can delete photos is `[UNKNOWN]`. The xlsx says bulk delete is paid `[DATA:ganesh-benchmark-xlsx]` | `[OBSERVED]` |

**Gaps:** the iOS Photos permission dialog is not captured, yet home shows the user's own photos, so it was asked somewhere `[INFERRED]`. Also missing: any review, delete, or "freed" screen, the Video tab, and the guide.

### The 8 measures

1. **First win.** The found-value moment is home #11 (120 GB / 255 GB, 427 MB similar photos, 281 MB screenshots). That is about 10 taps from launch (Continue ×6, the ATT answer, the trial interstitial, Try free then ✕, or Skip trial), all **after** the paywall. Freed GB: `[UNKNOWN]`, not captured.
2. **Ask ledger.**

   | Order | Ask | What the user had received by then |
   |---|---|---|
   | 1 | Accept the terms (#2) | A fake "62 of 64 GB" alarm |
   | 2 | Tracking (ATT) (#3) | Nothing |
   | 3 | 4 × Continue through the claims (#4–#7) | Four unverifiable stats |
   | 4 | Start a ₹699/week trial (#9) | Animated counters |
   | 5 | Photos access (`[UNKNOWN]` where) | — |
   | 6 | Unlock Contacts (#11) | A real scan |

   This is the longest pre-value run in the set: 9 screens before the user sees anything true about their phone.
3. **Abstractions.** "Goal" (#5, invented). Duplicate *contacts* (an adjacent job). "Quick Clean" vs "Large Files Clean" vs "Photo Cleaning" (three names for overlapping things, #9). "Automated Free Up" (#6, a name with nothing behind it). "Pro". On home: Similar Photos, Screenshots, Contacts. Home is lean (3 tabs). The onboarding invents more concepts than the product shows.
4. **Feel-good moments.** "Ready to clean!" plus a true "120 GB / 255 GB" bar (#11) is **earned** and calm. The green "25 from 100% used" bar (#9) *feels* good but is not tied to the phone `[INFERRED]`.
5. **Feel-bad moments.** "62 of 64 GB used" with a red ✕ (#2) is fake fear. "50% faster response times" (#7) is a false performance claim. "3 day free trial is enabled!" (#8) is a pre-enabled trial. "2558 people have joined today!" (#9) is a manufactured counter. The tracking prompt comes on the third screen (#3).
6. **Paywall.** Soft paywall: "Skip trial" is visible immediately, but grey. A single weekly plan at ₹699 with a 3-day trial (India). Nothing was shown before the price except claims. No downsell observed.
7. **Repeat cost.** Home is short: storage readout, then 2 photo buckets with MB chips. About 1 tap to a bucket. Return hooks (notifications, widget): `[UNKNOWN]`; no notification ask was captured.
8. **Feature map.**
   - **Table stakes:** similar photos, screenshots, video, storage readout.
   - **Differentiators:** the simplest home in the set (3 tabs); a "Save more space — View Guide" card that admits not everything is photos.
   - **Bloat:** contacts in the onboarding story, "automated", "performance".

## Keep / Kill / Different

**Keep**
- The home layout of #11: a true storage reading, "Ready to clean!", and 2 buckets with MB on the button. This is the cleanest first view in the category.
- "Save more space — View Guide": honest help for the non-photo part of storage.
- "Skip trial" visible from the first frame (#9).

**Kill**
- "62 of 64 GB used" (#2) and every claim screen #4–#7 ("+86%", "160", "8h", "50% faster").
- The ATT prompt on screen 3 (#3). We need no cross-app tracking for a utility; if we ever need attribution, use SKAdNetwork/AdAttributionKit without ATT.
- The pre-enabled trial interstitial (#8) and the live "joined today" counter (#9).

**Different**
- Replace 4 claim screens with 0. Go splash → one-sentence promise → Photos access → a live scan showing their real numbers.
- One plan screen, after the first freed MB, with an annual or lifetime option next to weekly, and a plain-language close control.

## A6 Failure mining
Not in this run (screens-only). The xlsx 2★ review warns that "if you did not pay or don't plan to then Don't Waste You're Time" after two hours of reviewing "duplicates" `[DATA:ganesh-benchmark-xlsx]`. That suggests deletion is gated after review effort. Verify in review mining.

## A8 Verdict (short)

Its product home is the cleanest in the set, with real numbers and three tabs. Its onboarding is the dirtiest: a fake 62/64 GB alarm, tracking on screen 3, four unverifiable stats including a false "50% faster" claim, and a pre-enabled weekly trial. **Copy:** the home (#11) and "View Guide". **Beat:** the claim carousel, ATT-first, and the weekly-only plan. **Most exploitable weakness:** users who review groups and then hit a paywall to delete (xlsx review, to be verified). Our free first clean removes exactly that anger.

Evidence strength: A3 **medium** (screens clear; plan mix differs from the xlsx) · A5 **medium** (no core-task or result screens).
