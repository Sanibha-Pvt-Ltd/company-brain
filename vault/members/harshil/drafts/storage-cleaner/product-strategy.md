---
type: category-product-strategy
category: storage-cleaner
member: harshil
updated: 2026-10-05
status: draft
sources: [context.md, screenshots:52 across 6 apps, knowledge:consumer_app_venture_knowledge_base_2026-10-04.md + organic-growth-knowledge-base.md + sanibha-app-factory-knowledge-base.md, web:7]
---

# Storage Cleaner — product strategy (v1)

Final recommendations built from [[research/categories/storage-cleaner/context]] (cited as "context §n") and the team's 52 in-app screenshots. The per-app teardown and cross-app tables are in [[members/harshil/drafts/storage-cleaner/product-strategy-evidence]] (cited as "E§n"). Screen tags read `[SCREEN:<app>/<file>]`. App short names: clean-manager, cleaner-kit, cleanup, clever-cleaner, darksy, freeup.

## TL;DR

- **Positioning:** keep context §14's *Make space. Keep what matters.* (safe, fast decisions), proven by **true numbers, biggest wins first, nothing deleted without your OK**. Hook: "See what's really filling your iPhone."
- **Why:** context §5 says users fear surprise charges, lost photos and over-promising ads. The screens show how the category over-promises: on one test phone, paywalls said "95 from 100% used" and "Almost Full" while the same phone's home screens showed about 47–55% used (R6, E§2).
- **UX 1 — true storage first:** real used/free storage before any ask. The first win is the first approved delete (7 taps), reported as "moved to Recently Deleted".
- **UX 2 — biggest first:** lead with large videos, not duplicates. Test phone: exact duplicates 0–17 MB, videos 2.18–2.62 GB (R7).
- **UX 3 — honest paywall:** soft, after the first cleanup; close visible from frame 1; no weekly at launch, no trial theatre, no tracking or notification ask before value.
- **v1 (12):** true storage overview · on-device scan · large videos · similar compare with a reason · duplicates · screenshots/utility · protected favourites · review tray · honest result + Recently Deleted guide · video compression (paid, first cut) · "new since last clean" · StoreKit 2 paywall with free daily allowance.
- **Cut:** email, contacts, calendar, vault, "boost", iCloud cleaning, health score.
- **Top new recommendation:** a "one iPhone, six cleaners" truth test as launch PR and challenger ad (§5.1).
- **Confidence: medium.** Context and screens agree on the trust problem. The screens stop at each app's home screen (no scan, delete or result screens), prices are ₹ only, and Swipewipe, Cleaner Guru and AI Cleaner have no screens.

## 1. What the research tells us

**Inputs and confidence:**
- **Context:** context.md, all 14 sections.
- **Screens:** 52 screenshots across 6 apps: Clean Manager, Cleaner Kit, Cleanup, Clever Cleaner, Darksy, FreeUp. They appear to be captured on **one phone** within about 12 minutes; the same photos show up in four apps (E§0) `[INFERRED]`.
- **Gaps:** no permission, scan, delete or result screens anywhere, and India-storefront prices only. Decisions about the moment of deletion therefore rest on context §5 and Apple docs, not on competitor screens.

**Context × screens synthesis.** Every decision below traces back to a row here.

| # | context claim | what the screens show | verdict | so for us |
|---|---|---|---|---|
| R1 | §14: storage recovery is the reason to download; "safe, fast decisions" is the identity | Every onboarding sells speed and automation ("instantly", "in seconds", "one tap") `[SCREEN:clean-manager/IMG_2227, cleanup/IMG_2234, cleaner-kit/IMG_2269]`. None sells safety. Delete flows were not captured | confirmed (the gap is real on screen) | Keep the storage hook. Make safety visible in the first five minutes, not only in settings |
| R2 | §5 A: surprise charges, weekly pricing, trial confusion | A weekly plan in **6/6** paywalls. "Trial enabled" interstitials in 3. No visible close in 3. Cleaner Kit's "MOST POPULAR" is a 12-month commitment billed monthly, next to "Cancel anytime" `[SCREEN:cleaner-kit/IMG_2271]` (E§2 table) | confirmed, and worse than described | No weekly at launch. Dated charge timeline. Close always visible. No trial interstitial |
| R3 | §5 B, §6 "Explainable AI": important photos get treated as duplicates | On one library, "similar" ranged from 427 MB to 1.35 GB across five apps, and none says why a photo was picked (E§2 pattern 4) | confirmed and quantified | Every similar group shows a one-line reason. The user picks |
| R4 | §5 C: users want previews before deleting videos | Home tiles show duration or size `[SCREEN:clean-manager/IMG_2231, darksy/IMG_2251]`. Preview screens not captured | partly visible | The video list has size, duration and a tap-to-play full preview |
| R5 | §5 D, §13: accidental deletion; "found" vs "actually freed" | No captured onboarding or paywall mentions Recently Deleted. No result screens captured (E§2 pattern 7) | not visible, so an open lane | Explain Recently Deleted before and after delete. The result screen says "moved", never "freed" |
| R6 | §5 E, §13: ads promise more than the app delivers; don't promise "12 GB" | "Free up to 80%" in 3 apps. Paywall storage figures contradict the same phone's home screens. Cleanable photo space was about 4.7–5.0 GB of about 107–120 GB used (E§2 contradiction table) | confirmed, and stronger | Every number is measured on the device or marked "≈". We never say "up to N%" |
| R7 | §6 "Storage recovery planning: least effort first" | Homes list categories, but not by size. Exact duplicates were 0–17 MB vs videos 2.18–2.62 GB on the same library `[SCREEN:cleanup/IMG_2241, darksy/IMG_2251, clever-cleaner/IMG_2278]` | refined | Home is ordered by GB, so videos usually lead. That *is* the recovery plan |
| R8 | §6, §7: transparent monetization is a trust differentiator, though Clever already offers generous free cleaning | Clever's "2 GB free daily" is real `[SCREEN:clever-cleaner/IMG_2275]`. But it asks for tracking on screen 1, pre-selects weekly and labels storage "Almost Full" while its own home shows "Free 53%" `[SCREEN:clever-cleaner/IMG_2272, IMG_2276, IMG_2278]` | refined (Clever is less clean than §3 and §8 suggest) | A free daily allowance is table stakes. Full-funnel honesty is the differentiator |
| R9 | §7: US weekly $4.99–$11.99; annual $29.99 (Cleanup, Swipewipe); lifetime $39.99 (Clever) | India storefront: weekly ₹699–₹999 everywhere. Lifetime ₹3,999 (Cleanup, Clever). Yearly ₹4,999 (Cleaner Kit). Cleanup shows lifetime with no annual, which differs from §7's US list `[SCREEN:cleanup/IMG_2242]` | refined; US plan mix `[UNKNOWN]` | Test annual + monthly vs annual + lifetime. Capture US paywalls before setting prices |
| R10 | §8: our quadrant is "functional + controlled", next to Clever | All 6 apps are dark or navy with a blue CTA and red/orange alarm bars. Swipe exists in 3 (clean-manager tab, clever-cleaner/IMG_2274, darksy/IMG_2246) (E§2) | confirmed quadrant; visual space is open | Keep the quadrant. Use a light, calm visual language. Swipe waits until later |
| R11 | §4, §9–10: real UI numbers beat illustration; storefront "Find → Understand → Clean safely"; mock "12.4 GB" | The real figure on the test phone was "5.0 GB Space to Clean" `[SCREEN:cleanup/IMG_2241]` and "Available to clean 4.70 GB" `[SCREEN:darksy/IMG_2251]` | refined | Keep the 3-shot story, re-ordered as Measure → Choose → Done. Demo numbers come from a real demo phone and are labelled as such |
| R12 | §4 lesson 3: big social-proof numbers are a weapon we lack | Social proof contradicts itself: "3M Users" then "Join 1 Million Happy Users!" `[SCREEN:darksy/IMG_2244, IMG_2245]`. The same testimonial appears twice `[SCREEN:cleaner-kit/IMG_2270]` | confirmed | Replace user counts with visible product proof ("How we measured") |
| R13 | §3: email, compression, vault and contacts are "competitive necessities" | Email in 4/6 onboardings. Contacts in 5/6. "Video Compressor" on paywalls `[SCREEN:cleanup/IMG_2239, clean-manager/IMG_2230]` | partly contradicted | Compression stays (it is storage). Email, contacts and vault are cut (not the storage job; see §4.3) |
| R14 | §11: Meta journeys A (storage emergency), B (deletion anxiety), C (screenshot graveyard) | No captured app leads with deletion anxiety. Screenshots on the test phone were 133–138 items, 265–283 MB `[SCREEN:clean-manager/IMG_2231, freeup/IMG_2262, darksy/IMG_2251, clever-cleaner/IMG_2278]` | A and B open; C small on this library | Run A as control and B as differentiator. C waits for a later custom product page (CPP) test |
| R15 | §12: test paywall before vs after scan; preview-only vs small free cleanup; annual vs + lifetime; weekly review | 6/6 put the paywall at the end of onboarding, before home (E§2 table) | the category runs §12's "control" | Ship scan-first as default. Keep §12's free-tier, plan-mix and retention tests. Run paywall-first only if payback fails |

**Read.** Context is right about the problem: trust, control, billing. The screens add two things that change the build.
- **The category's main lie is its numbers.** So "truthful measurement" has to be a product feature, not just a slogan.
- **Space sits in videos, not duplicates.** So the "plan" context §6 asks for is simply biggest-first.

What the screens cannot show is how competitors handle deletion. Our deletion UX rests on context §5 and Apple's own behaviour.

## 2. Positioning

### 2.1 Who and the job
- **Decision:** target an iPhone owner at the "storage full" moment who fears losing photos and being charged.
- **Why:**
  - Trigger: context §11 Concept A.
  - Fears: context §5 B and D (photos) and §5 A (billing).
  - Search terms: "storage cleaner", "phone cleaner", "clean iPhone" `[ESTIMATE:knowledge/consumer_app_venture §4.1]`.
  - Demographics: `[UNKNOWN]`.
- **Job:** "Show me what's actually eating my space, let me drop the big stuff without losing anything I care about, and don't trick me into paying."

### 2.2 The call

| Option | Acq. pull | Diff. | Defensibility | Monetization | Build 6 wks | Honesty | Total |
|---|---|---|---|---|---|---|---|
| A. Context §14 as written: control + reassurance | 4 | 3 | 2 | 4 | 3 | 4 | 20 |
| B. "Honest cleaner": true numbers, clean billing | 3 | 4 | 2 | 3 | 4 | 5 | 21 |
| C. "Biggest wins first" (videos lead) | 5 | 3 | 2 | 4 | 4 | 4 | 22 |
| D. Swipe / memories (context §2, §8) | 3 | 2 | 2 | 3 | 3 | 4 | 17 |
| **E. A's line + B's proof + C's hook** | 5 | 4 | 3 | 4 | 3 | 5 | **24** |

Scores are `[INFERRED]`.

- **Decision:** E.
- **Why:**
  - A's line matches the fears in context §5.
  - B answers R2, R6 and R12.
  - C answers R7.
  - D is set aside: Swipewipe owns enjoyment (context §2, §8), and swipe is already in 3 of the 6 captured apps (R10).
  - Defensibility is 3, not 2: leaders can copy our words, but their weekly-default, fear-bar paywalls look central to how they make money (E§2) `[INFERRED]`.
- **Build/design:** every screen proves "true", "biggest" and "your OK". No swipe in v1.

**Statement:** For iPhone owners who just hit "storage full" and are afraid of deleting the wrong photo, **[KeepSpace, placeholder per context §9]** is the storage cleaner that shows what is really filling your phone, measured on your phone and biggest first, and deletes only what you approve. Unlike Cleanup, Cleaner Kit, Clean Manager, Darksy and FreeUp, whose paywalls in our captures showed storage figures that contradicted their own home screens, it shows real numbers and tells you exactly when the space comes back.

**Promise hierarchy** (context §14's table, with the proof added):
- Hook: "See what's really filling your iPhone."
- Differentiator: "Real numbers. Nothing deleted without your OK."
- Emotional benefit: "Keep what matters."
- Retention reason: "New clutter since last time, plus space still waiting in Recently Deleted."

### 2.3 Proof points (what the user sees)
1. True storage on screen 1 via `volumeAvailableCapacityForImportantUsage` `[APPLE:https://developer.apple.com/documentation/foundation/urlresourcevalues/volumeavailablecapacityforimportantusage]`, with a "How we measured" sheet.
2. Every size is either measured or marked "≈".
3. A one-line reason on every similar group (R3).
4. Favourites protected by default (context §8 table).
5. Result text: "moved to Recently Deleted; frees after 30 days or when you empty it" `[APPLE:https://support.apple.com/en-us/104967]`.
6. Paywall shows price, period, renewal date and the free/paid split, with the X visible immediately.

### 2.4 Storefront and ad
- **Decision:** context §9's storefront becomes **Measure → Choose → Done**.
  1. Real storage bar + "Your biggest videos".
  2. A similar group with its reason.
  3. Review tray + the honest result line.
  
  Context §10 screens 4–6 are kept as written, in one UI language.
- **Ads:** Meta Concept A is the control, Concept B the differentiator test, and the truth test (§5.1) the challenger. Concept C waits (R14).
- **Why:** R7, R11 and R5.
- **Build/design:**
  - Store shots come from a real demo phone, captioned as such.
  - The name stays a placeholder until cleared.

### 2.5 What we will never claim
- Device "% full" or "% used" we didn't read. Guideline 1.1.6 bans "inaccurate device data" `[APPLE:https://developer.apple.com/app-store/review/guidelines/]`.
- "Free up to N%" (R6, context §13).
- "Faster", "boost" or "overheating" `[SCREEN:freeup/IMG_2258, darksy/IMG_2245]`. Guideline 2.3.1(a) bans promoting services an app doesn't offer.
- Cleaning of iCloud, system data, caches or "junk" `[ESTIMATE:knowledge/consumer_app_venture §4.4]`.
- "Freed" at delete time (R5).
- User counts, ratings, "joined today" or "Featured by Apple" (R12).
- Recovery after Recently Deleted is emptied (context §9, citing Apple Support).

## 3. UI/UX

### 3.1 Design principles (tie-breakers)
1. **Every number is measured, or marked "≈".** (R6)
2. **Give before you ask:** no permission or payment before the user sees something real. (R2, R15)
3. **Biggest win first.** (R7)
4. **Every suggestion carries a one-line reason; the user decides.** (R3)
5. **Say when the space comes back.** (R5)
6. **Four categories max on home, one idea per screen.** Darksy shows 9+ tiles `[SCREEN:darksy/IMG_2251]`; FreeUp's short home works `[SCREEN:freeup/IMG_2262]`.
7. **Calm, not alarm:** red appears only on the irreversible Delete button. (R10)

### 3.2 Information architecture
- **Decision:** two tabs.
  - **Clean** (home): true storage line, then Videos, Similar, Screenshots & utility, Duplicates, ordered by GB.
  - **History**: past cleanups, plus GB still waiting in Recently Deleted.
  - **Settings** sits behind a gear: plan, protected items, notifications, "How we measure".
  - **Review tray** is a persistent bottom bar.
- **Why:** Competitors carry 5 tabs mixing non-storage jobs `[SCREEN:clean-manager/IMG_2231, cleanup/IMG_2241]`. FreeUp shows that 3 tabs are enough `[SCREEN:freeup/IMG_2262]`.
- **Build/design:** no Email, Contacts, Vault, Swipe or Tools surfaces.

### 3.3 First five minutes
- **Decision:** the flow below. The first win is screen 8, at 7 taps.
- **Why:** In 6/6 captured apps the paywall comes before any real value, after 4–9 onboarding screens (E§2 table, R15). Context §7 proposes: scan → show storage → inspect → pay → bulk clean.

| # | Screen | On it | Primary action | Asks | Given so far | Taps |
|---|---|---|---|---|---|---|
| 1 | Welcome | Device's real used/free; "We clean photos and videos" | Scan my photos | none (Terms link) | true storage | 1 |
| 2 | Photos pre-prompt | Analysed on this iPhone · nothing uploaded · nothing deleted without your OK | Continue | — | privacy promise | 2 |
| 3 | iOS Photos prompt | system | Allow | Photos | — | 3 |
| 4 | Progressive scan | Live counts; videos appear first | Can open Videos early | — | growing results | — |
| 5 | Clean (home) | Categories by GB, "≈" where estimated | Open top category | — | full inventory | 4 |
| 6 | Large videos | Size · duration · date; tap to play | Select | — | previews | 5 |
| 7 | Review tray → iOS confirm | Total GB · "Moves to Recently Deleted for 30 days" | Delete N items | system confirm | full control | 6–7 |
| 8 ★ | Result (first win) | "1.2 GB moved to Recently Deleted" + how to empty it now | Done / Show me how | optional reminder toggle | GB moved + how to free it | 7 |
| 9 | Soft paywall | What you did, what's left (real GB), free vs paid, plans, X | Choose or close | payment (optional) | a completed cleanup | — |

The "1.2 GB" figure is a layout placeholder, not data.

- **Build/design:**
  - First value (real sizes) arrives at tap 4. In the captures, competitors showed 4–9 screens before home, *plus* the permission (E§2).
  - No competitor first win (freed GB) was captured, so that comparison stays `[UNKNOWN]` until §6 Q1 is answered.

### 3.4 Permissions
- **Photos.** Decision: ask for `.readWrite` after our pre-prompt.
  - Limited access: scan only the selected items and show a banner to expand. Suppress the automatic limited-access alert with `PHPhotoLibraryPreventAutomaticLimitedAccessAlert` `[APPLE:https://developer.apple.com/documentation/photos/phauthorizationstatus/limited]`.
  - Denied: still show true device storage, plus an "Open Settings" card.
- **Delete.** Decision: batch each review into one change request. Why: Apple says "For each call to this method, iOS shows an alert asking the user for permission to edit the contents of the photo library" `[APPLE:https://developer.apple.com/documentation/photos/phphotolibrary/performchanges(_:completionhandler:)]`. Silent deletion is impossible, which is good for trust.
- **Notifications.** Decision: only as an opt-in toggle on the result screen. Why: Cleaner Kit asks on onboarding screen 2 `[SCREEN:cleaner-kit/IMG_2267]`; Cleanup asks after home `[SCREEN:cleanup/IMG_2240]`.
- **ATT.** Decision: not at launch. Why: 2 of 6 apps ask on screens 1–2 `[SCREEN:clever-cleaner/IMG_2272, freeup/IMG_2254]`, and Guideline 5.1.1(iv) bans manipulating consent `[APPLE:https://developer.apple.com/app-store/review/guidelines/]`. s4 confirms attribution; if ATT is needed, ask after the first win.

### 3.5 Core loop
- **Decision:**
  - Day 2: History shows "X GB still waiting in Recently Deleted" and "New since last clean".
  - Week 2: an optional weekly review, keeping context §10 screen 6 and §12's retention test.
  - Nothing new: "You're all caught up." No streaks, no health score.
- **Why:** context §13's moved-vs-reclaimed distinction becomes an honest reason to return (R5). The knowledge base's health-score idea `[ESTIMATE:knowledge/consumer_app_venture §4.2]` invites fake urgency.

### 3.6 Key screens

| Screen | Most important element | States to design |
|---|---|---|
| Clean (home) | True storage line | scanning (progressive), limited access, nothing to clean ("the rest is apps and system data, which iOS manages"), denied, error/resume |
| Large videos | Size + full preview; paid "Compress instead" shows before/after sizes | iCloud-only ("≈ size, in iCloud"), none large |
| Similar group | Reason line ("Suggested keep: sharpest of 4") + user toggles; favourites "Protected" | group of 2, all protected, user overrides |
| Review tray | "Nothing has been deleted yet." Total GB, and "Moves to Recently Deleted for 30 days. Deleting syncs to all devices using iCloud Photos." `[APPLE:https://support.apple.com/en-us/104967]`. The only red button | empty, user cancels the system confirm |
| Result | "moved" + 2-step guide to empty Recently Deleted. A direct album link is `[UNKNOWN: feasibility]` | partial failure (name the items), allowance reached (paywall) |
| Paywall | §3.7 | offline, pending, subscribed, not trial-eligible |

### 3.7 Paywall
- **Placement.** Decision: soft. Shown after the first result, and when a selection goes past the free daily allowance. The X is visible from frame 1. Why: R2, R15, and context §7 ("You have seen what the product can do").
- **Plans.** Structure only; **our prices are not set here**.
  - Decision: test annual + monthly vs annual + lifetime. No weekly at launch.
  - Why:
    - Weekly appears in 6/6 captured paywalls (R2) and sits at the centre of context §5 A and the knowledge base's trust evidence `[ESTIMATE:knowledge/organic-growth-knowledge-base §3.5]`.
    - Lifetime is seen at Cleanup and Clever `[SCREEN:cleanup/IMG_2242, clever-cleaner/IMG_2276]`.
    - US references from context §7: Cleanup $7.99–$11.99 weekly / $29.99 annual; Swipewipe $4.99–$9.99 weekly / $29.99 annual; Clever $6.99 weekly with trial / $39.99 lifetime.
- **Trial and cancel.**
  - Any trial shows a dated timeline with the charge, as in `[SCREEN:clean-manager/IMG_2230, darksy/IMG_2250]`.
  - No "trial enabled" interstitial and no pre-selected weekly.
  - Show the no-trial price plainly to users who aren't eligible (context §5 A).
  - Add one cancel line mirroring Apple's sheet `[SCREEN:freeup/IMG_2260]`.
- **Free keeps:** the full scan and all sizes, every preview, deletes up to a daily allowance (size set by test; visible benchmark "2 GB free daily" `[SCREEN:clever-cleaner/IMG_2275]`), and History.
- **Guideline 3.1.2:** say what the user gets before asking for money `[APPLE:https://developer.apple.com/app-store/review/guidelines/]`.

### 3.8 Visual language (directional; tokens belong to brand-designer)
- **Decision:**
  - Follow the system appearance, with light-led store shots.
  - One calm accent colour; neutral bars; red only on Delete.
  - Real photos shown large; no decorative "AI" art.
- **Why:**
  - All 6 apps are dark or navy with alarm bars (R10).
  - Context §4 says blue is fine; repeating the same colour, layout and message is the problem.
  - Clean Manager's "AI" orbit graphic `[SCREEN:clean-manager/IMG_2227]` is the decorative art we are avoiding.

### 3.9 Voice, accessibility, refusals
- **Voice:** plain, specific and calm.
  - We ship lines like "Nothing is deleted until you tap Delete.", "These look alike. We suggest keeping the sharpest one. You decide." (context §9's parent example) and "≈ means estimated. Tap to see how we counted."
  - We never ship:
    - "Free up to 80% of your storage with our AI-powered technology." `[SCREEN:clean-manager/IMG_2228]`
    - "Almost Full" `[SCREEN:clever-cleaner/IMG_2276]`
    - "50% faster response times with regular Free Up" `[SCREEN:freeup/IMG_2258]`
    - "3-day free trial is enabled!" `[SCREEN:darksy/IMG_2248]`
    - "2558 people have joined today!" `[SCREEN:freeup/IMG_2263]`
- **Accessibility:**
  - Dynamic Type everywhere, including plan cards.
  - VoiceOver reads each thumbnail's type, date, size and selection, and each group's reason.
  - Contrast to AA, with solid size chips.
  - Reduced Motion swaps animation for counters.
  - "≈" is never shown by colour alone.
- **Refuse list** (sources in E§1 Kill lists):
  - fake storage figures (E§2)
  - "up to N%"
  - "*Based on internal data" stat screens
  - performance claims
  - trial interstitials
  - paywalls with no visible close
  - a commitment plan sold as "most popular"
  - an unexplained "Save 89%"
  - badge counts that change between views
  - permission prompts before value
  - unprovable social proof

## 4. v1 product features

### 4.1 Feature table

| feature | user value | evidence | stake / diff | free / paid | iOS API / feasibility | effort [INFERRED] | v1? |
|---|---|---|---|---|---|---|---|
| 1. True storage overview | Truth on screen 1 | R6; clever-cleaner/IMG_2278 shows it can be read | diff | free | `volumeAvailableCapacityForImportantUsage` (iOS 11+) | S | yes |
| 2. On-device progressive, resumable scan | Fast, private | context §5 "time saved"; QA at 1K–200K libraries `[ESTIMATE:knowledge/consumer_app_venture §4.4]` | stake | free | PhotoKit + Vision; background limits `[UNKNOWN]`, spike | L | yes |
| 3. Large videos by size + preview | Biggest real space | R4, R7 | diff (as lead) | free view; delete in allowance | Duration: PHAsset. Bytes: see note below | M | yes |
| 4. Similar compare + reason, user picks | Speed without loss | R3; context §6 | diff | as above | Vision feature prints `[APPLE:https://developer.apple.com/documentation/vision/vngenerateimagefeatureprintrequest]` (iOS 13+); aesthetics + `isUtility` `[APPLE:https://developer.apple.com/documentation/vision/calculateimageaestheticsscoresrequest]` (iOS 18+); blur detection has no Apple API I verified, `[UNKNOWN: accuracy]` | L | yes |
| 5. Exact duplicates | Expected | 3 onboardings sell it (E§2 pattern 3) | stake | as above | hashing image data | S | yes |
| 6. Screenshots & "utility" images by age | Easy wins | clean-manager/IMG_2231, freeup/IMG_2262; context §8 table | stake | as above | screenshot media subtype; `isUtility` (iOS 18+) | S | yes |
| 7. Protected favourites | Safety | context §8 table | diff | free | `PHAsset.isFavorite` | S | yes |
| 8. Review tray + batched delete | Control, one confirm | R1, R5; Apple alert per change | diff | free | `PHAssetChangeRequest.deleteAssets` `[APPLE:https://developer.apple.com/documentation/photos/phassetchangerequest/deleteassets(_:)]` | M | yes |
| 9. Honest result + Recently Deleted guide + History | Knows when space returns | R5; context §13 | diff | free | Apple Support 30 days; direct album link `[UNKNOWN]` | S | yes |
| 10. Video compression, one preset | Keep video, regain space | R13; clever-cleaner/IMG_2275 before/after | stake | **paid** | AVFoundation export, then save, then delete original with confirm | M | yes; **first cut** |
| 11. "New since last clean" + optional weekly reminder | Repeat without guilt | context §10, §12 | diff | reminder free; weekly bulk paid | Photos change observer; local notifications | S | yes |
| 12. StoreKit 2 paywall + free daily allowance | Monetize honestly | R2, R8, R15 | stake | — | StoreKit 2 | M | yes |

**Note on per-file size (re-checked against Apple docs):**
- **The documented property is iOS 27+ only.** `PHAssetResource.dataSize`, "The size of the resource in bytes", is listed as introduced in **iOS 27.0** for both its Swift and Objective-C declarations. No other byte-size property appears in PHAssetResource's documented topic list `[APPLE:https://developer.apple.com/documentation/photos/phassetresource]`.
- **iOS 26 and earlier:** there is a documented but slower route. `PHAssetResourceManager.requestData(for:options:dataReceivedHandler:completionHandler:)` (iOS 9+) streams the resource's bytes, which can be counted `[APPLE:https://developer.apple.com/documentation/photos/phassetresourcemanager]`. Its speed and whether it forces iCloud downloads are `[UNKNOWN: feasibility]`.
- **Decision:**
  - Use `dataSize` on iOS 27+.
  - On older iOS, measure large videos by streaming and estimate the rest, marked "≈".
  - Settle this in a **week-1 on-device spike** (§5.4).

**Fit:** effort sums to 2 L + 4 M + 6 S `[INFERRED]`. That fits about 6 weeks only if the scan engine (2) and similarity (4) start in week 1. Compression is the release valve.

### 4.2 Later (v1.1 / v2), each with its trigger
- **Swipe mode:** if users ask to hand-sort non-similar photos, or D7 lags while scan→delete is healthy. Context §8 puts Swipewipe and Slidebox in that quadrant; we don't lead there.
- **Widget:** if D7/D30 return is the weakest funnel step.
- **Screenshot topics / context §11 Concept C:** if a screenshot-graveyard CPP wins on cost per qualified install.
- **Live Photo → still:** if Live photos turn out to be a meaningful GB share in real cohorts. Only "12.5 MB" on the test phone `[SCREEN:clever-cleaner/IMG_2278]`.
- **Contacts merge:** only on repeated user demand. It frees no storage.
- **Weekly plan:** only if annual/monthly can't reach payback.

### 4.3 Cut list
| Cut | Reason |
|---|---|
| Email cleaning | Not storage. Gmail restricted scopes may trigger verification `[ESTIMATE:knowledge/consumer_app_venture §4.4]` |
| Contacts / calendar | No storage value, adds tabs |
| Vault / "Secret Storage" | Different job, trust risk |
| iCloud cleaning as a feature | Deletion already syncs; nothing separate to sell (context §9) |
| "Boost" / speed / RAM / junk / cache | Not possible on iOS; App Review risk (§2.5) |
| "AI Categories" / "With Text" tiles | Invented abstractions `[SCREEN:darksy/IMG_2251]` |
| Health score | Manufactured urgency |

### 4.4 Free vs paid
- **Decision:**
  - **Free:** a user can fully see what is filling the phone, with true numbers. They can preview and compare everything, delete up to a daily allowance, and learn how to get the space back.
  - **Paid:** unlimited cleanup at once, video compression, and the weekly review.
- **Why:**
  - Context §7 frames the exchange as "decide whether completing the cleanup is worth paying for".
  - Clever already proves a free allowance (R8), so the free tier itself is not our edge. It is table stakes, and it earns reviews.
- **Build/design:** the limit appears *after* a completed cleanup, against the user's own real GB. That is what keeps it from feeling like a trap `[INFERRED]`.

### 4.5 Success metrics
1. **Photos permission grant:** target >70–75% `[ESTIMATE:knowledge/consumer_app_venture §6, "targets, not industry facts"]`.
2. **Scan → first approved delete in session 1:** target >25–30% of activated users `[ESTIMATE: same]`.
3. **Install → paid:** ~6% "as initial strong target" `[ESTIMATE: same]`. Our own target `[UNKNOWN: set after first cohort]`.
4. **Refund rate:** <5–7% `[ESTIMATE: same]`. Also track the share of 1–2★ reviews mentioning "charged" or "scam".
5. **Freed vs moved:** share of moved GB actually freed within 7 days. Target and measurement `[UNKNOWN: set after first cohort; s4 to confirm it is observable]`.

The primary money metric stays context §12's D30 net proceeds per install, with refunds and support tracked separately.

## 5. New recommendations

None of these is in context.md.

| # | What | Why | Cheap test | Kill if |
|---|---|---|---|---|
| 5.1 | **"One iPhone, six cleaners" truth test** as launch PR and challenger ad: each paywall's storage figure vs iOS Settings on one phone, then ours | Already documented (E§2). Knowledge base suggests pitching journalists who cover scammy cleaners `[ESTIMATE:knowledge/organic-growth-knowledge-base §3.5]`. Turns context §11 Concept B into proof | One organic short + one Meta creative vs Concept A, on cost per qualified install | s6 flags comparative-claim risk, or it clearly loses to control |
| 5.2 | **Lead with videos, not duplicates**: onboarding, home order, store shot 1 | R7. Three competitors open with duplicates (E§2 pattern 3) | Aggregate category GB on-device over the first 500 scans; CPP test | Cohort medians show similar photos beat videos on GB |
| 5.3 | **Recently Deleted as the day-2 loop**, with an opt-in reminder | Context §13 separates the states but has no mechanic (R5) | Opt-in rate; D2 return, opted-in vs not | Low opt-in and no D2 lift. Reading the album's size is `[UNKNOWN: feasibility]`; fallback is "You moved X GB on [date]" |
| 5.4 | **Week-1 on-device spike on file sizes** | Positioning depends on true or "≈" numbers (§4.1 note) | `dataSize` on iOS 27, byte-streaming on iOS 26; local vs iCloud-only; 1K/10K/50K libraries | Streaming too slow or forces downloads → show counts + "≈" on older iOS and set minimum OS |
| 5.5 | **"How we measured" on every number** | Replaces the social proof we lack (R12) | Track ⓘ taps | Almost unused → keep in-app, drop from store shots |
| 5.6 | **No-ATT launch** | Two competitors ask at launch (§3.4) | s4 confirms an Apple Ads-first launch works without it | Meta is the main channel and can't optimise without it → ask after first win |

## 6. Risks and open questions

| Risk | Mitigation |
|---|---|
| Spend war. Cleanup reported at 83–99% Apple Search Ads share of voice on core keywords; break-even CPI $12.83 vs $2.90 market `[ESTIMATE:knowledge/sanibha-app-factory §4.10]` | Win on creative (§5.1, §5.2), CPPs and PR. Don't bid head-on on "cleanup" terms at launch (s8) |
| Honest paywall misses payback | Order of fixes: placement and allowance tests, then plan mix, then weekly. Never fear copy |
| Leaders copy "honest" wording | Our moat is the whole system: true numbers, honest result, clean billing. Re-capture competitors monthly |
| Sizes wrong on iOS < 27 | §5.4 spike; "≈" labels; count fallback |
| Scan performance on 50K–200K libraries | Progressive, resumable scan; QA matrix `[ESTIMATE:knowledge/consumer_app_venture §4.4]` |
| A wrong delete leads to 1★ and a refund | Protected favourites; Recently Deleted explained before and after; iCloud-sync line in the tray (context §9) |
| App Review: misleading claims | Audit against Guidelines 1.1.6, 2.3.1 and 3.1.2 before submission (s7) |
| Apple Photos' own duplicate merge (context §13) | We lead with videos and similar photos, not exact duplicates |
| Build capacity (2 L items) | Compression is the first cut; swipe and widget already deferred |

**Open questions (cheapest answer):**
1. Competitors' Photos pre-prompts, limited-access, delete and result screens, and close-button delays → one capture session per app, from install, plus a screen recording.
2. US paywalls and prices → capture with a US Apple Account.
3. Does Clever's "2 GB free daily" behave as stated? → hands-on test.
4. Swipewipe, Cleaner Guru, AI Cleaner (context §1, no screens) → capture.
5. Can we read the size of Recently Deleted, or open it? → docs + 1-day prototype.
6. Was it one capture device? → ask Ganesh.

## 7. Verification

**Checked in this pass:**
- **Screen claims:** every screen figure and quote in this note was checked against the evidence file. E§0–E§2 was moved over unchanged from the version whose 12 key screens were re-opened earlier today (IMG_2230, 2231, 2239, 2241, 2250, 2251, 2262, 2266, 2271, 2275, 2276, 2278).
- **Counts:** "6/6 weekly" and "6/6 paywall before home" were re-counted from E§1. Weekly appears in clean-manager/IMG_2230, cleaner-kit/IMG_2271, cleanup/IMG_2239, clever-cleaner/IMG_2276, darksy/IMG_2250 and freeup/IMG_2261. For Cleaner Kit, home was not captured, so "before home" means "at the end of onboarding".
- **Context:** quotes and US prices for §§3, 5, 7, 9, 13, 14 were re-checked by grep.
- **Knowledge base:** figures 83–99%, $12.83 / $2.90, >70–75%, >25–30%, ~6% and ~5–7% re-checked by grep.

**Corrected or confirmed:**
- **`PHAssetResource.dataSize` iOS 27 claim, re-checked as asked:** confirmed. The doc JSON lists iOS 27.0 for both declarations, and no other size property exists on the class.
- **Added from that check:** the documented `PHAssetResourceManager` streaming fallback (iOS 9+). Its performance is marked `[UNKNOWN: feasibility]`.

**Not verifiable (marked in body):**
- The one-device inference.
- The source of FreeUp's "62 of 64 GB" figure.
- Reading or opening Recently Deleted.
- Blur accuracy.
- Background scan limits.
- US plan structures.
- Close-button delays.

**Previous calls:**
- *2026-10-05:* restructured into main note + evidence file per the updated skill. No positioning, UX or feature decision changed.
- *2026-10-05:* the iOS 27 `dataSize` claim was confirmed. Added the documented streaming fallback for iOS 26 and earlier, plus a week-1 spike. Previously this only said "estimate on older OS".
