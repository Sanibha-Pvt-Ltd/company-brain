---
type: app
category: plant-identifier
app: "Plant Identifier: Plantiary"
app_store_id: 1596971856
member: ganesh
run_by: harshil
updated: 2026-10-04
status: draft
scope: screens-only
screens_analysed: 13
reviews_analysed: 0
sources: [screenshots:13 (ganesh, India storefront), ganesh-benchmark-xlsx, itunes-lookup-us]
---

# Plant Identifier: Plantiary (Blacke Teknoloji)

Screens-only stage A run on the **India storefront** (around 2026-10-03). Prices are ₹ and are not US prices. No plant-identifier lens exists yet. Related: [[members/ganesh/drafts/plant-identifier/screens-synthesis]].

## A1 Snapshot (short)

| Field | Value | Tag |
|---|---|---|
| Developer | Blacke Teknoloji Sanayi Ve Ticaret Limited Sirketi | `[DATA:itunes-lookup-us 2026-10-04]` |
| Price model | Free download, weekly + annual subscription | `[OBSERVED #12]` |
| US rating | 4.66 from 28,301 ratings | `[DATA:itunes-lookup-us 2026-10-04]` |
| Version / last update | 2.2.50, 2026-08-05 (oldest update in the set) | `[DATA:itunes-lookup-us]` |
| First release | 2021-12-03 | `[DATA:itunes-lookup-us]` |
| Genre / size | Education, 154 MB (153,985,024 bytes) | `[DATA:itunes-lookup-us]` |
| Positioning | "Identify Plants & Diseases"; widens to insects, birds, mushrooms, "Chat AI Botanist", "Plant Decorator" | `[OBSERVED #1, #4, #5, #13]` |
| Ganesh's row | Onboarding 4; paywall "Early Dismissible Wall"; free = "Basic plant search and static care guide overview"; paid = "Automated watering calendar, disease scanner, photo identification history"; offer "₹1,499/yr (3-day trial) or ₹499/mo" | `[DATA:ganesh-benchmark-xlsx]` |

**I disagree with Ganesh's row on three points:**
- **Onboarding length.** The xlsx says 4 screens. The screens show 6 promo/permission cards plus 4 quiz questions, so 10 screens before the paywall `[OBSERVED #1–#11]`.
- **Price.** The xlsx says ₹1,499/yr or ₹499/mo with a 3-day trial. The screen shows "7 days free, then just ₹ 699/wk" and "Annual ₹ 3,999/yr" `[OBSERVED #12]`.
- **Trial length.** 3 days in the xlsx, 7 days on screen.

Possible causes: A/B test, price change, or the xlsx was filled from the listing `[UNKNOWN]`.

## A2 Business performance
Not in this run (screens-only).

## A3 Monetization (from screens)

- **Placement:** after 6 cards, a location request and a 4-question quiz, and before any ID (#12). `[OBSERVED]`
- **Plans (India):** the first plan card is labelled "**Free** · 7 Days" and is **preselected**; next to it is "Annual ₹ 3,999/yr". The line under the cards reads "7 days free, then just ₹ 699/wk", and the CTA is "Continue with free trial". `[OBSERVED #12]` The "Free" plan appears to be a ₹699/week subscription with a trial, since the ₹699/wk line sits under the preselected "Free" card `[INFERRED]`. Calling it "Free" is the most misleading plan label in the set `[INFERRED]`. ₹699 × 52 = ₹36,348 a year vs ₹3,999 on the annual plan `[INFERRED: arithmetic]`.
- **Bullets:** "Try Premium free for 7 days", "No commitment, cancel anytime you want", "Save your plants with instant diagnosis", "Access expert care tips & plant guides". `[OBSERVED #12]`
- **Close:** a grey text link "Cancel" in the footer row with "Restore Purchases" and "Terms". It looks like a legal link. There is no X. `[OBSERVED #12]`
- **Trial reminder:** none visible. `[OBSERVED #12]`
- **Proof on the paywall:** "4.8 ★★★★★", "Featured in 20+ countries". The US listing shows 4.66 `[DATA:itunes-lookup-us]`.
- **Other touchpoints:** none captured on home (#13) `[OBSERVED]`; later touchpoints are `[UNKNOWN]`.

## A4 Acquisition
Not in this run (screens-only).

## A5 Product teardown (screens lens)

### Journey and gaps
IMG_2186 to IMG_2198, 2:43 to 2:44, in order. #6 (IMG_2191) repeats #5 dimmed. The status bar is dimmed too, which is consistent with a system alert being on screen (notification or tracking prompt) `[INFERRED]`; the alert itself was not captured. Location was granted after #7 (location arrow from #8).

**Gaps:**
- **No identification at all was captured**, demo or real.
- No result screen.
- No care, diagnosis, AI chat or settings/subscription screens.

This is the biggest screenshot gap for a shortlisted app.

### Per-screen table

| # | stage | what user sees | asks of user | gives to user | verbatim copy | lever | friction / dark pattern | tag |
|---|---|---|---|---|---|---|---|---|
| 1 | onboarding 1/6 | orchid scan mockup | Continue | promise | "Identify Plants & Diseases" "Snap a photo to identify plants and get health assessments" "Moth Orchild" "Phalaenopsis" | curiosity | typo "Orchild" | `[OBSERVED]` |
| 2 | onboarding 2/6 | care card mockup | Continue | promise | "Plant Care Guides" "Use the extensive plant directory" "Water" "Light" "Temp" "Diffuculty" "Poison" | competence | typo "Diffuculty" | `[OBSERVED]` |
| 3 | onboarding 3/6 | lock-screen task list | Continue | promise | "Care Reminder" "Get care schedules and set tasks" "Water" "Fertilize" "Rotate" | relief | none | `[OBSERVED]` |
| 4 | onboarding 4/6 | butterfly scan | Continue | scope expansion | "Explore Nature" "Identify butterflies, moths, and spiders" | novelty | widens the job beyond plants | `[OBSERVED]` |
| 5 | onboarding 5/6 | chat mockup | Continue | promise | "Chat AI Botanist" "Try our advanced AI plant chatbot" | authority | none | `[OBSERVED]` |
| 6 | system prompt (inferred) | #5 dimmed | respond to an uncaptured system alert | nothing | n/a | n/a | permission asked with zero value delivered | `[OBSERVED]` `[INFERRED]` |
| 7 | permission 6/6 | map illustration | Continue → location prompt | nothing | "Enable Location Access" "To deliver accurate weather updates, we need your permission to access your location." | reason given | location for weather, not for the job | `[OBSERVED]` |
| 8 | quiz 1/4 | 7 goal options | pick ≥1 | nothing | "Your Goals" "What do you want to achieve with Plantiary?" "Smart plant care routine" "Diagnose plant diseases" "Identify unknown plants" "Identify wild mushroom" "Identify insect and bugs" "Identify birds" "Style spaces with plants" | investment | Continue disabled until answered | `[OBSERVED]` |
| 9 | quiz 2/4 | 3 options | pick | nothing | "Environment" "Where do you keep your plants?" "Indoor" "Outdoor" "Indoor & Outdoor" | investment | same | `[OBSERVED]` |
| 10 | quiz 3/4 | 4 options | pick | nothing | "Skill Level" "Do you have a green thumb?" "Struggling" "Beginner" "Experienced" "Gardener" | identity | same | `[OBSERVED]` |
| 11 | quiz 4/4 | 3 options | pick | nothing | "Commitment Level" "How much time do you want to spend on your plants?" "Low" "Medium" "High" | investment | answers never visibly used before the paywall | `[OBSERVED]` |
| 12 | paywall | proof hero, bullets, 2 plan cards | pay or find "Cancel" | nothing | "Unlock Premium" "Try Premium free for 7 days" "No commitment, cancel anytime you want" "Save your plants with instant diagnosis" "Free 7 Days" "Annual ₹ 3,999/yr" "7 days free, then just ₹ 699/wk" "Continue with free trial" "Restore Purchases" "Terms" "Cancel" | free framing, proof | weekly plan labelled "Free" and preselected; close disguised as a footer link; no reminder; "then **just** ₹699/wk" | `[OBSERVED]` |
| 13 | home | weather, carousels, multi-domain ID grid, tools | pick one of many entry points | menu | "Broken clouds, 33°C" "Search Plants" "Foliage Plants" "Pet-friendly Plants" "Explore Nature" "Identify Insects" "Identify Plants" "Identify Birds" (New) "Identify Mushroom" "Plantiary Tools" "Plant Decorator" (New) "Preview plants indoors or outdoors" "Disease Diagnosis" "Ask AI Botanist" tabs "Home · Explore · Community · My Garden" | breadth | plants are 1 of 4 ID targets; 4 tabs + camera; no first-ID guidance | `[OBSERVED]` |

### 8 measures

1. **First win.** **Not reached in 13 screens.** At least 12 taps are spent before home (#1–#12) `[OBSERVED]`. The first ID is entirely after the paywall `[OBSERVED]`; its tap count is `[UNKNOWN]`.
2. **Ask ledger.**
   1. Uncaptured system prompt (#6). Received so far: 5 promo cards.
   2. Location (#7). Received so far: nothing.
   3. Goals (#8). Received so far: nothing.
   4. Environment (#9). Received so far: nothing.
   5. Skill (#10). Received so far: nothing.
   6. Commitment (#11). Received so far: nothing.
   7. Paywall (#12). Received so far: nothing.

   **Seven asks with nothing given back**, the clearest "run of asks" in the set `[OBSERVED]`. The quiz answers are never reflected back as a plan before the paywall (no "your plan is ready" screen captured), so the investment is not paid off `[OBSERVED]`/`[INFERRED]`.
3. **Abstractions.**
   - Goals, Environment, Skill Level and Commitment Level are four profile dimensions the ID job doesn't need.
   - Insects, birds and mushrooms are invented scope.
   - "Plant Decorator" is invented.
   - "Community" is invented for this job.
   - "AI Botanist" is optional.
   - "My Garden" is needed.
   - "Explore Nature" vs "Plantiary Tools" are two groupings.
4. **Feel-good moments.**
   - The "Care Reminder" checklist (#3) is manufactured, a mockup.
   - "Do you have a green thumb?" (#10) invites identity, but nothing reflects it back.
   - No earned moment is captured.
5. **Feel-bad moments.**
   - "Struggling" with a wilted-rose emoji as a skill option (#10) is mild shame.
   - The "Free" label on a ₹699/wk plan (#12).
   - The disguised Cancel (#12).
   - Two typos in onboarding (#1, #2).
   - Location requested for weather before any ID (#7).
6. **Paywall.** Soft but disguised, before any ID. The "Free 7 Days" weekly plan is preselected vs annual ₹3,999. No reminder and no billing date shown.
7. **Repeat cost.** Camera button, then shutter, probably 2 taps `[OBSERVED #13]`/`[INFERRED]`. But the home screen splits attention across 4 ID targets and several tools. Return hooks: care reminders (#3), weather (#13), community (#13).
8. **Feature map.**
   - Table stakes: plant ID, care guide, reminders, My Garden.
   - Differentiators: multi-domain ID (insects, birds, mushrooms), AI Botanist chat, Plant Decorator (AR-style preview, `[INFERRED]` from "Preview plants indoors or outdoors").
   - Bloat: everything not about the user's own plants, plus the 4-question quiz.

## Keep / Kill / Different

**Keep**
- **The location rationale copy pattern (#7).** It says why before asking. Even so, we won't ask for location at all.
- **The "Care Reminder" task-list visual (#3).** Water / Fertilize / Rotate with check states is a good picture of the daily loop.

**Kill**
- The 4-question quiz with no payoff (#8–#11).
- The location ask before value (#7).
- The "Free" label on a weekly plan (#12).
- The footer-link Cancel (#12).
- The "Struggling" option with a wilted emoji (#10).
- Insects, birds, mushrooms and Decorator scope creep (#4, #13).
- The Community tab (#13).

**Different**
- No quiz. Profile the user from what they photograph: indoor/outdoor and plant types are visible in the photo `[INFERRED]`.
- One job: the user's plants. Plan names say exactly what they cost ("Yearly ₹X / $X").
- Close is an X, visible from 0 s.

## A6 Failure mining
Not in this run (screens-only). Ganesh's xlsx quotes, undated and truncated:
- 1★ "$10 a week is crazy … They consistently try to trick you into signing up for the premium version so you get wrapped into paying $10 a week or $520 a year"
- 1★ "Deceitful Deceptive Money Grab"

`[DATA:ganesh-benchmark-xlsx]` The weekly pricing seen on #12 is consistent with the "$10 a week" complaint; the actual US weekly price is `[UNKNOWN]`.

## A7 Tech & ops
Not in this run (screens-only).

## A8 Verdict (short)

Plantiary is the cautionary tale: the most asks (7), the widest scope (plants, insects, birds, mushrooms, decor, chat, community), and the most deceptive plan label ("Free" = ₹699/wk). It also has the oldest update in the set (2026-08-05). No identification was captured, so the core product cannot be judged from these screens.

**Copy:** the location rationale wording pattern, the task-list visual.
**Beat:** the quiz, scope creep, the disguised paywall.
**Most exploitable weakness:** "Free 7 Days" that silently becomes weekly billing. The xlsx's "$10 a week is crazy" review shows the anger is real.

Evidence strength:
- A1 medium
- A3 strong for this capture (conflicts with the xlsx)
- A5 weak (no ID, result, care or diagnosis)
- A8 weak to medium
