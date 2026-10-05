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

**Store copy lines** (ASO agent fits to field limits)
- Subtitle candidate: "Make space. Keep what matters."
- Promotional text: "See what's really filling your iPhone. Biggest videos first. Nothing is deleted until you say so."
- Description opener: "KeepSpace measures your photos and videos on your iPhone, shows the biggest first, and moves only what you approve to Recently Deleted."
- Any privacy sentence ("analysed on this iPhone", "nothing uploaded") ships only if the build and the privacy label match it.

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

| # | Caption (exact) | Screen shown | Demo state it needs |
|---|---|---|---|
| 1 | See what's really filling your iPhone. | Real storage bar + "Your biggest videos" | Real demo phone; videos ranked by size; one "≈" chip visible |
| 2 | These look alike. You decide. | A similar-photo group with its reason ("Suggested keep: sharpest of 4. You decide.") | Group of 3–4 with one favourite shown as "Protected" |
| 3 | Nothing is deleted until you tap Delete. | Review tray + "moved to Recently Deleted" result | Tray with total GB and the red Delete button; result line visible |
| 4 | Find the videos taking up the most space. | Videos ranked by size with previews | Duration and size chips, one iCloud badge |
| 5 | Your camera roll, finally organized. | Screenshots, near-duplicates, utility images | Group headers with counts and GB |
| 6 | A little cleaner every week. | Weekly review, cleanup history, new clutter | History with one past cleanup and "New since last clean" |

- All figures in store shots come from a real demo phone and are captioned as such.
- No user counts, ratings, "Featured by Apple" or "joined today" badges.
- Shots 1–3 read as one story: Measure, Choose, Done.

**Ad angles**

| Role | Angle | Ad message | First 3 seconds | Lands on |
|---|---|---|---|---|
| Control | Storage emergency | "Your storage is full again? See which photos and videos are taking up space." | The iPhone storage warning appears | Store shot 1 |
| Differentiator | Deletion anxiety | "Not every similar photo is a duplicate. Compare the pictures before you decide what to delete." | Near-identical photos where the small differences matter | Custom product page led by "These look alike. You decide." |
| Challenger | "One iPhone, six cleaners" truth test | Each competitor's storage claim vs iOS Settings on the same phone, then ours. | Split screen: competitor figure vs iOS Settings | Store shot 1 |
| Later | Screenshot graveyard | Held for a later custom product page test. | — | — |

- Truth-test footage is a real screen recording with date and device shown; s6 reviews comparative claims before it runs.

**We never claim**
- A device "% full" / "% used" we didn't read.
- "Free up to N%".
- Faster, boost, overheating, RAM, junk or cache cleaning.
- iCloud, system data or "other storage" cleaning.
- "Freed" at the moment of deletion.
- Recovery after Recently Deleted is emptied.
- User counts, ratings or social-proof badges.
- "100% safe", or that we know your most meaningful photo; we suggest, you decide.
- Any "up to N GB" figure we did not measure on the user's own phone.

## UI/UX

**Design principles** (tie-breakers for every design decision)
1. Every number is measured, or marked "≈".
2. Give before you ask: no permission or payment before the user sees something real.
3. Biggest win first.
4. Every suggestion shows a one-line reason; the user decides.
5. Say when the space comes back.
6. Max four categories on home, one idea per screen.
7. Calm, not alarm: red only on the Delete button.

When two principles collide, the lower number wins.

**App structure**
- **Clean** tab (home):
  - true storage line at top;
  - categories ordered by GB: Videos, Similar, Screenshots & utility, Duplicates.
- **History** tab:
  - past cleanups;
  - GB still waiting in Recently Deleted; if iOS does not let us read it, "You moved X GB on [date]".
- **Settings** (gear icon): plan and Restore Purchases, Favourites protection (on by default) and protected items, notifications (weekly review, Recently Deleted reminder), Photos access status with Open Settings, "How we measure", Terms, Privacy Policy, Contact support.
- **Review tray:** persistent bottom bar showing selected items and total GB; hidden when nothing is selected.
- Not in the app: Email, Contacts, Vault, Swipe, Tools tabs.
- Empty History: "Nothing cleaned yet. Your first cleanup will show here."

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

Screen detail, copy and edge cases:
1. **Welcome.** Headline "See what's really filling your iPhone." Storage line "X GB used of Y GB" with a "How we measured" link. Sub: "We look at photos and videos. Nothing is deleted without your OK." Footer: Terms and Privacy links. Storage line is neutral colour, no red bar.
   - If the storage figure can't be read: "Storage unavailable right now." The flow is not blocked.
   - If Photos access is already granted (reinstall): skip 2–3 and start the scan.
2. **Pre-prompt.** Title "Let us look at your photos." Body "KeepSpace analyses your library on this iPhone. Nothing is uploaded. Nothing is deleted without your OK." Buttons: Continue; secondary "Not now".
   - "Not now" opens Clean in the permission-denied state. It is never a dead end.
3. **iOS prompt.** Purpose string: "KeepSpace looks at your photos and videos on this iPhone to find large and similar items. Nothing leaves your phone." Outcomes: Full access goes to 4; Limited goes to 4 on the selected items with the banner; Denied goes to Clean in the denied state.
4. **Scan.** It is the home layout filling in, not a separate wait screen.
   - Line: "Scanning on this iPhone · {done} of {total} items."
   - Cards appear as results arrive; sizes show "≈" until measured; the first category to complete is videos.
   - App backgrounded: "Paused. Reopen KeepSpace to continue." Resumes from where it stopped.
5. **Clean.** Line "Found {X GB} to review." Four cards max, solid size chips, three thumbnails each.
6. **Large videos.** See key screens.
7. **Tray and confirm.** The tray sheet lists what's selected; Delete triggers one iOS confirm.
8. **Result.** See key screens. The reminder toggle is off by default.
9. **Paywall.** Shown once, after the first result. Dismissed with X; it does not return until the allowance is reached or the user taps Upgrade in Settings.

**Key screens**

| Screen | Most important element | States to design |
|---|---|---|
| Clean (home) | True storage line | Scanning (progressive); limited access; nothing to clean ("the rest is apps and system data, which iOS manages"); permission denied; error / resume |
| Large videos | Size + full preview; paid "Compress instead" with before/after sizes | iCloud-only ("≈ size, in iCloud"); no large videos |
| Similar group | Reason line ("Suggested keep: sharpest of 4") + user toggles; favourites marked "Protected" | Group of 2; all protected; user overrides the suggestion |
| Review tray | "Nothing has been deleted yet." Total GB. "Moves to Recently Deleted for 30 days. Deleting syncs to all devices using iCloud Photos." The only red button | Empty; user cancels the system confirm |
| Result | "moved" + 2-step guide to empty Recently Deleted | Partial failure (name the items); free allowance reached → paywall |
| Paywall | Plans with price, period, renewal date; X visible | Offline; purchase pending; already subscribed; not trial-eligible |

Layout and exact copy per state:

- **Clean (home).** Top to bottom: storage line and neutral bar; "Found {X GB} to review."; up to four cards in GB order (title, item count, size chip, three thumbnails); tray bar above the tab bar.
  - Limited access banner: "You gave access to {n} photos. Add more for a full picture." Buttons "Add more photos", "Keep as is". The storage line still shows the true device figure.
  - Denied card: "Photos access is off. We can't find photos or videos to review without it." Button "Open Settings". The storage line stays.
  - Nothing to clean: "Nothing big to review. The rest of your storage is apps and system data, which iOS manages." plus "You can see apps by size in Settings > General > iPhone Storage."
  - Error: "Something stopped the scan. Your photos are untouched." Button "Try again".
  - Return visit: cached results show at once; a quick re-scan adds "New since last clean: {X GB}".
- **Large videos.** Rows sorted by size, largest first. Row: poster, duration badge, size chip, date, iCloud badge if the original is not on the phone, checkbox. Sort: Size (default), Date, Duration. Tapping the poster plays full screen.
  - iCloud-only preview: "Downloading preview…" with progress; failure "Couldn't load this preview. Check your connection." Selection still works.
  - Empty: "No large videos found."
  - Paid "Compress instead" (row sheet): shows "Original {size} → New {size}" after the real export, before anything is saved. Then "Save smaller copy". The original is deleted only through the tray and the iOS confirm.
  - Compress failures: "Couldn't compress this video. Nothing was changed." and "Not enough free space to make the smaller copy. Delete something first."
- **Similar group.** Header "{n} similar photos · {size}". Large thumbnails; one carries "Suggested keep" and a reason line. Tap two to compare side by side with zoom.
  - Reason lines come from a closed list: "Sharpest of {n}", "Highest resolution of {n}", "Best overall quality of {n}". If none can be computed: "No clear difference. You choose." and no suggested keep.
  - Nothing in a similar group is pre-selected. Group buttons: "Select all except suggested", "Keep all".
  - "Keep all" hides the group until new similar items join it.
  - Favourite: marked "Protected". Tapping it asks "This is a Favourite. Select anyway?"
  - All protected: "All of these are protected. Nothing to select."
  - User overrides: the suggestion stays marked; no nagging copy.
- **Exact duplicates.** Header "{n} identical copies · {size}". One original marked "Keep"; the extra copies are pre-selected. Selection is still not a deletion.
- **Screenshots & utility.** Grouped by age. Receipts, documents and other utility images are never pre-selected. Thumbnails are large enough to read.
- **Review tray.** Bar: "{n} selected · {X GB}" with "Review". Sheet: grouped thumbnails, each removable; "Nothing has been deleted yet."; "Moves to Recently Deleted for 30 days. Deleting syncs to all devices using iCloud Photos."; allowance line "Free today: {X GB} left"; red button "Delete {n} items".
  - Over the allowance: "Over today's free limit by {X GB}." Buttons "Remove items to fit", "See plans".
  - Cancelled at the iOS confirm: the tray stays as it was; toast "Nothing was deleted."
  - Items no longer in the library: "{n} items are no longer in your library. We removed them from your selection."
  - Any "≈" size in the selection shows "≈" on the total.
- **Result.** "{X GB} moved to Recently Deleted." Sub: "It frees up after 30 days, or now if you empty it." Steps: "1. Open Photos > Albums > Recently Deleted. 2. Tap Select, then Delete All." Buttons "Done", "Show me how". Toggle "Remind me to check Recently Deleted". Home then shows "Waiting in Recently Deleted: {X GB}".
  - Partial failure: "{k} of {n} items couldn't be deleted. Nothing else was changed." Link "See which".

**Permissions**

| Permission | When | Pre-prompt | If denied or limited | If revoked later |
|---|---|---|---|---|
| Photos | After screen 2, from "Continue" | Our pre-prompt (screen 2) | Denied: true device storage plus "Open Settings" card. Limited: scan only the selected items, banner to expand, automatic iOS limited-access alert suppressed | Next launch shows the denied state; History is kept |
| Delete | Each review, one batched delete | Tray copy | One iOS confirm; cancelling changes nothing | — |
| Notifications | Opt-in toggle on the result screen only | The toggle label | Toggle shows "Notifications are off in Settings" with a link | Reminders stop; no re-ask |
| Tracking (ATT) | Not at launch; if needed later, only after the first win | — | — | — |

**Day 2 and beyond**
- History shows "X GB still waiting in Recently Deleted" and "New since last clean".
- Optional weekly review reminder. Copy: "New photos and videos since your last clean: {X GB} to review." Sent only when there is something new; never more than once a week; day and time chosen by the user.
- When nothing's new: "You're all caught up."
- No streaks, no health score, no fear notifications.

**Paywall**
- **Type:** soft.
- **When:**
  - after the first result;
  - when a selection goes past the free daily allowance.
- **Never:** at launch, on tab switch, or while a scan is running.
- **Close:** X visible from the first frame, top corner, full tap target.
- **Plans to test:** annual + monthly vs annual + lifetime. No weekly plan at launch. Prices set later from US paywall captures.
- **Trials:**
  - any trial shows a dated timeline with the charge date;
  - no "trial enabled!" interstitial;
  - no pre-selected weekly plan;
  - the no-trial price is shown plainly to users who aren't trial-eligible.
- **Cancel:** one line explaining how to cancel, mirroring Apple's sheet.
- **Free users keep:** full scan and all sizes, every preview, deletes up to a daily allowance, History.

Paywall rules:
- **Order on screen:** what you just did and real GB left; free vs paid list; plan cards; one dated timeline if a trial exists; primary button; cancel line; Restore, Terms, Privacy.
- **Plan cards:** price in the larger type, then period, then renewal. A per-period equivalent shows only if it is exact and the full price stays larger. "Pay once" on lifetime. A "Save N%" label shows only with its basis printed beside it. No "Most popular".
- **Card button copy:** "Start free trial" only when the card has a trial; otherwise "Continue".
- **Cancel line:** "Cancel anytime in Settings > Apple Account, at least one day before the renewal date."
- **Allowance:** counted in GB moved to Recently Deleted per local calendar day. Size `[UNKNOWN: set by test]`. The tray always shows what is left.
- **States:**
  - offline: "You're offline, so plans can't load." Buttons "Try again", close.
  - purchase pending: "Waiting for approval. You'll get access when it's approved."
  - already subscribed: close the sheet; Settings shows the plan.
  - not trial-eligible: show the full price, no trial wording.
  - purchase not completed: "The purchase didn't complete." Nothing else changes.
  - Restore: "Purchases restored." or "No purchases found for this Apple Account."
  - subscription expired: back to the free allowance; History and previews stay.

**Visual language** (direction only; final tokens from brand-designer)
- Follow system light/dark; store shots light-led.
- One calm accent colour; neutral storage bars; red only on Delete.
- Real photos shown large; no decorative "AI" art or orbit graphics.
- Density: one idea per screen; cards, not dense grids; solid size chips on photos.
- Motion: short, functional (count-up, card arrival); nothing that loops.

**Voice and copy**
- **Tone:** plain, specific, calm.
- **Lines we ship:**
  - "Nothing is deleted until you tap Delete."
  - "These look alike. We suggest keeping the sharpest one. You decide."
  - "≈ means estimated. Tap to see how we counted."
  - "X GB moved to Recently Deleted. It frees up after 30 days, or now if you empty it."
  - "Nothing has been deleted yet."
  - "You're all caught up."
  - "Photos access is off. We can't find photos or videos to review without it."
  - "Something stopped the scan. Your photos are untouched."
- **Copy we never use:**
  - "Free up to 80% of your storage"
  - "Almost Full" (when it isn't)
  - "50% faster"
  - "3-day free trial is enabled!"
  - "2558 people have joined today!"
  - "Boost your iPhone's storage"
  - "Join 1 Million Happy Users!"
  - "My phone stopped overheating and lagging after the cleanup."

**Accessibility**
- Dynamic Type everywhere, including plan cards; chips and rows wrap rather than truncate.
- VoiceOver reads each thumbnail's type, date, size and selection state, and each group's reason. Tray bar reads "{n} selected, {X GB}, Review". "≈" is read as "about".
- Selection is shown by a checkmark shape plus fill, never by colour alone. "Protected" has a lock icon and the word.
- Every swipe or drag action has a button alternative.
- AA contrast; solid size chips.
- Reduced Motion swaps animation for counters.
- Photo and video previews have no autoplay sound.

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
- Duplicated or invented testimonials.
- "Skip trial" as the only way out of a paywall.
- A monthly-labelled plan that is a 12-month commitment.
- Email, contacts, vault or other non-storage tabs.

## v1 product features

| # | Feature | What it does | Free / paid | Needs | Size |
|---|---|---|---|---|---|
| 1 | True storage overview | Real device used/free on screen 1, with a "How we measured" sheet | Free | Nothing | S |
| 2 | On-device scan | Progressive and resumable; nothing uploaded; results stream in, videos first; caches results for return visits | Free | Photos permission | L |
| 3 | Large videos | Ranked by size; duration, date, full-screen preview; iCloud-only items marked "≈" | Free to view; delete within allowance | 2, 8, preview download | M |
| 4 | Similar photos | Grouped; suggested keep with a one-line reason; user toggles each photo; Keep all hides a group | Within allowance | 2, similarity engine, quality signals for reasons | L |
| 5 | Exact duplicates | Identical copies grouped for fast bulk review; extras pre-selected | Within allowance | 2 | S |
| 6 | Screenshots & utility images | Grouped by age; receipts, documents and other utility shots; never pre-selected | Within allowance | 2 | S |
| 7 | Protected favourites | Favourites never auto-selected; user can protect any item; protected list in Settings | Free | 2; local store | S |
| 8 | Review tray + batched delete | One tray, total GB, one confirm, one batched delete; trims stale items | Free | 3–6; allowance counter from 12 | M |
| 9 | Honest result + History | "Moved to Recently Deleted" result, guide to empty it, cleanup history | Free | 8; local store | S |
| 10 | Video compression | One preset; before/after size shown before saving; saves the new copy, then deletes the original through the tray with confirm. First cut if late | Paid | 3, 8, free space for the new copy, paid check from 12 | M |
| 11 | New since last clean | Detects new clutter; optional weekly reminder | Reminder free; weekly bulk paid | 2, 9, local notification opt-in | S |
| 12 | Paywall + free allowance | StoreKit 2; soft paywall; daily free delete allowance | — | Products set up in App Store Connect; prices from s5 | M |

**Build order:** 1 → 2 → (3, 4, 5, 6, 7 in parallel) → 8 → 9 → 12 → 11 → 10 (10 is the first cut).

**Feature rules**
- **Selection defaults:** videos, similar photos and screenshots start unselected; exact-duplicate extras start selected; Favourites never selected.
- **Allowance:** counts GB moved to Recently Deleted per local calendar day; scanning, previews and History never count. Over the limit, the user trims the selection or opens the paywall; nothing is deleted partially without being told.
- **iCloud-only items:** show "≈ size, in iCloud"; previews download on tap; deleting follows the same tray copy.
- **Reasons:** "Sharpest of N" ships only if the blur-measure spike passes; otherwise the reason falls back to resolution or overall quality, or "No clear difference. You choose."
- **Minimum iOS:** `[UNKNOWN: set after the week-1 spike]`.

**Paid unlocks:** unlimited cleanup in one session, video compression, weekly bulk review.

**Free vs paid**
- **Free:** see everything filling the phone with true numbers, preview and compare everything, delete up to a daily allowance, learn how to get the space back.
- **Paid:** unlimited cleanup, video compression, weekly review.

**Build notes**
- Start the scan engine (2) and similar photos (4) in week 1 — they're the two large items.
- Week-1 on-device spike on file sizes:
  - exact sizes via `PHAssetResource.dataSize` on iOS 27+;
  - byte-streaming fallback on older iOS;
  - if the fallback is too slow, show counts + "≈" and set the minimum iOS version.
- Same spike: measure blur-detection accuracy, and check whether Recently Deleted can be read or opened.
- Video compression is the release valve if the schedule slips.
- Each delete call shows its own iOS confirm, so the tray batches everything into one call.

**Later (v1.1+) and what triggers each**

| Feature | Bring in when |
|---|---|
| Swipe mode | Users ask to hand-sort, or D7 lags while scan → delete is healthy |
| Widget | D7/D30 return is the weakest funnel step |
| Screenshot topics | The screenshot-graveyard store-page test wins |
| Live Photo → still | Live Photos turn out to be a meaningful GB share |
| Contacts merge | Repeated user demand |
| Weekly plan | Annual/monthly can't reach payback |
| Blurry-photo review | The blur-accuracy spike passes on a labelled test set |
| Similar videos | Support or review requests ask for it, or videos stay the top GB category |

**Not building** (each is outside the storage job, or against iOS rules or trust):
- email cleaning
- contacts/calendar
- private vault
- iCloud cleaning
- boost/speed/RAM/junk/cache
- "AI categories" tiles
- health score

**v1 success metrics**

| # | Metric | Defined as | Decision it drives |
|---|---|---|---|
| 1 | Photos permission grant rate | Allow (full or limited) ÷ prompts shown | Pre-prompt copy |
| 2 | Scan → first approved delete in session 1 | Users who confirm a delete ÷ users whose scan completed | Home order, tray copy |
| 3 | Install → paid conversion | Paid starts ÷ installs | Paywall timing, plan mix |
| 4 | Refund rate and share of 1–2★ reviews mentioning "charged" / "scam" | Refunds ÷ purchases; tagged reviews ÷ 1–2★ reviews | Paywall disclosure copy |
| 5 | Share of moved GB actually freed within 7 days | GB gone from Recently Deleted ÷ GB moved; measurable only if iOS lets us read it | Day-2 reminder |
| 6 | **D30 net proceeds per install (primary money metric)** | Net proceeds by day 30 ÷ installs | Everything else is read against this |

Targets are set after the first cohort `[UNKNOWN]`. Event names come from s4.

## New recommendations

1. **"One iPhone, six cleaners" truth test**
   - Each competitor's storage claim vs iOS Settings on one phone, then ours.
   - Use as launch PR and challenger ad.
   - Test: one organic short + one Meta creative vs the control ad.
   - Kill if: s6 flags the comparative claim, or it clearly loses to the control.
2. **Lead with videos, not duplicates, everywhere:** onboarding, home order, store shot 1.
   - Test: aggregate category GB over the first scans; a custom product page.
   - Kill if: real cohorts show similar photos beat videos on GB.
3. **Recently Deleted as the day-2 return reason**, with an opt-in reminder to empty it.
   - Kill if: opt-in is low and day-2 return does not improve; if iOS won't let us read it, use "You moved X GB on [date]".
4. **Week-1 file-size spike** before any UI is final.
   - Kill if: streaming is too slow on older iOS, so show counts and "≈" and raise the minimum iOS.
5. **"How we measured"** sheet behind every number, in-app and in store shots.
   - Kill if: almost unused, so keep it in-app and drop it from store shots.
6. **Launch without the tracking prompt;** Apple Ads first.
   - Kill if: Meta is the main channel and can't optimise without it, so ask after the first win.

## Before build

1. Ganesh captures:
   - competitors' Photos permission, scan, delete and result screens;
   - US-storefront paywalls;
   - a screen recording to time close-button delays;
   - Swipewipe, Cleaner Guru and AI Cleaner.
2. Set US prices from the captured US paywalls (s5).
3. Fix open numbers: daily allowance size, minimum iOS version, reminder timing, trial yes or no.
4. Check the Recently Deleted steps in the result copy against Apple Support before they ship.
5. Run brand-designer (name + visual), ux-designer (key screens above) and s1-spec on this note; s2-standards on the paywall rules; s4-analytics on the metric table; s6-legal on name clearance and the truth-test ad.
6. Bharat signs off → promote to `research/categories/storage-cleaner/`.

## Competitor reference

Facts as seen in the team's captures (`ganesh_screenshots/Storage Cleaners/`, India storefront, prices in ₹ as shown, IMG_ files in capture order, one phone in a single 2:49–3:01 window). No analysis here. Not captured in any app: Photos permission prompt (other than ATT and notifications), scan, review, delete, result.

**Clean Manager** (7 files: IMG_2226–2232)
- Key screens: welcome IMG_2226; onboarding IMG_2227–2229 (3 steps: "AI Photo Cleanup", "Boost your iPhone's storage", "Clean out your email inbox"); paywall IMG_2230 and again IMG_2232; home IMG_2231.
- Paywall: end of onboarding, before home; X visible top right; shown twice. Trial timeline "Due today ₹0.00 / Due: 10 October 2026 ₹999.00"; button "Start 7 days free trial".
- Plans: one, weekly ₹999.00 after a 7-day trial; "Clean Manager Pro" feature line "Smart Cleaning, Video Compressor, Secret Storage, Manage Contacts, No Ads and Limits."
- Home: "55% / 255 GB"; Photos 415 medias 2.86 GB; Videos 52 medias 2.62 GB; Others 135.2 GB; Similar photos 108 medias 536 MB; Duplicate photos 9 medias 17 MB; All videos 50 medias 2.24 GB; Screenshots 133 medias 280 MB; tabs Home, Contacts, Swipe, Compress, Tools; gold "Premium" button.
- Storage figures shown: "? of 256GB used" (IMG_2226); "71% from 100% used" with badges "800" (IMG_2230); "43% from 100% used" with badges "443" (IMG_2232).
- Dark patterns seen: "Free up to 80% of your storage with our AI-powered technology." (IMG_2228); changing badge counts and percentages between two views of the same paywall (IMG_2230, IMG_2232); email onboarding (IMG_2229).
- Permissions seen: none captured. Welcome text states Photos access is required (IMG_2226).

**Cleaner Kit** (7 files: IMG_2264, 2266–2271)
- Key screens: App Store page IMG_2264 ("39K RATINGS 4.4", BPMobile, "Featured by Apple", "70M+ users"); welcome IMG_2266; onboarding IMG_2267–2270 (5 dots); paywall IMG_2271. Home not captured.
- Paywall: end of onboarding; no close control visible; Terms, Privacy, Restore at the bottom.
- Plans: MONTHLY "12-month commitment (₹11,748.00 total)" ₹979 per month, tagged "MOST POPULAR"; YEARLY ₹4,999.00/year "just ₹95.88/week"; WEEKLY "Free for 7 days, then ₹699.00/week"; "Auto-renewable. Cancel anytime."
- Storage figures shown: "240 GB of 256 GB used" (IMG_2266, IMG_2268).
- Dark patterns seen: system notification prompt over onboarding screen 2 (IMG_2267); "Reclaim up to 80% of your space" with "*Based on internal data from Cleaner Kit" (IMG_2268); "800,000+ 5-star ratings" with a testimonial repeated twice (IMG_2270); "Shrunk my videos and got back 50GB!" (IMG_2270); monthly plan marked "MOST POPULAR" next to "Cancel anytime" (IMG_2271).
- Duplicate pairs in IMG_2267 show the right-hand image pre-checked.

**Cleanup: Phone Storage Cleaner** (10 files: IMG_2233–2242)
- Key screens: onboarding IMG_2233–2236 (3 steps: "Delete Duplicate Photos", "Optimize iPhone Storage", "Clean Your Email Inbox"); trial interstitials IMG_2237–2238; paywall 1 IMG_2239; home with notification prompt IMG_2240; home IMG_2241; paywall 2 IMG_2242.
- Paywall 1: after the interstitials, before home; no close shown, "Restore Purchase" top left; "Free trial enabled" row; timeline "Due today ₹0.00 / Due 10 October 2026 ₹999.00"; button "Try Free".
- Paywall 2: X small and grey, top left; "Unlock Unlimited Access"; three feature lines; testimonial carousel.
- Plans: weekly ₹999.00 with a 7-day free trial (selected); lifetime ₹3,999.00 tagged "Save 89%"; button "Start my 7-day free trial".
- Home: "5.0 GB Space to Clean" with "See Analysis"; "Optimize Storage — Free up to 2 GB from your files quickly"; Similars "New photos (918.3 MB)"; Duplicates "0 Photos" (greyed row); Similar Videos; Similar Screenshots ("18 Photos (19.8 MB)" in IMG_2240, "New photos (19.8 MB)" in IMG_2241); tabs Home, Email, Contacts, Optimize, Extras; "PRO" pill.
- Storage figures shown: "? GB of 255 GB used" (IMG_2235); "95 from 100% used" with badges "611" and "329" (IMG_2239).
- Notification prompt: shown over home, after the paywall (IMG_2240).
- Dark patterns seen: "Free up to 80%" with "*Based on Cleanup internal data" (IMG_2235); "Try 7 days" then "For free!" full-screen interstitials (IMG_2237–2238); "Save 89%" with no basis shown (IMG_2242).

**Clever Cleaner: Photo Storage** (7 files: IMG_2272–2276, 2278–2279)
- Key screens: onboarding with ATT prompt IMG_2272; onboarding IMG_2273–2275 ("1 of 4" to "3 of 4"); paywall as step 4 IMG_2276; home IMG_2278; paywall again IMG_2279.
- Paywall: end of onboarding; X visible top right; shown twice.
- Plans: Weekly "3 days free, then ₹ 699 per week" (selected); Lifetime "Best Value" "₹ 3,999 pay once"; button "Start Free Trial"; "Auto-renewable. Cancel anytime".
- Onboarding: "Swipes Free" (IMG_2274); "2 GB free daily" with Similars and Compress, before/after "827.5 MB" to "299.9 MB", "SAVE 527.6 MB" (IMG_2275).
- Home: "120.28 GB of 255 GB used"; "Photo Library 2%", "Data and apps 45%", "Free 53%"; buttons Smart cleanup, Swipe, Compress; tiles Similars 1.35 GB, Videos 2.62 GB, Screenshots 283.1 MB, Live photos 12.5 MB; "Premium" crown pill.
- Storage figure shown on paywall: "Photo Storage — Almost Full" with a Similars / Heavies / Screenshots / Lives bar (IMG_2276, IMG_2279).
- Permissions seen: ATT prompt on the first screen (IMG_2272) with Allow / Ask App Not to Track.
- Dark patterns seen: ATT before any value (IMG_2272); weekly plan pre-selected; "Almost Full" label (IMG_2276).

**Darksy: Smart Storage Cleaner** (9 files: IMG_2243–2251)
- Key screens: splash IMG_2243; onboarding IMG_2244–2247 (4 dots: "3M Users" with an "87%" ring and "CLEAN" button; "What our users say"; "PhotoSwipe"; "Email Cleaner"); trial interstitials IMG_2248–2249; paywall IMG_2250; home IMG_2251.
- Paywall: after the trial interstitial, before home; no close shown; button loading; "No payment now" under the button; Weekly / Yearly toggle with Weekly selected; Conditions, Privacy Policy, Restore.
- Plans: weekly "Free for 3 days, then ₹699.00/week" with timeline "Due today 3 days free 0 ₹ / Due October 6, 2026 ₹699.00". Yearly price not captured. Feature line "Smart Cleaning, Compressor, Secret space, Contact and calendar management, Cloud Storage".
- Home: "Available to clean 4.70 GB", "Free 126 GB", "Used: 107 GB", "Clutter: 4.70 GB", "Total: 238 GB"; tiles Videos 2.18 GB, Similar 625 MB, Duplicates 5.65 MB, Selfies (placeholder image, no size), AI Categories 1.68 GB, Screenshots 265 MB, Blurred 109 MB, With Text 437 MB, then Compression and Contacts; tabs Cleaner, PhotoSwipe, Cloud, Email, More; "Try For Free" pill with badge "1".
- Storage figure shown on paywall: "35% from 100% used", badges "11" and "7" (IMG_2250).
- Dark patterns seen: "3M Users" (IMG_2244) then "Join 1 Million Happy Users!" (IMG_2245); "My phone stopped overheating and lagging after the cleanup." (IMG_2245); "3-day free trial is enabled!" with a toggle animating on (IMG_2248–2249).

**Phone Storage Cleaner: Free up ("FreeUp Cleaner")** (12 files: IMG_2252–2263)
- Key screens: splash IMG_2252; onboarding IMG_2253–2258 (6 screens); trial interstitial IMG_2259; Apple purchase sheet over paywall IMG_2260; paywall loading IMG_2261; home IMG_2262; paywall again IMG_2263.
- Paywall: after the trial interstitial, before home; "Skip trial" top right and "Restore" top left; "3-day free trial" row with a check; button "Try Free" / "Try free"; "Secured with Apple".
- Plans: weekly "Free for 3 days then ₹ 699/weekly"; Apple sheet shows "3-day free trial Starting today", "₹ 699 per week Starting on 6 Oct 2026", and "No commitment. Cancel at any time in Settings > Apple Account at least one day before each renewal date." Feature line "Quick Clean, Large Files Clean, Photo Cleaning, Manage Contacts, No Ads and Limits."
- Home: "Storage Used: 120 GB / 255 GB", "424 items"; "Ready to clean!"; Similar Photos 46 items 427 MB; Screenshots 138 items 281 MB; Contacts "Unlock"; "Save more space — View Guide"; tabs Home, Photo, Video; "PRO" pill.
- Storage figures shown: "62 of 64 GB used" (IMG_2253); "25 from 100% used" with badges "200" and "120" (IMG_2261, IMG_2263); badges "343" and "278" on IMG_2260.
- Permissions seen: ATT prompt on onboarding screen 2 (IMG_2254) with the text "This data will be used to gather performance statistics for personalizing your cleaning experience and fixing errors and crashes."
- Dark patterns seen: "+86%", "160", "8h" and "50%" stat screens each with "*Based on Free Up internal data" (IMG_2255–2258); "Boost Performance — 50% faster response times with regular Free Up" (IMG_2258); "3 day free trial is enabled!" (IMG_2259); "2558 people have joined today!" (IMG_2263); "1 Million+ devices cleaned up!" (IMG_2253).
