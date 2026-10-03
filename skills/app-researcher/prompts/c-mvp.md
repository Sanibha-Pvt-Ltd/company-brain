# Stage C — MVP recommendation

You are head of product. Decide Sanibha's MVP for the category. Output: `members/<member>/drafts/<cat>/mvp.md` with `status: draft`. Admin promotes to `research/categories/<cat>/mvp.md` after team review.

Inputs: `overview.md`, `lens.md`, `market.md`, every app note. Every recommendation cites its evidence (note + section or review quote). Single-source evidence is flagged `⚠ single-source`.

Write `mvp.md`:

1. **Positioning** — one sentence; target persona; the promise on our first screen; why we win against the current leaders.
2. **Problems we solve** — ranked by evidence strength, in user words.
3. **Feature matrix** — features × competitors (✓ / ✗ / paid).
4. **MUST-HAVE (table stakes)** — present in most competitors, or absent = 1-star reviews. Each: why, evidence, simplest acceptable version.
5. **DIFFERENTIATORS (max 3)** — drawn from the cross-app failure matrix. Each: the bet, evidence, success metric, how fast incumbents could copy it.
6. **SKIP for MVP** — tempting but weak evidence or high cost. Say why.
7. **Flow** — first launch → onboarding → permission → first value → paywall → core loop → retention hook, as a screen list with the purpose of each screen. Value before paywall unless evidence says otherwise.
8. **Monetization** — products, prices, trial, paywall placement, two paywall variants to test; benchmarked against `market.md`. Include the "trust pledges" the 1–2★ analysis supports (e.g. no surprise charges, no ads).
9. **Growth** — ASO (name candidates, subtitle, 10 keywords), screenshot story, first 3 ad angles to test (from 5★ language and complaint inversions), organic channels.
10. **Targets** — realistic month-3 and month-12 downloads/revenue anchored to comparable new entrants; metrics to watch (D1, trial-start %, trial→paid %).
11. **Risks** — App Store guidelines, privacy permissions, iOS API limits, trust, competitor response.
12. **Scope check** — buildable by our team in ~6 weeks? If not, cut and rank; list what moves to v1.1.
13. **Open questions** — and which research would change the decision; which apps need more data.

Do not mark `status: final` — that happens only after team review and Bharat's sign-off (record with `log_decision`).
