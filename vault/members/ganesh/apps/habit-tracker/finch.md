---
type: app
category: habit-tracker
app: "Finch: Self-Care Pet"
app_store_id: 1528595748
member: ganesh
run_by: harshil
updated: 2026-10-04
status: draft
scope: screens-only
screens_analysed: 35
reviews_analysed: 0
sources: [screenshots:35, ganesh-benchmark-xlsx, itunes-lookup-us]
---

# Finch: Self-Care Pet (category winner)

Screens: `ganesh_screenshots/Habit Trackers/Finch: Self-Care Pet/` IMG_1976–2011 (35 files; **IMG_2000 missing**). India storefront, captured on or about 2026-10-03 `[INFERRED: trial screen says "You will be charged on Oct 10" for a 7-day trial]`. Context: [[members/ganesh/drafts/habit-tracker/screens-synthesis]]

## A1 Snapshot (short)

| Field | Value |
|---|---|
| Developer | Finch Care Public Benefit Corporation `[DATA:itunes-lookup-us 2026-10-04]` |
| US price | Free with IAP `[DATA:itunes-lookup-us 2026-10-04]` |
| US rating | 4.95 from 759,175 ratings `[DATA:itunes-lookup-us 2026-10-04]` |
| Version | 3.73.220, released 2026-10-02. First release 2021-05-12. Genre Health & Fitness `[DATA:itunes-lookup-us]` |
| Lead promise | "Your new self-care best friend." `[OBSERVED #2]`. The listing opens with "Take care of your pet by taking care of yourself!" `[DATA:itunes-lookup-us description]` |

## A2 Business performance
Not in this run (screens-only).

## A3 Monetization (from screens)

- **Model on screen:** "Finch Plus", an annual plan with a 7-day free trial. "Unlimited free access for 7 days, then ~~₹699.00~~ ₹3,499 per year (save -401%)" `[OBSERVED #29]`. These are **India storefront** prices. The US price is `[UNKNOWN]`; a US-storefront capture would settle it.
- **Placement:** soft paywall. It comes after the 13-question quiz and the "Generating your self-care goals" loader, and before the home screen. It is a **4-screen sequence** (#26–#29), or 5 if the missing IMG_2000 belongs here: "Finch is free to use / But we'd love for you to try Finch Plus for 7 days free too!" (#26). Then "Free to cancel anytime / We'll send a reminder 2 days before your free trial ends" (#27). Then "One-time offer! / -401% OFF when you start your free trial now" (#28). Then the trial timeline (#29) `[OBSERVED]`.
- **Dismissability:** #29 has a text link, "Skip this one-time offer" `[OBSERVED]`. #26–#28 have only a "See my FREE offer" button. No close ✕ is visible on them, so the only way forward runs through the trial screen `[OBSERVED]`.
- **Price framing is broken:** the strike-through ₹699 is *lower* than the real ₹3,499, and the copy claims "save -401%". The struck price is probably a monthly price mislabelled as a discount `[INFERRED]`. A negative-percent "discount" is nonsense, and US users would read it as a trick `[INFERRED]`.
- **Pressure copy:** "Offer expires when you exit this screen!" and "Biggest discount ever—just for you & Rainbow" `[OBSERVED #28–#29]`.
- **Honest part (keep):** a trial timeline with "Today / Day 5 / Day 7" and an explicit charge date ("You will be charged on Oct 10, cancel anytime before") `[OBSERVED #29]`.
- **Disagreement with Ganesh's xlsx:** the xlsx says "₹3,499/yr with 3-day free trial" and "After Mental Health Quiz (27 questions)" `[DATA:ganesh-benchmark-xlsx]`. The screens show a **7-day** trial (#26, #29) and **13 quiz questions** after the 4 pet-setup screens. The xlsx's 29 onboarding screens are close to our ~31 pre-home screens. Ganesh, please correct the trial length.

## A4 Acquisition
Not in this run (screens-only). One on-screen data point: the attribution survey "How did you hear about Finch?" lists Facebook/Instagram first, then Podcasts/Spotify, Google, TikTok, Games, App Store, Friends/family, News, YouTube and Therapist/medical professional `[OBSERVED #30]`. The "Games" and "Therapist" options hint at channels Finch buys or earns `[INFERRED]`.

## A5 Screens lens

### Per-screen table (capture order = journey order; IMG_2000 missing between #25 and #26)

| # | file | stage | what user sees | asks of user | gives to user | verbatim copy | lever | friction / dark pattern | tag |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 1976 | first-launch | splash, bird face | — | brand | "Finch" | — | — | [OBSERVED] |
| 2 | 1977 | first-launch | bird, two buttons | tap | promise | "Your new self-care best friend." "Hatch a new pet" / "Login" | curiosity, care | none; no account wall | [OBSERVED] |
| 3 | 1978 | onboarding | 6 coloured eggs around a bird | pick egg colour | choice, ownership | "Choose your Finch Egg! Finches are lively, social, and inquisitive." | IKEA effect | — | [OBSERVED] |
| 4 | 1979 | onboarding | egg cracking | — | anticipation | — | delight | — | [OBSERVED] |
| 5 | 1980 | onboarding | hatched bird, pronoun picker | pronouns | a pet | "You hatched a birb! Your birb's pronouns" | identity, attachment | — | [OBSERVED] |
| 6 | 1981 | onboarding | name field prefilled "Rainbow" | name (optional edit) | pet named | "What do you want to name your baby birb? You can change this later." "Shuffle" | ownership | low friction: prefilled + shuffle | [OBSERVED] |
| 7 | 1982 | onboarding | trait picker | pick trait | pet personality | "Choose a trait for Rainbow / Rainbow cares about… Curiosity / Resilience / Compassion / Logic" | identity projection | invented concept (traits) | [OBSERVED] |
| — | gap | onboarding | user's own name entry not captured; #8 greets "T" | user name | — | — | — | — | [INFERRED] |
| 8 | 1983 | onboarding | pet asks a question, 2 answers | pick a definition | framing | "Nice to meet you, T! They call me a self-care pet. What is self-care?" / "Self-care means doing what you can, even when you're not feeling your best." | reframing, low bar | — | [OBSERVED] |
| 9 | 1984 | onboarding | pet hugs heart, stat toast | — | reward | "Wow! When you take care of yourself, you take care of me, too! Let's do it together, cheep!" "Rainbow gained +5.6 Compassion" | reciprocity, variable reward | **manufactured** stat for answering a quiz | [OBSERVED] |
| 10 | 1985 | permission | mock notification from pet | notifications | — | "Get reminders from Rainbow" "From Rainbow: Remember to drink water!" "Turn on notifications" / "Maybe later" | persona-voiced ask | fair: equal-weight "Maybe later" | [OBSERVED] |
| 11 | 1986 | onboarding | quiz intro | Next | — | "Let's learn a bit about you! Rainbow is curious about how she can grow with you." | ask framed as pet's need | — | [OBSERVED] |
| 12 | 1987 | quiz | 4-step progress bar "ABOUT YOU" | gender | — | "What's your gender?" + "Prefer not to answer" | — | skippable | [OBSERVED] |
| 13 | 1988 | quiz | — | used before? | — | "Have you used Finch before?" "No, this is my first time!" / "Yes, but I'm starting fresh" | — | — | [OBSERVED] |
| 14 | 1989 | quiz | "ENERGY & ACTIVITY" | sleep hours | — | "How long do you usually sleep at night?" | — | — | [OBSERVED] |
| 15 | 1990 | quiz | — | out of bed | — | "How easy is it for you to get out of bed?" | — | — | [OBSERVED] |
| 16 | 1991 | quiz | — | activity | — | "How active are you during the day?" incl. "I have conditions that limit my movement" | inclusive options | — | [OBSERVED] |
| 17 | 1992 | quiz | mid-transition "HOW'S LIFE"; question cut off | stress frequency | — | "How often do you feel o[verwhelmed]…" "I feel overwhelmed sev[eral times a] week" | — | capture caught the animation; full question not readable | [OBSERVED] |
| 18 | 1993 | quiz | — | support network | — | "How many people can you lean on for support in tough times?" "3 or more … Just me" | — | sensitive | [OBSERVED] |
| 19 | 1994 | quiz | — | routine satisfaction | — | "How happy are you with your current routine?" | — | — | [OBSERVED] |
| 20 | 1995 | quiz | "SUPPORT AREAS", list | mental-health conditions (multi) | — | "Do you struggle with any of these mental health challenges? Anxiety / ADHD / Bipolar Disorder / PTSD / OCD / Depression…" | relevance | **health-data ask before any value**; no visible "none" option in view `[UNKNOWN below fold]` | [OBSERVED] |
| 21 | 1996 | quiz | same, Anxiety ticked | Next | — | — | — | — | [OBSERVED] |
| 22 | 1997 | quiz | areas list | support areas (multi) | — | "What areas would you like support with? Build healthy eating habits / Be more active / Manage stress and anxiety / Self-acceptance and confidence / Appreciate the good things / Boost focus and productivity" | goal framing | — | [OBSERVED] |
| 23 | 1998 | quiz | eating ticked | Next | — | — | — | — | [OBSERVED] |
| 24 | 1999 | quiz | follow-up (branch from #23) | barriers (multi) | — | "What makes it hard for you to stick to healthy eating?" | personalisation | branching adds questions per area picked | [OBSERVED] |
| 25 | 2001 | loading | ring + review carousel | wait | social proof | "Generating your self-care goals with Rainbow…" "45 million+ people have chosen Finch" | labour illusion | **manufactured** loader | [OBSERVED] |
| — | 2000 | — | missing file | — | — | — | — | gap (likely another quiz or paywall screen) | [UNKNOWN] |
| 26 | 2002 | paywall 1/4 | pet + heart, laurels | tap | reassurance | "Finch is free to use / But we'd love for you to try Finch Plus for 7 days free too!" "Over 500K+ 5-star reviews worldwide" "See my FREE offer" | reciprocity, honesty | no ✕ visible | [OBSERVED] |
| 27 | 2003 | paywall 2/4 | pet with bell | tap | trust | "Free to cancel anytime / We'll send a reminder 2 days before your free trial ends" "Loved by 45M+ users" | trust | no ✕ visible | [OBSERVED] |
| 28 | 2004 | paywall 3/4 | pet in sunglasses | tap | "discount" | "One-time offer! -401% OFF when you start your free trial now" "Editors' Choice" "Biggest discount ever—just for you & Rainbow" | scarcity, pet guilt-by-association | **nonsense discount**, fake scarcity | [OBSERVED] |
| 29 | 2005 | paywall 4/4 | trial timeline | start trial or skip | clarity on billing | "Start your 7-day FREE trial" "Today / Day 5 / Day 7 … You will be charged on Oct 10" "~~₹699.00~~ ₹3,499 per year (save -401%)" "Skip this one-time offer" "Offer expires when you exit this screen!" | loss aversion | struck price < real price; urgency | [OBSERVED] |
| 30 | 2006 | survey | attribution list | source | — | "How did you hear about Finch?" | — | an ask after the paywall, before home | [OBSERVED] |
| 31 | 2007 | content | "DAY 1" story card | — | warmth | "Here's to the weekend!" "A GENTLE REMINDER / Our emotions make us human." | care, normalising | — | [OBSERVED] |
| 32 | 2008 | celebration | pet + big "1" | — | streak | "1 DAY STREAK" | progress | **manufactured**: no goal completed yet | [OBSERVED] |
| 33 | 2009 | celebration | week strip, Sat ticked | "Let's go!" | streak | "Great job! Open the app every day to maintain your self-care streak with Rainbow!" | consistency | streak = opening the app, not doing habits | [OBSERVED] |
| 34 | 2010 | commitment | 4 options | streak goal | — | "How many days in a row will you take care of Rainbow?" "2 days Baby steps / 5 days Strong start / 7 days Clearly committed / 14 days Unstoppable streak" "Commit to this goal!" "You got this, cheep!" | commitment device | framed as caring for the pet, so a miss = neglecting it `[INFERRED]` | [OBSERVED] |
| 35 | 2011 | core-task | forest scene, pet, goal list, tab bar | check a goal | 7 pre-filled micro-goals | "1st Adventure 0 / 15" "7 goals left for today!" "Start the day: Get out of bed / Brush teeth / Wash my face" (each "5" + reward icon + ✓) "Building habits is better together" tabs "Home / Quests / Shop / Friends / Bag / Rainbow" | ready-made plan, tiny wins | 6 tabs + currency on day 1 | [OBSERVED] |

### The 8 measures

1. **First win.** Two kinds. *Emotional* first win: the pet hatches at tap ~2 (#5), before any ask about the user `[OBSERVED]`. *Habit* first win: the first check-in **was not captured**. Home (#35) shows three one-tap goals ("Get out of bed", "Brush teeth", "Wash my face") with ✓ buttons, so the first check-in is 1 tap past home `[OBSERVED]`. Approximate taps from launch to first check-in: **≈38**, after the paywall `[INFERRED]`. Method: 1 tap per single-select screen, 2 per multi-select-plus-Next, plus ≥2 for the uncaptured name entry and the missing IMG_2000.
2. **Ask ledger.** Gives come first: an egg, a hatched pet and a name (#3–#6) before the first personal ask (#8). Then about **21 asks** come before any habit is done: pronouns, pet name, trait, user name, the self-care definition, notifications, gender, used before, sleep, getting out of bed, activity, stress, support network, routine satisfaction, **mental-health conditions**, support areas, eating barriers, 4 paywall screens, attribution, and the streak commitment `[OBSERVED]`. By then the user has received a pet, two pet-voiced compliments, a "+5.6 Compassion" toast, a loader and a streak they did not earn. They have **not** received a completed habit. The gives keep it from feeling like a form, but it is still a long run of asks.
3. **Abstractions** (all visible by #35): pet, egg, pronouns, trait, trait stats ("+5.6 Compassion"), self-care goals, time-of-day sections ("Start the day"), an "Adventure" progress bar (0/15), at least 3 reward-currency icons on the goals (orange, gummy bear, candy), streak, streak-goal commitment, Quests, Shop, Friends, Bag, and Finch Plus. That makes **≈15 concepts** `[OBSERVED]`. The job needs only goal + check-in + streak/history. Everything else is invented. **Crucially, none of these concepts must be understood to make the first check-in**: the ✓ button works without them `[INFERRED from #35 layout]`.
4. **Feel-good moments.** Earned: "When you take care of yourself, you take care of me, too!" (#9). It frames future care, and the reward is tied to real actions later `[OBSERVED]`. Normalising content: "Self-care means doing what you can, even when you're not feeling your best." (#8) and "Our emotions make us human." (#31). These lower the bar rather than raise it. Manufactured: "+5.6 Compassion" for answering a quiz question (#9), "Generating your self-care goals…" (#25), "1 DAY STREAK" before any goal is done (#32), and "-401% OFF" (#28).
5. **Feel-bad moments.** No guilt copy appears in the captured screens `[OBSERVED]`. The risk is structural. "How many days in a row will you take care of Rainbow?" (#34) ties a missed day to neglecting a creature the user named and loves `[INFERRED]`. Missed-day behaviour is **not captured** `[UNKNOWN]`. A hands-on day-2/day-3 capture is needed. The mental-health checklist (#20) is a sensitive ask before value. On the paywall: the nonsense discount, "Offer expires when you exit this screen!", and no ✕ on 3 of 4 screens.
6. **Paywall.** See A3: soft, 4 screens, pre-home, after the quiz; annual-only with a 7-day trial; the skip link is on the last screen only; the price framing is broken; the trial timeline is honest.
7. **Repeat cost.** 1 tap per goal (✓ on each row) `[OBSERVED #35]`. Return hooks: pet-voiced notifications (#10), the app-open streak (#33), the streak goal (#34), the Adventure bar (#35) and the daily story card (#31). Widgets were not seen `[UNKNOWN]`.
8. **Feature map.** Table stakes: goal list, one-tap check, reminders, streak. Differentiators: a pet that grows with self-care, pet-voiced copy, micro-goal defaults ("Get out of bed") and mental-health-aware onboarding. Bloat for the core job: traits/stats, the Adventure, multiple currencies, Shop and Bag, Quests, and an attribution survey before home.

**Why Finch's emotional model works.** Finch moves the reason to come back from *your* streak to *someone else's* wellbeing. The user cares for Rainbow, and caring for Rainbow happens to mean caring for themselves (#9). Three mechanics carry this:
- **Give before ask.** Finch hands over a pet in two taps, and every later ask is voiced as the pet's curiosity ("Rainbow is curious about how she can grow with you", #11).
- **A low bar.** Self-care is redefined as "doing what you can, even when you're not feeling your best" (#8), and the defaults are "Get out of bed" and "Brush teeth" (#35). Success is nearly guaranteed on day 1.
- **Diegetic concepts.** The currencies, Adventure and Shop are dressed as the pet's world rather than productivity jargon, so they read as play, not homework `[INFERRED]`.

Part of the emotion is manufactured: the stat toasts, the streak for opening the app and the loader. The part users would defend is earned. The pet reacts to things they actually did, and the copy never shames them in the captured screens.

## Keep / Kill / Different

**Keep**
- Give before ask: a companion or object in the first 2 taps (#3–#5).
- Micro-habit defaults that make the day-1 win nearly certain: "Get out of bed", "Brush teeth", "Wash my face" (#35).
- Reframing copy that lowers the bar: "doing what you can, even when you're not feeling your best" (#8).
- Persona-voiced notification ask with an equal-weight "Maybe later" (#10).
- The trial timeline with an explicit charge date (#29).

**Kill**
- "+5.6 Compassion" stats for answering a question (#9); traits (#7).
- "1 DAY STREAK" before any habit is done (#32–#33).
- The mental-health diagnosis checklist before value (#20).
- The 4-screen paywall without ✕, "-401% OFF", the struck price below the real price, and "Offer expires when you exit this screen!" (#26–#29).
- Attribution survey before home (#30).
- 6 tabs and ≥3 currencies on day 1 (#35).

**Different**
- One companion whose state changes **only** on real check-ins. No stats for answering questions and no streak for opening the app.
- First check-in on screen 2, not screen ~36: preselected micro-habit, tap ✓, the companion reacts.
- Missed day = the companion rests; it is never sad or hurt. No "days in a row" commitment contract.
- Any personal questions come **after** the first check-in, are optional, and each one visibly changes the plan.

## A6 Failure mining
Not in this run (screens-only).

## A8 Verdict (short)

Finch wins because it makes self-care feel like caring for someone else. It gives a pet before asking anything, sets the bar at "get out of bed", and wraps heavy game mechanics in a warm, non-judging world. It is not light. It is the most concept-heavy app in the set (≈15 concepts on day 1), and its onboarding runs about 38 taps with a manipulative paywall before the first check-in. **Copy:** give-first companion, micro-habit defaults, low-bar copy, trial timeline. **Beat:** time to first check-in, honest pricing, no manufactured rewards. **Most exploitable weakness:** the paywall's broken discount maths and urgency copy contradict the app's "gentle friend" brand. That is a trust gap a calm competitor can own.

Evidence strength: A1 strong (API) · A3 strong for India prices, US `[UNKNOWN]` · A5 medium (first check-in and missed-day not captured; IMG_2000 missing) · emotional-model reading medium `[INFERRED]`, to be validated by review mining.
