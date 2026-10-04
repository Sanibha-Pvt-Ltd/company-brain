---
type: app
category: storage-cleaner
app: "Cleanup: Phone Storage Cleaner"
app_store_id: 1510944943
member: ganesh
run_by: harshil
updated: 2026-10-04
status: draft
scope: screens-only
screens_analysed: 10
reviews_analysed: 0
sources: [screenshots:10, ganesh-benchmark-xlsx, itunes-lookup-us]
---

# Cleanup: Phone Storage Cleaner (category winner)

Screens: `ganesh_screenshots/Storage Cleaners/Cleanup: Phone Storage Cleaner/` IMG_2233–2242, India storefront, captured on or about 2026-10-03 `[INFERRED: the paywall shows "Due 10 October 2026" after a 7-day trial]`. Context: [[research/categories/storage-cleaner/overview]] · [[members/ganesh/drafts/storage-cleaner/screens-synthesis]]

## A1 Snapshot (short)

| Field | Value |
|---|---|
| Developer | DEEP FLOW SOFTWARE SERVICES - FZCO `[DATA:itunes-lookup-us 2026-10-04]` |
| US price | Free with IAP `[DATA:itunes-lookup-us 2026-10-04]` |
| US rating | 4.65 from 728,417 ratings `[DATA:itunes-lookup-us 2026-10-04]` |
| Version | 6.22.0, released 2026-09-22. First release 2020-12-05 `[DATA:itunes-lookup-us]` |
| Lead promise in onboarding | "Delete Duplicate Photos", then "Optimize iPhone Storage", then "Clean Your Email Inbox" `[OBSERVED #1–#3]` |

## A2 Business performance
Not in this run (screens-only). For desk estimates see the overview, §4.

## A3 Monetization (from screens)

- **Model on screen:** a weekly subscription with a 7-day trial, plus a lifetime option. "Free for 7 days, then ₹999.00/week" `[OBSERVED #6]`. "₹999.00/week, cancel anytime / 7-day FREE TRIAL" and "₹3,999.00, Lifetime" with the badge "Save 89%" `[OBSERVED #9]`. These are **India storefront** prices. The US price was not captured: `[UNKNOWN]`. To find it, take a US-storefront capture or read the listing's IAP list.
- **Touchpoints:** two paywalls. The first is a full-screen onboarding paywall after a 2-screen "Try 7 days / For free!" interstitial (#5–#6). The second, "Unlock Unlimited Access" (#9), appears after the home screen. Possibly it is triggered by tapping a feature or the PRO button `[UNKNOWN which]`.
- **Dismissability:** on the onboarding paywall (#6) the only top-left text is "Restore Purchase", and no close control is visible in the capture `[OBSERVED]`. The user did reach home afterwards (#7), so an exit exists, but its form and delay are `[UNKNOWN]`. The second paywall has a visible ✕ top-left `[OBSERVED #9]`.
- **Default plan:** on #9 the weekly plan is the highlighted (selected) tile. The lifetime tile carries "Save 89%" `[OBSERVED]`.
- **Disagreement with Ganesh's xlsx:** the xlsx lists the offer as "₹999/yr (7-day free trial) or ₹3,999 Lifetime" `[DATA:ganesh-benchmark-xlsx]`. The screens show **₹999/week**, not per year `[OBSERVED #6, #9]`. Treat the xlsx price as a transcription error. Ganesh, please correct the row.
- Paywall SDK: `[UNKNOWN]` (not in scope).

## A4 Acquisition
Not in this run (screens-only).

## A5 Screens lens

### Per-screen table (capture order = journey order; no reordering needed)

| # | file | stage | what user sees | asks of user | gives to user | verbatim copy | lever | friction / dark pattern | tag |
|---|---|---|---|---|---|---|---|---|---|
| 0 | (missing) | welcome / permission priming | Partly visible behind #1 as it slides away: a "We… C…" title, the Photos icon, a red bar, "? of", "…eeds a…", "…ur priv…", "…ms of" | Probably Photos access `[INFERRED]` | Nothing yet | Not fully visible | Priming | Not captured, so this is a **gap** | `[OBSERVED fragment]` `[INFERRED]` |
| 1 | IMG_2233/2234 | onboarding 1/3 | Two near-identical selfies with a red check on one, then three photos with up-arrows | Tap Next | A picture of the promise | "Delete Duplicate Photos" / "Eliminate duplicate photos instantly and reclaim your storage!" | Simple demo | None | `[OBSERVED]` |
| 2 | IMG_2235 | onboarding 2/3 | Photos + iCloud icons; a storage bar with "? GB of 255 GB used"; Photos is the large red segment | Tap Next | Device capacity (255 GB is real) | "Optimize iPhone Storage" / "Free up to 80% of your storage and get more space." / "*Based on Cleanup internal data" | Authority, big number | "Up to 80%" is an unverifiable claim; the red Photos segment is a drawing, not this phone's real split | `[OBSERVED]` |
| 3 | IMG_2236 | onboarding 3/3 | Mail icon with a "7.002" badge and a red bar | Tap Next | Nothing | "Clean Your Email Inbox" / "Delete spam and promotional emails with just one tap." | Scope creep: a second job | The 7.002 badge is canned and reads like an alarm | `[OBSERVED]` |
| 4 | IMG_2237/2238 | pre-paywall interstitial | Animated text on a blank screen | Nothing; it auto-advances `[INFERRED]` | Primes "free" | "Try 7 days" → "For free!" | Framing free before showing the price | Price anchoring hidden behind "free" | `[OBSERVED]` |
| 5 | IMG_2239 | paywall 1 (onboarding) | Photos badge "611" and iCloud badge "329"; a full red bar; a plan card; a timeline | Start trial | Counts (611/329) of unknown origin | "Clean your Storage" / "Get rid of what you don't need" / "95 from 100% used" / "Cleanup Pro: Smart Cleaning, Video Compressor, Secret Storage, Manage Contacts, No Ads and Limits." / "Free for 7 days, then ₹999.00/week" / "Free trial enabled" / "Due today ₹0.00 · Due 10 October 2026 ₹999.00" / "Try Free" / "Secured with Apple" | Fear (a full bar), urgency, a "free" CTA | **"95 from 100% used" is false for this device**: the same phone reads 120 GB / 255 GB used (~47%) in two other apps (Phone Storage Cleaner #10, Clever Cleaner #6). No close control visible. "Free trial enabled" is pre-set. The weekly price is in small print under a "Try Free" CTA | `[OBSERVED]` `[INFERRED: cross-app device reading]` |
| 6 | IMG_2240 | permission | iOS notification prompt over the dimmed home screen | Allow notifications | By now: a home screen showing "5.0 GB Space to Clean", but no clean done | "\"Cleanup\" Would Like to Send You Notifications" | Habit loop setup | Asked before any value is delivered | `[OBSERVED]` |
| 7 | IMG_2241 | home / core | "5.0 GB Space to Clean" with a red bar; an "Optimize Storage" banner; "Similars" cards ("New photos (918.3 MB)"); "Duplicates 0 Photos"; "Similar Videos"; "Similar Screenshots" ("New photos (19.8 MB)"); tab bar: Home, Email, Contacts, Optimize, Extras; PRO button | Choose a category | **First real scan result: 5.0 GB found** | "5.0 GB Space to Clean" / "See Analysis" / "Optimize Storage — Free up to 2 GB from your files quickly" / "Duplicates 0 Photos" | Real, specific number (earned) | 5 tabs, 4+ photo categories and a PRO badge on the first view. The red bar again signals danger. The "Duplicates 0" card is dead weight | `[OBSERVED]` |
| 8 | IMG_2242 | paywall 2 (upsell) | Three benefits, a 5★ testimonial carousel, two plan tiles | Start trial or close | Nothing new | "Unlock Unlimited Access" / "Instantly Detect Similar Photos" / "No Ads and Limits" / "Save Both Storage & Time" / "₹999.00/week, cancel anytime · 7-day FREE TRIAL" / "₹3,999.00, Lifetime · Save 89%" / "Start my 7-day free trial" | Social proof; "Save 89%" anchoring on lifetime | Weekly preselected. "Save 89%" compares lifetime against an unknown number of weeks | `[OBSERVED]` |

Not captured (**gaps**): the welcome/permission screen (#0); the iOS Photos permission dialog; any category review screen; any delete action; any "space freed" result; any rating prompt. The overview (S13) reports a rating ask after deletion in a third-party walkthrough. We cannot confirm it from our screens.

### The 8 measures

1. **First win.** The first moment of *found* value is home #7: "5.0 GB Space to Clean" `[OBSERVED]`. That is about 7 taps (Next ×3, welcome ×1, the trial interstitial, an exit from the paywall, the notification prompt) and comes **after** paywall 1. A *freed*-GB moment is not in the captures `[UNKNOWN]`. So the true first win (GB actually freed) is either behind paywall 2 or uncaptured. Next step: a hands-on test to see whether a free user can delete anything.
2. **Ask ledger.**

   | Order | Ask | What the user had received by then |
   |---|---|---|
   | 1 | Photos access (probably on #0) `[INFERRED]` | Nothing |
   | 2 | 3 × Next through the carousel | Promises only |
   | 3 | Start a ₹999/week trial (#5) | A fake "95 from 100% used" plus unexplained counts |
   | 4 | Notifications (#6) | Nothing; no clean done yet |
   | 5 | Start a trial again (#8) | A found-GB number (5.0 GB) and category previews |

   Four asks come before anything is cleaned. That run of asks with nothing given back is the main finding.
3. **Abstractions.** Similars vs Duplicates (the job needs one "repeats" concept, so this split is invented; Duplicates shows 0). Similar Videos and Similar Screenshots as separate buckets (a filter, not a concept). "Optimize" (meaning compression; it gets its own tab). "Secret Storage" (an invented, unrelated vault). Email cleaner (a different job). Contacts (an adjacent job). "Extras" (an invented catch-all). "PRO". "See Analysis". That is about 8 concepts on day 1, of which the job needs about 2: *repeats* and *big stuff*. `[OBSERVED #5, #7]` `[INFERRED: needed vs invented]`
4. **Feel-good moments.** "5.0 GB Space to Clean" is **earned**, a real scan of this library. Photo thumbnails of the user's own moon shots in "Similars" are earned and personal. The testimonial on #8 ("So much faster than I could do one by one!") is manufactured social proof but harmless.
5. **Feel-bad moments.** "95 from 100% used" (#5) on a phone that is about 47% full is **manufactured fear**, the worst item in this flow. Red bars appear on every storage visual (#2, #5, #7). The canned "7.002" mail badge (#3). "For free!" (#4) primes a ₹999/week product. "Free trial enabled" is pre-set (#5). No visible close on #5.
6. **Paywall.** Soft paywall, shown twice. Placement: onboarding end, before the real scan result. The weekly plan is the default, with the price shown as "₹999.00/week" in secondary text. The trial is a 7-day free trial with a "Due today ₹0.00" timeline (this timeline is honest and good). Lifetime is ₹3,999. No downsell was observed. Prices are India storefront.
7. **Repeat cost.** Home puts categories one tap away, with "New photos (918.3 MB)" chips that suggest an incremental scan of new photos since last time (a good return hook) `[OBSERVED #7]` `[INFERRED]`. Return triggers: notifications (asked on #6). Widget and streak: `[UNKNOWN]`.
8. **Feature map.**
   - **Table stakes:** similar/duplicate photo groups, similar screenshots, video compression, storage readout.
   - **Differentiators:** the "New photos (X MB)" incremental chips; email cleanup as a second ad angle (overview §6.1); breadth.
   - **Bloat:** Secret Storage, Extras, a separate Duplicates card at 0, Contacts in the main tab bar, the email tab for a storage job.

## Keep / Kill / Different

**Keep**
- The real, single-number scan result as the hero ("5.0 GB Space to Clean", #7).
- The "New photos (918.3 MB)" chips. They make the second visit cheap and give a real reason to return.
- The trial timeline "Due today ₹0.00 / Due 10 October 2026" (#5). It is honest and specific.
- A plain demo of the job in one picture (#1).

**Kill**
- The fake "95 from 100% used" meter (#5) and every canned storage or mail number (#2 "? GB", #3 "7.002").
- "For free!" interstitials ahead of a weekly price (#4).
- A paywall with no visible close control (#5), and a pre-set "Free trial enabled" (#5).
- The notification ask before anything has been cleaned (#6).
- Similars vs Duplicates as two concepts. Kill Secret Storage, Extras, and Email in a storage app (#5, #7).

**Different**
- Run the real scan first and show *this phone's* number ("4.9 GB you can free, of 120 GB used") before any price.
- Let the first clean finish for free (one category end to end), show "Freed 918 MB" with the new free space, then offer the plan.
- One "Repeats" concept (similar + duplicate merged, best shot pre-picked) and one "Big stuff" concept (videos, Live Photos). Nothing else on the first screen.
- Ask for notifications only after the first freed-GB moment, framed as "Tell me when new clutter passes 500 MB".

## A6 Failure mining
Not in this run (screens-only). The 3 reviews in Ganesh's xlsx point at billing ("charged… every 7 days. 6.41 every week") and "ghost files" after cancelling `[DATA:ganesh-benchmark-xlsx]`. These are leads for review mining, not a sample.

## A8 Verdict (short)

Cleanup wins on a fast path to a big, real number (5.0 GB found on home) and on breadth (photos, video, email, contacts) that feeds many ad angles. Its onboarding leans on manufactured fear ("95 from 100% used" on a ~47%-full phone) and on a weekly price behind "free" framing, with four asks before any cleaning. **Copy:** the scan-number hero, the incremental "New photos" chips, the honest trial timeline. **Beat:** the fake meter, the concept sprawl (8 concepts and 5 tabs), and asks before value. **Most exploitable weakness:** its paywall claims the phone is nearly full when it isn't. An app that shows the true reading and still finds GB wins on trust.

Evidence strength: A3 **medium** (screens clear; US price unknown; exit path for #5 unknown) · A5 **medium** (no clean or result screens captured).
