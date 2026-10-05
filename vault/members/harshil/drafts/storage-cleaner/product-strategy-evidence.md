---
type: category-product-strategy-evidence
category: storage-cleaner
member: harshil
updated: 2026-10-05
status: draft
sources: [context.md, screenshots:52 across 6 apps, knowledge:consumer_app_venture_knowledge_base_2026-10-04.md + organic-growth-knowledge-base.md + sanibha-app-factory-knowledge-base.md, web:7]
---

# Storage Cleaner — product strategy evidence (v1)

This is the working material (Phases 0–2) behind [[members/harshil/drafts/storage-cleaner/product-strategy]]. Context: [[research/categories/storage-cleaner/context]]. Section numbers here (E§0, E§1.x, E§2) are what the main note cites.

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
| 7 | IMG_2258 | onboarding 6 | speedometer | tap | — | "Boost Performance" · "50%" · "faster response times with regular Free Up" | Performance claim a photo cleaner cannot deliver (main note §2.5) |
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
