---
type: app
category: storage-cleaner
app: "Cleaner Kit - Clean Up Storage"
app_store_id: 1194582243
member: ganesh
run_by: harshil
updated: 2026-10-04
status: draft
scope: screens-only
screens_analysed: 6
reviews_analysed: 0
sources: [screenshots:7 (6 in-app + 1 App Store page), ganesh-benchmark-xlsx (row match uncertain), itunes-lookup-us]
---

# Cleaner Kit (BP Mobile)

Screens: `ganesh_screenshots/Storage Cleaners/Cleaner Kit - Clean Up Storage/` IMG_2264, 2266–2271 (**IMG_2265 missing**), India storefront. IMG_2264 is the **App Store product page**, not the app. It is used only as proof of capture context (India listing: "39K RATINGS 4.4", "Utilities") and is excluded from the screen analysis per the source rule. Context: [[research/categories/storage-cleaner/overview]] · [[members/ganesh/drafts/storage-cleaner/screens-synthesis]]

**xlsx row match is uncertain.** The only BP Mobile LLC storage row is named "Storage Cleaner*". It says "After Photo Scan · ₹1,499/yr (3-day trial) or ₹3,499 Lifetime" `[DATA:ganesh-benchmark-xlsx]`. The screens show neither of these (see A3). It may be another BP Mobile app, or the row is outdated. Ganesh to confirm.

## A1 Snapshot (short)

| Field | Value |
|---|---|
| Developer | BP Mobile LLC `[DATA:itunes-lookup-us]` |
| US price | Free with IAP `[DATA:itunes-lookup-us]` |
| US rating | 4.44 from 351,373 ratings `[DATA:itunes-lookup-us 2026-10-04]` (India: "39K RATINGS 4.4" `[OBSERVED IMG_2264]`) |
| Version | 5.32, released 2026-09-30. First release 2017-01-26 `[DATA:itunes-lookup-us]` |
| Lead promise | "Welcome to Cleaner Kit" + "240 GB of 256 GB used" `[OBSERVED #1]` |

## A2 Business performance
Not in this run (screens-only).

## A3 Monetization (from screens)

- **Three plans on one paywall** `[OBSERVED #6]`:
  - "MONTHLY · 12-month commitment (₹11,748.00 total) · ₹ 979 per month", tagged **"MOST POPULAR"** and highlighted.
  - "YEARLY · ₹4,999.00/year · just ₹95.88/week".
  - "WEEKLY · Free for 7 days, then ₹699.00/week".
  - All India storefront; US prices are `[UNKNOWN]`. Sensor Tower lists US weekly products of about $4.99–$6.99 (overview S10) `[ESTIMATE]`.
- **The "monthly" plan is an annual commitment billed monthly**, at ₹11,748 a year: 2.35× the yearly plan's ₹4,999. It is labelled "MOST POPULAR" and visually selected. This is the most aggressive price framing in the set `[OBSERVED]` `[INFERRED: the ratio is arithmetic]`.
- Yearly is reframed as weekly ("just ₹95.88/week"), the price-per-small-unit trick.
- **Dismissability:** no close control is visible on #6 `[OBSERVED]`. Delay or hidden ✕: `[UNKNOWN]`. Footer: "Auto-renewable. Cancel anytime." and "Cancel anytime".
- Further offers or downsells after closing: `[UNKNOWN]` (not captured). The overview's walkthrough (S15) reports additional offers after the first paywall.

## A4 Acquisition
Not in this run. The India product page shows "Featured by Apple" and "70M+ users" in its screenshot set `[OBSERVED IMG_2264]` (listing art, so not used for the screens lens).

## A5 Screens lens

### Per-screen table

| # | file | stage | what user sees | asks of user | gives to user | verbatim copy | lever | friction / dark pattern | tag |
|---|---|---|---|---|---|---|---|---|---|
| — | IMG_2264 | App Store page (excluded) | Product page | — | — | — | — | — | `[OBSERVED]` |
| — | IMG_2265 | (missing) | — | — | — | — | — | **Gap**: possibly the launch or splash | `[UNKNOWN]` |
| 1 | IMG_2266 | welcome 1/5 | Photos + iCloud icons; a striped red bar | Get Started (and accept the terms) | A canned crisis | "Welcome to Cleaner Kit" / "240 GB of 256 GB used" / "By continuing, you accept our Terms of Use and Privacy Policy." / "Get Started" | Fear | **Fake**: this phone is 255 GB with about 120 GB used (Phone Storage Cleaner #11, Clever Cleaner #6) `[INFERRED cross-app]` | `[OBSERVED]` |
| 2 | IMG_2267 | onboarding 2/5 + permission | A duplicate-photo pairs demo; the iOS notification prompt fading over it | Allow notifications | A demo | "Clear Duplicate Photos" / "Remove repeated shots instantly to free up space" / "\"Cleaner Kit\" Would Like to Send You Notifications" | — | Notifications asked on screen 2, before anything | `[OBSERVED]` |
| 3 | IMG_2268 | onboarding 3/5 | Floating photos; an iPhone storage bar | Next | A claim | "Optimize iPhone Storage" / "Reclaim up to 80% of your space" / "iPhone 240GB of 256 GB used" / "*Based on internal data from Cleaner Kit" | Authority | The same "up to 80%" claim and canned 240/256 as Cleanup #2 (a shared template?) `[INFERRED]` | `[OBSERVED]` |
| 4 | IMG_2269 | onboarding 4/5 | A Mail icon with a "2546" badge and an orange bar | Next | Nothing | "Clean Out Your Inbox" / "Remove spam and promotional emails in one tap" | Scope creep | A canned badge | `[OBSERVED]` |
| 5 | IMG_2270 | onboarding 5/5 | Laurels; a stack of short testimonials | Next | Social proof | "800,000+ ★★★★★ 5-star ratings" / "\"Shrunk my videos and got back 50GB!\"" / "\"My contacts are cleaned up... so much better.\"" (alex_1990, **shown twice**) | Social proof | "800,000+ 5-star ratings" exceeds the US total of 351,373 ratings of all stars `[DATA:itunes-lookup-us]` and the India "39K". It may be a worldwide figure, but that is unverifiable `[INFERRED]`. The duplicated testimonial suggests filler | `[OBSERVED]` |
| 6 | IMG_2271 | paywall | 3 plans; "Continue" CTA | Pick a plan | Nothing from the user's phone | "Clean Up Your iPhone Fast & Easy" / "Get rid of junk, compress large videos, and clear contacts & calendar. Ad-free." / plans as in A3 / "Continue" / "Cancel anytime" | Decoy and anchor: "MOST POPULAR" on the most expensive plan | No visible close. A 12-month commitment disguised as "MONTHLY". The weekly-unit reframe | `[OBSERVED]` |

**Gaps:** IMG_2265; the Photos permission; everything after the paywall (home, scan, review, delete, result). **We have no in-app value screen for Cleaner Kit at all.**

### The 8 measures

1. **First win.** Not reached in the captures. At least 6 screens and taps elapse with zero real data about the user's phone, ending at a paywall with no visible exit `[OBSERVED]`. First win is `[UNKNOWN]`; capture past the paywall in a hands-on test.
2. **Ask ledger.**

   | Order | Ask | What the user had received by then |
   |---|---|---|
   | 1 | Accept the terms (#1) | A fake "240 of 256 GB" |
   | 2 | Notifications (#2) | Nothing |
   | 3 | 3 × Next (#3–#5) | Claims and testimonials |
   | 4 | Choose a paid plan, with no visible way out (#6) | Nothing real |

   Pure asks, zero gives.
3. **Abstractions** (from onboarding and paywall copy). Duplicates, iCloud, email inbox, contacts, calendar, "junk", video compression: 7 jobs promised before one is shown. Calendar cleanup in particular is invented scope for a storage job.
4. **Feel-good moments.** Testimonials (#5) are manufactured. "Fast & Easy" (#6) is a claim. None of them is earned.
5. **Feel-bad moments.** "240 GB of 256 GB used" in red (#1, #3) is fake fear. Notifications on screen 2. "MOST POPULAR" on a ₹11,748 12-month lock-in dressed as "MONTHLY" (#6). No visible close (#6).
6. **Paywall.** Hard-looking (no visible ✕), placed at the end of onboarding, before any scan. Three plans with decoy pricing. The trial exists only on weekly (7 days, ₹699/week). India storefront.
7. **Repeat cost.** `[UNKNOWN]`: no post-paywall screens.
8. **Feature map** (from the paywall copy only).
   - **Table stakes:** duplicates, video compress.
   - **Differentiators claimed:** contacts, calendar, email ("Ad-free").
   - **Bloat:** calendar, email for a storage job, the "junk" catch-all.

## Keep / Kill / Different

**Keep**
- Nothing on screen is worth copying as-is. The one usable idea: a "yearly" plan shown with its full price ("₹4,999.00/year"). Keep the plan, drop the per-week reframe.

**Kill**
- Fake capacity (#1, #3), notifications on screen 2 (#2), unverifiable "800,000+ 5-star ratings" and duplicated testimonials (#5).
- The "MONTHLY · 12-month commitment" decoy marked "MOST POPULAR" (#6). Nothing we ship will hide an annual commitment inside a monthly label.
- A paywall with no visible close (#6).

**Different**
- Zero claims before a real scan. Show the user's own number before any plan.
- At most 2 plans, each shown at its true billing period and total. Mark as "most popular" only the plan that actually is, in our own data.

## A6 Failure mining
Not in this run (screens-only). The xlsx BP Mobile row includes a 1★ review saying the contact merge "merged many entries that were for completely different people" `[DATA:ganesh-benchmark-xlsx]`, if that row is this app. It is a lead for review mining: destructive merges are a trust breaker.

## A8 Verdict (short)

Cleaner Kit is the incumbent bundle (since 2017, 351K US ratings) and runs the most aggressive funnel in the set. It shows fake capacity, asks for notifications on screen 2, cites unverifiable social proof, and ends at a three-plan paywall with a 12-month commitment labelled "MONTHLY" and no visible close, all before showing anything real. Its 4.44★ US rating is the lowest of the four `[DATA:itunes-lookup-us]`. **Copy:** nothing in the UI; the breadth only as an ad-angle list. **Beat:** every ask-before-value step. **Most exploitable weakness:** price framing users will feel cheated by once they notice (₹11,748 vs ₹4,999 for the same year). Confirm in review mining.

Evidence strength: A3 **strong** for the paywall screen itself · A5 **weak** (6 in-app screens, all pre-paywall; xlsx row match uncertain).
