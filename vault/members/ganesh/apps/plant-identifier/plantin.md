---
type: app
category: plant-identifier
app: "PlantIn: Plant Identifier • Care"
app_store_id: 1527399597
member: ganesh
run_by: harshil
updated: 2026-10-04
status: draft
scope: screens-only
screens_analysed: 12
reviews_analysed: 0
sources: [screenshots:12 (ganesh, India storefront), ganesh-benchmark-xlsx, itunes-lookup-us]
---

# PlantIn: Plant Identifier • Care (Vortemol Limited)

Screens-only stage A run. Ganesh captured the screenshots on the **India storefront** (around 2026-10-03, `[INFERRED]` from Plant App's trial due date captured in the same session). Prices are ₹ and are not US prices. No category lens exists yet for plant-identifier (`research/categories/plant-identifier/lens.md` is missing), so lens questions are not answered here. Related: [[members/ganesh/drafts/plant-identifier/screens-synthesis]].

## A1 Snapshot (short)

| Field | Value | Tag |
|---|---|---|
| Developer | Vortemol Limited | `[DATA:itunes-lookup-us 2026-10-04]` |
| Price model | Free download, subscription + lifetime IAP | `[DATA:itunes-lookup-us]` `[OBSERVED #7]` |
| US rating | 4.56 from 229,566 ratings | `[DATA:itunes-lookup-us 2026-10-04]` |
| Version / last update | 5.62.0, 2026-09-29 | `[DATA:itunes-lookup-us]` |
| First release | 2020-08-14 | `[DATA:itunes-lookup-us]` |
| Genre / size | Education, 214 MB | `[DATA:itunes-lookup-us]` |
| Positioning | "Become a Plant Hero" (#1); leads with care schedule, then disease ("Spot plant issues in seconds"), then social proof | `[OBSERVED #1–#6]` |
| Ganesh's row | Onboarding 5 screens; paywall "Early (4 info cards, zero friction)"; free = "Quick plant identification results and basic care overview"; paid = "Light meter, customized misting schedule, 1-on-1 botanist consultation chat"; offer "₹2,999/yr (3-day trial) or ₹4,999 Lifetime" | `[DATA:ganesh-benchmark-xlsx]` |

The onboarding claims "4.8 ★ Loved worldwide" and "40M+ Global users" (#6). The US listing shows 4.56 `[DATA:itunes-lookup-us]`. The 4.8 may be a global or another storefront's figure `[UNKNOWN]`.

## A2 Business performance
Not in this run (screens-only).

## A3 Monetization (from screens)

- **Placement:** one paywall after 5 promo screens and **before any identification** (#7). It is soft: an X is visible top-right in the capture. `[OBSERVED #7]` We can't tell from a still whether the X appears after a delay `[UNKNOWN]`. Fix: screen-record the paywall.
- **Plans (India):** "Annual · 3-day free trial · ₹ 2,999 / year" preselected; "Lifetime ~~₹19,996.00~~ ₹ 4,999". `[OBSERVED #7]` These match Ganesh's row `[DATA:ganesh-benchmark-xlsx]`.
- **Trial reminder:** "Remind me before the trial ends" is a toggle that is **off by default**. `[OBSERVED #7]`
- **Anchor:** the lifetime price is struck through from ₹19,996.00 to ₹4,999. Whether ₹19,996 was ever charged is `[UNKNOWN]`, so treat the anchor as invented until shown otherwise `[INFERRED]`.
- **In-result gating:** the toxicity chip "Poisonous 🔒" is locked on the free result (#11). `[OBSERVED #11]`
- **Other touchpoints:** none captured after the main paywall. The home screen (#12) shows no upsell banner `[OBSERVED #12]`. Later upsells are `[UNKNOWN]`.
- **Storefront note:** US plans and prices may differ (weekly plans are common in this category) `[UNKNOWN]`. Check with a US Apple ID.

## A4 Acquisition
Not in this run (screens-only).

## A5 Product teardown (screens lens)

### Journey and gaps
The captures run IMG_2199 to IMG_2210, 2:45 to 2:46, in order. **Gaps:** #4 (IMG_2202) duplicates #3. The camera permission prompt was not captured, and the demo ran on a prepared photo, so it may not need the camera. No real identification of Ganesh's own plant, no care/diagnosis flow, and no settings/subscription screen were captured.

### Per-screen table

| # | stage | what user sees | asks of user | gives to user | verbatim copy | lever | friction / dark pattern | tag |
|---|---|---|---|---|---|---|---|---|
| 1 | first-launch | Peace lily with floating care chips | accept legal by continuing | nothing yet | "Welcome to PlantIn!" "Become a Plant Hero" "By continuing you accept our Privacy Policy, Terms & Conditions and Billing Policy" | identity ("Hero") | consent bundled into Continue | `[OBSERVED]` |
| 2 | onboarding 1/4 | care countdown chips | tap Next | promise of reminders | "Your plant care just got easier" "Water Need today" "Prune In 12 days" "Fertilize In 23 days" | relief | none | `[OBSERVED]` |
| 3 | onboarding 2/4 | wilting plant, red scan frame, treatment card | tap Next | promise of diagnosis | "Spot plant issues in seconds" "Overwatering Disease detected" "3. 3. Remove dead leaves" | fear then fix | typo "3. 3." in marketing copy | `[OBSERVED]` |
| 4 | onboarding 2/4 (dup) | same as #3 | n/a | n/a | n/a | n/a | duplicate capture | `[OBSERVED]` |
| 5 | onboarding 3/4 | grid of plants | tap Next | social proof | "220,000+ plants cured" | proof | unverifiable claim | `[OBSERVED]` |
| 6 | onboarding 4/4 | testimonials, laurels | tap Next | social proof | "Trusted by millions of plant lovers" "40M+ Global users" "4.8 Loved worldwide" "Mirana Marci Plant mom" | proof | 4.8 vs US 4.56 | `[OBSERVED]` `[DATA:itunes-lookup-us]` |
| 7 | paywall | before/after illustration, 2 plans | pay or close | nothing new | "Try For Free" "Annual 3-day free trial ₹ 2,999 / year" "Lifetime ₹19,996.00 ₹ 4,999" "Remind me before the trial ends" | anchoring, free framing | struck-through anchor; reminder off by default; X timing unknown | `[OBSERVED]` |
| 8 | core-task (demo) | stock snake-plant photo | tap "Let's try" | invitation to a demo | "We've set up a plant for you!" "Try identifying our plant to see how easy it is." "Let's try" "Identify my plants" | low-effort first try | the first win is on *their* plant, not yours | `[OBSERVED]` |
| 9 | core-task (demo) | full-screen photo, shutter | tap shutter | n/a | "Want to know what this plant is?" "Tap here to identify" | curiosity | none | `[OBSERVED]` |
| 10 | loading | photo with progress bar, 3 steps | wait | n/a | "Plant identification" "Analyzing image" "Identifying characteristics" "Preparing results" | perceived effort | staged steps on a pre-known stock photo (theatre) | `[OBSERVED]` `[INFERRED]` |
| 11 | result | Snake Plant card, care tabs | nothing | name, latin, aliases, difficulty, water, fertilize | "Snake Plant" "Latin name: Sansevieria trifasciata" "Poisonous 🔒" "Difficulty Medium" "Water Every 10 days" "Fertilize Regularly" "Identify my plants" | competence | **toxicity locked**; outdated latin name (now *Dracaena trifasciata*, listed only as an alias) | `[OBSERVED]` |
| 12 | home | empty My Plants, mascot pot | add plant / identify | empty state | "Local weather Show" "Let's add your plants to keep them alive" "+ Add plant" "Tap here to identify" tabs "My Plants · Feed · Search · More" | care, mild guilt ("keep them alive") | 4 tabs plus a camera button on day 1 | `[OBSERVED]` |

### 8 measures

1. **First win.** A plant name appears on screen 11 after about 8 taps (Continue, Next ×4, close paywall, Let's try, shutter) `[OBSERVED #1–#11]`. It comes **after** the paywall, which can be dismissed. The win is on a prepared stock photo, so the user has not felt the benefit on their own plant yet. A real first ID is `[UNKNOWN]`.
2. **Ask ledger.**
   1. Legal consent (#1). Received so far: nothing.
   2. Paywall (#7). Received so far: 4 promo cards, no value.
   3. Demo tap (#8–#9). Received so far: nothing real.

   There is no account, quiz, notification or location ask before the demo `[OBSERVED]`. The camera permission is not captured `[UNKNOWN]`. This is the lightest ask ledger of the four apps.
3. **Abstractions.**
   - "Plant Hero" is invented and adds nothing.
   - "My Plants" is a collection the job needs.
   - "Feed" is invented.
   - "Local weather" is a semi-concept that needs location `[OBSERVED #12]`.
   - The care tabs "Care / Plant requirements / General information" split one card into three `[OBSERVED #11]`.
4. **Feel-good moments.**
   - The care countdown (#2) is manufactured, a mockup.
   - "We've set up a plant for you!" (#8) is a pleasant handhold but manufactured.
   - The result card with aliases (#11) is earned but on a demo.
   - The mascot pot (#12) adds warmth.
5. **Feel-bad moments.**
   - Struck-through ₹19,996 anchor (#7).
   - "Remind me before the trial ends" defaults to off (#7).
   - Locked "Poisonous 🔒" (#11): safety info behind a paywall is the most hostile gate a parent or pet owner can meet.
   - "keep them alive" (#12) is mild guilt.
   - Typo "3. 3." (#3) undermines trust.
6. **Paywall.** One soft paywall before any ID. Plans: annual ₹2,999 with a 3-day trial, or lifetime ₹4,999 `[OBSERVED #7]`. The user sees only promo cards before the price. No downsell was captured `[UNKNOWN]`. Close timing is `[UNKNOWN]`.
7. **Repeat cost.** From home: camera button, then shutter, so 2 taps to identify `[OBSERVED #12]`, `[INFERRED]` for the shutter. Return hooks: care reminders (promised #2), local weather (#12). Notification opt-in is not captured `[UNKNOWN]`.
8. **Feature map.**
   - Table stakes: photo ID, care basics (water, difficulty, fertilize), My Plants, reminders.
   - Differentiators: per-task care countdown (#2), diagnosis with treatment steps (#3), lifetime plan.
   - Bloat: Feed, "Plant Hero", weather on the home header.
   - From the xlsx `[DATA:ganesh-benchmark-xlsx]`: light meter and botanist chat are paid.

## Keep / Kill / Different

**Keep**
- The short, quiz-free onboarding with no account (#1–#6). It is the lowest-ask flow in the set.
- The care countdown chips "Water Need today / Prune In 12 days" (#2). This is the clearest picture of the ongoing value.
- The result card that lists all common names (#11). People search by the name they heard.
- A lifetime option (#7). It defuses "subscription trap" anger `[INFERRED]`.

**Kill**
- The struck-through ₹19,996 anchor (#7).
- The trial reminder defaulting to off (#7).
- Locking toxicity (#11).
- Fake staged steps on a known photo (#10).
- The "Plant Hero" identity line (#1).
- The Feed tab (#12).

**Different**
- Run the first ID on the user's own plant before any price screen. Offer the sample photo only as a fallback link.
- Show toxicity for pets and kids free on every result.
- Default the trial reminder to on.
- Use the accepted current latin name, with the old name as "formerly".

## A6 Failure mining
Not in this run (screens-only). Ganesh's xlsx has one 1★ quote, truncated and undated, so not a mined sample: "Really Difficult to Cancel Subscription — EvergreenEmily: …I have been trying" `[DATA:ganesh-benchmark-xlsx]`.

## A7 Tech & ops
Not in this run (screens-only).

## A8 Verdict (short)

PlantIn is the most restrained of the four. It has no account, no quiz and one paywall, then a guided demo ID with a clean result card. Its weak points are honesty details rather than structure:
- the ₹19,996 anchor
- the reminder defaulting to off
- locked toxicity
- staged "analyzing" steps

**Copy:** the low-ask onboarding, the countdown-style care framing, the lifetime plan.
**Beat:** demo-plant-only first win, locked safety info, pricing tricks.
**Most exploitable weakness:** "Poisonous 🔒". A free safety answer is a one-line screenshot promise PlantIn structurally can't match without giving up a paid lever.

Evidence strength:
- A1 medium (listing only)
- A3 medium (one paywall still, no recording)
- A5 medium (no real ID, care or diagnosis screens)
- A8 weak to medium
