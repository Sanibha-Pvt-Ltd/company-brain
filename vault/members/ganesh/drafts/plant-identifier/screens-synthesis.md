---
type: category-screens
category: plant-identifier
member: ganesh
run_by: harshil
updated: 2026-10-04
status: draft
sources: [screenshots:53 (ganesh, India storefront, ~2026-10-03), ganesh-benchmark-xlsx, itunes-lookup-us]
---

# Plant identifier: screens synthesis

**The category winner, PictureThis (4.80★, 1,117,470 US ratings), is missing from the screen evidence.** We have no team screenshots of it. This synthesis covers 4 challengers only:
- [[members/ganesh/apps/plant-identifier/plantin]] (12 screens)
- [[members/ganesh/apps/plant-identifier/plantum]] (15)
- [[members/ganesh/apps/plant-identifier/plant-app]] (13)
- [[members/ganesh/apps/plant-identifier/plantiary]] (13)

Capture checklist: [[members/ganesh/apps/plant-identifier/picturethis]].

**Ground rules for reading this:**
- All screens are from the India storefront, so prices are ₹ and the US plan mix is `[UNKNOWN]`.
- No review mining was done in this run.
- No category lens exists yet (`research/categories/plant-identifier/lens.md` is missing).

## 1. Pattern table

| | PlantIn | Plantum | Plant App | Plantiary | PictureThis |
|---|---|---|---|---|---|
| Screens to first plant name | 11 | 12 | 13 | not reached in 13 | `[UNKNOWN]` |
| Taps to first name (approx.) | ~8 | ~6–7 | ~9–10 | >12, not reached | `[UNKNOWN]` |
| Whose plant is the first ID on | prepared demo photo (same image #8–#11) | probably the demo `[INFERRED]` (#11 shows no image) | prepared demo photo (same image #10–#12) | n/a | `[UNKNOWN]` |
| Asks before any real value | 2 (consent, paywall) | 4 (account + email opt-out, trial theatre, paywall, demo) | 5–6 (unlabeled button, trial theatre, paywall, location, demo) | 7 (system prompt, location, 4-question quiz, paywall) | `[UNKNOWN]` |
| Invented concepts visible by home | 3 (Plant Hero, Feed, weather) | 5 (Care Tools vs Plantum Tools, Water Calculator, Explore, account) | 6+ (Tree vs Plant Identifier, Light Meter, Water Meter, Ask Botanist, 3 tabs × 5 chips on result) | 9+ (4 quiz dimensions, insects/birds/mushrooms, Decorator, Community, AI Botanist) | `[UNKNOWN]` |
| Paywall placement | after 5 cards, before ID | after cards + "trial enabled" animation, before ID | after cards + "trial enabled" animation, before ID | after 6 cards + location + 4-question quiz, before ID | xlsx: "After First Scan" `[DATA:ganesh-benchmark-xlsx]` |
| Hard or soft | soft (X) | soft (pale "Cancel" over a photo) | soft (X on #8; none on pre-screen #7) | soft (footer text "Cancel") | `[UNKNOWN]` |
| Plans seen (₹, India) | annual ₹2,999 + 3-day trial; lifetime ₹4,999 (struck from ₹19,996) | 3-day trial → ₹699/wk; yearly ₹3,999 | 3-day trial → **₹1,499/wk only** | "Free 7 Days" → ₹699/wk (preselected); annual ₹3,999 | xlsx: ₹2,499/yr, 7-day trial |
| Trial reminder | toggle, off | toggle, off | none; billing date shown | none | `[UNKNOWN]` |
| Toxicity on result | locked "Poisonous 🔒" | free "Pet-toxic" (but contradictory tags elsewhere) | locked "Unlock For Free" | not captured | xlsx: paid |
| Fake "analysing" steps | yes, 3 steps | spinner | yes, 3 steps | not captured | `[UNKNOWN]` |
| Repeat cost (home → ID) | 2 taps | 2 taps | 2 taps | 2 taps (attention split over 4 ID targets) | `[UNKNOWN]` |

All `[OBSERVED]` unless tagged otherwise. Tap counts are approximate because stills don't show every tap.

**xlsx disagreements:** screens contradict Ganesh's xlsx on price for 3 of 4 apps.
- Plantum: ₹3,999/yr + ₹699/wk on screen, vs ₹1,999/yr + ₹449/mo in the xlsx.
- Plant App: ₹1,499 **per week** on screen, vs per year in the xlsx.
- Plantiary: ₹699/wk + ₹3,999/yr with a 7-day trial on screen, vs ₹1,499/yr + ₹499/mo with a 3-day trial in the xlsx.

Two other points:
- Plantum's paywall is "after scan" in the xlsx but before the scan on screen.
- Plantiary's onboarding is 4 screens in the xlsx and 10 on screen.

Treat the xlsx price column as unreliable until reconciled.

## 2. Patterns worth naming

1. **The "prepared plant" demo is the category's first win.**
   - Who does it: 3 of 4 apps, each with the same move after the paywall.
     - PlantIn #8: "We've set up a plant for you!"
     - Plantum #10: "See Plantum in Action!"
     - Plant App #10: "We've prepared a plant"
   - How it plays out: a prepared photo is "identified" behind a loading screen (staged 3-step analysis in PlantIn and Plant App, a spinner in Plantum). The user gets a name without photographing their own plant. `[OBSERVED]` for PlantIn and Plant App, where the same prepared image runs through the scan screens; `[INFERRED]` for Plantum, whose loading screen (#11) shows no image.
   - Why it exists `[INFERRED]`:
     - It skips the camera permission.
     - It guarantees a correct result.
     - It avoids paying for an ID API call before the user converts.
   - Why it's weak: it proves nothing about the user's plant, and the job ("what is *this* plant on my windowsill?") is still unanswered.
2. **"Trial is enabled" theatre.**
   - Who does it: Plantum (#6–#7) and Plant App (#6–#7).
   - What happens: a toggle animates on with "Your 3-day free trial is enabled!" / "3 days trial is enabled" before any price is shown `[OBSERVED]`.
   - Why it works: it makes users feel they already own the trial before they see the cost (endowment).
3. **Weekly pricing behind "free".**
   - What's on screen: three of four paywalls lead with or preselect a weekly plan (₹699–₹1,499/wk) `[OBSERVED]`.
   - The worst labels:
     - Plantiary labels it "Free".
     - Plantum's CTA reads "Try for $0.00".
   - These match the xlsx review anger, though those quotes are undated and unmined: "$10 a week is crazy", "The free trial is a scam" `[DATA:ganesh-benchmark-xlsx]`.
4. **Safety info is a paywall lever, and it's sloppy.**
   - Gated: toxicity is locked in PlantIn (#11) and Plant App (#13).
   - Contradictory in the apps' own marketing:
     - Plantum #4: "Poisonous" + "Pet-safe" on the same plant.
     - Plant App #4: "Safe to animals · Poisonous".
     - Plantum #12: "Easy" + "Medium" `[OBSERVED]`.
   - Plant App's own disclaimer: "Toxicity information may be subject to error" (#13).
5. **Scope creep is how challengers try to differentiate.**
   - Plantiary: insects, birds, mushrooms, decorator, community.
   - Plant App: tree identifier, light meter, water meter.
   - Plantum: water calculator, articles.

   None of it serves "name my plant, keep it alive" `[OBSERVED]`/`[INFERRED]`.
6. **Bright spots to copy:**
   - Plant App's billing timeline "Due today ₹0.00 / Due October 6, 2026 ₹ 1,499" (#8).
   - Plantum's automatic health check on every ID (#12).
   - PlantIn's quiz-free, account-free onboarding (#1–#6).
   - PlantIn's care countdown framing "Water Need today / Prune In 12 days" (#2).

## 3. Hypothesis verdict

**Starting hypothesis** `[INFERRED prior]`: "Identification is commoditised. Value moves to care and diagnosis, so a paywall before the first ID is the main anger point. Our edge is probably a free first ID with paid care and diagnosis."

**Verdict: partly confirmed, and the edge needs to be sharper.**

- **Confirmed:** all 4 challengers put a paywall before the user's first identification `[OBSERVED]`. 3 of 4 sell diagnosis on the paywall itself ("Plant disease autodetection" Plantum #8, "Diagnose issues instantly" Plant App #8, "Save your plants with instant diagnosis" Plantiary #12); PlantIn's paywall (#7) has no feature copy, and it sells diagnosis in onboarding instead ("Spot plant issues in seconds", #3) `[OBSERVED]`. Value is marketed as care and diagnosis, not ID.
- **Not confirmed as stated:** the paywall is never hard. Every one is dismissible, and 3 of 4 then give a free name on a demo plant (Plantum's demo use is `[INFERRED]`). A "free first ID" alone would look the same as what they already do on a screenshot.
- **The real gap** `[INFERRED from screens]`:
  - The first ID is never on the user's own plant before a price.
  - Safety info (toxicity) is gated or contradictory.
  - Pricing hides weekly billing behind "free"/"enabled" framing.
- **Anger point:** we can't confirm "paywall before first ID is the main anger point" without review mining. The xlsx quotes point more at **weekly pricing, cancellation and trial traps** than at ID gating, and one names toxicity/ID gating (Plant App 2★) `[DATA:ganesh-benchmark-xlsx]`. That sample is too small and unmined to rank causes.
- **Winner caveat:** if Ganesh's xlsx is right that PictureThis paywalls "After First Scan", the category winner already does free-first-ID. That would support the hypothesis's direction but make it table stakes, not a differentiator `[UNKNOWN]` until captured.

## 4. Our first five minutes (screen by screen)

Goal: the user names *their* plant and learns whether it's safe and what it needs, with at most 2 asks before that. Then they meet one honest paywall when they ask for ongoing care or diagnosis.

1. **Launch → camera, 0 asks.**
   - One line over a live viewfinder placeholder: "Point at a plant. We'll tell you what it is."
   - Two buttons: shutter, and "Choose a photo". The photo picker (PHPicker) needs no permission `[INFERRED: iOS PHPicker behaviour]`.
   - Small text link: "No plant nearby? Try a sample."
   - No splash stats, no laurels, no account, no quiz.
2. **Shutter → camera permission, the only system prompt so far (ask 1).**
   - Triggered by the tap, so the reason is obvious.
   - If denied: fall back to "Choose a photo".
3. **Identifying, real time only.**
   - Show the user's photo with one progress indicator for as long as the API takes.
   - No staged "Detecting leaves" steps.
4. **Result (the first win, ~2 taps from launch).** It shows:
   - Common name, every other common name, and the current latin name ("formerly …").
   - Confidence in words ("Very likely", "Possibly"), plus the top 2 alternatives with photos to compare.
   - **Free and never locked:** "Toxic to cats and dogs" / "Toxic if eaten by children" / "Not known to be toxic", with the source and a plain disclaimer.
   - Three care basics: light, water rhythm, difficulty.
   - Automatic quick health read on *this photo*, Plantum's idea done honestly. It says "Looks healthy", "Possible problem: overwatering — see why", or "Can't tell from this photo — take a close-up of a leaf".
   - Primary CTA: "Save to my plants".
5. **Save → "Remind you when it needs water?" (ask 2, optional).**
   - Yes → notification permission.
   - No → saved anyway.
6. **Paywall, only at a paid moment.** It appears when the user taps one of:
   - the full care schedule and reminders beyond the first plant,
   - a full diagnosis with a treatment plan,
   - IDs beyond the free allowance.

   On the paywall:
   - Close X visible from 0 s.
   - Yearly plan preselected, with a 7-day trial and the reminder toggle **on by default**.
   - Monthly as the alternative. **No weekly plan.**
   - Plant App's billing timeline with real dates.
   - What the user has already got (the named plant, its safety answer) stays free.
7. **Home after day 1:** a "My plants" list with today's tasks ("Water the Snake Plant today"), plus the camera button. Nothing else.

**Asks before value:** 1, the camera prompt at the moment of need, vs 2–7 for the challengers.
**Concepts before value:** 0.
**Concepts by end of day 1:** 1 ("My plants").

**Monetization honesty check:**
- Paid: ongoing care (the reminder loop), diagnosis with treatment, and volume.
- Never paid: the answer to "what is it and is it dangerous".
- The free ID allowance size depends on ID API unit cost, see open questions.

## 5. Up to 3 differentiators (each tied to evidence)

1. **"Your plant, first": a real ID on the user's own plant before any price, in about 2 taps.**
   - Evidence: all 4 challengers show a price before any ID (PlantIn #7, Plantum #8, Plant App #8, Plantiary #12). PlantIn (#8–#11) and Plant App (#10–#12) then identify a prepared demo photo `[OBSERVED]`; Plantum offers one (#10) and probably used it `[INFERRED]`. Plantiary reaches no ID in 13 screens `[OBSERVED]`.
   - Screenshot-1 promise: "Point. Name it. No sign-up, no paywall first."
2. **"Is it safe?" is always free and never contradictory.**
   - Evidence:
     - Toxicity locked: PlantIn #11 "Poisonous 🔒", Plant App #13 "Unlock For Free · Poisonous".
     - Contradictory safety copy: Plantum #4 "Poisonous"/"Pet-safe", Plant App #4 "Safe to animals · Poisonous".
     - xlsx 2★ on Plant App: "locked behind a paywall including … toxicity info" `[DATA:ganesh-benchmark-xlsx]`.
   - Pet owners and parents are the users with the most urgent reason to open the app `[INFERRED]`.
   - Product rule: one toxicity line per audience (pets, children), shown on every result, with source and confidence.
3. **Honest subscription: yearly or monthly, no weekly, close visible, reminder on, billing date shown.**
   - Evidence:
     - Weekly plans preselected or trial-attached: Plantum #8 ₹699/wk, Plant App #8 ₹1,499/wk, Plantiary #12 "Free" = ₹699/wk.
     - "Trial enabled" theatre: Plantum #6–#7, Plant App #6–#7.
     - Reminders off by default: PlantIn #7, Plantum #8.
     - Disguised close: Plantum #8, Plantiary #12.
     - xlsx anger quotes: "$10 a week is crazy", "The free trial is a scam" `[DATA:ganesh-benchmark-xlsx]`.
   - Screenshot promise: "No weekly charges. We remind you before any trial ends."

Not chosen as a differentiator: diagnosis quality. All four promise it; none of the captures show a real diagnosis flow, so there is no evidence yet. Needs PictureThis "Plant Doctor" capture and review mining.

## 6. Concepts we refuse to add

| Concept | Seen in | Why not |
|---|---|---|
| Account / sign-in before value | Plantum #2 | No job need; iCloud sync covers multi-device `[INFERRED]` |
| Onboarding quiz (goals, environment, skill, commitment) | Plantiary #8–#11 | 4 asks with no visible payoff; the photo tells us indoor/outdoor and plant type |
| Insects / birds / mushrooms / trees as separate IDs | Plantiary #4, #13; Plant App #9 | Scope creep. A tree is a plant; the others are different jobs and different apps |
| Separate "Disease Identifier" tool | Plant App #9; Plantum #13 | Diagnosis belongs on the plant's result and profile, not in a second camera mode |
| Light meter, water meter, water calculator | Plant App #9; Plantum #13 | The care schedule should answer "when do I water", not an instrument |
| Feed / Community / Explore articles | PlantIn #12; Plantiary #13; Plantum #14–#15 | Content treadmill; pulls attention from the user's plants |
| Weather / location on home | PlantIn #12; Plant App #9; Plantum #13; Plantiary #7, #13 | A permission ask for marginal value. Only add if watering schedules measurably improve with it |
| Identity labels ("Plant Hero", "Struggling", "Trendy") | PlantIn #1; Plantiary #10; Plantum #12 | Manufactured identity or shame; adds nothing to the job |
| AI chatbot persona as a tab or tool | Plantiary #5, #13 ("Ask AI Botanist" tool row, not a tab); Plant App "Ask Botan…" tab | Maybe later as "Ask about this plant" inside a plant's page. Not a separate concept on day 1 |
| Plant Decorator / AR preview | Plantiary #13 | Different job (shopping/design) |

## 7. Open questions (send to review mining or a hands-on test)

1. **PictureThis screens.** Does the winner really give the first ID free on the user's own plant ("After First Scan")? What is free on its result? How fast does the close button appear? Ganesh: see the capture checklist in [[members/ganesh/apps/plant-identifier/picturethis]].
2. **US pricing.**
   - Are weekly plans also the default in the US storefront?
   - What are the US prices? (A Plantiary review in the xlsx says "$10 a week"; the listed US price is `[UNKNOWN]`.)
   - Recapture all 5 paywalls with a US Apple ID.
3. **xlsx vs screen price conflicts.** Plantum, Plant App and Plantiary differ (see §1). Is it A/B testing, a price change, or a data-entry error? Recapture on a fresh install twice.
4. **Close-button timing on every paywall.** Stills can't show the delay. Screen-record.
5. **Real own-plant ID flows.** None of the 4 apps were captured identifying Ganesh's own plant. We need accuracy, alternatives shown, and what is gated on a *real* result.
6. **Review mining (stage A6).** Rank the anger clusters: weekly price/trial trap vs paywall-before-ID vs accuracy vs toxicity gating vs cancellation. This decides whether differentiator 3 or 1 leads screenshot 1.
7. **ID API unit cost.** It decides the free allowance (e.g. N IDs/day free) without making free-first-ID unprofitable. Tech-lead estimate needed (Harshil).
8. **Diagnosis quality.** Is any app's diagnosis good enough to justify a subscription? Hands-on test with 5 known-sick plants across the apps.
9. **Missing captures, minor:**
   - Plant App #1's unlabeled icon button.
   - Plantiary #6's system prompt.
   - Camera and notification prompts in all four apps.
   - Settings/cancel paths in all four apps.

## What would change the call
- If PictureThis (the winner) shows a paywall *before* the first ID, differentiator 1 becomes stronger.
- If review mining shows accuracy, not pricing, is the dominant 1–2★ cluster, a "confidence + alternatives" result becomes differentiator 1, and honest pricing drops to table stakes.
- If US paywalls show no weekly plans, differentiator 3 weakens to "reminder on + close visible".

## Next stage
1. Ganesh captures PictureThis per the checklist.
2. Run A6 review mining for all 5 apps (`scripts/fetch-app.py`).
3. Write stage 0 lens for plant-identifier.
4. Stage B market.

## Verification (2026-10-04)
Every claim was traced to the four verified app notes, to the screenshot, or to xlsx/API. Checked: ~90 quoted strings, ~69 screen refs, 25 ₹ figures, 18 xlsx mentions (all price/placement/onboarding conflicts re-read from cells E–H of rows 15, 19, 20 and Category Winners B4), and PictureThis 4.80 / 1,117,470 against the API. Screen counts 12+15+13+13 = 53.
- Corrections:
  - **"All 4 sell care and diagnosis on the paywall"** → 3 of 4. PlantIn's paywall (#7) has no feature copy; "Spot plant issues in seconds" is onboarding #3.
  - **Plantum's first ID "stock demo" `[OBSERVED]`** → probably the demo `[INFERRED]`, because #11 shows no image. Edited in the pattern table, pattern 1, the verdict and differentiator 1. PlantIn and Plant App remain `[OBSERVED]`: the same image runs through their scan screens.
  - "AI chatbot persona as a tab, Plantiary #13" → in Plantiary it is a tool row, not a tab.
  - "$9.99/wk for Plantiary `[INFERRED]`" → US price `[UNKNOWN]`. The review says "$10 a week".
- Unverifiable here: close-button delays, US plan mix, and all PictureThis screen behaviour.
