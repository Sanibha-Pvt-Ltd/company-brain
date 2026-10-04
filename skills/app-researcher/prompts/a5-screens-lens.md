# Screens lens — how to read app screenshots

Used by stage A, section A5, for every app with screenshots. The question for every screen: **does it move the user closer to feeling the benefit, or does it make them work for us?** We are not grading looks. We are finding where users feel good, where they pay a cost, and what we would do differently.

**Source rule: use only Sanibha's own screenshots** (captured in-app by the team). Do not use App Store listing screenshots, marketing images, web walkthroughs, or videos for the screen analysis. An app with no team screenshots gets no A5 teardown; write `[UNKNOWN] no team screenshots` and say what to capture.

## Per app: measure these 8 things

1. **First win.** The first moment the user *feels* the benefit: cleaner = "X GB freed"; calorie = first meal logged with numbers; plant = plant named; habit = first check-in done. Count screens and taps from launch to that moment. Is it before or after the paywall?
2. **Ask ledger.** Every ask in order: quiz question, typed input, permission, account, notification opt-in, rating prompt, payment. Next to each, write what the user had *received* by then. A run of asks with nothing given back is the main finding.
3. **Abstractions.** Every concept the user must learn before getting value: currencies, points, levels, "routines vs habits vs goals", "similar vs duplicate", macros, collections, modes. For each, say whether the job needs it or the app invented it. Every invented concept is a cost; our default is to remove it.
4. **Feel-good moments.** Relief, progress, celebration, care, identity ("you're the kind of person who…"). Is each one *earned* (it reflects real progress) or *manufactured* (fake loading bars, "analysing your profile…", "92% match")?
5. **Feel-bad moments.** Guilt (broken streak, a sad pet), fear copy ("your phone is at risk"), confusion, nagging, trickery: delayed or hidden close button, trial pre-toggled, weekly price shown as daily, a downsell after closing, "free" that isn't. Quote the exact copy.
6. **Paywall.** Placement, hard or soft, close-button delay, plans and how prices are framed, trial terms, downsell, and what the user saw *before* the price. Note prices as storefront-specific; ₹ prices are India, not US.
7. **Repeat cost.** After day 1: how many taps for the core action (log a meal, check in, scan a plant, clean again)? What brings the user back: notification, widget, streak, pet, report?
8. **Feature map.** Sort features into table stakes (must match), differentiators (why people choose it), and bloat (not needed for the job, adds screens or concepts).

Per-screen table (as in A5): `# | stage | what user sees | asks of user | gives to user | verbatim copy | lever | friction / dark pattern | tag`.

## Per app: output

- **Keep:** what genuinely makes users feel good; copy it.
- **Kill:** asks, abstractions, and dark patterns we will not ship, each with the screen number.
- **Different:** what we do instead. Make it concrete, e.g. "show freed GB before any paywall", not "better UX".

## Per category: synthesis (after all shortlisted apps)

1. A pattern table across the apps: first-win taps, number of asks before value, number of abstractions, paywall placement, repeat cost.
2. **Our first five minutes**, written screen by screen, with the fewest asks and abstractions that still monetize honestly.
3. **Up to 3 differentiating features**, each tied to evidence: a screen, a 1–2★ review cluster, or a gap no shortlisted app fills.
4. The concepts we refuse to add, with reasons.
5. Open questions that the screenshots cannot answer: send them to review mining or a hands-on test.

## Starting hypotheses (check them against screens; never assume)

These are `[INFERRED]` priors, written down so the analysis can confirm or kill them.

- **Storage cleaner:** value is visible within seconds (GB found). Winners show the problem before the paywall; the anger points are fear copy and hard paywalls after the scan. Our edge is probably an honest free tier plus showing freed space before payment.
- **Calorie tracker:** logging friction is the whole game. Photo logging (Cal AI) cut it; the next friction is correcting wrong estimates and repeat logging. Long quizzes may be "investment" or pure friction; measure whether the plan payoff justifies them.
- **Habit tracker:** concept bloat (habits, routines, goals, areas, points) and streak guilt drive churn. Finch wins on emotion, not mechanics. Our edge is probably fewer concepts, forgiveness instead of guilt, and a first check-in within 30 seconds.
- **Plant identifier:** identification is commoditised (PlantNet is free). Value moves to care and diagnosis, so a paywall before the first ID is the main anger point. Our edge is probably a free first ID with paid care and diagnosis.
