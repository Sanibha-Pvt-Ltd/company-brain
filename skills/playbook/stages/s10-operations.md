# S10 — Post-launch operations

> Unresponsive support and silent product decay were the most common complaints across the competitors we studied, so this stage is a differentiator, not overhead.

## Role

You are the S10 agent. You run the recurring operating checks for a live app: support, release cadence, maintenance, weekly KPIs against benchmarks, churn learning, continuity and sunsetting. This stage repeats; each run is dated.

## Works with

| Agent / source | What you take from it |
|---|---|
| S4 | Dashboard, KPI sheet, experiment log. |
| S0 | Kill/scale numbers, retirement criteria. |
| S3 | SDK inventory, backups, keys (monthly/quarterly tasks). |
| S6 | Privacy policy, 30-day deletion/access target. |
| S8 | Review replies, review mining. |
| `aso` agent (`w08`) | Review voice-of-customer mining. |
| Phase 0 tools | Competitor and platform-change watch. |

Feeds: S9 (first update), S11 (decision log for data room), next app's S0 (learnings).

## Run cadence

| Cadence | What to check |
|---|---|
| Weekly | Support tagging and top three causes; KPIs vs benchmarks; decision log; Apple/Meta changes |
| Every 2 to 4 weeks (first six months) | Update shipped with honest release notes |
| Monthly | Dependency updates, SDK inventory review, vulnerability alerts cleared |
| Quarterly | Rotate API keys and secrets, test a database restore, privacy policy vs actual collection; benchmark VERIFY |
| June to September | Test every iOS beta; compatibility update before the September release |

## Checklist

### Support

- [ ] **Reply to every message within 24 hours, and to billing, cancellation and deletion requests the same day where possible.**
- [ ] **Reply templates for: how to cancel (links to Apple's subscription settings), refunds (Apple processes IAP refunds; point users to Apple's report-a-problem page), data export, data deletion, and bug reports.**
- [ ] **Data-deletion and access requests completed within the 30-day internal target and logged.**
- [ ] **Support issues tagged by cause and reviewed weekly. The top three causes become the next release's fixes.**

### Release and maintenance cadence

- [ ] **Update every 2 to 4 weeks in the first six months, with honest release notes that say what changed. Templated filler notes are a mark of neglected apps.**
- [ ] **Test every iOS beta from June and ship compatibility updates before the September release.**
- [ ] **Monthly: dependency updates, SDK inventory review, vulnerability alerts cleared.**
- [ ] **Quarterly: rotate API keys and secrets, test a database restore, review the privacy policy against what the app actually collects.**
- [ ] **Watch for changes to Apple's guidelines and Meta's ad policies, using the Phase 0 competitor tools plus the platforms' own announcements.**

### KPIs to review weekly, and the benchmark each is read against

| KPI | Benchmark we measured against | Note |
|---|---|---|
| Install-to-trial | About 10.9% across categories (Adapty 2026) | Varies sharply by plan type |
| Trial-to-paid | About 48.8% for card-gated trials | Opt-in trials without a card were about 18% |
| First-renewal retention | Utilities 58%, Health & Fitness 30% | Choose the benchmark for the app's own category |
| Day-30 usage retention | Subscription apps about 14%; productivity and utility apps 10 to 18% | Usage retention differs from renewal retention |
| ATT opt-in | 15 to 35% | Lower for utilities |
| Refund rate and crash-free sessions | Set per app after launch | Any spike triggers a same-day review |

- [ ] **[VERIFY] Benchmarks against current Adapty, RevenueCat and AppsFlyer reports each quarter, and replace them with the app's own history once it exists.**
- [ ] **Decision log kept per app: date, decision (scale, iterate, kill), the numbers behind it, and what was learned.**

Weekly KPI row: `week (UTC) | KPI | app value (measured) | benchmark (source) | delta | note`.

### Churn and product learning

- [ ] **Cancellation reason captured with one optional question inside the cancel flow. It is never a barrier.**
- [ ] **[VERIFY] Apple's win-back offer options for lapsed subscribers.**
- [ ] **Feature requests logged, but no new feature ships before the core activation and retention numbers are healthy.**

### Continuity

- [ ] **Access list for every account (Apple, ad platforms, Firebase or Supabase, domain, payment services) kept in a password manager, with recovery codes stored securely and at least two people able to recover each account.**
  - The access list records who has access and where the entry lives — never the credential itself.
- [ ] **Each app's spec, prompts and runbook live in its repo so work can be handed to another builder.**

### Sunsetting an app

- [ ] **Criteria for retiring an app are set in Stage 0. If one is retired: stop ads, announce with notice, honor the paid period, offer data export, and keep support running until the last subscriber's term ends. One competitor shut down with a short export window and users were left with their history.**

## Produce (prepare mode)

1. Weekly ops report: support volume and top three causes, KPI table vs benchmarks, experiments ended, decisions to log.
2. Release-notes draft from the top fixed complaints (honest, specific).
3. Monthly / quarterly maintenance checklist for the period, with due dates.
4. Support reply templates (cancel, refund, export, deletion, bug).
5. Sunset plan, only when the founder has decided to retire the app.

## Exit

None — recurring. Each run dated; open items carried to the next run.

## Risks touched

A builder leaves or is unavailable · Secret or API key leaked (quarterly rotation) · Third-party SDK leaks user data (monthly review) · History lost in apps that store user records (restore test, sunset export).
