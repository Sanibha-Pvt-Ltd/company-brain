---
name: playbook
description: Sanibha App Creation Playbook — twelve stage agents (s0 to s11) that take one app from idea validation to finance and company operations. Use when asked to run, audit, or prepare a playbook stage for an app.
---

# Sanibha App Creation Playbook — stage agents

Source of truth: **Sanibha App Creation Playbook & Checklist**, v0.1, 5 Oct 2026, @Bharat (repo root PDF). Every checklist item in `stages/` is copied from it word for word. If the playbook and this skill disagree, the playbook wins; tell Harshil so the skill is fixed. Never add an item, number, benchmark or rule that is not in the playbook. When a new version of the playbook appears, the stage files are re-synced from it, not edited by hand.

## How you are invoked

`Use <stage agent>, app <app>[, member <name>][, mode audit|prepare]`

| Agent | Stage file | Stage |
|---|---|---|
| s0-validation | `stages/s0-validation.md` | Idea validation and go/no-go |
| s1-spec | `stages/s1-spec.md` | Product and UX spec |
| s2-standards | `stages/s2-standards.md` | In-app standards |
| s3-engineering | `stages/s3-engineering.md` | Engineering and architecture |
| s4-analytics | `stages/s4-analytics.md` | Analytics, attribution and measurement |
| s5-monetization | `stages/s5-monetization.md` | Monetization and pricing |
| s6-legal | `stages/s6-legal.md` | Legal and compliance |
| s7-submission | `stages/s7-submission.md` | App Store submission and ASO |
| s8-marketing | `stages/s8-marketing.md` | Marketing and growth |
| s9-launch | `stages/s9-launch.md` | Launch |
| s10-operations | `stages/s10-operations.md` | Post-launch operations |
| s11-finance | `stages/s11-finance.md` | Finance and company operations |

Coordinator: `playbook-orchestrator` (`orchestrator.md`) builds the per-app status board, enforces stage order and gates, and dispatches stage agents in parallel.

Read this file, then the stage file, then run it. App missing: ask once, then proceed. Mode missing: default `audit`.

- **audit** — walk every item in the stage, record its status with evidence, list what blocks the stage.
- **prepare** — draft the stage's deliverables (the "Produce" section of each stage file) for the founder or builder to review. Prepared drafts never tick a box by themselves.

## Playbook rules (verbatim)

- Every app passes the same twelve stages in order, and a stage is done only when every box is ticked and the founder has signed it off. Duplicate this doc once per app so progress never mixes between apps.
- **[GATE]** marks an item that blocks release until it is ticked.
- **[VERIFY]** marks an item whose rules change or depend on your situation. Check it against current Apple/Meta documentation, or with a lawyer or chartered accountant, before relying on it.
- Stages 1 to 6 can overlap. Nothing is submitted to Apple until Stages 0 to 7 are signed off.
- This is a shared spec, not shared code. Each app keeps its own codebase and backend, and every app must satisfy every [GATE] item here.
- Interns own the build items for their assigned apps. The founder owns validation, legal sign-off, pricing, marketing spend and the go/no-go call.

## Apps and builders (status as of 5 Oct 2026)

| App | Builder | Status as of 5 Oct 2026 |
|---|---|---|
| Fax | Kushagra | Mockup and handover spec done; build paused |
| Baby tracker | Kushagra | Mockup, spec and privacy requirements done; build paused |
| Sleep tracker | Kushagra | Not started |
| Universal TV remote | Kushagra | Not started |
| Storage cleaner | Ganesh | Not started |
| Calorie counter | Ganesh | Not started |
| Plant identifier | Ganesh | Not started |
| Habit tracker | Ganesh | Not started |
| AI resume builder | Harshil | Not started |
| Recipe importer | Harshil | Not started |
| Immigration case tracker | Harshil | Not started |
| Document scanner / PDF toolkit | Harshil | Not started |

Phase 0 internal tools (store-listing watcher, paywall tracker, review-mining agent, ad-tracking digest, design-system auditor, onboarding benchmarker) are due before any app coding starts. Several stages read their feeds. If a tool does not exist yet, say so and mark the dependent item `blocked: Phase 0 tool missing`.

## How to judge an item

Each item gets exactly one status:

| Status | Meaning | Needs |
|---|---|---|
| `done` | Ticked | Evidence: file path, link, screenshot, commit, App Store Connect page, or a logged decision |
| `open` | Not done, nothing blocks it | Next action and owner |
| `blocked` | Waits on something else | What it waits on (another item, a stage, a founder decision, a professional) |
| `n/a` | Does not apply to this app | One-line reason (e.g. "no account system", "no background work") |

- No evidence, no `done`. "The builder said so" is not evidence; a chat message from the builder is evidence only for what it states, quoted and dated.
- **Founder-owned items** (validation, legal sign-off, pricing, marketing spend, go/no-go, and any item that says "founder") are `done` only when the founder's decision is recorded in `logs/decisions` (via `log_decision`) or in the app's note with the founder named and a date. You may prepare the material; you never decide for the founder.
- **[VERIFY] items:** at run time open the current official page (Apple guideline, Apple developer docs, Meta business help, FTC/state source) and record the URL, the date you read it and what it says, quoted. If you cannot reach an official source, the item stays `open` with `VERIFY pending`. Items that need a lawyer or chartered accountant stay `blocked: needs <professional>` until their answer is recorded; never substitute your own reading of the law for theirs.
- A **[GATE]** item that is not `done` or `n/a` blocks release. List every open gate at the top of the output.
- Benchmarks quoted in the playbook (Adapty 2026, industry ATT opt-in, Meta thresholds, etc.) are the playbook's numbers. Repeat them exactly as written, with the playbook as source, and note that Appendix D asks for them to be checked against the current source and replaced by the app's own measured data once it exists.

## Evidence discipline

Inherits `skills/app-researcher/SKILL.md` (tags `[OBSERVED]`, `[DATA:<source>]`, `[REVIEW]`, `[ESTIMATE:<source>]`, `[INFERRED]`, `[UNKNOWN]`) and the binding accuracy rules in `rules/company.md`: no made-up data points; another agent's output is not evidence until traced to its source; re-open the source for every key number before final output. Every model figure is labeled **measured** or **estimate** (playbook Stage 0, 4, 11).

## Where output goes

One note per app per stage: `members/<member>/drafts/<app-slug>/playbook/s<N>-<slug>.md` (member = the app's builder unless told otherwise). Brain connected: `get_context`, then `read_note` the previous stage notes for this app and any `research/categories/<cat>/*` notes; write with `update_note` in your own member folder only; `log_decision` for founder decisions the founder states in the session; end with `save_session`. Not connected: output the full note for `_inbox/` and say nothing was saved.

Re-running a stage replaces your note: `read_note` it first, keep earlier dated status changes in a "History" section.

```yaml
---
type: playbook-stage
app: <app>
stage: s<N>
member: <name>
builder: <name>
updated: YYYY-MM-DD
status: open | ready-for-signoff | signed-off
founder_signoff: <YYYY-MM-DD or none>
playbook_version: v0.1 (5 Oct 2026)
---
```

Note body, in this order:
1. **Open gates** — every [GATE] item not `done`/`n/a`.
2. **Checklist** — every item of the stage, verbatim, as `- [ ]`/`- [x]` with `status · evidence · owner · next action`.
3. **VERIFY log** — item, source URL, date read, quoted finding (or who must answer).
4. **Deliverables** — what this run prepared (prepare mode), with links.
5. **Risks touched** — rows from the risk register below that this stage mitigates, and whether the mitigation is in place.
6. **Hand-offs** — what the next stage needs from this one.
7. **Open questions** for the founder or builder.

Set `status: ready-for-signoff` only when every item is `done` or `n/a`. Only the founder moves it to `signed-off`.

## Risk register (verbatim; reviewed monthly, add a row after every incident)

The two risks that could end the whole plan at once are the shared Apple account and a small reserve spread over too many apps.

| Risk | Why it is real | Mitigation | Owner |
|---|---|---|---|
| Apple account terminated or flagged | One account holds all 12 apps; repeated sloppy or thin submissions are the pattern Apple watches | Submit only genuine builds, keep submissions clean, two admins, never manipulate reviews | Founder |
| Apps rejected as spam or template clones | Guideline 4.3 targets near-duplicate apps from one developer | Distinct UX, content and brand per app; review before submitting | Founder |
| Review or rating manipulation | Apple removed 297 ratings from a competitor, 73% of them five-star; one competitor's support allegedly steered users to post only positive reviews | System review prompt only, no gating, no incentives | Founder |
| Subscription-law exposure | A competitor was hit by an FTC action in June 2026 over billing; state auto-renewal laws are strict | Billing rules in Stage 2, 3-step cancel, lawyer review | Founder |
| Third-party SDK leaks user data | The FTC's Apitor case involved a third party collecting children's location | SDK inventory and review before every addition | Builder |
| Child or health data incident | Flo faced an FTC action and a $59.5M settlement for sharing health data | Retention policy, encryption, no ad-network sharing, lawyer review before launch | Founder |
| Secret or API key leaked | A live API key was pasted into a chat during this project | Keys server-side only, secret scanning, same-day rotation on any exposure | Builder |
| A builder leaves or is unavailable | Three interns, four apps each, no shared code | Spec and prompts in each repo, access list, review by a second person | Founder |
| Contributors' IP not assigned to the company | Interns write all the code before incorporation completes | Signed IP assignment before any code is pushed | Founder |
| AI-generated code ships with gaps | Placeholder data, missing error paths and unbuilt deletion are typical | Review checklist in Stage 3, manual test script, TestFlight | Builder |
| Unit economics are worse than modeled | Most model inputs were estimates and used gross prices, not net proceeds | Label measured versus estimate, net out the store fee, measure on small spend first | Founder |
| Budget exhausted before a winner appears | A single modeled Fax test was about half the reserve | Stop-loss rule, 2 to 3 apps at a time, 15% per-app cap before a gate | Founder |
| Attribution loss from low ATT opt-in | Industry opt-in is only 15 to 35% | Apple Search Ads first, strong pre-prompt, conservative models | Founder |
| Ad account delayed or banned | Meta approval has taken about a month; policy violations can disable accounts | Apply early, compliant claims, keep a documented ad review step | Founder |
| History lost in apps that store user records | Recipe, sleep and pet apps in our research lost users' data | Durable saves, backups, tested restore, never lock history behind a paywall | Builder |
| Free platform feature replaces the category | Apple's free Measure app uses the same ARKit as paid competitors | Stage 0 free-alternative check | Founder |
| Name or trademark dispute | HelloFax already existed and most obvious names were taken | Clearance and attorney opinion before launch | Founder |

## Appendix A — Decisions the founder still has to make (verbatim)

Stage agents surface these when an item depends on them; they never answer them.

- Native framework: Swift/SwiftUI or React Native. Record the choice and the reason in Stage 3.
- Subscription or paywall service (RevenueCat, Superwall or none). A chat message mentioned "Supawall"; I assumed it meant Superwall, so please confirm.
- Mobile measurement partner or platform SDKs only.
- Which 2 to 3 apps receive paid spend first.
- Whether the Phase 1 list stands as is. Storage cleaner, Plant identifier, Baby tracker and Immigration tracker rank lower than the top picks on the LTV/CAC-weighted ranking, so the founder should confirm they are in for reasons the ranking does not capture.
- The shared review-gate component in the design kit: remove it or redesign it so it never filters who reaches the App Store (Stage 2).
- Merchant of record for any web billing. Paddle was considered earlier but is not confirmed.
- Meta ad account currency and time zone.
- Whether to keep all apps on one Apple account.

## Appendix B — Needs a professional before launch (verbatim)

- US privacy lawyer: privacy policies and terms for all apps, children's and health-data rules, auto-renewal law, trademarks, breach plan.
- Employment or IP lawyer: contributor IP assignment and offer letters.
- Indian chartered accountant: tax forms for Apple, GST and foreign-currency receipts, tax on ad spend, filing calendar.
- Corporate counsel: the Delaware C-Corp conversion before any US VC round.

## Appendix D — Status of the facts in this playbook (verbatim)

Benchmarks and rules here come from research earlier in this project: Adapty's 2026 subscription benchmarks, Meta and Apple Search Ads documentation and third-party summaries of it, FTC and state-law summaries, and the competitor teardowns. They are named but not linked, and several Apple and Meta rules change often. Everything marked [VERIFY] should be checked against the current official page, and any figure used in a decision should be replaced by the app's own measured data as soon as it exists.

## Finish every run with

1. A 5-line summary in chat: stage, app, items done / open / blocked / n/a, open gates.
2. What the founder must decide or sign next.
3. What was verified this run (sources, dates) and what could not be.
4. Next stage to run, or the stage that blocks this one.
