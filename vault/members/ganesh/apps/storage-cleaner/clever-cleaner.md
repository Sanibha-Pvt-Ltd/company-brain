---
type: app
category: storage-cleaner
app: "Clever Cleaner: Photo Storage"
app_store_id: 1666645584
member: ganesh
run_by: harshil
updated: 2026-10-04
status: draft
scope: screens-only
screens_analysed: 7
reviews_analysed: 0
sources: [screenshots:7, itunes-lookup-us]
---

# Clever Cleaner (CleverFiles)

Screens: `ganesh_screenshots/Storage Cleaners/Clever Cleaner: Photo Storage/` IMG_2272–2279 (**IMG_2277 missing**), India storefront, captured at 3:01 on the same device as the other apps `[OBSERVED]`. The US listing title is now "Clever Cleaner: AI CleanUp App" `[DATA:itunes-lookup-us]`. Context: [[research/categories/storage-cleaner/overview]] · [[members/ganesh/drafts/storage-cleaner/screens-synthesis]]

**No row in Ganesh's xlsx.** Searching "5 Parameters Benchmark" found no CleverFiles row. The nearest, "Storage Cleaner •" by LILUCAT LTD, is a different developer and is not used here `[DATA:ganesh-benchmark-xlsx]`.

## A1 Snapshot (short)

| Field | Value |
|---|---|
| Developer | CleverFiles Inc. `[DATA:itunes-lookup-us]` |
| US price | Free with IAP `[DATA:itunes-lookup-us]` |
| US rating | 4.78 from 82,958 ratings `[DATA:itunes-lookup-us 2026-10-04]` |
| Version | 3.4, released 2026-09-14. First release 2025-02-27 `[DATA:itunes-lookup-us]` |
| Lead promise | "Smart ✦ Cleanup, Compress & Organize your Photo Storage." `[OBSERVED #2]` |

## A2 Business performance
Not in this run (screens-only).

## A3 Monetization (from screens)

- **Free tier stated before the paywall:** "Swipes Free" (#3) and "2 GB free daily" (#4) `[OBSERVED]`. It is the only app of the four that names its free allowance up front.
- **Plans:** "Weekly — 3 days free, then ₹ 699 per week" (preselected) and "Lifetime — Best Value — ₹ 3,999 pay once" `[OBSERVED #5]`. India storefront. The overview reports US products of $6.99 weekly and $39.99 lifetime from the listing (S5) `[ESTIMATE:overview S5]`. Not verified here.
- **Touchpoints:** the onboarding paywall as step 4 of 4 (#5), and the same paywall re-shown from home (#7, IMG_2279). The trigger for the re-show is `[UNKNOWN]`: possibly the "Premium" pill or a feature tap.
- **Dismissability:** ✕ visible top-right on first render `[OBSERVED #5, #7]`. Footer: "Auto-renewable. Cancel anytime".

## A4 Acquisition
Not in this run.

## A5 Screens lens

### Per-screen table

| # | file | stage | what user sees | asks of user | gives to user | verbatim copy | lever | friction / dark pattern | tag |
|---|---|---|---|---|---|---|---|---|---|
| 1 | IMG_2272 | permission | The ATT prompt fading over the welcome screen | Allow tracking | Nothing | "Allow \"Clever Cleaner\" to track your activity across other companies' apps and websites? …measure our app's advertising efficiency and will be used for anonymous analytics only." (partly legible) | Honest purpose copy | Tracking asked at second zero, before any value | `[OBSERVED]` |
| 2 | IMG_2273 | onboarding 1/4 | Floating sample photos with keep ✓ / delete ✕ badges | Continue | A visual of the job | "Welcome to Clever Cleaner" / "Smart ✦ Cleanup, ⇣ Compress & ☝ Organize your Photo Storage." / "1 of 4" | Clarity; "1 of 4" sets the length | None | `[OBSERVED]` |
| 3 | IMG_2274 | onboarding 2/4 | A swipe-card demo (thumbs up / trash) | Continue | **A free promise** | "Swipes [Free]" / "Transform your mess into organized enjoyable memories within minutes." / "2 of 4" | Free label; "memories" (care, not fear) | None | `[OBSERVED]` |
| 4 | IMG_2275 | onboarding 3/4 | Similars grid; a Compress before/after "827.5 MB → 299.9 MB, SAVE 527.6 MB" | Continue | **A free allowance, stated** | "[2 GB free daily]" / "Free up phone storage and make room for new memories." / "Similars — Remove similar photos and reclaim storage space." / "Compress — Free up space by compressing large videos, photos, and Lives." / "3 of 4" | A concrete MB example; reciprocity | The sample numbers are illustrative but clearly a demo (a car photo) | `[OBSERVED]` |
| 5 | IMG_2276 | paywall 4/4 | Premium header; a "Photo Storage — Almost Full" bar segmented Similars/Heavies/Screenshots/Lives; 2 plans | Start trial or ✕ | Nothing new | "Clever Cleaner Premium" / "Unlimited Smart Cleanup with Clever Cleaner Premium." / "Photo Storage · Almost Full" / "Weekly · 3 days free, then ₹ 699 per week" / "Lifetime · Best Value · ₹ 3,999 pay once" / "Start Free Trial" / "Auto-renewable. Cancel anytime" | Loss aversion ("Almost Full") | **"Almost Full" is false for this phone**: its own home (#6) says the Photo Library is 2% and 53% is free. Weekly is preselected | `[OBSERVED]` |
| — | IMG_2277 | (missing) | — | Probably the iOS Photos permission `[INFERRED]` | — | — | — | **Gap** | `[UNKNOWN]` |
| 6 | IMG_2278 | home / core | "Storage 120.28 GB of 255 GB used"; legend "Photo Library 2% · Data and apps 45% · Free 53%"; 3 actions (Smart cleanup, Swipe, Compress); cards Similars 1.35 GB, Videos 2.62 GB, Screenshots 283.1 MB, Live photos 12.5 MB; "Premium" pill. The paywall is visibly animating away | Pick an action | **A true storage breakdown, plus about 4.3 GB of reviewable items** | as listed | Honest framing (says photos are only 2%) | Three actions plus four cards is a lot of choices. "Heavies" and "Lives" are jargon (on #5) | `[OBSERVED]` |
| 7 | IMG_2279 | paywall (re-shown) | Same as #5 | Trial or ✕ | — | same as #5 | — | The re-show trigger is `[UNKNOWN]` | `[OBSERVED]` |

**Gaps:** IMG_2277 (the Photos permission, probably). No Swipe session, no Smart cleanup run, no delete, no "freed" screen, no capture of the daily-limit counter. So we can't see how "2 GB free daily" is metered or shown.

### The 8 measures

1. **First win.** Found value comes on home #6 (Similars 1.35 GB, Videos 2.62 GB) after about 5–6 taps (ATT, Continue ×3, ✕ on the paywall, Photos permission). That is **after** the paywall, but the paywall closes in one tap. Freed GB is not captured `[UNKNOWN]`, though the free 2 GB a day means a first freed-GB moment should be possible without paying `[INFERRED from #4]`.
2. **Ask ledger.**

   | Order | Ask | What the user had received by then |
   |---|---|---|
   | 1 | Tracking (ATT) (#1) | Nothing |
   | 2 | 3 × Continue (#2–#4) | A clear free-tier promise ("Swipes Free", "2 GB free daily") |
   | 3 | Trial (#5, closable) | Promises |
   | 4 | Photos access (gap) | — |

   This is the shortest pre-value run among the four, and the only one that gives *a commitment* (the free allowance) before asking for money.
3. **Abstractions.** Smart cleanup vs Swipe vs Compress (3 modes; the job needs maybe 2: "review repeats" and "shrink big stuff"). "Heavies" and "Lives" (jargon). Similars. "Premium". A daily GB quota is a currency-like concept; it is honest but is still one more thing to learn `[INFERRED]`.
4. **Feel-good moments.** "Transform your mess into organized enjoyable memories" (#3) speaks to care and identity, not fear. The free badges (#3, #4) earn trust. The home storage legend "Photo Library 2%" (#6) is honest even though it shrinks the app's own value. The "SAVE 527.6 MB" demo is a concrete preview.
5. **Feel-bad moments.** "Almost Full" in red on the paywall (#5) contradicts the app's own home ("Free 53%"). That is manufactured fear, even in the most honest app. ATT at second zero (#1). Weekly preselected over lifetime (#5).
6. **Paywall.** Soft paywall: ✕ visible immediately. It comes at the end of a 4-step onboarding, after stating the free tier. Two plans: weekly ₹699 with a 3-day trial (default) and ₹3,999 lifetime ("Best Value"). India storefront. No downsell seen.
7. **Repeat cost.** Home has 3 round action buttons plus category cards with GB, so 1 tap to a task. Swipe is free and unlimited per the overview (S28) `[ESTIMATE:overview]`, which is a repeat-use hook. Notifications were not asked in the captures; widget `[UNKNOWN]`.
8. **Feature map.**
   - **Table stakes:** similars, video compress, screenshots, storage readout.
   - **Differentiators:** free Swipe and a stated daily free GB; the honest storage breakdown; compression of Live Photos.
   - **Bloat:** three overlapping entry modes on day 1.

## Keep / Kill / Different

**Keep**
- Stating the free tier before the paywall ("Swipes Free", "2 GB free daily", #3–#4).
- The ✕ visible on first render (#5), and lifetime offered next to weekly.
- The true storage breakdown on home (#6), "Photo Library 2% · Data and apps 45% · Free 53%".
- "Memories" language over "junk" language (#3, #4).

**Kill**
- "Almost Full" on the paywall (#5) when the app's own home says 53% free.
- ATT as the very first screen (#1).
- Jargon: "Heavies", "Lives" (#5). Three modes on the home row (#6).

**Different**
- Keep the honesty, but turn it into the first-run payoff: "Your photos use 5 GB. Here are 1.3 GB of near-repeats, ready to go." That is one screen, one action.
- Replace the daily GB quota with "your first clean is free, all of it". One rule, no currency to learn. Charge for ongoing and automatic cleaning.
- Offer annual (not only weekly or lifetime) to fit occasional-cleanup behaviour. Validate this in stage B.

## A6 Failure mining
Not in this run (screens-only).

## A8 Verdict (short)

Clever Cleaner is the most honest flow in the set. It names its free tier before asking, makes the paywall closable, and on home admits that photos are only 2% of the phone. Yet even it fakes "Almost Full" on the paywall. Its 4.78★ with 83K ratings in about 19 months `[DATA:itunes-lookup-us]` suggests honesty does not cost ratings. Revenue impact is `[UNKNOWN]`. **Copy:** the stated free tier, the visible ✕, the honest breakdown. **Beat:** the three-mode home, the jargon, and the fake "Almost Full". **Most exploitable weakness:** the free tier is a metered quota (2 GB a day) that users must understand. "First clean free" is simpler and feels more generous.

Evidence strength: A3 **medium** · A5 **medium-weak** (7 screens, one gap, no core-task screens).
