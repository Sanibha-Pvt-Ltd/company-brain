---
type: category-screens
category: storage-cleaner
member: ganesh
run_by: harshil
updated: 2026-10-04
status: draft
scope: screens-only
sources: [screenshots:35 in-app (Cleanup 10, Phone Storage Cleaner 12, Clever Cleaner 7, Cleaner Kit 6), ganesh-benchmark-xlsx, itunes-lookup-us]
---

# Storage cleaner: screens synthesis (4 shortlisted apps)

App notes: [[members/ganesh/apps/storage-cleaner/cleanup]] · [[members/ganesh/apps/storage-cleaner/phone-storage-cleaner]] · [[members/ganesh/apps/storage-cleaner/clever-cleaner]] · [[members/ganesh/apps/storage-cleaner/cleaner-kit]]. Desk research: [[research/categories/storage-cleaner/overview]] (this note extends §5 and §9; it does not repeat them).

**Setup note.** All four apps were captured on one iPhone within about 10 minutes (2:51–3:01), India storefront, on or about 2026-10-03 `[OBSERVED status-bar times]` `[INFERRED date from trial end dates]`. Two apps independently read the device as **120 GB of 255 GB used** (Phone Storage Cleaner #11, Clever Cleaner #6), and Clever splits it as "Photo Library 2% · Data and apps 45% · Free 53%" `[OBSERVED]`. That one fact lets us check every storage claim in every onboarding against the truth.

## 1. Pattern table

| | Cleanup (winner) | Phone Storage Cleaner | Clever Cleaner | Cleaner Kit |
|---|---|---|---|---|
| Screens analysed | 10 | 12 | 7 | 6 (+1 store page) |
| Taps to *found* GB (real scan number) | ~7, home "5.0 GB Space to Clean" | ~10, home "427 MB" + "281 MB" | ~5–6, home "Similars 1.35 GB / Videos 2.62 GB" | not reached |
| Taps to *freed* GB | `[UNKNOWN]` | `[UNKNOWN]` | `[UNKNOWN]` (2 GB/day free) | `[UNKNOWN]` |
| Found-GB before or after paywall | after | after | after (✕ is immediate) | n/a |
| Asks before any real data | 3–4 (Photos?, 3× Next, trial; notifications right after) | 8+ (terms, ATT, 4 claim screens, trial) | 4 (ATT, 3× Continue, closable trial) | 6 (terms, notifications, 3× Next, paywall) |
| Fake storage claim | "95 from 100% used" | "62 of 64 GB used" | "Almost Full" | "240 GB of 256 GB used" |
| Other unverifiable claims | "up to 80%", "7.002" emails | "+86%", "160", "8h", "50% faster" | — | "up to 80%", "800,000+ 5-star ratings" |
| Day-1 concepts | ~8 (Similars, Duplicates, Videos, Screenshots, Optimize, Secret Storage, Email, Contacts, Extras) | ~5 (Quick Clean, Large Files, Photo Cleaning, Contacts, "Goal") | ~6 (Smart cleanup, Swipe, Compress, Similars, Heavies, Lives) | ~7 promised (duplicates, iCloud, email, contacts, calendar, junk, compress) |
| Pre-paywall "free" priming | "Try 7 days / For free!" | "3 day free trial is enabled!" | "Swipes Free", "2 GB free daily" (a real allowance) | — |
| Default plan (India ₹) | weekly ₹999, 7-day trial | weekly ₹699, 3-day trial (only plan) | weekly ₹699, 3-day trial | "MONTHLY" ₹979 with a 12-month lock-in (₹11,748) |
| Lifetime / annual shown | lifetime ₹3,999 | none seen | lifetime ₹3,999 | yearly ₹4,999 |
| Close visible on first paywall | no | yes ("Skip trial", grey) | yes (✕) | no |
| Permission asked earliest | Photos (gap) / notifications at home | ATT on screen 3 | ATT on screen 1 | notifications on screen 2 |
| Repeat cost (home → task) | 1 tap; "New photos (X MB)" chips | 1 tap; MB chips | 1 tap; 3 modes + cards | `[UNKNOWN]` |

All prices are India storefront `[OBSERVED]`. US prices were not captured. Ganesh's xlsx prices disagree with the screens for Cleanup (xlsx "₹999/yr", screen "₹999/week") and for Phone Storage Cleaner (xlsx "₹999/yr or ₹1,999 Lifetime", screen "₹699/week" only). Clever has no xlsx row, and the Cleaner Kit row match is uncertain. **Trust the screens; the xlsx needs a pass.**

## 2. Hypothesis check

> Prior `[INFERRED]`: "value is visible within seconds (GB found). Winners show the problem before the paywall; the anger points are fear copy and hard paywalls after the scan. Our edge is probably an honest free tier plus showing freed space before payment."

| Part | Verdict | Evidence |
|---|---|---|
| "Value is visible within seconds (GB found)" | **Partly confirmed.** The scan *is* fast, and every app that got past the paywall showed a real GB/MB number on home. But it takes 5–10 taps, not seconds, because onboarding comes first | Cleanup #7, PSC #11, Clever #6 |
| "Winners show the problem before the paywall" | **Killed.** No app shows the *user's real* problem before the paywall. All four show a **fabricated** problem instead (95% / 62 of 64 GB / Almost Full / 240 of 256 GB) on a phone that is 47% full | Cleanup #5, PSC #2, Clever #5, Kit #1 |
| "Anger point = hard paywalls *after the scan*" | **Revised.** The paywall comes *before* the scan in all four. The likely anger point is a hard paywall *after review effort* (the user spends time selecting, then deletion is gated). Ganesh's xlsx has one such review for PSC | xlsx PSC 2★ "Spent about two hrs… Don't Waste You're Time" `[DATA:ganesh-benchmark-xlsx]`; to be confirmed by A6 |
| "Fear copy" | **Confirmed and sharpened.** The fear is not in words; it is in **fake meters**. Each app's red bar is a drawing, not a reading | as above |
| "Our edge: honest free tier + freed space before payment" | **Confirmed as the gap, with one caveat.** Clever already does the honest free tier (2 GB/day, Swipes Free, ✕ visible). No app in our captures shows *freed* space before payment. That gap is open; the free-tier gap is not | Clever #3–#5 |

**Biggest surprise:** even the most honest app (Clever) fakes "Almost Full" on its paywall while its own home says 53% free. Fake meters are an industry habit, not one bad actor. Second surprise: on a typical phone, photos are only a small share of used space ("Photo Library 2%"). A photo cleaner can honestly recover a few GB, not "up to 80%". Users who expect 80% will feel cheated later. We should set the expectation right on screen 1.

## 3. Our first five minutes (screen by screen)

Rule: one ask before value (Photos access), zero invented numbers, the paywall only after the first freed MB.

| # | Screen | Asks | Gives | Copy direction |
|---|---|---|---|---|
| 1 | Welcome: one sentence plus a looping 2-second demo of picking the best shot of 5 near-identical photos | Tap "Scan my photos" | A clear promise | "Find the repeats and big videos in your photos. You choose what goes." |
| 2 | Pre-permission explainer, then the iOS Photos dialog (full or limited access both work) | **Photos access**, the only ask before value | Privacy line: "Scanning happens on this iPhone. Nothing is uploaded." | Ask for Photos only. No ATT, no notifications, no terms wall (the terms link sits in the footer) |
| 3 | Live scan with a real counter, then the true storage reading | — | **The real number**: "Your iPhone: 120 GB of 255 GB used. Photos and videos: 5.1 GB. We found **1.9 GB** you can likely free." | If photos are a small share, say so, and link one line to "Where the rest went" (the Settings > iPhone Storage guide; PSC's "View Guide" idea) |
| 4 | One suggested clean: the largest "Repeats" group set, best shot pre-kept, the rest pre-selected, reviewable in one scroll | Tap "Free 918 MB" | Control: tap any photo to flip keep/delete | Two concepts only, **Repeats** and **Big videos** |
| 5 | Result: "Freed 918 MB. They are in Recently Deleted for 30 days." Storage bar animates to the new free space | — | **The first win, earned**, plus a safety net | A celebration tied to the real delta, and a recovery reassurance (deletion-fear segment, overview §2) |
| 6 | Offer, after the win and only now: "Keep going: 1.0 GB more found, plus big-video shrink and a weekly tidy-up" | Choose a plan or "Not now" (an equal-weight button) | A free path that stays useful (the first full clean of a category is free; new photos are scanned free) | Show annual first, with its full price and billing period. Weekly can exist but is not the default. No "free" interstitials, no pre-enabled toggles, close visible on frame 1. US price is a stage B/C decision |
| 7 | (Later, after the 2nd session) "Tell me when new repeats pass 500 MB?" | Notifications, opt-in with a stated trigger | A reason to say yes | Never on day 1 before a win |

Taps to freed GB: about 4 (Scan → Allow → Free 918 MB → done), with 1 ask before value. Every competitor captured needs 5–10 taps just to *see* a real number.

## 4. Up to 3 differentiators (each tied to evidence)

1. **Truth meter: real numbers only, from the first frame.** Every storage visual reads this phone, and photos' true share is stated even when it is small. *Evidence:* 4 of 4 apps show a fabricated capacity or "almost full" state on a 47%-full phone (Cleanup #5, PSC #2, Clever #5, Kit #1). Clever's home shows the truth (#6) but its paywall contradicts it. Nobody keeps the truth end to end. This gap is directly visible in our screens. *Marketing line candidate:* "No fake alarms. Your real storage, real savings." `[INFERRED]`
2. **Freed before paid.** The first full clean (one category, end to end) is free, and the result shows the actual MB freed before any plan appears. *Evidence:* in all 4 flows the paywall appears before any real scan result, and no capture shows a freed-GB moment before payment. The likely anger point is review-then-gated deletion (xlsx PSC 2★; to be confirmed in A6). Clever's metered "2 GB free daily" is the closest competitor; ours is simpler (no quota to learn).
3. **Two concepts and one ask.** "Repeats" (similar plus duplicate merged, best shot auto-kept) and "Big videos" (with compress). Photos is the only permission before value. *Evidence:* competitors carry 5–8 day-1 concepts (Cleanup splits Similars from Duplicates and shows "Duplicates 0 Photos", #7; Clever has Smart cleanup/Swipe/Compress plus Heavies/Lives). ATT appears on screen 1 (Clever) or 3 (PSC), and notifications on screen 2 (Kit) or before any clean (Cleanup #6).

## 5. Concepts we refuse to add

| Concept | Seen in | Why we refuse |
|---|---|---|
| Similars vs Duplicates as separate buckets | Cleanup #7 | The user's job is "remove repeats"; the split is an implementation detail and shows empty states ("0 Photos") |
| Secret Storage / vault | Cleanup #5 | A different job; adds a passcode concept to a cleaner |
| Email inbox cleaning | Cleanup #3, Kit #4 | A different job, needs a mail account login, and gives no device storage on iOS for most users `[INFERRED]`; it is an ad angle, not a product need |
| Contacts / calendar cleanup in v1 | PSC #5, Kit #6, Cleanup tab bar | Adjacent job, a new permission, and a destructive-merge risk (xlsx BP Mobile 1★ review) |
| "Performance boost", "8h saved", "+86% space" | PSC #4–#7 | False or unverifiable; also App Store review risk |
| "Goal" graphs, "Extras", "Optimize" as a tab | PSC #5, Cleanup #7 | Invented labels with no user job behind them |
| "Heavies", "Lives" jargon | Clever #5 | Say "Big videos" and "Live Photos" |
| Daily GB quota as the free tier | Clever #4 | A currency to learn and track. "First clean free" plus "new photos scanned free" is one rule |
| Live "people joined today" counters, laurel stats | PSC #9, PSC #2, Kit #5 | Manufactured proof; erodes the trust we are selling |
| A "monthly" label on an annual commitment | Kit #6 | We will not ship it, ever |

## 6. Open questions (send to review mining / hands-on test)

1. **Can a free user delete anything** in Cleanup and PSC, and at what point is deletion gated (select → paywall?)? Run a hands-on test on a fresh install with a seeded library. Capture every screen past the paywall.
2. **How do the paywalls exit?** Cleanup #5 and Kit #6 show no visible close: is there a delayed ✕, a swipe-down, or nothing? Record a screen recording with timestamps.
3. **US storefront plan mix and prices** for all four (weekly vs annual vs lifetime, trial lengths). India showed weekly-default everywhere. Capture on a US Apple ID; also pull the iTunes IAP list.
4. **Review mining (A6):** clusters for (a) "charged weekly / didn't know", (b) "reviewed for hours, then paywall", (c) "deleted photos I wanted", (d) "it said my phone was full". Count each per app over the last 12 months to size differentiators 1 and 2.
5. **Do Cleanup's paywall badges "611 / 329" reflect a real pre-scan?** If they do, Cleanup does show a partial real problem before payment, which changes the "Killed" verdict to "partly". Test with a near-empty photo library.
6. **Rating prompt timing** (the overview reports a post-delete ask in Cleanup) and **notification content** after day 1: needs a 3–7 day hands-on.
7. **What fraction of a typical US user's storage is photos and videos?** If it is often small (as on this phone), our honest "you can free 1.9 GB" may convert worse than fake "80%". Test in stage C with a fake-door or a creative test.
8. **Missing captures to retake:** Cleanup welcome/permission (#0), Clever IMG_2277, Cleaner Kit IMG_2265, plus all four apps' post-paywall core task, result, and settings screens.

**Next stage:** A2/A4/A6 for these four (listing.json plus negatives.md via `scripts/fetch-app.py`), then B Market.
