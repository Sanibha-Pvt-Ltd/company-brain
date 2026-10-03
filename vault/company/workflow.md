---
type: reference
updated: 2026-10-03
---

# Workflow: research to build

1. **Lens (stage 0)** — once per category. Defines the user problem, teardown questions, complaint taxonomy, keyword universe, and the ~20 apps to cover, split 4-per-person with no overlap. Run by Harshil or Bharat.
2. **App deep-dive (stage A)** — every member, per assigned app. Inputs: `negatives.md` + `listing.json` from `tools/fetch-app.py`, plus real screenshots/PDFs the member captured by hand. Output in the member's own folder.
3. **Market (stage B)** — one person per category, after most stage-A notes exist. Combines all members' notes into size, landscape, cross-app failure matrix, entry verdict.
4. **MVP (stage C)** — same person. Must-haves, differentiators (max 3), skips, flow, monetization, growth, targets, risks, 6-week scope check.
5. **Review** — the team reads the drafts; admin promotes them to `research/categories/<cat>/`. Bharat signs off → `status: final`, logged in [[logs/decisions]].
6. **Portfolio (stage E)** — after at least 3 categories reach step 5, rank all categories to choose build order.
7. **Build spec (stage D)** — for the chosen category/app: screens, stories, iOS notes, StoreKit products, analytics, launch checklist. Admin creates `projects/<app>.md`.
8. **Design and build** — hand-off to the UX/brand/iOS agents (planned) and the team. See [[company/agents]].

## Cadence

- Refresh review data weekly: rerun `fetch-app.py`; new reviews merge into the history.
- Log decisions as they happen (`log_decision`), not at the end.
- Every agent run ends with a summary, open questions, and "what would change the call".

## Roles

| Person | Does |
|---|---|
| Bharat | Signs off MVPs and category ranking; promotes drafts; business direction |
| Harshil | Brain/server/keys; promotes drafts; engineering decisions |
| Kushagra, Ganesh | Stage A on assigned apps; stage B/C when assigned a category |
