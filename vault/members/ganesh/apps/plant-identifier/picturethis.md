---
type: app
category: plant-identifier
app: "PictureThis - Plant Identifier"
app_store_id: 1252497129
member: ganesh
run_by: harshil
updated: 2026-10-04
status: draft
scope: listing-only
screens_analysed: 0
reviews_analysed: 0
sources: [itunes-lookup-us, ganesh-benchmark-xlsx]
---

# PictureThis - Plant Identifier (Glority Global Group Ltd.)

**This is the category winner per Ganesh's benchmark, and it has no screen teardown.**

`[UNKNOWN] no team screenshots.` Per the screens lens source rule, App Store listing images, marketing images and web walkthroughs are not used for screen analysis. Every A5 measure for PictureThis is `[UNKNOWN]` until Ganesh captures the flow. Related: [[members/ganesh/drafts/plant-identifier/screens-synthesis]].

## A1 US listing snapshot

| Field | Value | Tag |
|---|---|---|
| Developer | Glority Global Group Ltd. | `[DATA:itunes-lookup-us 2026-10-04]` |
| Price | Free download (IAP) | `[DATA:itunes-lookup-us]` |
| US rating | 4.80 from 1,117,470 ratings (about 5× PlantIn, the next largest in the set) | `[DATA:itunes-lookup-us 2026-10-04]` |
| Version / last update | 5.72.0, 2026-09-22 | `[DATA:itunes-lookup-us]` |
| First release | 2017-07-20 (oldest in the set) | `[DATA:itunes-lookup-us]` |
| Genre / size / age | Education, 244 MB, 4+ | `[DATA:itunes-lookup-us]` |

## Ganesh's xlsx row

`[DATA:ganesh-benchmark-xlsx]`, India storefront, ₹ prices (not US):

| Column | Value |
|---|---|
| Onboarding screens | 5 |
| Paywall placement | "After First Scan" |
| What's free | "Preview botanical identification, basic plant encyclopedic name card." |
| What's paid | "Plant Doctor disease diagnosis, 98% accuracy database access, pet toxicity warnings." |
| Offer on paywall | "₹2,499/yr with 7-day free trial" |
| Top pick | "Top Pick 🏆" |
| Review 1 | ★★★★☆ "Mostly great" (JEMMjams): "I've tried several plant ID apps and Picture This is by far the best. It's easy to use and I often get a match…" |
| Review 2 | ★★★★★ "Too many bugs" (Ddthntstheus): "I did the free week trial of premium access, and loved the plant identification part… the premium is supposed to give unlimited plant identification. But the free week has only has three or so free, before you have to buy another by watching an ad or sharing it on face book or something." |
| Review 3 | ★★★★★ "Great app with little disturbance" (AvocadoWizard): "It's so easy to just whip out the app anywhere and snap a pic of any plant and get almost instant results…" |

The review quotes are undated and truncated in the xlsx, so they are not a mined sample. They are also titled/star-mismatched: "Too many bugs" is rated 5★.

**What matters if Ganesh's row holds:** PictureThis is the only app in the set where the paywall comes *after* the first scan. It also gates pet toxicity, like PlantIn and Plant App. That would make it the only shortlisted app that already does "first ID before paywall". It would weaken our differentiator 1 to "first ID before paywall *on your own plant, unlimited for the first session*". We can't verify either point without screens `[UNKNOWN]`.

## Not in this run
- A2 business performance: not in this run (screens-only).
- A3 monetization from screens: `[UNKNOWN] no team screenshots`.
- A4 acquisition: not in this run (screens-only).
- A5 screens lens: `[UNKNOWN] no team screenshots`.
- A6 failure mining: not in this run (screens-only).

## Capture checklist for Ganesh

Use a fresh install, the India storefront (note it), and a real potted plant in good light. **Screen-record the whole run** (Control Centre → Screen Recording), then also take stills of each screen. One flow at a time; don't skip screens. Name the folder `ganesh_screenshots/Plant Identifiers/PictureThis - Plant Identifier/`.

1. **Onboarding:**
   - every screen from the first launch frame to the first camera/home screen, including any splash, sign-in or account wall, quiz, and rating prompt;
   - if there is a "Skip" or "Continue without account", capture both the screen and where it leads.
2. **Permissions:**
   - every system prompt (camera, photos, notifications, location, App Tracking Transparency) and the app's own pre-prompt screen before each;
   - note *when* in the flow each appears.
3. **First ID:**
   - the camera screen (with any tips/overlay);
   - the shutter tap;
   - every loading/"analysing" screen (note how many seconds it lasts in the recording);
   - any interstitial before the result (ad, paywall, share prompt).
   - Do it on **your own plant**, not a sample. If a sample/demo plant is offered, capture that screen too, then choose your own plant.
4. **Result screen:**
   - scroll the whole result top to bottom;
   - capture every locked/blurred element (pet toxicity, care, diagnosis), what happens when you tap it, and the "similar species"/alternatives section if any.
5. **Paywall (every instance):**
   - **Close-button timing:** from the recording, note the seconds from the paywall appearing to the X becoming visible and tappable. Note its position and contrast.
   - All plans and prices exactly as shown, which is preselected, trial length, any reminder toggle and its default, and the billing date line if shown.
   - Tap close and capture whatever comes next (downsell, second offer, "are you sure").
   - Capture any later paywall triggers (e.g. 2nd/3rd ID, diagnosis tap) and the ID count at which they appear.
6. **Care and diagnosis:**
   - add the plant to "My Plants" / garden;
   - capture the care schedule screen, reminder set-up and notification opt-in;
   - run "Plant Doctor"/diagnosis on a leaf with a visible problem (yellowing or spots), and capture the result and what is free vs gated.
7. **Settings and subscription:**
   - settings screen, account screen, "manage subscription"/restore/cancel path inside the app (how many taps to Apple's subscription page);
   - any upsell banners on home.
8. **Day 2 (optional but valuable):** reopen the next day. Capture any notification received, the home state, and the taps needed for a second ID.

Then re-run stage A screens-only for PictureThis and update [[members/ganesh/drafts/plant-identifier/screens-synthesis]].
