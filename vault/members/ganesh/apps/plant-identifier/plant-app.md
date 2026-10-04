---
type: app
category: plant-identifier
app: "Plant App: Plant Identifier"
app_store_id: 1595795215
member: ganesh
run_by: harshil
updated: 2026-10-04
status: draft
scope: screens-only
screens_analysed: 13
reviews_analysed: 0
sources: [screenshots:13 (ganesh, India storefront), ganesh-benchmark-xlsx, itunes-lookup-us]
---

# Plant App: Plant Identifier (ScaleUp Yazılım), not PictureThis

Screens-only stage A run on the **India storefront**. Every capture with a visible clock shows 2:27 (#10–#11 show no clock); the paywall shows "Due October 6, 2026" after a 3-day trial, so the capture date is about 2026-10-03 `[INFERRED]`. Prices are ₹ and are not US prices. No plant-identifier lens exists yet. Related: [[members/ganesh/drafts/plant-identifier/screens-synthesis]].

## A1 Snapshot (short)

| Field | Value | Tag |
|---|---|---|
| Developer | SCALEUP YAZILIM HIZMETLERI ANONIM SIRKETI | `[DATA:itunes-lookup-us 2026-10-04]` |
| Price model | Free download, weekly subscription (only plan seen) | `[OBSERVED #8]` |
| US rating | 4.70 from 55,488 ratings | `[DATA:itunes-lookup-us 2026-10-04]` |
| Version / last update | 3.6.11, 2026-09-30 | `[DATA:itunes-lookup-us]` |
| First release | 2022-04-19 | `[DATA:itunes-lookup-us]` |
| Genre / size | Education, 188 MB (187,792,384 bytes) | `[DATA:itunes-lookup-us]` |
| Positioning | "Keep your plants happy!"; paywall "Grow Healthier Plants · Care for every plant with AI" | `[OBSERVED #1, #8]` |
| Ganesh's row | Onboarding 5; paywall "Early (3 intro screens) + Feature Gated"; free = "Basic photo identification and plant encyclopedic name card"; paid = "Toxicity/Poison alerts, plant doctor disease diagnosis, watering reminders"; offer "₹1,499/yr with 3-day free trial" | `[DATA:ganesh-benchmark-xlsx]` |

**I disagree with Ganesh's row on price.** The screen says "Free for 3 days, then ₹ 1,499/week" and "Due October 6, 2026 ₹ 1,499" `[OBSERVED #8]`. It is **per week**, not per year. ₹1,499 × 52 ≈ ₹77,948 a year `[INFERRED: arithmetic]`. This changes how we read this app's monetization. Placement and gating in the xlsx match the screens.

The onboarding claims "10,000,000+ users", "4.7 100,000+ ratings" and "#1 Choice for Plant Lovers (2022–2025)" (#2). The US listing has 55,488 ratings `[DATA:itunes-lookup-us]`, so the 100,000+ figure must be global or unverified `[UNKNOWN]`.

## A2 Business performance
Not in this run (screens-only).

## A3 Monetization (from screens)

- **Placement:** after 3 promo cards and a 2-screen "3 days trial is enabled" animation, before any ID (#6–#8). `[OBSERVED]`
- **Plans (India):** one plan only. "PlantApp PRO … Free for 3 days, then ₹ 1,499/week", "Free Trial Enabled ✓", "Due today 3 days free ₹0.00", "Due October 6, 2026 ₹ 1,499". `[OBSERVED #8]` No yearly or lifetime option was visible in the capture `[OBSERVED]`. Others may exist off-screen or behind the trial toggle `[UNKNOWN]`.
- **Good:** the billing timeline ("Due today / Due October 6, 2026") states the date and amount. That is the most honest element on any paywall in this set `[OBSERVED #8]`.
- **Bad:** "Free Trial Enabled" is pre-checked, and the screen before it (#7) has only a "Try for Free" button and no visible close `[OBSERVED #7]`. On #8 an X is visible top-right; its delay is `[UNKNOWN]`.
- **In-result gating:** the toxicity row reads "Unlock For Free · Poisonous · Unlock" (#13). It is gated behind a "for free" label, which most likely means the trial `[INFERRED]`.
- **Other touchpoints:** home banner "Free Premium Available · Tap to claim" (#9).
- **Storefront note:** the US plan mix is `[UNKNOWN]`. Recapture with a US Apple ID.

## A4 Acquisition
Not in this run (screens-only).

## A5 Product teardown (screens lens)

### Journey and gaps
IMG_2151 to IMG_2163, in order; every visible clock reads 2:27 (#10–#11 have none).

**Gaps:**
- #1 is a white card on a grey backdrop with a black button showing only a copy/clipboard icon. Its purpose is `[UNKNOWN]` (possibly an install-attribution or paste-link step). Recapture with a screen recording.
- The location permission prompt was not captured, but location is granted by #9 (status-bar arrow, city and temperature on home).
- The camera prompt was not captured.
- No own-plant ID, no Disease Identifier, no My Garden, no settings/subscription screens.

### Per-screen table

| # | stage | what user sees | asks of user | gives to user | verbatim copy | lever | friction / dark pattern | tag |
|---|---|---|---|---|---|---|---|---|
| 1 | first-launch | greenhouse card, black button with icon only | tap unlabeled button | nothing | "Welcome to Plant App" "Keep your plants happy!" | warmth | unlabeled primary button | `[OBSERVED]` |
| 2 | first-launch | stats with laurels | Get Started / Sign in | proof | "10,000,000+ users" "4.7 100,000+ ratings" "#1 Choice for Plant Lovers (2022–2025)" "Welcome to PlantApp" "Already registered? Sign in" "Get Started" | authority | unverifiable "#1" | `[OBSERVED]` |
| 3 | onboarding 1/3 | camera mockup | Continue | promise | "Take a photo to identify the plant!" | curiosity | none | `[OBSERVED]` |
| 4 | onboarding 2/3 | care-guide mockup | Continue | promise | "Get plant care guides" "White Bird of Paradise" "Strelitzia alba" "Toxic to people Poisonous" "Safe to animals Poisonous" "Wild banana (Strelitzia nicolai)…" | competence | **mockup says "Safe to animals" and "Poisonous" together, and names two different species** | `[OBSERVED]` |
| 5 | onboarding 3/3 | person watering a plant | Continue | promise | "Get timely care reminders!" | care | none | `[OBSERVED]` |
| 6 | pre-paywall | toggle animating | none (auto) | nothing | "3 days trial is enabled" | endowment | trial "enabled" before the price | `[OBSERVED]` |
| 7 | pre-paywall | toggle on, CTA | tap "Try for Free" | nothing | "3 days trial is enabled" "Try for Free" "Terms of Use" "Privacy Policy" "Restore" | endowment | **no visible close on this screen** | `[OBSERVED]` |
| 8 | paywall | before/after slider, PRO box, timeline | start trial or close | billing clarity | "Grow Healthier Plants" "Care for every plant with AI" "Before Plantapp" "PlantApp PRO Effortless plant care, Smart AI guidance for every plant, Diagnose issues instantly, A personalized care plan for your greenery" "Free for 3 days, then ₹ 1,499/week" "Free Trial Enabled" "Due today 3 days free ₹0.00" "Due October 6, 2026 ₹ 1,499" "Try for Free" | free framing | weekly-only plan; trial pre-checked; ₹1,499/wk | `[OBSERVED]` |
| 9 | home | city weather, tools grid, coachmark | tap to identify | tool menu | "Free Premium Available Tap to claim" "Plant Tools" "Plant Identifier" "Disease Identifier" "Tree Identifier" "Light Meter" "Water Meter" "Ask Botanist" "Show More" "Identify your plant! Tap here to identify your first plant! You can use the plant we have prepared or take your own pictures" | guidance | 6+ tools and "Show More" on day 1; location already used | `[OBSERVED]` |
| 10 | core-task (demo) | camera view with a sheet | choose demo or own plant | invitation | "We've prepared a plant" "Identify the plant we have prepared for you to see how quick and easy PlantApp is." "Try with an example" "Identify my real plant" | low-effort first try | demo is the primary CTA | `[OBSERVED]` |
| 11 | core-task (demo) | stock monstera in a frame | tap shutter | n/a | "Now tap here!" "Want to know which plant it is?" | curiosity | none | `[OBSERVED]` |
| 12 | loading | photo, 3 spinners | wait | n/a | "We scan for you" "We analyze your plant with AI" "Analyzing image" "Detecting leaves" "Identifying plant" | perceived AI effort | staged steps on a known example (theatre) | `[OBSERVED]` `[INFERRED]` |
| 13 | result | Monstera card | unlock toxicity | name, tabs | "Monstera Deliciosa" "Monstera Deliciosa" "Plant Notes" "Plant Info" "Care Guide" "Overview" "Requirements" "Culture" "FAQ" "Unlock For Free Poisonous Unlock" "Attention Toxicity information may be subject to error. Do not use PlantApp as only source of information and do not consume a plant without consulting an expert." | caution | **toxicity locked**; common name = latin name repeated; 3 tabs plus 5 chips under Plant Info (chips under the other tabs not captured) | `[OBSERVED]` |

### 8 measures

1. **First win.** A plant name appears on screen 13 after about 9–10 taps: unlabeled button, Get Started, Continue ×3, Try for Free on #7, close on #8, coachmark/camera, "Try with an example", shutter `[OBSERVED]`/`[INFERRED]`. It comes **after** the paywall and is on a stock example.
2. **Ask ledger.**
   1. Unlabeled button (#1). Received so far: nothing.
   2. Get Started (#2). Received so far: claims.
   3. "Try for Free" with the trial pre-enabled (#6–#7). Received so far: 3 promo cards.
   4. Paywall (#8). Received so far: nothing real.
   5. Location (granted before #9, prompt not captured). Received so far: nothing real.
   6. Demo (#10–#11). Received so far: nothing real.
   7. "Unlock" for toxicity (#13). Received so far: a demo name.

   Five or six asks before a real benefit `[OBSERVED]`/`[INFERRED]`.
3. **Abstractions.** Home exposes many tools for one job: "Plant Identifier", "Disease Identifier", "Tree Identifier", "Light Meter", "Water Meter", "Ask Botanist", "Show More" (#9). Tree vs plant identifier is an invented split; a tree is a plant. Light Meter and Water Meter are invented instruments. "My Garden" is needed. The result has "Plant Notes / Plant Info / Care Guide" × "Overview / Requirements / Culture / FAQ / A…" (#13), which is heavy taxonomy.
4. **Feel-good moments.**
   - The billing timeline (#8) gives honest relief, which is rare.
   - The coachmark "Tap here to identify your first plant!" (#9) is kind guidance.
   - The demo result (#13) is manufactured, a stock photo.
5. **Feel-bad moments.**
   - Unlabeled first button (#1).
   - Weekly ₹1,499 (#8).
   - Trial pre-enabled with no close on #7.
   - Contradictory safety mockup (#4).
   - Locked toxicity behind "Unlock For Free" (#13).
   - A disclaimer that says toxicity "may be subject to error" right after locking it (#13).
   - "Free Premium Available" (#9) after the user has just declined.
6. **Paywall.** Soft (X on #8), one weekly plan, a 3-day trial pre-checked, and a clear billing date. The user saw only 3 promo cards before the price.
7. **Repeat cost.** Centre camera button, then shutter: 2 taps `[OBSERVED #9]`, `[INFERRED]` for the shutter. Return hooks: care reminders (promised #5), weather (#9). Notifications are `[UNKNOWN]`.
8. **Feature map.**
   - Table stakes: ID, care guide, reminders, My Garden.
   - Differentiators: billing timeline transparency, Ask Botanist.
   - Bloat: Tree Identifier, Light Meter, Water Meter, FAQ/Culture tabs, weather.

## Keep / Kill / Different

**Keep**
- **The billing timeline (#8):** "Due today ₹0.00 / Due October 6, 2026 ₹ 1,499". Copy it exactly, with our own honest numbers.
- **The first-ID coachmark (#9).** One sentence, points at the one button.
- **A plain toxicity disclaimer (#13).** Keep it, but next to a free answer.

**Kill**
- The unlabeled button (#1).
- The trial-enabled theatre and the no-close #7.
- The weekly-only plan (#8).
- The tool-grid sprawl (#9).
- Staged scan steps (#12).
- Locked toxicity (#13).
- Contradictory safety mockup copy (#4).

**Different**
- One camera button on home, no tool grid. Diagnosis is a result section, not a separate "Disease Identifier".
- Use the billing timeline with a yearly plan, reminder on by default.
- Show toxicity free with the disclaimer.

## A6 Failure mining
Not in this run (screens-only). Ganesh's xlsx quotes, undated and truncated:
- 2★ "Most features are locked behind a paywall including diagnosis/light meter/plant ID/toxicity info and more, while some aspects are advertised as 'free'"
- 1★ "The free trial is a scam … there was literally no option for that [cancel]"

`[DATA:ganesh-benchmark-xlsx]`

## A7 Tech & ops
Not in this run (screens-only).

## A8 Verdict (short)

Plant App wins on polish and an honest billing timeline. It loses on value per ask: 5–6 asks, a weekly-only ₹1,499 plan, and a demo ID whose safety row is locked. The xlsx 2★ quote names toxicity gating directly, and the screens confirm it (#13).

**Copy:** billing timeline, first-ID coachmark, disclaimer tone.
**Beat:** weekly-only pricing, tool sprawl, locked toxicity.
**Most exploitable weakness:** the "Unlock For Free · Poisonous" row. It is a safety answer behind a trial, contradicted by its own marketing (#4).

Evidence strength:
- A1 medium
- A3 strong for this capture (conflicts with the xlsx price unit)
- A5 medium (no own-plant ID, diagnosis or settings)
- A8 medium
