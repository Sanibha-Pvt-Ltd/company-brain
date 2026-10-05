---
type: category-product-strategy
category: storage-cleaner
member: harshil
updated: 2026-10-05
status: draft
sources: [context.md, screenshots:52 across 6 apps, knowledge:consumer_app_venture_knowledge_base_2026-10-04.md + organic-growth-knowledge-base.md + sanibha-app-factory-knowledge-base.md, web:6]
---

# Storage Cleaner — product strategy (v1)

Built on [[research/categories/storage-cleaner/context]]. Inputs were that note and the team's 52 in-app screenshots. Nothing else from the team was read.

## TL;DR

- **Positioning:** *Make space. Keep what matters.* is kept as the line. The proof behind it changes: **real numbers, biggest wins first, nothing deleted without your approval.** The hook is "see what's really filling your iPhone" and leads with large videos. Fear does not sell it. `[INFERRED]`
- **Strongest screen finding:** the 6 apps were all captured on one phone (§0). That phone's own home screens show **about 47–55% used**. On the same phone the fear screens claimed "240 GB of 256 GB used", "95 from 100% used" and "Almost Full". Our edge is that every number on our screens is true and can be checked. `[SCREEN: see §2 table]`
- **UX decision 1:** the first screen shows the phone's **real** used and free storage before any permission. The first win is the first approved delete, with the GB shown honestly as "moved to Recently Deleted". It takes 7 taps. No competitor showed a freed-GB screen in the captures.
- **UX decision 2:** we lead with **large videos**, not "duplicates". On the captured library, exact duplicates came to 0–17 MB. Videos came to 2.18–2.62 GB. `[SCREEN: clean-manager/IMG_2231, cleanup/IMG_2241, darksy/IMG_2251, clever-cleaner/IMG_2278]`
- **UX decision 3:** a soft paywall that appears **after** the first win. The close button shows from the first frame. There is no trial theatre ("trial is enabled!"), no weekly price as the default, and no ATT or notification ask before value.
- **v1 features (12):** real storage overview · on-device scan · large videos · similar-photo compare with a stated reason · exact duplicates · screenshots and "utility" images · protected favourites · review tray · honest result screen + Recently Deleted guide · basic video compression (paid) · "new since last clean" · StoreKit 2 paywall with a free daily allowance.
- **Cut from v1:** email cleaning, contacts, vault, calendar, "boost performance", iCloud cleaning, and AI categories.
- **Top new recommendation:** a **"one iPhone, six cleaners" truth test**. We publish the same-device contradictions as our launch PR and creative angle, and run our own app through the same test (§6.1).
- **Confidence: medium.** The screens are strong up to each app's home screen. **None** of them show a scan, a review, a delete or a result screen. Every price is in ₹ (IN storefront), and Swipewipe, Cleaner Guru and AI Cleaner were not captured.

## 0. Inputs and confidence

**Screenshot inventory** (`ganesh_screenshots/Storage Cleaners/`, read in filename order, all 52 opened):

| Tag used here | Folder | Files | Stages captured | Missing |
|---|---|---|---|---|
| clean-manager | Clean Manager: Storage Cleaner | 7 (IMG_2226–2232) | welcome, 3 onboarding, paywall, home, paywall again | Photos permission prompt, scan, review, delete, result |
| cleaner-kit | Cleaner Kit - Clean Up Storage | 7 (IMG_2264, 2266–2271; no 2265) | App Store page, welcome, 4 onboarding, paywall | home, permission, scan, everything after paywall |
| cleanup | Cleanup: Phone Storage Cleaner | 10 (IMG_2233–2242) | onboarding, trial interstitials, paywall, home (+notification prompt), 2nd paywall | permission, scan, review, delete, result |
| clever-cleaner | Clever Cleaner: Photo Storage | 7 (IMG_2272–2276, 2278–2279; no 2277) | ATT prompt, 3 onboarding, paywall, home, paywall | permission, the free "2 GB daily" flow, delete, result |
| darksy | Darksy: Smart Storage Cleaner | 9 (IMG_2243–2251) | splash, 4 onboarding, trial interstitial, paywall, home | permission, scan, review, delete, result |
| freeup | Phone Storage Cleaner: Free up | 12 (IMG_2252–2263) | splash, ATT, 5 onboarding, trial interstitial, Apple purchase sheet, paywall, home, paywall again | permission, scan, review, delete, result |

**One device, one library.** All six apps were captured within the same window: status-bar times run 2:49 → 3:01 and the battery reads 79 → 75. The same photos appear in four apps' home screens (a moon photo in clean-manager/IMG_2231, cleanup/IMG_2241, clever-cleaner/IMG_2278 and freeup/IMG_2262; App Store-listing screenshots appear in clean-manager/IMG_2231 and cleanup/IMG_2240). Treating this as one phone and one library is `[INFERRED]`, but strongly supported. This lets us compare what each app *claimed* against what the phone *actually* showed.

**Storefront:** every in-app price is in ₹, so these are the India storefront. I report them as seen and do not convert them. US prices come only from context §7.

**context.md sections:** 1 landscape · 2 visual languages · 3 20-app audit · 4 first three store screenshots · 5 customer dissatisfaction (anxieties A–E) · 6 whitespace · 7 pricing · 8 visual map · 9 proposed storefront · 10 screenshots 4–6 · 11 Meta creative concepts A–C · 12 experiments · 13 what not to do · 14 final recommendation and hypothesis.

**Not captured, which limits confidence:**
- Photos permission prompts and pre-prompts, in any app.
- Scan or progress screens.
- Any review, compare or delete screen.
- Any "you freed X GB" screen.
- Close-button delays. Stills cannot show timing.
- Swipewipe, Cleaner Guru, AI Cleaner and Smart Cleaner. These are in context §1 but have no screens.

Our teardown therefore covers **launch → home** only. Every claim about first wins and repeat cost beyond home is `[UNKNOWN]` or `[INFERRED]`.

**Background read:** rules/company.md, company/about.md, company/tech-context.md, a5-screens-lens.md. From the knowledge base I read only the storage-cleaner sections of three files. Web use was limited to Apple docs, App Review Guidelines and Apple Support (cited inline).

## 1. Screen teardown

Columns: `# | file | stage | what user sees | asks | gives | verbatim copy | lever / friction`.

### 1.1 Clean Manager

| # | file | stage | what user sees | asks | gives | verbatim copy | lever / friction |
|---|---|---|---|---|---|---|---|
| 1 | IMG_2226 | welcome | Photos + Gmail icons, red bar | Terms consent; Photos access stated | nothing | "? of 256GB used" · "Your data stays private, we never collect or share your content." | Unknown number shown on a red "used" bar is a fear cue; the privacy line is good |
| 2 | IMG_2227 | onboarding 1/3 | "AI" orbit graphic | tap | claim | "Clean up duplicate and blurry photos instantly and free up space in seconds!" | Decorative AI, no real UI |
| 3 | IMG_2228 | onboarding 2/3 | 6 near-identical child photos | tap | claim | "Free up to 80% of your storage with our AI-powered technology." | Unbacked % claim (see §2: photos were ~2% of this device's storage) |
| 4 | IMG_2229 | onboarding 3/3 | Mail icon with "6583" badge | tap | claim | "Automatically remove spam and promotional emails and keep your inbox organized." | Email is out of scope for storage |
| 5 | IMG_2230 | paywall | Photos/iCloud with "800" badges, bar "71% from 100% used", X visible | payment | nothing real yet | "Due today … 1 week free ₹0.00 · Due: 10 October 2026 ₹999.00" · "7 days trial, then ₹999.00/week" | Good: trial timeline with date. Bad: fabricated-looking 800/800 badges and 71% |
| 6 | IMG_2231 | home | "55% / 255 GB", Photos 415 medias 2.86 GB, Videos 52 medias 2.62 GB, Others 135.2 GB; Similar 108 medias 536 MB; Duplicate 9 medias 17 MB; All videos 50 medias 2.24 GB; Screenshots 133 medias 280 MB; tabs Home/Contacts/Swipe/Compress/Tools | — | **first real value**: categories with sizes | "Similar photos" / "Duplicate photos" | Dense but real. "medias" is clumsy copy |
| 7 | IMG_2232 | paywall again | Same template, now "443" badges, "43% from 100% used" | payment | — | same plan copy | Badge and % changed between two views of the same paywall, so the numbers are not from the library `[INFERRED]` |

**Keep:**
- Trial timeline showing the "Due today" amount and the exact charge date. `[SCREEN:clean-manager/IMG_2230]`
- Visible X on the paywall. `[SCREEN:clean-manager/IMG_2230]`
- A home screen that splits Photos / Videos / Others with real sizes. `[SCREEN:clean-manager/IMG_2231]`
- The one-line privacy promise at the point of asking. `[SCREEN:clean-manager/IMG_2226]`

**Kill:**
- "? of 256GB used" on a red bar before we know anything. `[SCREEN:clean-manager/IMG_2226]`
- "Free up to 80% of your storage". `[SCREEN:clean-manager/IMG_2228]`
- Badge counts that change between views ("800" vs "443"). `[SCREEN:clean-manager/IMG_2230, IMG_2232]`
- Email onboarding in a storage app. `[SCREEN:clean-manager/IMG_2229]`

**Different:**
- Show the device's real "55% of 255 GB" (which the app clearly can read on home) on screen 1, not on screen 6. `[SCREEN:clean-manager/IMG_2231]`
- Put the paywall after the first approved delete, not before home. `[SCREEN:clean-manager/IMG_2230]`

### 1.2 Cleaner Kit

| # | file | stage | what user sees | asks | gives | verbatim copy | lever / friction |
|---|---|---|---|---|---|---|---|
| 1 | IMG_2264 | App Store page | "39K RATINGS 4.4", BPMobile, Utilities; store shots | — | — | "CLEAN UP IPHONE & ICLOUD" · "Featured by Apple" · "70M+ users" · "Space to c… 194.5" | Scale-based social proof we cannot match (context §4 lesson 3) |
| 2 | IMG_2266 | welcome | Photos + iCloud, striped red bar | Terms | a number | "240 GB of 256 GB used" | **Contradicted**: other apps on the same phone showed ~120 GB used (§2) |
| 3 | IMG_2267 | onboarding 2/5 | duplicate pairs with checkmarks; **system notification prompt on top** | notification permission | nothing | "Clear Duplicate Photos" · "Remove repeated shots instantly to free up space" | Asks before giving anything |
| 4 | IMG_2268 | onboarding 3/5 | storage bar Photos/Applications/iOS/System Data | tap | fake breakdown | "Reclaim up to 80% of your space" · "240GB of 256 GB used" · "*Based on internal data from Cleaner Kit" | Unbacked % + contradicted number |
| 5 | IMG_2269 | onboarding 4/5 | Mail "2546" | tap | claim | "Remove spam and promotional emails in one tap" | Scope creep |
| 6 | IMG_2270 | social proof 5/5 | laurels, user quotes | tap | — | "800,000+ 5-star ratings" · alex_1990 "My contacts are cleaned up... so much better." (shown **twice**) | Duplicated testimonial reads as filler |
| 7 | IMG_2271 | paywall | 3 plans, **no close control visible** | payment | — | "MONTHLY 12-month commitment (₹11,748.00 total) ₹ 979 per month" tagged "MOST POPULAR" · "YEARLY ₹4,999.00/year just ₹95.88/week" · "WEEKLY Free for 7 days, then ₹699.00/week" · "Auto-renewable. Cancel anytime." | "Most popular" is a 12-month commitment billed monthly, sitting next to "Cancel anytime". ₹979 × 12 = ₹11,748, which is 2.35× the yearly plan `[INFERRED]` |

**Keep:**
- Real product UI in store shots (a big GB number). `[SCREEN:cleaner-kit/IMG_2264]`
- A visible yearly-vs-weekly comparison with a per-week equivalent. `[SCREEN:cleaner-kit/IMG_2271]`

**Kill:**
- A notification prompt on onboarding screen 2. `[SCREEN:cleaner-kit/IMG_2267]`
- "240 GB of 256 GB used". `[SCREEN:cleaner-kit/IMG_2266]`
- "Reclaim up to 80%". `[SCREEN:cleaner-kit/IMG_2268]`
- Repeated testimonials. `[SCREEN:cleaner-kit/IMG_2270]`
- A commitment plan labelled "Most popular" beside "Cancel anytime", with no close visible. `[SCREEN:cleaner-kit/IMG_2271]`

**Different:**
- One plan card per product with its renewal shown in plain words. No commitment-monthly plan. Close visible. `[INFERRED]`

**Conflict with context:** context §7 lists Cleaner Kit US products at $4.99–$6.99. The IN paywall shows three plan types, including a 12-month-commitment monthly plan. US availability of that structure is `[UNKNOWN]`. To check, capture the US paywall.

### 1.3 Cleanup (Codeway)

| # | file | stage | what user sees | asks | gives | verbatim copy | lever / friction |
|---|---|---|---|---|---|---|---|
| 1 | IMG_2233 | welcome→onb 1 (transition) | welcome partially visible ("? of"), then duplicates | Terms | — | "Delete Duplicate Photos" · "Eliminate duplicate photos instantly and reclaim your storage!" | — |
| 2 | IMG_2234 | onboarding 1/3 | selfie pair + swipe-up chevrons | tap | — | same | Animated demo of the mechanic (good) |
| 3 | IMG_2235 | onboarding 2/3 | Photos/iCloud, bar | tap | — | "Free up to 80% of your storage and get more space." · "? GB of 255 GB used" · "*Based on Cleanup internal data" | Unbacked % |
| 4 | IMG_2236 | onboarding 3/3 | Mail "7.002" | tap | — | "Delete spam and promotional emails with just one tap." | Scope creep |
| 5 | IMG_2237–2238 | interstitial | animated text | none | — | "Try 7 days" → "For free!" | Trial theatre before the price |
| 6 | IMG_2239 | paywall 1 | Photos "611" / iCloud "329", full red bar; **no close visible** (only "Restore Purchase") | payment | — | "95 from 100% used" · "Cleanup Pro … Smart Cleaning, Video Compressor, Secret Storage, Manage Contacts, No Ads and Limits." · "Free for 7 days, then ₹999.00/week" · "Free trial enabled" · "Due 10 October 2026 ₹999.00" · "Try Free" | **95% contradicted** (same phone: ~47–55%) |
| 7 | IMG_2240 | home + notification prompt | "5.0 GB Space to Clean"; system notification prompt | notification permission | real total | "Optimize Storage · Free up to 2 GB from your files quickly" | Notification ask arrives right after value (better timing than Cleaner Kit) |
| 8 | IMG_2241 | home | Similars "New photos (918.3 MB)", Duplicates "0 Photos", Similar Videos, Similar Screenshots "18 Photos (19.8 MB)"; tabs Home/Email/Contacts/Optimize/Extras | — | **first real value** | "5.0 GB Space to Clean" · "See Analysis" | Honest "0 Photos" duplicates on this library |
| 9 | IMG_2242 | paywall 2 | X visible top-left (small, grey) | payment | — | "Unlock Unlimited Access" · "₹999.00/week, cancel anytime 7-day FREE TRIAL" · "₹3,999.00, Lifetime" tagged "Save 89%" · testimonial "So much faster than I could do one by one!" | "Save 89%" has no stated basis |

**Keep:**
- An animated demo of the real select/swipe mechanic in onboarding. `[SCREEN:cleanup/IMG_2234]`
- A single headline number on home ("5.0 GB Space to Clean"). `[SCREEN:cleanup/IMG_2241]`
- The notification ask placed after home, not before. `[SCREEN:cleanup/IMG_2240]`
- A lifetime option next to weekly. `[SCREEN:cleanup/IMG_2242]`

**Kill:**
- "95 from 100% used". `[SCREEN:cleanup/IMG_2239]`
- "Try 7 days / For free!" interstitials. `[SCREEN:cleanup/IMG_2237–2238]`
- A first paywall with no visible close. `[SCREEN:cleanup/IMG_2239]`
- "Save 89%" with no stated basis. `[SCREEN:cleanup/IMG_2242]`
- "Free up to 80%". `[SCREEN:cleanup/IMG_2235]`

**Different:**
- Our home headline number links to "how we counted". `[INFERRED]`

**Conflict with context:** context §7 lists Cleanup US as "$7.99–$11.99 weekly; $29.99 annual". The IN paywall shows weekly + **lifetime**, and no annual. Screens beat claims for what the app shows in IN. The US offer is `[UNKNOWN]`; to check, capture the US paywall.

### 1.4 Clever Cleaner

| # | file | stage | what user sees | asks | gives | verbatim copy | lever / friction |
|---|---|---|---|---|---|---|---|
| 1 | IMG_2272 | launch, onboarding 1/4 | **system ATT prompt over the first screen** | tracking permission | nothing | "Allow "Clever Cleaner" to track your activity across other apps and websites?" | Biggest ask, zero value given |
| 2 | IMG_2273 | onboarding 1/4 | real-looking photo collage with ✓/✕ | tap | — | "Smart ✦ Cleanup, Compress & Organize your Photo Storage." | Shows the keep/delete mechanic |
| 3 | IMG_2274 | onboarding 2/4 | swipe card, keep/trash | tap | — | "Swipes Free" · "Transform your mess into organized enjoyable memories within minutes." | States what is free |
| 4 | IMG_2275 | onboarding 3/4 | similars grid; compress before/after | tap | concrete example | "2 GB free daily" · "827.5 MB → 299.9 MB · SAVE 527.6 MB" | Best onboarding screen in the set: concrete free allowance + a before/after number |
| 5 | IMG_2276 | paywall 4/4 | X visible; storage bar labelled | payment | — | "Photo Storage · Almost Full" · "Weekly 3 days free, then ₹ 699 per week" (pre-selected) · "Lifetime Best Value ₹ 3,999 pay once" · "Auto-renewable. Cancel anytime" | **"Almost Full" contradicted** by its own home (next row) |
| 6 | IMG_2278 | home | rainbow header, real storage, category tiles | — | **first real value** | "120.28 GB of 255 GB used" · "Photo Library 2% · Data and apps 45% · Free 53%" · Similars 1.35 GB · Videos 2.62 GB · Screenshots 283.1 MB · Live photos 12.5 MB | The most honest storage breakdown seen. It also proves photos were 2% of this phone |
| 7 | IMG_2279 | paywall again | same as #5 | payment | — | same | Re-shown |

**Keep:**
- "2 GB free daily", a concrete free allowance stated before the paywall. `[SCREEN:clever-cleaner/IMG_2275]`
- Before/after compression sizes. `[SCREEN:clever-cleaner/IMG_2275]`
- The honest "Photo Library 2% · Data and apps 45% · Free 53%" breakdown. `[SCREEN:clever-cleaner/IMG_2278]`
- Weekly + lifetime only, which keeps the plan choice simple. `[SCREEN:clever-cleaner/IMG_2276]`

**Kill:**
- An ATT prompt on the first screen. `[SCREEN:clever-cleaner/IMG_2272]`
- "Almost Full" while 53% is free. `[SCREEN:clever-cleaner/IMG_2276, IMG_2278]`
- Weekly pre-selected. `[SCREEN:clever-cleaner/IMG_2276]`

**Different:**
- Show the 2%-of-storage truth and say what we *can* clean. `[INFERRED]`

**Conflict with context:** context §3 frames Clever Cleaner as "Clean without mandatory payment or ads". The screens show an ATT prompt at launch and a paywall at the end of onboarding with weekly pre-selected and a fear label. The paywall is closeable, and the free allowance is real (IMG_2275). It is **less clean than context implies**, which widens our opening on honesty.

### 1.5 Darksy

| # | file | stage | what user sees | asks | gives | verbatim copy | lever / friction |
|---|---|---|---|---|---|---|---|
| 1 | IMG_2243 | splash | icon | — | — | — | — |
| 2 | IMG_2244 | onboarding 1/4 | "87%" ring, decorative CLEAN button | tap | fake gauge | "3M Users" · "Clean Up Photos, Free Up Space" | 87% gauge is not this phone (§2) `[INFERRED]` |
| 3 | IMG_2245 | onboarding 2/4 | testimonials | tap | — | "Join 1 Million Happy Users!" · Nina_Bee "My phone stopped overheating and lagging after the cleanup." | **3M on screen 2 vs 1M on screen 3**; performance claim |
| 4 | IMG_2246 | onboarding 3/4 | stock photo card | tap | — | "PhotoSwipe" · "Enjoy a fun and easy way to clean up!" | — |
| 5 | IMG_2247 | onboarding 4/4 | gradient bar | tap | — | "Email Cleaner" · "Remove old emails, newsletters, and spam in just a couple of taps" | Scope creep |
| 6 | IMG_2248–2249 | interstitial | toggle animates off→on | none | — | "3-day free trial is enabled!" | Trial pre-toggled theatre |
| 7 | IMG_2250 | paywall | Photos "11" / iCloud "7"; Weekly/Yearly toggle; **no close visible**, CTA loading | payment | — | "35% from 100% used" · "Cleaner Darksy Pro … Free for 3 days, then ₹699.00/week" · "Due October 6, 2026 ₹699.00" · "No payment now" | Timeline is good; "No payment now" under a weekly auto-renew is soft framing |
| 8 | IMG_2251 | home | "Available to clean 4.70 GB", "Free 126 GB", "Used: 107 GB · Clutter: 4.70 GB · Total: 238 GB"; tiles Videos 2.18 GB, Similar 625 MB, Duplicates 5.65 MB, Selfies, Screenshots 265 MB, AI Categories 1.68 GB, Blurred 109 MB, With Text 437 MB; tabs Cleaner/PhotoSwipe/Cloud/Email/More | — | **first real value** | "Try For Free" (badge "1") | Clear separation of Used / Clutter / Free. Too many tiles (9+) |

**Keep:**
- The Used / Clutter / Free / Total line, where clutter sits next to the true total. `[SCREEN:darksy/IMG_2251]`
- Size chips on photo tiles. `[SCREEN:darksy/IMG_2251]`
- A dated trial timeline. `[SCREEN:darksy/IMG_2250]`

**Kill:**
- Inconsistent social proof ("3M Users" vs "1 Million"). `[SCREEN:darksy/IMG_2244, IMG_2245]`
- A testimonial claiming the phone stopped "overheating and lagging". `[SCREEN:darksy/IMG_2245]`
- "3-day free trial is enabled!" toggle. `[SCREEN:darksy/IMG_2248–2249]`
- A paywall with no visible close. `[SCREEN:darksy/IMG_2250]`
- Nine category tiles on home. `[SCREEN:darksy/IMG_2251]`

**Different:**
- Four categories max on home, ordered by GB. `[INFERRED]`

### 1.6 Phone Storage Cleaner: Free up ("FreeUp Cleaner")

| # | file | stage | what user sees | asks | gives | verbatim copy | lever / friction |
|---|---|---|---|---|---|---|---|
| 1 | IMG_2252 | splash | broom on blue | — | — | — | — |
| 2 | IMG_2253 | onboarding 1 | iCloud icon with ✕, red bar | Terms | — | "1 Million+ devices cleaned up!" · "62 of 64 GB used" · "Clean your storage easily!" | iCloud quota number shown before any sign-in or permission; source `[UNKNOWN]` and likely illustrative `[INFERRED]` |
| 3 | IMG_2254 | onboarding 2 + ATT | system ATT prompt | tracking permission | nothing | "Allow "FreeUp Cleaner" to track your activity across other companies' apps and websites?" · "This data will be used to gather performance statistics for personalizing your cleaning experience and fixing errors and crashes." | ATT purpose text describes crash/performance data, which is not tracking `[INFERRED]` |
| 4 | IMG_2255 | onboarding 3 | bar chart | tap | — | "+86%" · "extra space for all your media with Free Up" · "*Based on Free Up internal data" | Unbacked |
| 5 | IMG_2256 | onboarding 4 | line chart | tap | — | "160" · "duplicate contacts removed on average" | Unbacked |
| 6 | IMG_2257 | onboarding 5 | clock | tap | — | "8h" · "gained per month with automated Free Up" | Unbacked |
| 7 | IMG_2258 | onboarding 6 | speedometer | tap | — | "Boost Performance" · "50%" · "faster response times with regular Free Up" | Performance claim a photo cleaner cannot deliver (§3.7) |
| 8 | IMG_2259 | interstitial | toggle | none | — | "3 day free trial is enabled!" | Trial theatre |
| 9 | IMG_2260 | Apple purchase sheet over paywall | badges "343"/"278"; Apple IAP sheet | payment | — | "3-day free trial Starting today" · "₹ 699 per week Starting on 6 Oct 2026" · "No commitment. Cancel at any time in Settings > Apple Account at least one day before each renewal date." | Apple's sheet is the clearest disclosure in the whole set |
| 10 | IMG_2261 | paywall (loading) | badges now "200"/"120" | — | — | "25 from 100% used" · "Free Up Pro … Free for 3 days then ₹ 699/weekly" | Badges changed vs #9 within the same minute |
| 11 | IMG_2262 | home | "Storage Used: 120 GB / 255 GB · 424 items"; Similar Photos 46 items 427 MB; Screenshots 138 items 281 MB; Contacts "Unlock"; tabs Home/Photo/Video | — | **first real value** | "Ready to clean!" | Clean, short, honest home. The best IA of the six |
| 12 | IMG_2263 | paywall again | "Skip trial" top-right | payment | — | "2558 people have joined today!" · "Try Free" | Unverifiable live counter |

**Keep:**
- A 3-tab, short home: "Ready to clean!", two categories with item counts + MB, and a locked third. `[SCREEN:freeup/IMG_2262]`
- Item count next to size. `[SCREEN:freeup/IMG_2262]`

**Kill:**
- Six claim screens with "*Based on Free Up internal data". `[SCREEN:freeup/IMG_2255–2258]`
- "Boost Performance … 50%". `[SCREEN:freeup/IMG_2258]`
- ATT on screen 2. `[SCREEN:freeup/IMG_2254]`
- "62 of 64 GB used". `[SCREEN:freeup/IMG_2253]`
- "2558 people have joined today!". `[SCREEN:freeup/IMG_2263]`
- "Skip trial" as the only way out, worded as if the trial were the default. `[SCREEN:freeup/IMG_2261, IMG_2263]`

**Different:**
- Copy this app's home structure. Delete everything before it except one honest permission screen. `[INFERRED]`

## 2. Cross-app patterns

**Comparison table** (screens to home are counted from the captures; the Photos permission was never captured, so the true count is at least one more for every app `[INFERRED]`):

| | Clean Manager | Cleaner Kit | Cleanup | Clever Cleaner | Darksy | FreeUp |
|---|---|---|---|---|---|---|
| Screens before first real value (home) | 5 (2226–2230) | ≥6, home not captured | 7 incl. 2 interstitials (2233–2239) | 4 (2273–2276) | 7 (2243–2250) | 9 (2252–2261) |
| Asks before value | Terms, (Photos), payment | Terms, **notifications**, payment | Terms, payment, (Photos) | **ATT**, payment, (Photos) | payment, (Photos) | Terms, **ATT**, payment, (Photos) |
| Permissions seen and when | none captured | notifications at onboarding 2 | notifications on home, after paywall | ATT on first screen | none captured | ATT at onboarding 2 |
| Invented abstractions | "medias", Similar vs Duplicate | Similar/Duplicate | Similars, "Optimize" | Similars, "Heavies", "Lives" | Similar, Duplicates, "AI Categories", "With Text", "Clutter" | Similar |
| Paywall placement / type | end of onboarding, closeable; re-shown | end of onboarding, close not visible | after interstitials, close not visible; 2nd paywall closeable | end of onboarding, closeable | after trial interstitial, close not visible | after trial interstitial; "Skip trial" |
| Plans seen (₹, IN) | weekly ₹999 w/ 7-day trial | monthly ₹979 (12-mo commitment), yearly ₹4,999, weekly ₹699 w/ 7-day trial | weekly ₹999 w/ 7-day trial; lifetime ₹3,999 | weekly ₹699 w/ 3-day trial (pre-selected); lifetime ₹3,999 | weekly ₹699 w/ 3-day trial; yearly (price not shown) | weekly ₹699 w/ 3-day trial |
| Dark patterns counted (from Kill lists) | 3 | 5 | 4 | 2 | 4 | 6 |
| Visual language | black, blue CTA, red bars | dark grey, blue CTA, red/orange bars, purple paywall | navy, blue CTA, red bar | black, rainbow home header, real photos | navy, blue CTA, red/orange gauges | navy, blue CTA, red bars |

**The same-device contradiction table** (the most important evidence in this note):

| What the app's **fear** screen said | File | What a **home** screen on the same phone said |
|---|---|---|
| "240 GB of 256 GB used" | cleaner-kit/IMG_2266, IMG_2268 | "120.28 GB of 255 GB used … Free 53%" (clever-cleaner/IMG_2278); "120 GB / 255 GB" (freeup/IMG_2262); "Used: 107 GB … Free 126 GB … Total: 238 GB" (darksy/IMG_2251); "55% / 255 GB" (clean-manager/IMG_2231) |
| "95 from 100% used" | cleanup/IMG_2239 | same as above |
| "71% from 100% used", then "43% from 100% used" | clean-manager/IMG_2230, IMG_2232 | clean-manager's own home: "55% / 255 GB" (IMG_2231) |
| "Almost Full" | clever-cleaner/IMG_2276 | clever-cleaner's own home: "Free 53%" (IMG_2278) |
| "35% from 100% used" | darksy/IMG_2250 | darksy's own home: "Used: 107 GB … Total: 238 GB" (IMG_2251) |
| "25 from 100% used" | freeup/IMG_2261, IMG_2263 | freeup's own home: "120 GB / 255 GB" (IMG_2262) |
| "Free up to 80%", "Reclaim up to 80%" | clean-manager/IMG_2228, cleaner-kit/IMG_2268, cleanup/IMG_2235 | "Photo Library 2%" (clever-cleaner/IMG_2278); cleanable totals of "5.0 GB" (cleanup/IMG_2241) and "4.70 GB" (darksy/IMG_2251) |

Arithmetic `[INFERRED]`:
- 120.28 / 255 = 47%.
- 107 / 238 = 45%.
- So real usage on this phone sat at roughly 45–55% depending on how each app counts. None of the paywall percentages match it, and two apps' paywalls showed different percentages from their own home screens.
- Cleanable photo space was about 4.7–5.0 GB out of about 107–120 GB used, i.e. about 4%.

**Patterns that matter:**

1. **Shared paywall template (category convention).** Four of the six apps use the same paywall: "Clean your storage / Get rid of what you don't need", Photos + iCloud icons with red count badges, a "% from 100% used" bar, and a Due-today/Due-date timeline. `[SCREEN:clean-manager/IMG_2230, cleanup/IMG_2239, darksy/IMG_2250, freeup/IMG_2261]` Clean Manager and Cleanup even share this feature line word for word: "Smart Cleaning, Video Compressor, Secret Storage, Manage Contacts, No Ads and Limits." `[SCREEN:clean-manager/IMG_2230; cleanup/IMG_2239]` Looking different from this template is cheap differentiation. `[INFERRED]`
2. **Fear numbers are the norm and they are wrong.** See the table above. This is the screen-level version of context §5 Anxiety E ("ad made it look easier") and of the knowledge base's trust problem. `[ESTIMATE:knowledge/organic-growth-knowledge-base §3.5]`
3. **Everyone sells duplicates, but the library had almost none.** "Delete Duplicate Photos" or "Clear Duplicate Photos" is onboarding screen 1 or 2 in three apps. `[SCREEN:cleanup/IMG_2233–2234, cleaner-kit/IMG_2267, clean-manager/IMG_2227]` On the actual library, exact duplicates were "17 MB" (clean-manager/IMG_2231), "0 Photos" (cleanup/IMG_2241) and "5.65 MB" (darksy/IMG_2251). Videos were "2.24 GB" (clean-manager/IMG_2231), "2.62 GB" (clever-cleaner/IMG_2278) and "2.18 GB" (darksy/IMG_2251). The real space is in videos. `[INFERRED from one library, so test on more]`
4. **"Similar" means something different in every app.** On one library, "similar" measured 536 MB / 108 medias (clean-manager/IMG_2231), 918.3 MB "new photos" (cleanup/IMG_2241), 1.35 GB (clever-cleaner/IMG_2278), 625 MB (darksy/IMG_2251) and 427 MB / 46 items (freeup/IMG_2262). That is a 3× spread. Users are never told why something counts as similar. This is the screen proof behind context §5 Anxiety B and §6 "Explainable AI".
5. **Trial theatre.** Three apps run a full-screen "trial is enabled!" or "Try 7 days / For free!" interstitial before the price. `[SCREEN:cleanup/IMG_2237–2238, darksy/IMG_2248–2249, freeup/IMG_2259]` This is the visible form of context §5 Anxiety A.
6. **Permissions before value.** Two apps ask ATT in the first two screens and one asks for notifications on onboarding screen 2. `[SCREEN:clever-cleaner/IMG_2272, freeup/IMG_2254, cleaner-kit/IMG_2267]` Only Cleanup asks for notifications after showing home. `[SCREEN:cleanup/IMG_2240]`
7. **Nobody captured shows deletion, recovery or result.** Context §5 Anxiety D (accidental deletion) and §13 (GB found vs actually freed) cannot be checked against screens. This is the **largest blind spot**, and also the opening: none of the captured onboardings mention Recently Deleted. `[SCREEN: absence across all 52 files]`
8. **Scope creep is the convention.** Email cleaning appears in 4 of 6 onboardings (clean-manager/IMG_2229, cleaner-kit/IMG_2269, cleanup/IMG_2236, darksy/IMG_2247). Contacts appear in tabs or the paywall in 5 of 6.

## 3. Positioning

### 3.1 Who exactly
- **Primary user:** a US iPhone owner whose phone has just said storage is full, usually while trying to take a photo or video or install an update. Context §11 Concept A uses this trigger. Who this person is demographically is `[UNKNOWN]`; the screens do not show it. Context §5 points to people with personal memories at stake (Anxiety B, D).
- **Trigger and search:** "storage full" leads to App Store searches such as "storage cleaner", "phone cleaner" and "clean iPhone". `[ESTIMATE:knowledge/consumer_app_venture_knowledge_base §4.1]`
- **What they fear:**
  1. Deleting the wrong photo. `[CONTEXT §5 B, D]`
  2. Being charged weekly for something "free". `[CONTEXT §5 A]` `[ESTIMATE:knowledge/organic-growth-knowledge-base §3.5]`
  3. The app not delivering what the ad promised. `[CONTEXT §5 E]`

### 3.2 Job to be done
"My phone says it's full. Show me what's actually eating the space, let me get rid of the big stuff I don't need without losing anything I care about, and don't trick me into paying."

### 3.3 Options

Scored 1–5 `[INFERRED]`:

| Option | Acquisition pull | Differentiation vs screens | Defensibility | Monetization fit | Build in 6 wks | Honesty | Total |
|---|---|---|---|---|---|---|---|
| A. Context §14: "Make space. Keep what matters.", control + reassurance | 4 | 3 | 2 | 4 | 3 | 4 | 20 |
| B. "The honest cleaner": real numbers, no fear, clear billing | 3 | 4 | 2 | 3 | 4 | 5 | 21 |
| C. "Biggest wins first": large videos + space plan | 5 | 3 | 2 | 4 | 4 | 4 | 22 |
| D. Swipe/memories (Swipewipe territory, context §2, §8) | 3 | 2 | 2 | 3 | 3 | 4 | 17 |
| **E. A's line + B's proof + C's hook** | 5 | 4 | 3 | 4 | 3 | 5 | **24** |

**Pick: E.**
- **What stays from context §14:** the line *Make space. Keep what matters.* and "review before removing". Both stand.
- **What the screens add:** the category's most visible lie is the **numbers**, not only missing review controls. So the proof must be truthful measurement plus showing when the space actually comes back.
- **Why videos lead:** that is where the space was on the observed library.
- **Defensibility (3, not 2):** incumbents *can* copy honest copy in a sprint. But their paywalls (weekly default, fear bars) seem central to how they make money, so dropping them costs revenue. `[INFERRED; it may not hold, see §7]`

### 3.4 Positioning statement
For iPhone owners who just hit "storage full" and are afraid of deleting the wrong photo, **[KeepSpace, placeholder]** is the storage cleaner that shows what is really filling your phone, measured on your phone and biggest first, and deletes only what you approve. Unlike Cleanup, Cleaner Kit, Clean Manager, Darksy and FreeUp, whose paywalls in our captures showed storage figures that contradicted their own home screens, it shows real numbers and tells you exactly when the space comes back.

### 3.5 Promise hierarchy
- **Acquisition hook:** "See what's really filling your iPhone." Lead with the biggest videos.
- **Product differentiator:** "Real numbers. Nothing deleted without your OK."
- **Emotional benefit:** "Keep what matters." (context §14)
- **Retention reason:** "New clutter since your last clean, plus space waiting in Recently Deleted."

### 3.6 Proof points (visible on screen)
1. Screen 1 shows the phone's real used and free storage, before any permission, with a "How we measured" link. The API is `volumeAvailableCapacityForImportantUsage` `[APPLE:https://developer.apple.com/documentation/foundation/urlresourcevalues/volumeavailablecapacityforimportantusage]`.
2. Every size is marked measured or "≈ estimated".
3. Each similar group shows *why* one photo is suggested to keep (e.g. "sharper"), and the user picks.
4. Favourites are excluded by default and labelled "Protected".
5. The result screen says "moved to Recently Deleted, frees up after 30 days or when you empty it" `[APPLE:https://support.apple.com/en-us/104967]`, with a how-to.
6. The paywall states the price, period, renewal date and what stays free, and the X is visible at once.

### 3.7 What we will never claim
- Any "% full" or "% used" not read from the device.
- "Free up to N%".
- "Boost performance", "faster", "stops overheating" (freeup/IMG_2258, darksy/IMG_2245). Guideline 1.1.6 bars "inaccurate device data" and 2.3.1(a) bars promoting services not offered `[APPLE:https://developer.apple.com/app-store/review/guidelines/]`.
- Cleaning iCloud, system data, other apps' caches or "junk files". iOS sandboxing prevents it. `[ESTIMATE:knowledge/consumer_app_venture_knowledge_base §4.4]`
- "Freed X GB" at the moment of deletion. The honest wording is "moved to Recently Deleted". `[APPLE:https://support.apple.com/en-us/104967]` `[CONTEXT §13]`
- User counts, ratings or "people joined today" we cannot prove.
- "Featured by Apple" unless we are.
- That we can recover photos after Recently Deleted is emptied. `[CONTEXT §9, citing Apple Support]`

### 3.8 Naming and storefront direction
- **Name territory:** plain and calm, saying "space + keep". **KeepSpace** stays a placeholder until cleared (context §9). No availability claims.
- **First three App Store screenshots as one story: Measure → Choose → Done.** This keeps context §9's Find → Understand → Clean safely, re-ordered so the hook leads with real numbers and videos.
  1. "See what's really filling your iPhone." Real storage bar plus "Your biggest videos" list with sizes. The demo library must be real, and the caption must say the figures come from a demo phone. `[INFERRED]`
  2. "These look alike. You choose." A similar group with a stated reason and the user's pick (context §9 screenshot 2).
  3. "Nothing is deleted until you say so." Review tray, then the honest result line about Recently Deleted (context §9 screenshot 3).
- **One ad angle:** context §11 Concept A (storage-full moment) as control. The challenger is the **truth test** (§6.1): split screen of a fear bar saying "95% used" vs the phone's real Settings screen, then our app. This is creative-claim territory and needs review before running (s8 agent). `[INFERRED]`

## 4. UI/UX

### 4.1 Design principles (tie-breakers)
1. **Every number is true or labelled "≈".** (§2 contradiction table)
2. **Give before you ask:** no permission or payment prompt before the user has seen something real. (clever-cleaner/IMG_2272, cleaner-kit/IMG_2267)
3. **Biggest win first:** order everything by GB, and videos usually lead. (§2 pattern 3)
4. **Explain every suggestion in one line; the user decides.** (§2 pattern 4; context §5 B)
5. **Say when the space comes back, not just what you removed.** (§2 pattern 7; context §13)
6. **One concept per screen, four categories max.** (darksy/IMG_2251 vs freeup/IMG_2262)
7. **Calm, not alarm:** red only for irreversible actions. (§2 table: red bars used as fear everywhere)

### 4.2 Information architecture
- **Two tabs only:**
  - **Clean** is home, with the storage bar, then Videos / Similar / Screenshots & utility / Duplicates ordered by GB.
  - **History** shows past cleanups and GB waiting in Recently Deleted, which is the reason to come back.
- **Settings** sits behind a gear: subscription, protected items, notifications, "How we measure".
- **The review tray** is a persistent bottom bar ("3 items · 1.2 GB · Review"), not a tab.
- **No Email, Contacts, Vault, Swipe or Tools tabs.** clean-manager/IMG_2231 has 5 tabs and cleanup/IMG_2241 has 5, each mixing in non-storage jobs. freeup/IMG_2262 shows 3 tabs work.

### 4.3 First five minutes

Taps are cumulative. The first win is starred.

| # | Screen | Purpose | What's on it | Primary action | Copy direction | Asks | Given so far | Taps |
|---|---|---|---|---|---|---|---|---|
| 1 | Welcome / real storage | First truth, before any ask | Real used/free from the volume API; one line on what we clean (photos & videos only) | "Scan my photos" | "Your iPhone: [live used] GB used of [live total] GB." (placeholders, filled from the device) "We'll find what's taking space in your photos and videos." | none (Terms link in footer) | real device storage | 1 |
| 2 | Photos pre-prompt | Earn full access | 3 lines: analysed on this iPhone; nothing uploaded; nothing deleted without your OK. "Select photos" path explained | "Continue" | Plain, no urgency | Photos permission (next) | storage truth + privacy promise | 2 |
| 3 | System Photos prompt | — | iOS sheet | "Allow Full Access" | — | Photos | — | 3 |
| 4 | Scan (progressive) | Show real progress | Live counters per category; videos appear first (sizes are cheapest to read) | Can tap "Videos" as soon as it's ready | "Found 52 videos · 2.6 GB so far" (live) | none | growing real results | — |
| 5 | Clean (home) | Choice | Storage bar; categories by GB with item counts; "≈" where estimated | Tap the top category (usually "Large videos") | "Biggest first" | none | full real inventory | 4 |
| 6 | Large videos | Decide | List sorted by size: thumbnail, duration, size, date; tap = full preview | Select 1–n | "Tap to preview before you choose." | none | previews | 5 (select) |
| 7 | Review tray + system confirm | Approve | Thumbnails, total GB, "Moves to Recently Deleted for 30 days" | "Delete 3 videos" → iOS confirm | "Nothing has been deleted yet." | delete confirm (system) | full control | 6–7 |
| 8 ★ | **Result (first win)** | Honest outcome | "1.2 GB moved to Recently Deleted." "iPhone frees it after 30 days, or now if you empty Recently Deleted." [Show me how] | "Show me how" / "Done" | Calm, specific | optional: "Remind me when it's freed?" (notification opt-in, see 4.4) | GB moved + how to free it now | 7 |
| 9 | Soft paywall | Convert after value | What they just did; what's left (real GB); what's free vs paid; plans; X visible | "Start [plan]" / X | See 4.7 | payment (optional) | a completed cleanup | — |

**First-win count: 7 taps**, including the permission and the system delete confirm. No captured competitor shows a first win (freed GB), so the comparison is on **first real value** (home with real sizes):
- Ours arrives at tap 3 plus the scan.
- Competitors needed 4–9 screens before home, and the permission still comes on top (§2 table).
- Best measured: clever-cleaner, 4 screens incl. one paywall.

Ours beats every captured flow to first value. The first-win comparison is `[UNKNOWN]` until the delete flows are captured (§7).

### 4.4 Permission strategy
- **Photos:** request `.readWrite` after our pre-prompt (screen 2).
  - **Limited access** is a real state `[APPLE:https://developer.apple.com/documentation/photos/phauthorizationstatus/limited]`. We scan only the selected items, show a banner "Scanning 40 selected photos · Allow full access to scan everything", and suppress the automatic limited-library alert so we control the moment (`PHPhotoLibraryPreventAutomaticLimitedAccessAlert`, same URL).
  - **Denied:** screen 1 still shows real device storage, plus a "Open Settings" card. No nagging loop.
- **Delete:** every batch triggers iOS's own confirmation. Per Apple, "For each call to this method, iOS shows an alert asking the user for permission to edit the contents of the photo library" `[APPLE:https://developer.apple.com/documentation/photos/phphotolibrary/performchanges(_:completionhandler:)]`. So we batch per review, and silent or background deletion is impossible by design.
- **Notifications:** asked **only** on the result screen, as an opt-in toggle tied to a concrete benefit ("Tell me when the 1.2 GB is freed" / "Weekly: new clutter since last clean"). Never at launch. Compare cleaner-kit/IMG_2267.
- **ATT:** not in v1. We do not request tracking at launch. Whether paid-UA attribution needs ATT is for the s4 agent; if it does, ask after the first win, never first (clever-cleaner/IMG_2272, freeup/IMG_2254). Guideline 5.1.1(iv) forbids manipulating consent `[APPLE:https://developer.apple.com/app-store/review/guidelines/]`.

### 4.5 Core loop and repeat use
- **Day 2:**
  - The History tab and an optional notification show "1.2 GB still waiting in Recently Deleted". This is a genuine, non-fear reason to return and finish the job.
  - "New since your last clean: 14 photos, 3 videos."
- **Week 2:** an optional weekly review ("A little cleaner every week", context §10 screenshot 6). The count is real; if there is nothing, say so: "You're all caught up."
- **Repeat cost:** open → Clean (pre-scanned, incremental) → top category → select → delete. That is 4 taps + the system confirm `[INFERRED]`. Competitor repeat cost is `[UNKNOWN]` (not captured).
- **No** streaks, scores or guilt copy. The "storage-health score" in `[ESTIMATE:knowledge/consumer_app_venture_knowledge_base §4.2]` stays out of v1 because it invites the manufactured urgency we refuse.

### 4.6 Key screens spec

**A. Clean (home)**
```
[ 118 GB used · 138 GB free · of 256 GB ]   ⓘ How we measured
[█████████████░░░░░░░░░░░░░]  Photos & videos: 5.1 GB
Biggest first
  ▶ Large videos        52 · 2.6 GB   >
  ▣ Similar photos   ≈108 · 540 MB   >
  ▤ Screenshots & notes 133 · 280 MB  >
  ⧉ Exact duplicates      9 · 17 MB   >
[ Review tray: 0 items ]
```
The figures above are layout placeholders, not data.

- **States:**
  - **Scanning:** progressive counters, categories unlock one by one.
  - **Partial (limited access):** banner.
  - **Nothing to clean:** "Your photos look tidy. The rest of your storage is apps and system data, which iOS manages. [Open iPhone Storage]".
  - **Denied:** device storage only + Settings card.
  - **Error:** retry; scan resumes.
- **Most important element:** the true storage line.

**B. Large videos**
- **Layout:** list of thumbnail + duration + size + date, sorted by size. Tap opens a full-screen player with "Keep / Add to cleanup". A "Compress instead" action is paid. Compression must say the original is replaced, show both sizes, and require the delete confirm.
- **States:** iCloud-only video (preview needs download, so show "≈ size, stored in iCloud"); none over threshold; loading thumbnail.
- **Most important element:** size + preview.

**C. Similar group compare**
- **Layout:** large selected image on top; filmstrip of the group below; one line of reason ("Suggested keep: sharpest of 4"); toggles per photo; Favourites marked "Protected".
- **States:** group of 2; all protected; user overrides the suggestion.
- **Most important element:** the reason line + the user's pick.
- **Feasibility:** similarity via Vision feature prints `[APPLE:https://developer.apple.com/documentation/vision/vngenerateimagefeatureprintrequest]` (iOS 13+). Quality and "utility" signals via `CalculateImageAestheticsScoresRequest`, which reports `isUtility`: "images that are not necessarily of poor image quality, but may not have memorable or exciting content" `[APPLE:https://developer.apple.com/documentation/vision/calculateimageaestheticsscoresrequest]` (iOS 18+). Blur detection has no dedicated Apple API that I verified; it would be computed `[UNKNOWN: accuracy, spike in week 1]`.

**D. Review tray**
- **Layout:** grid of everything selected across categories; total GB; one line "Moves to Recently Deleted for 30 days. Deleting syncs to all devices using iCloud Photos." `[APPLE:https://support.apple.com/en-us/104967]`; red "Delete N items" button (the only red in the app).
- **States:** empty; mixed local/iCloud; user cancels the system confirm (return, nothing changed).
- **Most important element:** "Nothing has been deleted yet."

**E. Result**
- **Layout:** GB moved; two-step guide to empty Recently Deleted; History link; optional reminder toggle.
- **States:** partial failure (some items not deleted, so name them); free allowance reached (soft paywall entry).
- **Most important element:** "moved", never "freed".
- Whether we can open the Recently Deleted album directly is `[UNKNOWN: feasibility]`. I found no documented API; we show instructions.

**F. Paywall** (see 4.7)
- **Layout:** what you did → what's left (real GB) → free vs paid table → plans → X from frame 1 → disclosure.
- **States:** offline; purchase pending; already subscribed; trial-ineligible (an introductory offer is only available once; context §5 A cites developer replies about this). Show the no-trial price plainly.

### 4.7 Paywall
- **Placement:** soft. It appears after the first result screen, and when the user selects beyond the free daily allowance. It is never in onboarding.
- **What precedes it:** the real scan + one completed cleanup.
- **Close:** visible immediately. No delay, no "Skip trial" wording.
- **Plans to test first** (structure only; **our prices are not set here**):
  - **Test 1:** annual (with or without intro trial) + monthly.
  - **Test 2:** annual + lifetime. Lifetime is seen in cleanup/IMG_2242 and clever-cleaner/IMG_2276, and context §7 lists Clever $39.99 lifetime.
  - **No weekly at launch** `[INFERRED]`. Weekly is the default in 5 of 6 paywalls (§2), and it is the core of the trust complaints `[CONTEXT §5 A]` `[ESTIMATE:knowledge/organic-growth-knowledge-base §3.5]`. It comes back only if annual or monthly cannot reach payback (§5.5).
  - US competitor references: Cleanup $7.99–$11.99 weekly, $29.99 annual; Swipewipe $4.99–$9.99 weekly, $29.99 annual; Clever $6.99 weekly with trial, $39.99 lifetime `[CONTEXT §7, citing US App Store IAP listings]`.
- **Trial framing:**
  - If we offer a trial, show a timeline with the exact charge date and amount, as clean-manager/IMG_2230 and darksy/IMG_2250 do. Copy that good part.
  - Default to the plan without a trial pre-selected, or no pre-selection at all `[INFERRED]`.
  - No "trial is enabled!" interstitial.
- **Cancel clarity:** one line, "Cancel anytime in Settings › Apple Account at least one day before renewal". This mirrors Apple's own sheet in freeup/IMG_2260. Add a "How to cancel" link.
- **Free users keep:**
  - the full scan and all sizes;
  - all previews and compare screens;
  - deletion up to a daily allowance (size set by test; the visible benchmark is Clever's "2 GB free daily" in clever-cleaner/IMG_2275);
  - History and the Recently Deleted guide.
- **3.1.2:** state what the user gets for the price before asking. "Before asking a customer to subscribe, you should clearly describe what the user will get for the price" `[APPLE:https://developer.apple.com/app-store/review/guidelines/]`.

### 4.8 Visual language (directional; tokens belong to brand-designer)
- **Competitor map from screens:** all 6 apps run dark/navy backgrounds with blue CTAs and red or orange alarm bars (§2 table). Clever adds a rainbow header (clever-cleaner/IMG_2278). The store creatives are blue/white or blue/purple, with Swipewipe on peach/rainbow `[CONTEXT §2, §4]`.
- **Our direction:**
  - Follow the system appearance, with light mode as the hero for store shots (stands apart from the in-app dark/navy wall).
  - One calm accent colour that is not alarm-red.
  - Neutral bars; red only on the Delete button.
  - Real photos at large size; numbers in tabular figures.
  - Standard iOS density, not tile mosaics.
  - Motion only for scan progress, and none decorative (no "AI" orbits, clean-manager/IMG_2227).

### 4.9 Voice and copy
**Tone:** plain, specific, calm, a little warm. We state facts, never pressure.

**Lines we would ship:**
1. "Nothing is deleted until you tap Delete."
2. "These look alike. We suggest keeping the sharpest one. You decide."
3. "1.2 GB moved to Recently Deleted. Your iPhone frees it after 30 days, or now if you empty that album."
4. "≈ means estimated. Tap to see how we counted."
5. "You're all caught up. Nothing new since Tuesday."

**Lines from competitor screens we would never ship:**
1. "Free up to 80% of your storage with our AI-powered technology." (clean-manager/IMG_2228)
2. "Almost Full" (clever-cleaner/IMG_2276, while its home said "Free 53%" in IMG_2278)
3. "50% faster response times with regular Free Up" (freeup/IMG_2258)
4. "3-day free trial is enabled!" (darksy/IMG_2248)
5. "2558 people have joined today!" (freeup/IMG_2263)

### 4.10 Accessibility basics
- **Dynamic Type** on every screen, including the paywall and its plan cards. The storage line wraps; it is not truncated.
- **VoiceOver:**
  - Each thumbnail reads type, date, size and selection state ("Video, 2 minutes 14 seconds, 412 megabytes, March 3, not selected").
  - Similar groups announce the suggestion and its reason.
  - The tray announces its total.
- **Contrast:** WCAG AA for text and size chips over photos. Use a solid chip, not translucent.
- **Reduced Motion:** replace scan animations with a counter.
- **Colour:** "measured vs ≈" is not shown by colour alone.

### 4.11 Refuse list
- Storage figures not read from the device (cleaner-kit/IMG_2266, cleanup/IMG_2239, clean-manager/IMG_2230, IMG_2232, darksy/IMG_2244, IMG_2250, freeup/IMG_2253, IMG_2261).
- "Almost Full" or alarm bars as decoration (clever-cleaner/IMG_2276).
- "Up to N%" and "internal data" statistic screens (clean-manager/IMG_2228, cleaner-kit/IMG_2268, cleanup/IMG_2235, freeup/IMG_2255–2258).
- Performance or overheating claims (freeup/IMG_2258, darksy/IMG_2245).
- Trial-enabled interstitials (cleanup/IMG_2237–2238, darksy/IMG_2248–2249, freeup/IMG_2259).
- Paywalls without a visible close (cleaner-kit/IMG_2271, cleanup/IMG_2239, darksy/IMG_2250).
- Commitment plans labelled "Most popular" beside "Cancel anytime" (cleaner-kit/IMG_2271).
- Unexplained "Save 89%" (cleanup/IMG_2242).
- Changing badge counts (clean-manager/IMG_2230 vs IMG_2232; freeup/IMG_2260 vs IMG_2261).
- ATT or notification prompts before value (clever-cleaner/IMG_2272, freeup/IMG_2254, cleaner-kit/IMG_2267).
- Unprovable social proof (cleaner-kit/IMG_2270, darksy/IMG_2244–2245, freeup/IMG_2253, IMG_2263).

## 5. v1 product features

### 5.1 Feature table

| feature | user value | evidence | stake / diff | free / paid | iOS API / feasibility | effort [INFERRED] | in v1? |
|---|---|---|---|---|---|---|---|
| 1. Real storage overview | Truth on screen 1 | §2 contradiction table; clever-cleaner/IMG_2278 shows it's readable | differentiator (honesty) | free | `volumeAvailableCapacityForImportantUsage`, iOS 11+ [APPLE link §3.6] | S | yes |
| 2. On-device progressive scan, resumable | Fast, private, no waiting | context §5 "Time saved"; perf QA at 1K–200K libraries [ESTIMATE:knowledge/consumer_app_venture §4.4] | stake | free | PhotoKit + Vision; background continuation `[UNKNOWN: duration limits, spike]` | L | yes |
| 3. Large videos by size + full preview | The biggest real space | §2 pattern 3; context §5 C | diff (as lead) | free to view, delete in allowance | PHAsset duration; per-asset size: `PHAssetResource.dataSize` exists **only iOS 27+**; earlier OS has no documented size API, so estimate and label "≈" | M | yes |
| 4. Similar photos: compare + stated reason, user picks | Speed without losing memories | §2 pattern 4; context §5 B, §6 | diff | free to view, delete in allowance | Vision feature prints (iOS 13+); aesthetics/isUtility (iOS 18+) | L | yes |
| 5. Exact duplicates | Expected by users | 3 onboardings sell it (§2 pattern 3) | stake | free | hashing of image data | S | yes |
| 6. Screenshots & "utility" images, grouped by age | Easy bulk wins | clean-manager/IMG_2231, freeup/IMG_2262; context §8, §11 C | stake | free | `PHAssetMediaSubtype.photoScreenshot`; `isUtility` iOS 18+ | S | yes |
| 7. Protected items (Favourites excluded by default) | Safety | context §8 table "Favorite photos: Protected" | diff | free | `PHAsset.isFavorite` | S | yes |
| 8. Review tray + single batched delete | Control, one confirm | context §5, §14; Apple's per-change alert [APPLE link §4.4] | diff | free | `PHAssetChangeRequest.deleteAssets` | M | yes |
| 9. Honest result + Recently Deleted guide + History | Knows when the space returns | context §13; §2 pattern 7 | diff | free | Apple Support 30 days [APPLE:https://support.apple.com/en-us/104967]; direct album link `[UNKNOWN]` | S | yes |
| 10. Video compression (one quality preset, before/after sizes) | Keep the video, get space back | clever-cleaner/IMG_2275; Cleanup/Clean Manager paywalls list "Video Compressor" | stake | **paid** | AVFoundation export + save new + delete original (confirm) | M | yes, **first to cut** if week 4 slips |
| 11. "New since last clean" + optional weekly reminder | Repeat use without guilt | context §10 screenshot 6, §12 retention test | diff (honest) | free (reminder), paid (weekly bulk) | `PHPhotoLibraryChangeObserver` / date fetch; local notifications | S | yes |
| 12. StoreKit 2 paywall + free daily allowance | Monetization | §4.7 | stake | — | StoreKit 2 | M | yes |
| Swipe mode | Fun manual sort | clever-cleaner/IMG_2274, darksy/IMG_2246, clean-manager tab | stake-ish | — | trivial UI | M | **later** |
| Home-screen widget (free space + waiting GB) | Ambient reminder | [ESTIMATE:knowledge/consumer_app_venture §4.2 pillar 5] | diff | free | WidgetKit | S | **later** |
| Screenshot topics (receipts, recipes…) | Context §11 Concept C wedge | context §11 C | diff | paid | Vision text recognition | M | **later** |

Rough effort sum `[INFERRED]`: 2 L + 5 M + 6 S. That fits a small team in about 6 weeks only if the scan engine (2) and similarity (4) start in week 1. Compression (10) is the pressure valve.

### 5.2 Later (v1.1 / v2), with triggers
- **Swipe mode:** bring in if session recordings or reviews show users want to manually sort non-similar photos, or if D7 is below target while scan→delete is healthy.
- **Widget:** if the D7/D30 return rate is the weakest funnel step.
- **Screenshot topics / Concept C:** if a Custom Product Page test for "screenshot graveyard" wins on cost per qualified install (context §11 C, §12).
- **Live Photo → still conversion:** if Live photos are a meaningful GB share across early cohorts. Only 12.5 MB on the captured library (clever-cleaner/IMG_2278).
- **Contacts merge:** only if support or reviews ask for it repeatedly. It does not free storage.
- **Weekly plan:** only if annual/monthly fails payback (see 5.5).

### 5.3 Cut list (won't build)
- **Email cleaning:** a different job. Gmail OAuth restricted scopes may trigger verification or security assessments `[ESTIMATE:knowledge/consumer_app_venture §4.4]`. It also fills 4 onboardings with claims (§2 pattern 8).
- **Contacts & calendar cleaning:** no storage value, adds tabs.
- **Secret vault / "Secret Storage":** a different job, and adds trust risk.
- **"Cloud" or iCloud cleaning:** we can only act on Photos assets the user authorises. iCloud deletion syncs across devices; that is the same action, not a separate feature. `[CONTEXT §9]`
- **"Boost performance", speed, RAM, junk or cache:** not possible on iOS, and App Review risk (§3.7).
- **"AI Categories" / "With Text" tiles:** invented abstractions (darksy/IMG_2251).
- **Storage-health score:** invites fake urgency (§4.5).

### 5.4 Free vs paid line
- **Free users can fully:**
  - see what is filling their iPhone, with true numbers;
  - preview and compare everything;
  - delete up to a daily allowance;
  - learn exactly how to get the space back.
  
  A user with a small problem can solve it without paying, which buys reviews and word of mouth.
- **Payment unlocks:**
  - unlimited cleanup in one go;
  - video compression;
  - the weekly "new clutter" review.
- **Why this converts without feeling like a trap:** the user meets the limit *after* seeing their own real GB and finishing one cleanup. The paywall then sells "finish the rest now" against a number they trust. That is context §7's "Now decide whether completing the cleanup is worth paying for", made concrete. `[INFERRED]`

### 5.5 Success metrics for v1
1. **Photos permission grant (full + limited).** Knowledge-base *internal target*, not a benchmark: >70–75% `[ESTIMATE:knowledge/consumer_app_venture §6 "Early Cleaner launch metrics proposed (targets, not industry facts)"]`.
2. **Scan → first approved delete in session 1.** Same source's target for "meaningful first-session cleanup": >25–30% of activated users `[ESTIMATE: same]`.
3. **Paywall view → paid (or install → paid).** Same source: install→paid ~6% "as initial strong target" `[ESTIMATE: same]`. Our own target is `[UNKNOWN: set after first cohort]`.
4. **Refund rate and 1–2★ share mentioning "charged" or "scam".** Same source: refunds ideally under ~5–7% `[ESTIMATE: same]`.
5. **D7 return to History or Clean.** `[UNKNOWN: set after first cohort]`
6. **North-star check (ours, new):** share of "moved" GB that is actually freed within 7 days (user empties Recently Deleted). `[UNKNOWN: set after first cohort]`; measurement method `[UNKNOWN]`, needs s4 to confirm it is observable.

## 6. New recommendations

None of these are in context.md.

1. **"One iPhone, six cleaners" truth test as a launch asset.**
   - **What:** a short video or blog post running each cleaner on one phone and setting its paywall figure next to iOS Settings. Then show ours.
   - **Why:** our captures already show it (§2 contradiction table). The knowledge base suggests pitching journalists who cover scammy cleaners `[ESTIMATE:knowledge/organic-growth-knowledge-base §3.5]`.
   - **Cheap test:** run one organic short and one Meta creative vs Concept A; measure cost per qualified install.
   - **Kill if:** s6 legal review flags comparative-claim risk, or the creative underperforms control by a clear margin in the first test.
2. **Lead with videos, not duplicates.**
   - **What:** onboarding, home order and store screenshot 1 lead with "Your biggest videos".
   - **Why:** 0–17 MB exact duplicates vs 2.18–2.62 GB videos on the observed library (§2 pattern 3), while three competitors open with duplicates.
   - **Cheap test:** instrument category GB on the first 500 scans (anonymous, on-device aggregated) and A/B the screenshot-1 CPP.
   - **Kill if:** median cohort data shows similar photos beat videos on GB.
3. **Recently Deleted as the day-2 loop.**
   - **What:** History shows "X GB waiting in Recently Deleted", with an opt-in reminder.
   - **Why:** context §13 separates "moved" from "reclaimed" but proposes no mechanic. This turns an honesty caveat into a reason to return.
   - **Cheap test:** opt-in rate on the result screen; D2 return of opted-in vs not.
   - **Kill if:** opt-in is very low and D2 shows no lift.
   - Feasibility of *reading* how much is still in Recently Deleted is `[UNKNOWN]`. Spike it; fall back to "you moved X GB on [date]".
4. **Week-1 technical spike on per-asset size without private API.**
   - **What:** decide the minimum iOS version and the size-estimation method.
   - **Why:** `PHAssetResource.dataSize` is documented only from iOS 27 [APPLE: §5.1 row 3]. Pre-27 sizes must be estimated, and our whole positioning depends on numbers being right or labelled.
   - **Kill/adjust if:** estimates differ from iOS 27 measured values by more than an agreed tolerance. Then show counts, not GB, on older OS.
5. **"How we measured" sheet on every number.** Not in context; it is the concrete proof mechanism for B/E. Cheap test: track taps on ⓘ; if almost nobody taps, keep it but drop it from store screenshots.
6. **No-ATT launch.** Not in context. Two of six competitors ask ATT before value (§2). Decide with s4 whether Apple Ads-first attribution lets us skip it in v1. Kill if s4 shows Meta optimisation is impossible without it *and* Meta is the primary channel.

## 7. Risks and open questions

**Risks**

| Risk | Mitigation |
|---|---|
| **Spend war:** Cleanup reported at 83–99% Apple Search Ads share of voice on core keywords; break-even CPI $12.83 vs $2.90 market `[ESTIMATE:knowledge/sanibha-app-factory §4.10]` | Win on creative (truth test, video-first), CPPs and organic/PR; do not bid head-on on "cleanup" terms at launch. s8 to plan |
| Honest paywall converts below payback | Measure D30 net per install, as context §12 says; the fallback order is pricing and placement tests, then weekly plan, never fear copy |
| Leaders copy "honest" wording in a sprint | Our moat is the whole system (true numbers + result honesty + billing). Track competitor screens monthly (re-capture) |
| Per-asset sizes wrong on iOS < 27 | §6.4 spike; label "≈"; count-based fallback |
| Scan performance on 50K–200K libraries (thermal, memory) | Progressive + resumable scan; QA matrix from `[ESTIMATE:knowledge/consumer_app_venture §4.4]` |
| User deletes something wrong despite confirm, leading to 1★ + refund | Favourites protected; Recently Deleted explained before and after; iCloud-sync warning in tray (context §9) |
| App Review: misleading-claim rejection | Claims audit against 1.1.6, 2.3.1, 3.1.2 before submission (s7) |
| Apple's built-in Photos duplicate merge reduces the need for us | Context §13 notes it; we lead on videos and similars, not exact duplicates |
| Build capacity: 12 features, 2 large | Compression is the first cut; swipe/widget already deferred |

**Open questions and the cheapest way to answer each**
1. What do competitors' **Photos permission pre-prompts** and **limited-access** flows look like? → Re-install each and capture from launch through the permission (one capture session).
2. **Delete, confirm and result flows** in each app: do any say "moved to Recently Deleted" or "freed"? → Capture review → delete → result, and screen-record the paywall to measure the close-button delay.
3. **US paywalls and prices.** All captures are ₹ IN. → Capture with a US Apple Account / storefront.
4. Does Clever's **"2 GB free daily"** really let a free user delete 2 GB, and what happens at the limit? → Hands-on test.
5. Is Cleaner Kit's in-app home honest? (Its paywall was never closed in the captures.) → Capture past the paywall.
6. Swipewipe, Cleaner Guru, AI Cleaner: **no screens**. → Capture the top-grossing three from context §1.
7. Can we read how much is in Recently Deleted, or open that album directly? → Apple docs + a 1-day prototype.
8. Is the "same device" inference right? → Ask Ganesh to confirm the capture device and date.

## 8. Verification

- **Checked:** every ₹ price, %, GB/MB figure, count and quoted string in §1–§4, re-checked against the screenshot notes taken while reading each file. The 12 most load-bearing screens were re-opened: IMG_2230, 2231, 2239, 2241, 2250, 2251, 2262, 2266, 2271, 2276, 2278, 2275. Context §§3, 5, 7, 9, 13, 14 quotes and US prices were re-checked by grep. Knowledge-base figures (83–99%, $12.83/$2.90, >70–75%, >25–30%, ~6%, ~5–7%, Gmail OAuth) were re-checked by grep. Apple quotes were re-fetched from developer.apple.com JSON docs and the App Review Guidelines page.
- **Corrected while drafting:**
  - The Cleaner Kit yearly per-week figure is quoted as shown ("₹95.88/week"), not recomputed.
  - Darksy's yearly price is marked "not shown"; only the Weekly/Yearly toggle is visible.
  - The knowledge-base line "None of the four were ever featured by Apple" was **not used**, because it is unclear which four apps it means. Cleaner Kit's "Featured by Apple" store claim (IMG_2264) is reported as seen, unverified.
- **Not verifiable (marked in body):**
  - The same-device inference (strong but `[INFERRED]`).
  - The source of freeup's "62 of 64 GB" iCloud figure.
  - Whether Recently Deleted can be read or opened by API.
  - Blur-detection accuracy.
  - Background-scan limits.
  - All US paywall structures.
  - Close-button delays.
- **Previous calls:** none. This is the first version of this note.
