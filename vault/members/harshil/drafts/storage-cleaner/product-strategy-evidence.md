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

## 3. Full reasoning behind the recommendations

Moved here from the main note on 2026-10-05. Section numbers below are the old main-note numbers.


- **Positioning:** keep context §14's *Make space. Keep what matters.* (safe, fast decisions), proven by **true numbers, biggest wins first, nothing deleted without your OK**. Hook: "See what's really filling your iPhone."
- **Why:** context §5 says users fear surprise charges, lost photos and over-promising ads. The screens show how the category over-promises: on one test phone, paywalls said "95 from 100% used" and "Almost Full" while the same phone's home screens showed about 47–55% used (R6, E§2).
- **UX 1 — true storage first:** real used/free storage before any ask. The first win is the first approved delete (7 taps), reported as "moved to Recently Deleted".
- **UX 2 — biggest first:** lead with large videos, not duplicates. Test phone: exact duplicates 0–17 MB, videos 2.18–2.62 GB (R7).
- **UX 3 — honest paywall:** soft, after the first cleanup; close visible from frame 1; no weekly at launch, no trial theatre, no tracking or notification ask before value.
- **v1 (12):** true storage overview · on-device scan · large videos · similar compare with a reason · duplicates · screenshots/utility · protected favourites · review tray · honest result + Recently Deleted guide · video compression (paid, first cut) · "new since last clean" · StoreKit 2 paywall with free daily allowance.
- **Cut:** email, contacts, calendar, vault, "boost", iCloud cleaning, health score.
- **Top new recommendation:** a "one iPhone, six cleaners" truth test as launch PR and challenger ad (§5.1).
- **Confidence: medium.** Context and screens agree on the trust problem. The screens stop at each app's home screen (no scan, delete or result screens), prices are ₹ only, and Swipewipe, Cleaner Guru and AI Cleaner have no screens.

### 1. What the research tells us

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

### 2. Positioning

#### 2.1 Who and the job
- **Decision:** target an iPhone owner at the "storage full" moment who fears losing photos and being charged.
- **Why:**
  - Trigger: context §11 Concept A.
  - Fears: context §5 B and D (photos) and §5 A (billing).
  - Search terms: "storage cleaner", "phone cleaner", "clean iPhone" `[ESTIMATE:knowledge/consumer_app_venture §4.1]`.
  - Demographics: `[UNKNOWN]`.
- **Job:** "Show me what's actually eating my space, let me drop the big stuff without losing anything I care about, and don't trick me into paying."

#### 2.2 The call

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

#### 2.3 Proof points (what the user sees)
1. True storage on screen 1 via `volumeAvailableCapacityForImportantUsage` `[APPLE:https://developer.apple.com/documentation/foundation/urlresourcevalues/volumeavailablecapacityforimportantusage]`, with a "How we measured" sheet.
2. Every size is either measured or marked "≈".
3. A one-line reason on every similar group (R3).
4. Favourites protected by default (context §8 table).
5. Result text: "moved to Recently Deleted; frees after 30 days or when you empty it" `[APPLE:https://support.apple.com/en-us/104967]`.
6. Paywall shows price, period, renewal date and the free/paid split, with the X visible immediately.

#### 2.4 Storefront and ad
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

#### 2.5 What we will never claim
- Device "% full" or "% used" we didn't read. Guideline 1.1.6 bans "inaccurate device data" `[APPLE:https://developer.apple.com/app-store/review/guidelines/]`.
- "Free up to N%" (R6, context §13).
- "Faster", "boost" or "overheating" `[SCREEN:freeup/IMG_2258, darksy/IMG_2245]`. Guideline 2.3.1(a) bans promoting services an app doesn't offer.
- Cleaning of iCloud, system data, caches or "junk" `[ESTIMATE:knowledge/consumer_app_venture §4.4]`.
- "Freed" at delete time (R5).
- User counts, ratings, "joined today" or "Featured by Apple" (R12).
- Recovery after Recently Deleted is emptied (context §9, citing Apple Support).

### 3. UI/UX

#### 3.1 Design principles (tie-breakers)
1. **Every number is measured, or marked "≈".** (R6)
2. **Give before you ask:** no permission or payment before the user sees something real. (R2, R15)
3. **Biggest win first.** (R7)
4. **Every suggestion carries a one-line reason; the user decides.** (R3)
5. **Say when the space comes back.** (R5)
6. **Four categories max on home, one idea per screen.** Darksy shows 9+ tiles `[SCREEN:darksy/IMG_2251]`; FreeUp's short home works `[SCREEN:freeup/IMG_2262]`.
7. **Calm, not alarm:** red appears only on the irreversible Delete button. (R10)

#### 3.2 Information architecture
- **Decision:** two tabs.
  - **Clean** (home): true storage line, then Videos, Similar, Screenshots & utility, Duplicates, ordered by GB.
  - **History**: past cleanups, plus GB still waiting in Recently Deleted.
  - **Settings** sits behind a gear: plan, protected items, notifications, "How we measure".
  - **Review tray** is a persistent bottom bar.
- **Why:** Competitors carry 5 tabs mixing non-storage jobs `[SCREEN:clean-manager/IMG_2231, cleanup/IMG_2241]`. FreeUp shows that 3 tabs are enough `[SCREEN:freeup/IMG_2262]`.
- **Build/design:** no Email, Contacts, Vault, Swipe or Tools surfaces.

#### 3.3 First five minutes
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

#### 3.4 Permissions
- **Photos.** Decision: ask for `.readWrite` after our pre-prompt.
  - Limited access: scan only the selected items and show a banner to expand. Suppress the automatic limited-access alert with `PHPhotoLibraryPreventAutomaticLimitedAccessAlert` `[APPLE:https://developer.apple.com/documentation/photos/phauthorizationstatus/limited]`.
  - Denied: still show true device storage, plus an "Open Settings" card.
- **Delete.** Decision: batch each review into one change request. Why: Apple says "For each call to this method, iOS shows an alert asking the user for permission to edit the contents of the photo library" `[APPLE:https://developer.apple.com/documentation/photos/phphotolibrary/performchanges(_:completionhandler:)]`. Silent deletion is impossible, which is good for trust.
- **Notifications.** Decision: only as an opt-in toggle on the result screen. Why: Cleaner Kit asks on onboarding screen 2 `[SCREEN:cleaner-kit/IMG_2267]`; Cleanup asks after home `[SCREEN:cleanup/IMG_2240]`.
- **ATT.** Decision: not at launch. Why: 2 of 6 apps ask on screens 1–2 `[SCREEN:clever-cleaner/IMG_2272, freeup/IMG_2254]`, and Guideline 5.1.1(iv) bans manipulating consent `[APPLE:https://developer.apple.com/app-store/review/guidelines/]`. s4 confirms attribution; if ATT is needed, ask after the first win.

#### 3.5 Core loop
- **Decision:**
  - Day 2: History shows "X GB still waiting in Recently Deleted" and "New since last clean".
  - Week 2: an optional weekly review, keeping context §10 screen 6 and §12's retention test.
  - Nothing new: "You're all caught up." No streaks, no health score.
- **Why:** context §13's moved-vs-reclaimed distinction becomes an honest reason to return (R5). The knowledge base's health-score idea `[ESTIMATE:knowledge/consumer_app_venture §4.2]` invites fake urgency.

#### 3.6 Key screens

| Screen | Most important element | States to design |
|---|---|---|
| Clean (home) | True storage line | scanning (progressive), limited access, nothing to clean ("the rest is apps and system data, which iOS manages"), denied, error/resume |
| Large videos | Size + full preview; paid "Compress instead" shows before/after sizes | iCloud-only ("≈ size, in iCloud"), none large |
| Similar group | Reason line ("Suggested keep: sharpest of 4") + user toggles; favourites "Protected" | group of 2, all protected, user overrides |
| Review tray | "Nothing has been deleted yet." Total GB, and "Moves to Recently Deleted for 30 days. Deleting syncs to all devices using iCloud Photos." `[APPLE:https://support.apple.com/en-us/104967]`. The only red button | empty, user cancels the system confirm |
| Result | "moved" + 2-step guide to empty Recently Deleted. A direct album link is `[UNKNOWN: feasibility]` | partial failure (name the items), allowance reached (paywall) |
| Paywall | §3.7 | offline, pending, subscribed, not trial-eligible |

#### 3.7 Paywall
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

#### 3.8 Visual language (directional; tokens belong to brand-designer)
- **Decision:**
  - Follow the system appearance, with light-led store shots.
  - One calm accent colour; neutral bars; red only on Delete.
  - Real photos shown large; no decorative "AI" art.
- **Why:**
  - All 6 apps are dark or navy with alarm bars (R10).
  - Context §4 says blue is fine; repeating the same colour, layout and message is the problem.
  - Clean Manager's "AI" orbit graphic `[SCREEN:clean-manager/IMG_2227]` is the decorative art we are avoiding.

#### 3.9 Voice, accessibility, refusals
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

### 4. v1 product features

#### 4.1 Feature table

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

#### 4.2 Later (v1.1 / v2), each with its trigger
- **Swipe mode:** if users ask to hand-sort non-similar photos, or D7 lags while scan→delete is healthy. Context §8 puts Swipewipe and Slidebox in that quadrant; we don't lead there.
- **Widget:** if D7/D30 return is the weakest funnel step.
- **Screenshot topics / context §11 Concept C:** if a screenshot-graveyard CPP wins on cost per qualified install.
- **Live Photo → still:** if Live photos turn out to be a meaningful GB share in real cohorts. Only "12.5 MB" on the test phone `[SCREEN:clever-cleaner/IMG_2278]`.
- **Contacts merge:** only on repeated user demand. It frees no storage.
- **Weekly plan:** only if annual/monthly can't reach payback.

#### 4.3 Cut list
| Cut | Reason |
|---|---|
| Email cleaning | Not storage. Gmail restricted scopes may trigger verification `[ESTIMATE:knowledge/consumer_app_venture §4.4]` |
| Contacts / calendar | No storage value, adds tabs |
| Vault / "Secret Storage" | Different job, trust risk |
| iCloud cleaning as a feature | Deletion already syncs; nothing separate to sell (context §9) |
| "Boost" / speed / RAM / junk / cache | Not possible on iOS; App Review risk (§2.5) |
| "AI Categories" / "With Text" tiles | Invented abstractions `[SCREEN:darksy/IMG_2251]` |
| Health score | Manufactured urgency |

#### 4.4 Free vs paid
- **Decision:**
  - **Free:** a user can fully see what is filling the phone, with true numbers. They can preview and compare everything, delete up to a daily allowance, and learn how to get the space back.
  - **Paid:** unlimited cleanup at once, video compression, and the weekly review.
- **Why:**
  - Context §7 frames the exchange as "decide whether completing the cleanup is worth paying for".
  - Clever already proves a free allowance (R8), so the free tier itself is not our edge. It is table stakes, and it earns reviews.
- **Build/design:** the limit appears *after* a completed cleanup, against the user's own real GB. That is what keeps it from feeling like a trap `[INFERRED]`.

#### 4.5 Success metrics
1. **Photos permission grant:** target >70–75% `[ESTIMATE:knowledge/consumer_app_venture §6, "targets, not industry facts"]`.
2. **Scan → first approved delete in session 1:** target >25–30% of activated users `[ESTIMATE: same]`.
3. **Install → paid:** ~6% "as initial strong target" `[ESTIMATE: same]`. Our own target `[UNKNOWN: set after first cohort]`.
4. **Refund rate:** <5–7% `[ESTIMATE: same]`. Also track the share of 1–2★ reviews mentioning "charged" or "scam".
5. **Freed vs moved:** share of moved GB actually freed within 7 days. Target and measurement `[UNKNOWN: set after first cohort; s4 to confirm it is observable]`.

The primary money metric stays context §12's D30 net proceeds per install, with refunds and support tracked separately.

### 5. New recommendations

None of these is in context.md.

| # | What | Why | Cheap test | Kill if |
|---|---|---|---|---|
| 5.1 | **"One iPhone, six cleaners" truth test** as launch PR and challenger ad: each paywall's storage figure vs iOS Settings on one phone, then ours | Already documented (E§2). Knowledge base suggests pitching journalists who cover scammy cleaners `[ESTIMATE:knowledge/organic-growth-knowledge-base §3.5]`. Turns context §11 Concept B into proof | One organic short + one Meta creative vs Concept A, on cost per qualified install | s6 flags comparative-claim risk, or it clearly loses to control |
| 5.2 | **Lead with videos, not duplicates**: onboarding, home order, store shot 1 | R7. Three competitors open with duplicates (E§2 pattern 3) | Aggregate category GB on-device over the first 500 scans; CPP test | Cohort medians show similar photos beat videos on GB |
| 5.3 | **Recently Deleted as the day-2 loop**, with an opt-in reminder | Context §13 separates the states but has no mechanic (R5) | Opt-in rate; D2 return, opted-in vs not | Low opt-in and no D2 lift. Reading the album's size is `[UNKNOWN: feasibility]`; fallback is "You moved X GB on [date]" |
| 5.4 | **Week-1 on-device spike on file sizes** | Positioning depends on true or "≈" numbers (§4.1 note) | `dataSize` on iOS 27, byte-streaming on iOS 26; local vs iCloud-only; 1K/10K/50K libraries | Streaming too slow or forces downloads → show counts + "≈" on older iOS and set minimum OS |
| 5.5 | **"How we measured" on every number** | Replaces the social proof we lack (R12) | Track ⓘ taps | Almost unused → keep in-app, drop from store shots |
| 5.6 | **No-ATT launch** | Two competitors ask at launch (§3.4) | s4 confirms an Apple Ads-first launch works without it | Meta is the main channel and can't optimise without it → ask after first win |

### 6. Risks and open questions

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

### 7. Verification

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
