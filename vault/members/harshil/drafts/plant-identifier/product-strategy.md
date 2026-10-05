---
type: category-product-strategy
category: plant-identifier
member: harshil
updated: 2026-10-05
status: draft
sources: [context.md, screenshots:80 across 8 apps, knowledge:us_ios_app_factory_knowledge_base_2026-10-04.md, web:0]
---

# Plant Identifier — final recommendations (v1)

Built on [[research/categories/plant-identifier/context]]. Decision-only. Prices, ID engine and name are open until the items under "Before build" are closed.

## Positioning

**Positioning statement**
For houseplant owners who just noticed yellow, brown or drooping leaves and don't know what they did wrong, Plant ER (working name) is the plant check-up app that looks at **your** plant for free, tells you what it might be and what to check first, then follows up until you can see whether it's recovering. Unlike PlantApp, Plantum, PlantIn and Plantaria, it shows you a real result on your own plant before it asks for money, and it never states a guess as a diagnosis.

**Messaging**

| Layer | Message |
|---|---|
| Line | Find out what's wrong. Know what to check. See if it's working. |
| Acquisition hook | "Your plant is turning yellow. Why?" |
| Differentiator | A free check-up on your own plant: likely causes ranked, what to check first, and an honest "can't tell from a photo" when that's true. |
| Emotional benefit | You know the next right thing to do for this plant. |
| Retention reason | A follow-up check on a set day, plus before-and-after photos that show whether your care is working. |

**Target user**
- Primary: indoor houseplant owner (1–10 plants) whose plant looks unwell right now.
- Secondary: curious identifier ("what is this plant?"), served free, offered "add to my plants" afterwards.
- Not v1: outdoor gardeners, foragers, mushroom, insect and bird identifiers.
- Searches: "plant identifier", "plant disease", "why are my plant leaves yellow", "plant care app".
- Fears: killing a plant they paid for, paying for a weekly subscription they forget, advice that makes it worse.

**Name:** Plant ER is a placeholder until it's cleared. Keep the name in the "plant check-up / plant doctor" territory. Don't use "AI" in the name and don't use "cure".

**Proof the user sees in the product**
1. The first result runs on the user's own photo, not on a sample plant, and comes before any paywall.
2. Each result shows 2–3 possible causes, each with a confidence word (Likely / Possible / Less likely) and the one-line visual reason.
3. Each cause has a "check this first" step the user can do in under a minute (finger soil test, drainage hole, light change).
4. When the photo can't settle it, the result says so in words and asks one question instead of guessing.
5. Pet and child toxicity is shown free on every plant, with a "verify with a vet or poison control" line.
6. A dated before photo and a set follow-up day are saved automatically.
7. The paywall states the price, the period, when the trial ends and the renewal date. The trial reminder is on by default and the X is visible from the start.

**App Store screenshots.** Shots 1–3 tell one story, and every shot uses real app UI on a real plant photo.

| # | Headline | Content |
|---|---|---|
| 1 | "Why are your plant's leaves turning yellow?" | Camera framing a yellowing Monstera leaf, one "Check my plant" button |
| 2 | "Know what to check first." | Result card: 3 ranked possible causes, "Check first: push a finger 2 inches into the soil" |
| 3 | "See if it's working." | Plant page: Day 1 photo next to follow-up photo, "Next check: Thursday" |
| 4 | "Check, don't just water on schedule." | Condition-check reminder ("Soil still wet? Skip watering") |
| 5 | "Safe for your cat? Free, on every plant." | Toxicity row on a plant page |
| 6 | "Identify any houseplant in seconds." | Identification result |

- Store shots never show user counts, accuracy percentages, "cured" counts, "Featured" laurels or award badges.
- Before/after pairs in the store are captioned "Example" and never show damaged leaves turning green again.

**Ad angles**

| Role | Angle | Ad message | Lands on |
|---|---|---|---|
| Lead | Problem | "Your plant is turning yellow. Why?" — phone over a yellow leaf, then ranked causes, then a finger soil check | Store shot 1, onboarding goes straight to camera |
| Test | Condition care | "Stop watering because it's Tuesday." — calendar alert, then damp soil, then "skip today" | Store shot 4 |
| Control | Identify | "What's this plant called?" — photo, then name | Store shot 6 |
| Later | Pet safety | "Is this plant safe for your cat?" | Store shot 5 |

**Never claim**
- Any accuracy percentage or "X times more accurate".
- "Cure", "save your plant", "guaranteed recovery", "diagnosed instantly".
- "Disease detected" for a care problem such as overwatering, low light or underwatering.
- User counts, ratings, "#1", "Featured" or awards we don't have.
- "Free" on any button that starts a paid trial without the renewal price beside it.
- Expert or botanist review, unless a human actually reviews the case.

## UI/UX

**Design principles**
1. Show a real result on the user's own plant before asking for anything.
2. Say "possible" until the user's answers say "likely". Never say "detected" for a photo guess.
3. Every result ends in one thing to check or do today, not a care encyclopedia.
4. Check conditions before acting: reminders ask "is the soil dry?" before they say "water".
5. One job per screen and one primary button. No tool grids.
6. Safety information is never behind a paywall.
7. No fake progress, no confetti for nothing, no countdown timers.

**Structure: 3 tabs plus a camera button**

| Tab | What lives there |
|---|---|
| My Plants (home) | Plant cards with status ("Check due Thu", "Recovering", "Healthy"), today's checks at the top, empty state = camera prompt |
| Camera (centre button) | Single capture screen; after capture: "Check a problem" (default) or "Just identify" |
| Settings | Subscription status and manage link, notification times, restore, privacy, help |

- Search, articles, community feed, weather and the tool grid are not in v1.
- A plant page holds the photo timeline, the active care plan, care basics, toxicity and the check history.

**First five minutes (numbered screens)**

| # | Screen | On screen | Primary action | Asks | Given so far |
|---|---|---|---|---|---|
| 1 | Welcome | One line: "Show me the leaf that's worrying you." A real plant photo. Links: "Just identify a plant", "Restore" | "Check my plant" | nothing | the promise |
| 2 | Camera pre-prompt | "We use the camera only to photograph your plant. Photos stay in the app." | "Allow camera" (then the system prompt) / "Choose from Photos" | camera, or a photo picked from the library | — |
| 3 | Capture | Live camera, frame guide, tip "Fill the frame with the affected leaves", library button | Shutter | photo | — |
| 4 | Checking | The user's own photo with a short indeterminate spinner and "Looking at your leaves…" (no fake step list) | none | — | — |
| 5 | **First result (first win)** | Plant name (with "Not right?" to correct it), symptom seen ("Yellowing on lower leaves"), 2–3 possible causes with Likely / Possible / Less likely, the full text of the top cause, "Check first" card, free toxicity row | "Answer 2 quick questions" | — | **name + symptom + ranked causes + first check** |
| 6 | Two questions | "Is the top 2 inches of soil wet or dry?" and "Has it moved or had a change in light recently?" with big tap answers plus "Not sure" | Tap answers | 2 taps | narrowed result |
| 7 | Updated result | Causes re-ranked, "What to do today" (1–3 steps), "What to watch for", "Can't tell yet" line if it's still ambiguous | "Save plant & set follow-up" | — | a full answer for today |
| 8 | Paywall | Shown when they save the plan. See the Paywall section | "Start free trial" / X | payment (optional) | everything above stays free |
| 9 | Notification pre-prompt | "We'll remind you on Thursday to take a follow-up photo. That's it." | "Remind me" (then the system prompt) / "Not now" | notifications | — |
| 10 | Plant page | Day 1 photo, plan, "Next check: Thursday" | "Done" | — | saved plant |

- First win is on screen 5, three taps from cold launch: Check my plant, Allow camera, shutter. In every competitor flow the team captured, the first result needed a paywall to be closed and used a prepared sample plant.
- Nothing is asked before screen 5 except the camera or a photo.
- No account. No quiz. No location.
- "Just identify a plant" goes to the same camera, then to an identification result with care basics and toxicity, then "Add to my plants".

**Permissions**

| Permission | When | Pre-prompt | On deny or limited |
|---|---|---|---|
| Camera | Screen 2, after the user taps "Check my plant" | Yes, one line | Photo picker always offered. Settings link in a banner, never a blocking wall |
| Photos | Never requested. Use the system PhotosPicker (no permission needed) | — | — |
| Notifications | After the first plant is saved with a follow-up date | Yes, names the date | Follow-ups still show on the My Plants home with a due badge. Ask again only when they add a second plant |
| Location | Not in v1 | — | — |
| ATT (tracking) | Not shown in onboarding. Only if attribution requires it, and only after the first result | System only | Ads attribution without IDFA |

**Core loop**
- Day 2–7: on the follow-up day, one notification: "Time for Monstera's follow-up photo." It opens the camera with the Day 1 photo as a ghost overlay. Then the question "Better / Same / Worse?" plus one condition question, then the plan updates.
- Watering: no fixed "water every N days". The reminder says "Check Monstera's soil today", the user answers dry or wet, and the next check moves earlier or later.
- Week 2: plant status changes to "Recovering", "Stable" or "Still struggling". If it's still struggling, offer the next cause to rule out.
- After recovery: "Keep checking every 2 weeks?", then the plant moves to routine care.
- Second plant: after the first follow-up, prompt "Add another plant" once.
- No streaks, no "your plant is sad" guilt and no overdue counters in red.

**Key screens**

1. **Result card (screen 5/7)**
```
[user photo]           Monstera deliciosa  (Not right?)
Seen: yellowing on lower leaves
Possible causes
  ● Likely      Too much water — soil stays wet, lower leaves yellow first
  ○ Possible    Low light — plant far from window
  ○ Less likely Natural old-leaf drop
Check first: push a finger 2" into the soil. Wet → hold off watering.
[ Answer 2 quick questions ]
Pets: Toxic to cats and dogs if chewed. Ask a vet if eaten.
```
- States: checking (spinner on the user's photo), no plant found ("We couldn't find a plant. Try closer, in daylight" with Retake), blurry photo (Retake with tip), plant unknown (show top matches, let the user pick, or "Continue without name"), healthy-looking ("No visible problem in this photo. Things a photo can't show: roots, soil moisture. Check soil anyway?"), offline ("Saved. We'll check when you're back online"), service error (Retry, photo kept).
- Most important element: the "Check first" step.

2. **Two questions (screen 6)**
- Two full-width tap cards per question plus "Not sure". No typing.
- States: "Not sure" on every question shows the result unchanged with "Try this check and come back".
- Most important element: the soil question.

3. **Plant page**
```
[Day 1 photo] [Day 4 photo] [+]
Status: Recovering · Next check Thu
Plan: 1. Let soil dry to 2"  2. Move 1 m closer to window
History ▸   Care basics ▸   Pets & kids ▸
```
- States: new (one photo, "Follow-up Thu"), check due (badge plus "Take follow-up photo"), recovering / stable / struggling, plan finished ("Back to routine checks"), free user over the plan limit (plan view is read-only, with the upgrade line below).
- Most important element: the photo timeline.

4. **Follow-up check**
- Camera with a ghost overlay of the last photo, then Better / Same / Worse, then one condition question, then the updated plan.
- States: skipped (it stays due, with no penalty copy), notification denied (the due badge on home is the only trigger).
- Most important element: the side-by-side comparison right after capture.

5. **My Plants home**
- "Today": checks due. Then plant cards.
- States: empty ("Got a plant that looks off? Check it" plus camera), all clear ("Nothing due today"), many plants (sorted by due first).
- Most important element: the "due today" row.

6. **Paywall.** See below.

**Paywall**
- Placement: after the first full result (screen 8), when the user taps "Save plant & set follow-up", and again whenever a free user hits a paid limit. It is never shown before the first result. No paywall on launch, and no repeat paywall in the same session.
- Type: soft. The X is visible and tappable from the first frame. Closing it keeps the result on screen and saves the plant with the free tier.
- What precedes it: the user's own result and today's steps.
- Plans to test first: annual with a free trial vs annual with no trial and a monthly option. **No weekly plan in v1.** Prices are not set here: they come from the s5-monetization agent after pulling US App Store IAP listings.
- Trial framing: show a timeline ("Today: free · [date]: reminder · [date]: billed [price]/year"). The trial-ending reminder is on by default and we send it ourselves. The button reads "Start free trial", with the full price and renewal under it at the same size as the body text.
- Cancel clarity: "Cancel anytime in Settings › Apple ID › Subscriptions" with a direct link, repeated in app Settings.
- Free users keep: unlimited identification (subject to the vendor cost check), one active problem plan, toxicity on every plant, saved plants with photos, the first follow-up on that plan.
- Disclosures: title, length, price per period, the trial terms and the auto-renew statement before purchase. Links to Terms and Privacy, plus a Restore button (App Review Guideline 3.1.2).
- Never: a fake "trial is enabled" toggle animation, a "Try for $0.00" button, strikethrough "was" prices, "Only now!", countdown timers, a pre-selected weekly plan, or a delayed or low-contrast close button.

**Visual direction**
- Light cream background, deep forest green for navigation and primary buttons, terracotta only to mark a problem, mint for progress and done. No red alarm screens.
- Real plant photos (the user's own wherever possible) on clean cards. No 3D renders, no stock lifestyle models, no illustrated mascots.
- Medium density: one card per idea, generous spacing, SF Pro with Dynamic Type, large title on home.
- Motion: a short check-off when a step is done, and a photo-comparison slider. No confetti and no glow effects.
- Light mode first, with dark mode supported. Competitors split between dark (Plantaria, Plantiary, PlantIn) and light green or white (Plantum, PlantApp, LeafSnap); we take calm light cream with a diagnostic layout.
- Final tokens come from the brand-designer agent.

**Voice**
- Calm, specific and plain. We talk like a friend who knows plants, not like an alarm.

Lines we ship:
1. "Show me the leaf that's worrying you."
2. "Possible causes. A photo can't see the roots, so let's check two things."
3. "Check first: push a finger 2 inches into the soil."
4. "Same as last time? That's normal in week one. Keep the plan."
5. "Free for 7 days, then [price]/year. We'll remind you 2 days before."

Lines we never ship (seen in competitor screens):
1. "Disease detected" for overwatering (PlantIn, IMG_2201)
2. "1.47X more accurate than others" (Plantaria, IMG_2172)
3. "Stop killing your plants with Plantum PRO" (Plantum, IMG_2218)
4. "3 days trial is enabled" toggle screen (PlantApp, IMG_2156–2157)
5. "Limited offer 14:56" (LeafSnap, IMG_2185)

**Accessibility**
- Dynamic Type on every screen. The result card reflows to one column at accessibility sizes.
- VoiceOver labels on every photo ("Monstera, Day 1, October 5"), on cause rows ("Likely: too much water") and on all icon buttons.
- Confidence words always appear as text, never as colour alone. Terracotta and green both meet contrast on cream.
- Reduce Motion replaces the comparison slider animation with a cross-fade and removes the check-off animation.
- Every action is reachable without the camera, through the photo picker.

**Refuse list**

| Pattern | Seen in |
|---|---|
| Paywall before the user's first result | PlantApp 2158, Plantaria 2178, Care App 2183, Plantiary 2197, PlantIn 2205, Plantum 2218 |
| Prepared sample plant as the "first identification" | PlantApp 2160, PlantIn 2206, Plantum 2220 |
| Animated "trial is enabled" toggle | PlantApp 2156–2157, Plantaria 2177, Plantum 2216–2217 |
| "Try for Free" button with no price on the same screen | PlantApp 2157 |
| Weekly plan pre-selected / "Most popular" weekly | Plantaria 2178, Care App 2183 |
| Trial reminder off by default | Plantaria 2178, PlantIn 2205, Plantum 2218 |
| Low-contrast or missing close on paywall | Plantum 2218 ("Cancel" over leaf image), Plantaria 2178 (no X seen) |
| Strikethrough "was" price | PlantIn 2205 |
| Countdown "Limited offer" | LeafSnap 2185 |
| "Free Premium Available" banner that is a trial | PlantApp 2159 |
| Toxicity locked behind paywall | PlantApp 2163, PlantIn 2209 |
| Unsourced accuracy, user and "cured" counts | Plantaria 2171–2173, PlantApp 2152, PlantIn 2203–2204 |
| Gesture ritual before use ("Draw a checkmark") | Plantaria 2174–2175 |
| Confetti for finishing onboarding | Plantaria 2176 |
| Fake multi-step "analyzing" checklist | PlantApp 2162, PlantIn 2208 |
| 4-question quiz before value | Plantiary 2193–2196 |
| Account / flora / language setup before first use | PlantNet 2145–2148, Plantum 2212 |
| Email opt-in by default via "I don't want emails" checkbox | Plantum 2212 |
| Location asked during onboarding for weather | Plantiary 2192 |
| Tool grids and non-plant identifiers (insects, birds, mushrooms) | Plantiary 2193, 2198; PlantApp 2159 |
| Fixed "Water every 10 days" | PlantIn 2209 |

## v1 product features

| # | Feature | What it does | Free / Paid |
|---|---|---|---|
| 1 | Camera + photo picker capture | One capture screen, frame guide, retake tips | Free |
| 2 | Plant identification | Top match with confidence word, "Not right?" shows alternates and lets the user pick | Free (cap only if vendor cost requires; set in spike) |
| 3 | Problem check-up | Symptom seen + 2–3 ranked possible causes + "Check first" step, on the user's photo | Free (first check per plant) |
| 4 | Two-question narrowing | Soil moisture + recent change, re-ranks causes | Free |
| 5 | Today's steps | 1–3 actions, plus "what to watch for" and "can't tell yet" | Free |
| 6 | Toxicity row | Cats, dogs and children, on every identified plant, with a verify line | Free |
| 7 | My Plants | Saved plants, photo timeline, status | Free (unlimited saves) |
| 8 | Care plan + follow-up | Scheduled follow-up photo, Better/Same/Worse, plan update | Free: 1 active plan · Paid: unlimited |
| 9 | Photo comparison | Ghost overlay on capture, side-by-side Day 1 vs latest | Free on the active plan |
| 10 | Condition-check reminders | "Check soil" reminders that adapt to dry/wet answers instead of a fixed watering interval | Paid (first plant free) |
| 11 | Repeat check-ups | New problem check on any plant, any time | Paid |
| 12 | Care basics | Light, water approach, humidity, difficulty for the identified plant (short, not an encyclopedia) | Free |
| 13 | Local notifications | Follow-up and check reminders, user-set time | Free |
| 14 | Subscription | StoreKit 2, paywall, restore, manage link, trial-ending reminder on by default | — |
| 15 | Settings & privacy | Delete all data, export photos, notification time | Free |

**Paid unlocks**
- Unlimited active care plans and follow-ups.
- Condition-check reminders on every plant.
- Repeat problem check-ups on any plant at any time.
- Full history across all plants.

**Later (with trigger)**

| Feature | Bring in when |
|---|---|
| One-time paid report (consumable) | Paywall view to trial is low and refund or "only needed once" feedback dominates |
| Light check (camera-based) | "Low light" is a top-2 likely cause in a large share of check-ups |
| Home screen widget for "checks due" | D7 follow-up completion is below target and notification opt-in is low |
| iCloud sync / multi-device | Support requests for device moves, or users on 2+ devices |
| Seasonal care adjustments | Winter cohort shows watering-related "Worse" follow-ups rising |
| Shared household plants | Repeated requests from couples or roommates |
| Human expert review | Paid users ask "is this right?" often and unit economics allow |
| Expanded plant library beyond common houseplants | Unknown-plant rate on check-ups stays high |
| Outdoor / garden plants | Indoor retention is proven and outdoor share of photos is meaningful |

**Not building**

| Competitor feature | Why not |
|---|---|
| Insect, bird, mushroom, tree identifiers | Off-job bloat, adds abstractions (Plantiary, PlantApp) |
| AI chat botanist | Generic answers, the exact complaint in reviews, plus open-ended cost |
| Community feed / groups | Moderation load, not the job |
| Article / explore feed | Content treadmill, no link to the user's plant |
| Weather on home | Location ask for little value |
| Plant decorator / AR placement | Not the job |
| Water meter / water calculator with fixed intervals | Contradicts condition-based care |
| Big species encyclopedia | Six-week scope, accuracy risk |
| Account sign-in | Not needed for local data in v1 |

**Free vs paid line**
A free user can photograph their own sick plant, get it named, see ranked possible causes, narrow them with two taps, get today's steps, see pet toxicity, save the plant, and complete one full follow-up plan with before-and-after photos. That is a complete answer to "what's wrong and what do I do". Paying unlocks ongoing care: unlimited plans and follow-ups, condition-check reminders on every plant, and repeat check-ups whenever something new looks off. The line converts because the user has already seen the app reason about their own plant and has a follow-up scheduled; what they pay for is the next weeks, not the first answer.

**Success metrics for v1**

| Metric | Target |
|---|---|
| Install → first result on own photo | UNKNOWN: set after first cohort |
| First result → plant saved with follow-up | UNKNOWN: set after first cohort |
| Paywall view → trial start | UNKNOWN: set after first cohort |
| Follow-up photo submitted by day 7 (of saved plans) | UNKNOWN: set after first cohort |
| Second plant added by D30 | UNKNOWN: set after first cohort |
| Trial → paid, and refund rate | UNKNOWN: set after first cohort |

## New recommendations

1. Keep pet and child toxicity free on every plant and use it as an ad and store angle ("Safe for your cat?"); two competitors lock it.
2. Turn the trial-ending reminder on by default and send it ourselves. Measure refund rate against a holdout with it off.
3. Remove the sample-plant demo entirely. Test "own photo first" against a sample-plant control on install to first result and paywall-to-trial.
4. Add a healthy-photo result that says "No visible problem in this photo" and lists what a photo can't show, instead of "HOORAY! YOUR PLANT LOOKS HEALTHY!". Track the "Worse" rate on later follow-ups for plants called healthy.
5. Use a ghost-overlay camera for follow-ups so before-and-after photos line up. Kill it if follow-up completion with it doesn't beat a plain camera.
6. Ship without location, accounts or quiz. Re-add one question only if result accuracy measurably needs it.
7. Spike the ID and diagnosis engine in week 1 with 30 real sick-plant photos (common US houseplants) through 2–3 vendors, plus a test of whether a photo + 2 questions re-ranks causes sensibly. Kill or narrow the problem-check promise if the top-3 causes miss the known cause too often.

## Before build

**Missing captures (take these before s1-spec)**
- A real-plant identification (not the sample) in PlantApp, PlantIn and Plantum, with the paywall closed.
- A diagnosis flow on a visibly unhealthy plant in PlantIn, Plantum, PlantApp and Plantiary: input screens, result, treatment, and any follow-up.
- PictureThis and Planta: not in the screenshot set at all, although context names them as the leaders. Capture onboarding, paywall, ID and diagnosis.
- Care plan or reminder setup and the first reminder notification in PlantIn and Plantum.
- Camera and notification permission prompts as each app asks them.
- Any screen after closing the paywall in Plantaria, Care App and Plantiary.
- US-storefront paywalls. All prices captured are ₹ (India); none are US.
- PlantNet's identification result (no ID was captured).

**Open questions**
- ID and diagnosis engine: vendor, cost per call, on-device option, accuracy on sick leaves. Resolve with a week-1 spike.
- Whether Apple Visual Look Up output is readable by third-party apps (feasibility unknown). Don't plan on it.
- Toxicity data source and licence.
- US prices for annual and monthly plans: pull current US IAP listings (s5-monetization).
- Name clearance for "Plant ER" or the final name (s6-legal).

**Next agents**
1. brand-designer: visual direction and tokens from the Visual direction section.
2. ux-designer: screens 1–10, the result card, plant page and follow-up check, with all listed states.
3. s1-spec: turn the v1 feature table into a build spec with the free/paid line and edge cases.
4. s5-monetization: US prices and the trial test plan.
5. s3-engineering: ID/diagnosis vendor spike and StoreKit 2 setup.
