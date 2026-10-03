# Stage 0 — Category lens

Run once per category, before anyone does stage A. Output: `members/<member>/drafts/<cat>/lens.md` (admin promotes to `research/categories/<cat>/lens.md`; until then stage A reads the draft).

Inputs: the category's `overview.md` if it exists (e.g. the storage-cleaner report), web research, App Store top charts for the category (web search "top free/grossing <category> apps US App Store", public chart pages).

Write `lens.md` with:

1. **The user problem** — in plain words, in the users' language (pull phrases from review titles/Reddit). Personas (2–3), the trigger moment that makes them open an app, frequency of need (one-off vs recurring). Verdict: does the need justify a subscription honestly, or is it a one-time-purchase/ad category?
2. **Teardown questions** — 15–20 category-specific questions every stage-A note must answer. Mix: onboarding promise, permissions and how they're framed, time-to-first-value, free quota before paywall, what's paywalled that users expect free, trust/safety anxieties unique to the category, retention hooks, iOS API limits. (Example for storage cleaners: how duplicates are shown and confirmed; delete safety/undo; scan-progress UI; photo-permission framing; "storage full" fear messaging.)
3. **Complaint taxonomy** — the seven default clusters (billing/trial traps · ads & upsell spam · bugs/crashes/data loss · missing or over-paywalled features · performance/battery/storage · privacy/trust · support/UX) plus 3–5 category-specific clusters you expect. Stage A uses this exact list so counts are comparable across apps.
4. **Keyword universe** — 30 seed search terms users type for this category, grouped by intent; note which look high-volume vs niche `[INFERRED]` unless sourced.
5. **Platform & guideline risks** — App Store Review Guidelines and iOS API limits that bite this category (e.g. subscription disclosure rules, health claims, background processing, photo/contacts access).
6. **Apps to cover** — target 20: top 10 by revenue/chart rank, 5 by downloads, 3 fast-growing new entrants (launched ≤24 months), 2 indie/underdogs. For each: name, App Store id, why included, price model. Assign in groups of 4 per member, no overlaps.

Close with open questions and the next stage (A, per assigned app).
