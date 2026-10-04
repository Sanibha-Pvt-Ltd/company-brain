---
type: app
category: calorie-tracker
app: "BitePal: Food Calorie Tracker"
app_store_id: 6479529917
member: ganesh
run_by: harshil
updated: 2026-10-04
status: draft
scope: screens-only
screens_analysed: 48
reviews_analysed: 0
sources: [screenshots:48 (IMG_1771–1818, India storefront), itunes-lookup-us, ganesh-benchmark-xlsx]
---

# BitePal: screens-only teardown

Related: [[members/ganesh/drafts/calorie-tracker/screens-synthesis]]

**Capture caveat.** The capture covers launch, onboarding, paywall, downsell, account and an empty home. No meal is logged, so there is no AI result and no correction. Screens 1783–1788 show back-and-forth navigation: the reminder and tone screens appear twice, and 1786 (the unselected tone picker) logically comes before 1783 (tone selected). The journey below is in content order.

## A1 Snapshot (US, short)

| Field | Value | Tag |
|---|---|---|
| Developer | Reface Lithuania UAB | [DATA:itunes-lookup-us 2026-10-04] |
| US rating | 4.66 from 55,700 ratings | [DATA:itunes-lookup-us] |
| First release / latest | 2024-06-10 / v2.33.0 on 2026-09-28 | [DATA:itunes-lookup-us] |
| Age rating | 4+ | [DATA:itunes-lookup-us] |
| Positioning | "Reach your weight goals" / "With Cute raccoon": a calorie tracker wrapped around a virtual pet | [OBSERVED 1771] |

- **A2 Business performance:** not in this run (screens-only).
- **A4 Acquisition:** not in this run (screens-only).
- **A6 Failure mining:** not in this run (screens-only).

## A3 Monetization (from screens, India storefront ₹)

- **Paywall 1 (1813):** comes after the plan reveal. It has a visible X and Restore.
  - Annual "Best deal -50% off", ~~₹6,998.99~~ → ₹3,499.00, shown as **₹291.58 / per month**. Pre-selected.
  - Weekly "Pay-as-you-go" at ₹399.00.
  - Button: "Claim 50% off now". Footer: "Secure payment. Cancel anytime."
  - **No trial is shown.**
- **Gift interstitial (1814):** "We have a gift! Just for you!" with an "Open now" button.
- **Downsell (1815):** "Limited time -60% offer", with a **countdown "Offer expire in: 59:59"**. ~~₹478.95~~ → **₹191.58 per month**. Footer: "First year ₹2,299.00, then ₹5,900.00/year. Cancel anytime."
- **Anchor inconsistency:**
  - The strike-through on 1813 implies ₹6,998.99 a year. The renewal on 1815 is ₹5,900/yr.
  - The 1815 strike-through, ₹478.95/mo, works out to about ₹5,747/yr.
  - So the three "full prices" do not agree [INFERRED from OBSERVED numbers].
- **Disagreement with Ganesh's notes:** the xlsx records "₹2,499/yr (3-day trial) or ₹499/mo" [DATA:ganesh-benchmark-xlsx]. The screens show ₹3,499/yr or ₹399/week with no trial, and a ₹2,299 first-year downsell. Prices may be A/B tested or may have changed. The screens are the primary source.
- **Free-tier gating on home (1818):** the Carbs, Fats and Proteins bars are each shown with a 🔒. There is a "BitePal Plus 🔒" badge at the left edge. The xlsx says "Unlimited AI food photo recognition" is paid [DATA:ganesh-benchmark-xlsx]. The free scan allowance is `[UNKNOWN]`.
- **US price:** `[UNKNOWN]`.

## A5 Screens lens

### Journey

| # | stage | what user sees | asks | gives | verbatim copy | lever | friction / dark pattern | tag |
|---|---|---|---|---|---|---|---|---|
| 1771 | first-launch | raccoon, a bowl at 310 kcal, a 16:8 badge | Get started | the promise | "Reach your weight goals" / "With Cute raccoon" | cuteness | none | [OBSERVED] |
| 1772 | onboarding | goal | lose/maintain/gain | — | "What is your main goal?" | — | — | [OBSERVED] |
| 1773 | onboarding | multi-select | extra goals | — | "Any additional goals?" Build healthy relationship with food; … Feel better about myself | identity | none; it offers "No additional goals" | [OBSERVED] |
| 1774 | claim | stat card | Next | a claim | "58% BitePal users consistently maintain their weight over 6 months" | social proof | no source | [OBSERVED] |
| 1775 | onboarding | experience | pick | — | "Have you tried calorie counting before?" I'm new / I've tried it before but quit / I'm currently counting | empathy ("quit" is normalised) | none | [OBSERVED] |
| 1776 | explainer | 3 features | Let's go | an explanation | "Just take a photo of your food" / "Get support from your virtual pet" | — | none | [OBSERVED] |
| 1777 | onboarding | yes/no | IF knowledge | — | "Do you know about intermittent fasting?" | — | scope creep: fasting enters a calorie app | [OBSERVED] |
| 1778 | explainer | fasting claims | Continue | education | "The New England Journal of Medicine reports that intermittent fasting may support brain health and even promote a longer, healthier life." | authority | health claim with "Source of recommendations" link; mild | [OBSERVED] |
| 1779 | pet reveal | trash can | Open | curiosity | "Open to see who is there" | surprise | none; a delightful beat | [OBSERVED] |
| 1780 | pet reveal | raccoon | Next | **a companion** | "This raccoon is now your virtual pet" | attachment | none | [OBSERVED] |
| 1781 | onboarding | name the pet (field shows "Wasabi"; dice randomiser button) | typed name | ownership | "Name your raccoon" | IKEA effect | typing ask, offset by the dice | [OBSERVED] |
| 1782 | onboarding | user's name | typed name | — | "Wasabi! I like it. And what's your name?" | warmth | typing ask | [OBSERVED] |
| 1786 | onboarding | tone picker | pick tone | **control over voice** | "How should I talk to you?" Cheerleader / Gentle & kind / Straight talker / Mindful guide | care | none; **best screen in the category** | [OBSERVED] |
| 1783 | onboarding | tone preview ("Gentle & kind") | — | a preview | "You showed up again today. That's the whole thing." | care, forgiveness | none | [OBSERVED] |
| 1785 / 1788 / 1784 | onboarding | reminder timing ("In the morning" ticked in 1784/1785, nothing ticked in 1788; whether it is a default is [UNKNOWN]) | pick times | — | "When would you like to receive reminders" / "Reminders build healthy eating habits 2x faster" | — | the "2x faster" claim has no source; "Set up later" is offered | [OBSERVED] |
| 1787 | permission (pre) | mock notification with ❤️🤍🤍🤍 "(1 left)" | Set up reminders | — | "We'll support you to keep logging" / "Don't forget to snap your meal 📸" | **loss aversion via pet hearts** | **guilt mechanic**: the mock shows 1 of 4 hearts left; that hearts drain when you don't log is [INFERRED] | [OBSERVED; mechanic INFERRED] |
| 1789 | interstitial | — | Let's go | — | "Now let's talk about your eating habits" | — | the user has already answered 9 asks (1772, 1773, 1775, 1777, 1781, 1782, 1786, 1784/5, 1787) | [OBSERVED] |
| 1790 | onboarding | meals per day | number | — | "How many meals per day do you usually have?" | — | — | [OBSERVED] |
| 1791 | onboarding | eating window | time range | an insight | "Eating window: 10 hours  Eating within an 8–10 hour window may support overall health." | — | — | [OBSERVED] |
| 1792 | upsell (concept) | fasting goal | try fasting / skip | a reframe | "You're already fasting for 14h" / "We've set your goal to match your rhythm and support faster results." | **flattering reframe** (an overnight gap renamed "fasting") | **ED flag**: nudges a restriction concept; "Skip for now" exists | [OBSERVED] |
| 1793 | onboarding | where you eat | pick | — | "Where do you usually eat?" | — | — | [OBSERVED] |
| 1794 | onboarding | diet type | pick | — | "What type of diet do you prefer?" … Ketogenic … | — | — | [OBSERVED] |
| 1795 | onboarding | restrictions chips | multi | — | "Do you have any food restrictions or allergies?" / "I eat everything" | — | good one-tap escape | [OBSERVED] |
| 1796–1797 | onboarding | water | yes/no/not sure | an education card | "Water boosts fat burn, energy, and focus" | — | the "fat burn" claim | [OBSERVED] |
| 1798 | disclaimer | sheet | Got it! | honesty | "our app is not a substitute for professional medical advice" | trust | none | [OBSERVED] |
| 1799 | onboarding | habits to change | multi | — | "What would you like to change in your eating habits?" … **Stop binge eating** … Stop stress overeating | — | **ED flag**: binge eating as a checkbox, with no follow-up or resource on screen | [OBSERVED] |
| 1800 | interstitial | — | Set up your goal | — | "Got it! We'll help you to reach your goals" | — | — | [OBSERVED] |
| 1801–1803 | onboarding | gender, age, activity | 3 asks | — | "What's your activity level?" Not active "I quickly lose my breath climbing stairs" | — | — | [OBSERVED] |
| 1804 | permission (pre) | Health | Connect / manual | a privacy promise | "We never use your health data for ads or sale" / "I'll add activities manually" | trust | none; a good escape plus a privacy line | [OBSERVED] |
| 1805 | onboarding | activity calories | Smart mode (Recommended) / All calories | — | "Only calories burned above your usual level add to your budget" | — | concept: exercise calories | [OBSERVED] |
| 1806–1807 | onboarding | height 160 cm, weight 60 kg, live BMI | 2 asks | **BMI feedback** | "Your BMI: 23.4 Healthy  You're in a healthy range. Let's focus on what matters most to you." | reassurance | none at a healthy BMI; behaviour at other BMIs `[UNKNOWN]` | [OBSERVED] |
| 1808 | result | personal summary: BMI bar (Underweight…Obese), activity, diet, metabolism | Next | **first personal output** | "You're right where you need to be!" / "Metabolism: Balanced: needs steady habits to see change" | identity | "Obese" label on the scale; "Metabolism" is an invented read-out | [OBSERVED] |
| 1809–1810 | onboarding | target weight 60 kg | 1 ask | validation | "Maintaining 60 kg is a realistic target" | reassurance | none | [OBSERVED] |
| 1811 | loading | 52% bar, 4 steps, "Loved by 10M+ users" | wait | — | "Personalizing your plan" | labour illusion | manufactured progress | [OBSERVED] |
| 1812 | result | plan: flat projection, **2,376 kcal**, macros C 59 g / F 195 g / P 95 g (digits partly hidden behind the button) | Commit to my goal | **the plan, before the paywall** | "Your personal plan is ready" / "You'll maintain your weight effortlessly" | commitment | "effortlessly" overpromises | [OBSERVED] |
| 1813 | paywall | annual vs weekly | pay | — | "Track calories" / "Claim 50% off now" | anchor, -50% | visible X; no trial | [OBSERVED] |
| 1814 | downsell | gift box | Open now | — | "We have a gift! Just for you!" | surprise | gamified discount | [OBSERVED] |
| 1815 | downsell | -60% card with 59:59 timer | Claim | — | "Limited time -60% offer" / "Offer expire in: 59:59" | **false urgency** | countdown timer; the renewal is ₹5,900/yr in small grey text | [OBSERVED] |
| 1816 | account | Apple / Google | sign in | — | "Now let's create account" / "Save your progress & reach your goals" | — | no skip visible | [OBSERVED] |
| 1817 | home overlay | "Feed Wasabi" | log last meal | — | "What did you eat last?" / "I'll do it later" | **pet-feeding = logging** | none; a good first-log prompt with camera, +, gallery | [OBSERVED] |
| 1818 | home | pet with 4 hearts, streak 0, shop, Calories eaten 0, macros 🔒, "Calories left to burn Goal: 475 kcal" | — | — | "Goal: 2,376 kcal" | streak, pet, shop | **macros locked**; an exercise "burn" goal shown by default | [OBSERVED] |

### The 8 measures

1. **First win.** Not reached. 1817 offers a first log, but it was not completed in the capture. The first log prompt is the **47th captured screen** (this includes 2 repeated reminder screens from back-navigation), after the paywall, downsell and account [OBSERVED]; tap count [UNKNOWN]. The first *personal* output (BMI and summary, 1807–1808) arrives at captured screens 37–38 and **before** the paywall.
2. **Ask ledger.** **25 asks before the plan** (27 with payment and account): goal, extra goals, experience, IF, pet name, own name, tone, reminder times, notifications, meals/day, eating window, fasting, where you eat, diet, restrictions, water, habits, gender, age, activity, Health, activity mode, height, weight, target, then payment and account. The xlsx says "16 questions" [DATA:ganesh-benchmark-xlsx]. The screens show more; the xlsx likely counted only the question screens [INFERRED]. Received in return: a pet (screen 10), a tone choice, a BMI summary and the plan. **This is the longest quiz of the five, but it is the only one that pays back emotionally along the way** (pet, tone, gentle preview).
3. **Abstractions.** Calories (needed). Macros (needed, but locked). **Pet hearts** (invented). **Streak flame** (invented). **Shop** (invented). **Intermittent fasting / eating window** (not needed for the job). **Smart vs All activity calories** (invented). **"Calories left to burn" goal** (invented). **"Metabolism type"** (invented). That makes **6 invented concepts**, plus fasting, which is not needed for the job.
4. **Feel-good moments.**
   - Pet reveal (1779–1780): earned delight.
   - Tone choice with the preview "You showed up again today. That's the whole thing." (1783): earned, because the user chose it.
   - BMI reassurance (1807): earned for this user.
   - "I've tried it before but quit" as a normal answer (1775): earned.
   - "Personalizing your plan" (1811): manufactured.
5. **Feel-bad moments.**
   - Pet hearts draining, "(1 left)" (1787).
   - A 59:59 countdown (1815).
   - "Stop binge eating" as a checkbox with no care path (1799).
   - Fasting framed as already happening (1792).
   - A default exercise "burn" goal (1818).
   - Macros visibly locked after a 25-ask quiz (1818).
   - **ED note:** Ganesh's notes include a 5★ review from a user with an ED who values "there's no calorie count" [DATA:ganesh-benchmark-xlsx]. The captured home *does* show "Calories eaten". So a hide-calories mode may exist but is not visible here `[UNKNOWN]`.
6. **Paywall.** Soft, with an X, placed after the plan. **Two-step discount ladder**: -50%, then a gift box, then -60% with a timer. No trial. Anchors are inconsistent. A weekly plan is offered.
7. **Repeat cost.** The home has a + FAB and a camera prompt ("Feed Wasabi"). A log is likely FAB → camera → shutter → confirm, about 3–4 taps [INFERRED]. The return hooks are the pet's hearts, a streak, reminders and a shop.
8. **Feature map.**
   - Table stakes: photo log, calorie goal, Health sync.
   - Differentiators: the **pet and tone of voice** (why people choose it).
   - Bloat: fasting, the water education card, the shop, "metabolism type", the burn goal.

### Keep / Kill / Different

- **Keep:**
  - The tone picker and its preview line (1786, 1783). It is the only screen in the category that asks *how the user wants to be spoken to*.
  - "I've tried it before but quit" (1775).
  - "I eat everything" one-tap (1795).
  - The Health-data privacy line (1804).
  - The plan shown before the paywall (1812).
  - The "What did you eat last?" first-log prompt (1817).
- **Kill:** heart-drain guilt (1787); the countdown downsell (1815); fasting as an onboarding branch (1777–1778, 1791–1792); a binge-eating checkbox with no care response (1799); a default burn goal (1818); locked macros on home after a long quiz (1818); a quiz of 25 asks before the plan.
- **Different:**
  - Take BitePal's warmth: tone choice, "showing up is the whole thing". Drop its leverage: hearts that drain, timers.
  - Ask tone in **one** screen *after* the first log, not as one of 25.
  - If a user picks anything like "binge eating", turn calorie numbers to a soft view by default and show a resource link. Don't set a deficit goal.

## A8 Verdict (short)

BitePal proves emotion sells in this category. A 2024 entrant has 55,700 US ratings [DATA:itunes-lookup-us]; that the pet and tone of voice drive this is [INFERRED], not shown by any source here. But it bolts the emotion onto the longest quiz of the five, a discount ladder with a fake timer, and guilt hearts. It is "gentle" in copy and "pressure" in mechanics. **Most exploitable weakness:** the brand promise ("gentle & kind") contradicts the monetization (a 59:59 timer, hearts draining). An app that is gentle in *both* has no competitor in this set.

- **Copy:** tone choice; normalising quitting; plan before paywall; the first-log prompt.
- **Beat:** ask count; honest pricing; no guilt mechanics.
- **Evidence strength:** onboarding/paywall strong; core loop weak (no log captured); ED handling `[UNKNOWN]` beyond the onboarding copy.

## Verification (2026-10-04)

**Checked:** all 48 screenshots (IMG_1771–1818) opened; ~45 verbatim quotes, ~25 numbers/prices, 48 IMG refs and the back-and-forth order (status-bar clock confirms 1786 at 1:15 came after 1783 at 1:14), 6 [INFERRED] calculations (BMI 60/1.6² = 23.4; ₹291.58×12 = ₹3,498.96; ₹478.95×12 = ₹5,747.40; 6 pm→8 am = 14 h; macros 59×4+195×9+95×4 = 2,371 ≈ 2,376), 4 xlsx claims (H10 prices, G10 "Unlimited AI food photo recognition", E10 "16 questions", J10 ED review "there's no calorie count") and 5 US listing fields.

**Corrections:**
- 1774 button "Continue" → "Next"; 1776 button "Love It!" → "Let's go" ("Love It!" is a sticker).
- 1781 "typed 'Wasabi'" → field shows "Wasabi" (typed vs dice is not visible).
- 1784/1785 "pre-ticked" → "ticked"; 1788 shows nothing ticked.
- 1787 heart-drain mechanic → tagged [INFERRED] (only a mock notification is shown).
- 1789 "already answered 10+ asks" → 9.
- 1812 macro digits noted as partly hidden behind the button.
- "BitePal Plus 🔒 tab" → badge.
- First win: "about 46 screens / about 50+ taps [OBSERVED]" → 47th captured screen (incl. 2 repeats); taps [UNKNOWN]. "about screen 36" → screens 37–38.
- Ask ledger "about 26 asks before any value" → 25 asks before the plan (27 with payment and account); "before any value" contradicted the pet at screen 10.
- "7 invented concepts" → 6 plus fasting (not needed).
- Verdict: "pet and tone are why it reached 55.7K ratings" → causal link marked [INFERRED].

**Not verifiable:** whether reminder tick and tone are defaults; free scan allowance; hide-calories mode; US price.
