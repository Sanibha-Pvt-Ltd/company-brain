---
type: category-product-strategy
category: storage-cleaner
member: harshil
updated: 2026-10-05
status: draft
sources: [context.md, screenshots:52 across 6 apps, knowledge base, Apple docs]
---

# Storage Cleaner — final recommendations (v1)

Reasoning and evidence: [[members/harshil/drafts/storage-cleaner/product-strategy-evidence]]. Built on [[research/categories/storage-cleaner/context]].

## Positioning

**Positioning statement**
For iPhone owners who just hit "storage full" and are afraid of deleting the wrong photo, KeepSpace is the storage cleaner that shows what is really filling your phone — measured on your phone, biggest first — and deletes only what you approve.

**Messaging**

| Layer | Message |
|---|---|
| Line | Make space. Keep what matters. |
| Acquisition hook | See what's really filling your iPhone. |
| Differentiator | Real numbers. Nothing deleted without your OK. |
| Emotional benefit | Keep what matters. |
| Retention reason | New clutter since last time, plus space still waiting in Recently Deleted. |

**Target user**
- iPhone owner at the "storage full" moment.
- Afraid of losing photos and of surprise charges.
- Searches "storage cleaner", "phone cleaner", "clean iPhone".

**Name:** KeepSpace — placeholder until cleared.

**Proof the user sees in the product**
1. True device storage on the very first screen, with a "How we measured" sheet.
2. Every size is measured, or marked "≈".
3. A one-line reason on every suggested group.
4. Favourites protected by default.
5. Result reads "moved to Recently Deleted; frees after 30 days or when you empty it".
6. Paywall shows price, period, renewal date and what's free vs paid, with the X visible immediately.

**App Store screenshots** — one consistent UI language across all six.

| # | Headline / content |
|---|---|
| 1 | **Measure:** real storage bar + "Your biggest videos" |
| 2 | **Choose:** a similar-photo group with its reason ("Suggested keep: sharpest of 4. You decide.") |
| 3 | **Done:** review tray + "moved to Recently Deleted" result |
| 4 | "Find the videos taking up the most space." — videos ranked by size with previews |
| 5 | "Your camera roll, finally organized." — screenshots, near-duplicates, utility images |
| 6 | "A little cleaner every week." — weekly review, cleanup history, new clutter |

- All figures in store shots come from a real demo phone and are captioned as such.
- No user counts, ratings, "Featured by Apple" or "joined today" badges.

**Ad angles**

| Role | Angle | Ad message |
|---|---|---|
| Control | Storage emergency | "Your storage is full again? See which photos and videos are taking up space." |
| Differentiator | Deletion anxiety | "Not every similar photo is a duplicate. Compare the pictures before you decide what to delete." |
| Challenger | "One iPhone, six cleaners" truth test | Each competitor's storage claim vs iOS Settings on the same phone, then ours. |
| Later | Screenshot graveyard | Held for a later custom product page test. |

**We never claim**
- A device "% full" / "% used" we didn't read.
- "Free up to N%".
- Faster, boost, overheating, RAM, junk or cache cleaning.
- iCloud, system data or "other storage" cleaning.
- "Freed" at the moment of deletion.
- Recovery after Recently Deleted is emptied.
- User counts, ratings or social-proof badges.

## UI/UX

**Design principles** (tie-breakers for every design decision)
1. Every number is measured, or marked "≈".
2. Give before you ask: no permission or payment before the user sees something real.
3. Biggest win first.
4. Every suggestion shows a one-line reason; the user decides.
5. Say when the space comes back.
6. Max four categories on home, one idea per screen.
7. Calm, not alarm: red only on the Delete button.

**App structure**
- **Clean** tab (home):
  - true storage line at top;
  - categories ordered by GB: Videos, Similar, Screenshots & utility, Duplicates.
- **History** tab:
  - past cleanups;
  - GB still waiting in Recently Deleted.
- **Settings** (gear icon): plan, protected items, notifications, "How we measure".
- **Review tray:** persistent bottom bar showing selected items and total GB.
- Not in the app: Email, Contacts, Vault, Swipe, Tools tabs.

**First five minutes**

| # | Screen | What's on it | Primary action | Taps |
|---|---|---|---|---|
| 1 | Welcome | Device's real used/free storage; "We clean photos and videos" | Scan my photos | 1 |
| 2 | Photos pre-prompt | "Analysed on this iPhone · nothing uploaded · nothing deleted without your OK" | Continue | 2 |
| 3 | iOS Photos prompt | System dialog | Allow | 3 |
| 4 | Progressive scan | Live counts; videos appear first; can open Videos early | — | — |
| 5 | Clean (home) | Categories by GB, "≈" where estimated | Open top category | 4 |
| 6 | Large videos | Size · duration · date; tap to play full preview | Select | 5 |
| 7 | Review tray → iOS confirm | Total GB; "Moves to Recently Deleted for 30 days" | Delete N items | 6–7 |
| 8 ★ | Result — first win | "X GB moved to Recently Deleted" + how to empty it now; optional reminder toggle | Done / Show me how | 7 |
| 9 | Soft paywall | What you did, what's left (real GB), free vs paid, plans, X | Choose or close | — |

**Key screens**

| Screen | Most important element | States to design |
|---|---|---|
| Clean (home) | True storage line | Scanning (progressive); limited access; nothing to clean ("the rest is apps and system data, which iOS manages"); permission denied; error / resume |
| Large videos | Size + full preview; paid "Compress instead" with before/after sizes | iCloud-only ("≈ size, in iCloud"); no large videos |
| Similar group | Reason line ("Suggested keep: sharpest of 4") + user toggles; favourites marked "Protected" | Group of 2; all protected; user overrides the suggestion |
| Review tray | "Nothing has been deleted yet." Total GB. "Moves to Recently Deleted for 30 days. Deleting syncs to all devices using iCloud Photos." The only red button | Empty; user cancels the system confirm |
| Result | "moved" + 2-step guide to empty Recently Deleted | Partial failure (name the items); free allowance reached → paywall |
| Paywall | Plans with price, period, renewal date; X visible | Offline; purchase pending; already subscribed; not trial-eligible |

**Permissions**
- **Photos:**
  - asked after our own pre-prompt;
  - limited access: scan only the selected items, show a banner to expand access, suppress the automatic iOS limited-access alert;
  - denied: still show true device storage, plus an "Open Settings" card.
- **Delete:** each review is one batched delete with one iOS confirm.
- **Notifications:** only as an opt-in toggle on the result screen.
- **Tracking (ATT):** not at launch; if needed later, ask only after the first win.

**Day 2 and beyond**
- History shows "X GB still waiting in Recently Deleted" and "New since last clean".
- Optional weekly review reminder.
- When nothing's new: "You're all caught up."
- No streaks, no health score, no fear notifications.

**Paywall**
- **Type:** soft.
- **When:**
  - after the first result;
  - when a selection goes past the free daily allowance.
- **Close:** X visible from the first frame.
- **Plans to test:** annual + monthly vs annual + lifetime. No weekly plan at launch. Prices set later from US paywall captures.
- **Trials:**
  - any trial shows a dated timeline with the charge date;
  - no "trial enabled!" interstitial;
  - no pre-selected weekly plan;
  - the no-trial price is shown plainly to users who aren't trial-eligible.
- **Cancel:** one line explaining how to cancel, mirroring Apple's sheet.
- **Free users keep:** full scan and all sizes, every preview, deletes up to a daily allowance, History.

**Visual language** (direction only; final tokens from brand-designer)
- Follow system light/dark; store shots light-led.
- One calm accent colour; neutral storage bars; red only on Delete.
- Real photos shown large; no decorative "AI" art or orbit graphics.

**Voice and copy**
- **Tone:** plain, specific, calm.
- **Lines we ship:**
  - "Nothing is deleted until you tap Delete."
  - "These look alike. We suggest keeping the sharpest one. You decide."
  - "≈ means estimated. Tap to see how we counted."
  - "X GB moved to Recently Deleted. It frees up after 30 days, or now if you empty it."
- **Copy we never use:**
  - "Free up to 80% of your storage"
  - "Almost Full" (when it isn't)
  - "50% faster"
  - "3-day free trial is enabled!"
  - "2558 people have joined today!"

**Accessibility**
- Dynamic Type everywhere, including plan cards.
- VoiceOver reads each thumbnail's type, date, size and selection state, and each group's reason.
- AA contrast; solid size chips.
- Reduced Motion swaps animation for counters.
- "≈" is never shown by colour alone.

**Patterns we refuse**
- Fake or alarm storage figures.
- "Up to N%" claims.
- "*Based on internal data" stat screens.
- Performance claims.
- Trial interstitials.
- Paywalls without a visible close button.
- A commitment plan labelled "most popular".
- An unexplained "Save 89%".
- Badge counts that change between views.
- Permission prompts before value.
- Unprovable social proof.

## v1 product features

| # | Feature | What it does | Free / paid | Size |
|---|---|---|---|---|
| 1 | True storage overview | Real device used/free on screen 1, with a "How we measured" sheet | Free | S |
| 2 | On-device scan | Progressive and resumable; nothing uploaded; results stream in, videos first | Free | L |
| 3 | Large videos | Ranked by size; duration, date, full-screen preview | Free to view; delete within allowance | M |
| 4 | Similar photos | Grouped; suggested keep with a one-line reason; user toggles each photo | Within allowance | L |
| 5 | Exact duplicates | Identical copies grouped for fast bulk review | Within allowance | S |
| 6 | Screenshots & utility images | Grouped by age; receipts, documents and other utility shots | Within allowance | S |
| 7 | Protected favourites | Favourites never auto-selected; user can protect any item | Free | S |
| 8 | Review tray + batched delete | One tray, total GB, one confirm, one batched delete | Free | M |
| 9 | Honest result + History | "Moved to Recently Deleted" result, guide to empty it, cleanup history | Free | S |
| 10 | Video compression | One preset; before/after size; saves the new copy, then deletes the original with confirm. First cut if late | Paid | M |
| 11 | New since last clean | Detects new clutter; optional weekly reminder | Reminder free; weekly bulk paid | S |
| 12 | Paywall + free allowance | StoreKit 2; soft paywall; daily free delete allowance | — | M |

**Free vs paid**
- **Free:** see everything filling the phone with true numbers, preview and compare everything, delete up to a daily allowance, learn how to get the space back.
- **Paid:** unlimited cleanup, video compression, weekly review.

**Build notes**
- Start the scan engine (2) and similar photos (4) in week 1 — they're the two large items.
- Week-1 on-device spike on file sizes:
  - exact sizes via `PHAssetResource.dataSize` on iOS 27+;
  - byte-streaming fallback on older iOS;
  - if the fallback is too slow, show counts + "≈" and set the minimum iOS version.
- Video compression is the release valve if the schedule slips.

**Later (v1.1+) and what triggers each**

| Feature | Bring in when |
|---|---|
| Swipe mode | Users ask to hand-sort, or D7 lags while scan → delete is healthy |
| Widget | D7/D30 return is the weakest funnel step |
| Screenshot topics | The screenshot-graveyard store-page test wins |
| Live Photo → still | Live Photos turn out to be a meaningful GB share |
| Contacts merge | Repeated user demand |
| Weekly plan | Annual/monthly can't reach payback |

**Not building:** email cleaning, contacts/calendar, private vault, iCloud cleaning, boost/speed/RAM/junk/cache, "AI categories" tiles, health score.

**v1 success metrics**
1. Photos permission grant rate.
2. Scan → first approved delete in session 1.
3. Install → paid conversion.
4. Refund rate and share of 1–2★ reviews mentioning "charged" / "scam".
5. Share of moved GB actually freed within 7 days.
6. Primary money metric: D30 net proceeds per install.

Targets are set after the first cohort.

## New recommendations

1. **"One iPhone, six cleaners" truth test**
   - Each competitor's storage claim vs iOS Settings on one phone, then ours.
   - Use as launch PR and challenger ad.
   - Test: one organic short + one Meta creative vs the control ad.
2. **Lead with videos, not duplicates, everywhere:** onboarding, home order, store shot 1.
3. **Recently Deleted as the day-2 return reason**, with an opt-in reminder to empty it.
4. **Week-1 file-size spike** before any UI is final.
5. **"How we measured"** sheet behind every number, in-app and in store shots.
6. **Launch without the tracking prompt;** Apple Ads first.

## Before build

1. Ganesh captures:
   - competitors' Photos permission, scan, delete and result screens;
   - US-storefront paywalls;
   - a screen recording to time close-button delays;
   - Swipewipe, Cleaner Guru and AI Cleaner.
2. Set US prices from the captured US paywalls.
3. Run brand-designer (name + visual), ux-designer (key screens above) and s1-spec on this note.
4. Bharat signs off → promote to `research/categories/storage-cleaner/`.
