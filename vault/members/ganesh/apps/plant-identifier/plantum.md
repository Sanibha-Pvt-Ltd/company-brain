---
type: app
category: plant-identifier
app: "Plantum - AI Plant Identifier"
app_store_id: 1476047194
member: ganesh
run_by: harshil
updated: 2026-10-04
status: draft
scope: screens-only
screens_analysed: 15
reviews_analysed: 0
sources: [screenshots:15 (ganesh, India storefront), ganesh-benchmark-xlsx, itunes-lookup-us]
---

# Plantum - AI Plant Identifier (AIBY Inc.)

Screens-only stage A run on the **India storefront** (around 2026-10-03). Prices are ₹ (one CTA shows "$", see A3). No plant-identifier lens exists yet. Related: [[members/ganesh/drafts/plant-identifier/screens-synthesis]].

## A1 Snapshot (short)

| Field | Value | Tag |
|---|---|---|
| Developer | AIBY Incorporated | `[DATA:itunes-lookup-us 2026-10-04]` |
| Price model | Free download (US listing); weekly + yearly subscription on the India paywall | `[DATA:itunes-lookup-us]` `[OBSERVED #8]` |
| US rating | 4.59 from 119,332 ratings | `[DATA:itunes-lookup-us 2026-10-04]` |
| Version / last update | 6.21, 2026-09-02 | `[DATA:itunes-lookup-us]` |
| First release | 2019-08-22 | `[DATA:itunes-lookup-us]` |
| Genre / size | Education, 109 MB (108,835,840 bytes) | `[DATA:itunes-lookup-us]` |
| Positioning | "Your plant identifier and care guide"; "Here to keep your plants safe"; paywall headline "Stop killing your plants" | `[OBSERVED #1, #2, #8]` |
| Ganesh's row | Onboarding 4; paywall "After Scan"; free = "Basic plant name identification with simple info card"; paid = "Health diagnosis, watering schedules, fertilizer reminders, advanced care guides"; offer "₹1,999/yr (3-day trial) or ₹449/mo" | `[DATA:ganesh-benchmark-xlsx]` |

**I disagree with Ganesh's row on two points:**
- **Paywall timing.** The xlsx says "After Scan". In these screens the paywall (#8) comes **before** the demo scan (#10–#12) `[OBSERVED]`.
- **Prices.** The xlsx shows ₹1,999/yr and ₹449/mo. The screens show "₹3,999.00 per year" and "then ₹699.00 per week" `[OBSERVED #8]`. Possible causes: an A/B price test, a price change, or the xlsx was filled from the listing's IAP list `[UNKNOWN]`. Fix: recapture the paywall twice on fresh installs and compare against the listing's IAP list.

## A2 Business performance
Not in this run (screens-only).

## A3 Monetization (from screens)

- **Placement:** after a splash, an account wall, 3 promo cards and a "trial is enabled" animation, and **before any identification** (#8). `[OBSERVED]`
- **Plans (India):**
  - "YEARLY ACCESS Just ₹3,999.00 per year" with an "ONLY NOW! ₹76.69 per week" badge.
  - "3-DAY FREE TRIAL then ₹699.00 per week". This tile is highlighted (filled cream with an orange border) and the CTA reads "Try for $0.00" and "No payment now". `[OBSERVED #8]`
- **Weekly vs yearly maths:** ₹699 × 52 = ₹36,348 a year on the weekly plan, about 9× the yearly plan `[INFERRED: arithmetic]`. The trial attaches to the expensive weekly plan.
- **Currency mismatch:** the CTA shows "$0.00" on a ₹ storefront `[OBSERVED #8]`. It looks like a hard-coded string `[INFERRED]`.
- **Close:** "Cancel" top-right in pale text over a leaf photo, close to invisible. "Restore" top-left is more legible than Cancel. `[OBSERVED #8]` Close delay is `[UNKNOWN]`.
- **Trial reminder:** "Remind me before billing" toggle, **off by default**. `[OBSERVED #8]`
- **Pre-paywall theatre:** two screens animate a toggle switching on with "Your 3-day free trial is enabled!" (#6–#7) **before** any price is shown. `[OBSERVED]`
- **Other touchpoints:**
  - Home banner "Try Premium Features for Free · Claim your offer now" with a "1" notification badge on an envelope (#13).
  - Crown icon on Explore (#15).
  - "Ask Experts" on the result (#12); whether it is paid is `[UNKNOWN]`.
- **What the user saw before the price:** marketing mockups only, no real value.

## A4 Acquisition
Not in this run (screens-only).

## A5 Product teardown (screens lens)

### Journey and gaps
IMG_2211 to IMG_2225, 2:47 to 2:48, in order. Screens #1 and #3–#10 have no status bar (full-screen onboarding). #5 is a mid-swipe capture.

**Gaps:**
- No capture of the system camera or notification prompts.
- No capture of what happens after "Continue" on the account wall.
- No identification of Ganesh's own plant.
- No Diagnose, My Plants, Water Calculator or settings/subscription screens.

### Per-screen table

| # | stage | what user sees | asks of user | gives to user | verbatim copy | lever | friction / dark pattern | tag |
|---|---|---|---|---|---|---|---|---|
| 1 | first-launch | splash with laurels | wait | proof | "Welcome to Plantum" "Your plant identifier and care guide" "Featured in 20+ countries" "Trusted by 20M+ users" "gold winner Best Mobile App Overall Award Contest" | authority | unverifiable award | `[OBSERVED]` |
| 2 | account | sign-in wall | sign in with Apple/Facebook/Google, or skip | nothing | "Here to keep your plants safe" "Continue Without Registration" "Skip" "I don't want to receive emails with the latest plant news and recommendations from botanists." | safety framing | **email marketing opt-out checkbox unchecked, so the default reads as opted in** `[INFERRED]`; account asked before any value | `[OBSERVED]` |
| 3 | onboarding | camera mockup | Continue | promise | "SNAP THE PLANT TO FIND OUT WHAT IT IS" | curiosity | none | `[OBSERVED]` |
| 4 | onboarding | result mockup | Continue | promise of health check | "GET DETAILED INFORMATION ABOUT ALL THE PLANTS YOU SEE" "HOORAY! YOUR PLANT LOOKS HEALTHY!" tags "Poisonous" and "Pet-safe" | relief | **mockup tags the same plant both "Poisonous" and "Pet-safe"** | `[OBSERVED]` |
| 5 | onboarding | lock-screen mockup (mid-swipe) | Continue | promise of reminders | "SET UP REMINDERS TO HEL[P] YOUR PLANT STAY HEALTH[Y]" (cut off mid-swipe) | care | none | `[OBSERVED]` |
| 6 | pre-paywall | toggle animating on | none (auto) | nothing | "Your 3-day free trial is enabled!" | default / endowment | trial "enabled" before any price or plan is shown | `[OBSERVED]` |
| 7 | pre-paywall | toggle on, orange | none (auto) | nothing | "Your 3-day free trial is enabled!" | endowment | same | `[OBSERVED]` |
| 8 | paywall | feature list, 2 plans | pay or find Cancel | nothing new | "Stop killing your plants with Plantum PRO" "Infinite plant identifications" "Plant disease autodetection" "Over 400,000 species of plants" "Care schedule for unlimited plants" "Remind me before billing" "YEARLY ACCESS Just ₹3,999.00 per year" "ONLY NOW!" "₹76.69 per week" "3-DAY FREE TRIAL then ₹699.00 per week" "Try for $0.00" "No payment now" "Cancel" | guilt, urgency, free framing | guilt headline; fake urgency "ONLY NOW!"; trial attached to the weekly plan; **near-invisible Cancel**; reminder off; $ on a ₹ store | `[OBSERVED]` |
| 9 | loading | blurred home, spinner | wait | n/a | "Ready in a moment..." | anticipation | none | `[OBSERVED]` |
| 10 | core-task (demo) | stock snake-plant photo with a frame | choose demo or own plant | invitation | "See Plantum in Action!" "Discover this plant's name and care tips in seconds." "Show me how it works" "Identify my plant" "Skip" | low-effort first try | demo is the primary CTA; own plant is secondary; which button was tapped is not captured | `[OBSERVED]` |
| 11 | loading | spinner | wait | n/a | "Recognition in progress..." | effort | spinner; no photo shown, so which image is being recognised is not visible | `[OBSERVED]` |
| 12 | result | Snake plant card with health box | nothing | name, category, tags incl. toxicity, auto health check, genus, latin | "Best Matches" "Snake plant" "Foliage Plants" "Air-purifying" "Easy" "Medium" "Pet-toxic" "Trendy" "Plant Health Beta" "HOORAY! YOUR PLANT LOOKS HEALTHY!" "The plant was diagnosed automatically. Contact our botany experts to be sure about the result." "Ask Experts" "Scientific Name: Dracaena trifasciata" | relief, care | "Easy" and "Medium" both tagged; "Trendy" is noise; auto "healthy" on what is probably the demo photo `[INFERRED]`, which the user never asked to diagnose | `[OBSERVED]` |
| 13 | home | greeting, offer banner, 4 tools | location (soft), claim offer | tool grid | "Location Unavailable Tap to enable geolocation and get weather updates." "Good Afternoon, plant lover!" "Try Premium Features for Free Claim your offer now" "Care Tools" "Diagnose" "Identify" "Water Calculator" "Reminders" "Plantum Tools" | warmth, curiosity (badge "1") | "1" badge on the offer's envelope graphic (whether it is a real notification is `[UNKNOWN]`); a second paywall entry on day 1 | `[OBSERVED]` |
| 14 | explore | article cards loading | n/a | n/a | "Explore" "Care Guides" "Fertilizing" "Holidays" "Humidity" | content | placeholder state | `[OBSERVED]` |
| 15 | explore | seasonal articles | read | content | "6 Amazing Botanical Gardens to Visit This Fall" "How to Bring Your Outdoor Plants Indoors This Fall" | seasonal relevance | red dot on the Explore tab pulls attention away from the core job | `[OBSERVED]` |

### 8 measures

1. **First win.** A plant name appears on screen 12 after about 6–7 taps: Skip or Continue without registration, Continue ×3, Cancel on the paywall, "Show me how it works", plus possibly a shutter `[OBSERVED]`/`[INFERRED]`. It comes **after** the paywall. It is probably the demo plant, not the user's: #10 offers the demo snake plant, #12 names a snake plant and its thumbnail resembles the #10 photo, and #12 still offers "Identify My Plant" `[INFERRED]`. #11 shows no image, so the screens don't prove which photo was identified.
2. **Ask ledger.**
   1. Account sign-in plus an email opt-out you have to tick to avoid marketing (#2). Received so far: nothing.
   2. Trial framed as already "enabled" (#6–#7). Received so far: 3 promo cards.
   3. Paywall (#8). Received so far: promo cards only.
   4. Demo (#10). Received so far: nothing real.
   5. Location, a soft banner on home (#13). Received so far: one ID, probably on the demo plant `[INFERRED]`.

   Four asks before any real value `[OBSERVED]`. Camera and notification prompts are `[UNKNOWN]`.
3. **Abstractions.**
   - "Plantum PRO" is needed as a tier name.
   - "Care Tools" vs "Plantum Tools" are two invented groupings (#13).
   - "Water Calculator" is an invented tool; the job is "when do I water this plant".
   - "Plant Health Beta" is fine.
   - "Best Matches" is fine.
   - "Explore" articles are not needed for the job.
4. **Feel-good moments.**
   - "HOORAY! YOUR PLANT LOOKS HEALTHY!" (#12) is **manufactured**: probably the demo photo `[INFERRED]` auto-diagnosed as healthy, a reassurance the user did not ask for.
   - "Good Afternoon, plant lover!" (#13) is mild warmth.
   - The seasonal articles (#15) are earned only if read.
5. **Feel-bad moments.**
   - "Stop killing your plants" (#8) is guilt.
   - "ONLY NOW!" (#8) is false urgency.
   - Near-invisible "Cancel" (#8).
   - Pre-opted-in emails (#2).
   - The "trial is enabled" animation before price (#6–#7).
   - Contradictory tags: "Poisonous"/"Pet-safe" (#4) and "Easy"/"Medium" (#12). These are trust breakers on safety info.
   - "1" badge on the offer graphic (#13), likely decorative `[INFERRED]`.
6. **Paywall.** Soft, before the first ID. The trial is on the weekly plan (₹699/wk); the yearly ₹3,999 is shown as ₹76.69/week. The close is the weakest in the set `[OBSERVED #8]`. Downsell after Cancel was not captured `[UNKNOWN]`. The home banner (#13) is a second touchpoint.
7. **Repeat cost.** Centre camera button on the tab bar, then shutter: 2 taps `[OBSERVED #13]`, `[INFERRED]` for the shutter. Return hooks: Reminders (#13), weather (needs location), seasonal articles (#15). The notification opt-in is `[UNKNOWN]`.
8. **Feature map.**
   - Table stakes: ID, care info, reminders, My Plants.
   - Differentiators: automatic health check on every ID ("Plant Health Beta", #12), human "Ask Experts" (#12).
   - Bloat: Explore articles, Water Calculator as its own tool, account wall, weather.

## Keep / Kill / Different

**Keep**
- **A health check on every ID (#12).** The user gets diagnosis without asking, which is the best bridge from "what is it" to "is it OK". It must be honest and tied to the user's photo, though.
- **"Continue Without Registration" (#2).** At least it exists.
- **The scientific name shown plainly (#12).**

**Kill**
- The account wall before value (#2).
- The pre-opted-in email checkbox (#2).
- "Trial is enabled" theatre before the price (#6–#7).
- The weekly plan as the trial default (#8).
- "ONLY NOW!" (#8).
- The low-contrast Cancel (#8).
- "$0.00" on a ₹ storefront (#8).
- The auto-"healthy" verdict on a (probably demo) photo (#12).
- Contradictory safety tags (#4, #12).
- The "1" badge on the offer graphic (#13).
- The Explore content tab (#15).

**Different**
- Run a health check automatically on the user's **own** first photo. When it can't tell, it says "can't tell from this photo — take a close-up of the leaves" instead of "HOORAY!".
- One toxicity line with no contradictions: "Toxic to cats and dogs" / "Not known to be toxic".
- Price shown before any trial language. Yearly plan as the default. Close button visible from 0 s.

## A6 Failure mining
Not in this run (screens-only). Ganesh's xlsx quote, 3★, undated and truncated: "First be weary. If you do not exit the 3day free trial it has you set for the annual premium of 50+ dollars. I'm stuck with it for a year…" `[DATA:ganesh-benchmark-xlsx]`.

## A7 Tech & ops
Not in this run (screens-only).

## A8 Verdict (short)

Plantum has the best product idea in the set: every ID comes with a health check. It also has the most manipulative paywall:
- guilt headline
- "ONLY NOW!"
- trial pre-"enabled" by animation
- weekly plan as the trial
- near-invisible Cancel
- reminder off by default
- an account wall in front of it all

**Copy:** health check bundled with ID, the scientific name, a skip-able sign-in.
**Beat:** the paywall honesty, contradictory safety tags, demo-only first win.
**Most exploitable weakness:** the trial→weekly ₹699 path. An honest "yearly only, reminder on, close visible" paywall is our counter-positioning. The xlsx 3★ review shows users already feel trapped.

Evidence strength:
- A1 medium
- A3 strong for this capture (prices conflict with the xlsx, so recheck)
- A5 medium (no own-plant ID, diagnose or settings)
- A8 medium
