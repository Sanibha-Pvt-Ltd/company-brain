---
type: reference
updated: 2026-10-03
---

# Agents

Seven agents, each a skill in `skills/<name>/` served by the brain (any member's Claude loads it with `get_skill`) and, for Claude Code, a thin wrapper in `.claude/agents/`.

| # | Agent | Job | Status |
|---|---|---|---|
| 1 | **brand-designer** | Finalise the brand design system: color, type, spacing, radius, iconography, voice. Writes `vault/brand/` | planned |
| 2 | **app-researcher** | Research apps/categories: review failure-mining, market, MVP recommendation, portfolio, build spec | **live** — [[skills/app-researcher/SKILL]] |
| 3 | **ux-designer** | Journey maps, mockups, flows from a build spec; uses Mobbin references. Writes `vault/design/` | planned |
| 4 | **ios-engineer** | iOS implementation guidance and ADRs from a build spec. Writes `vault/tech/` | planned |
| 5 | **aso** | App Store optimization: keywords, metadata, product pages, localization, review/Apple Ads intelligence, experiments. Notes in own member folder | **live** — [[skills/aso/SKILL]] (pre-launch mode until an app ships) |
| 6 | **seo** | Web SEO for app landing pages/content: GSC mining, refreshes, links, BOFU/programmatic, experiments | **live** — [[skills/seo/SKILL]] (no site data yet) |
| 7 | **product-strategist** | v1 call per category from `context.md` + team screenshots: positioning, UI/UX, final v1 features, new recommendations. Writes `members/<m>/drafts/<cat>/product-strategy.md` | **live** — [[skills/product-strategist/SKILL]] (pilot: storage-cleaner) |

app-researcher also has stage U (universe discovery across all consumer-utility subcategories, run before stage 0 to pick the categories). ASO and SEO run on competitor evidence from app-researcher notes before launch, and on real data after.

Handoff chain: researcher's `build-spec.md` → ux-designer → (brand tokens) → ios-engineer. Each later agent reads the previous agents' canonical notes from the brain, so the brain is the contract between them.

## Playbook stage agents (S0–S11)

Built 2026-10-05 from **Sanibha App Creation Playbook & Checklist** v0.1 (5 Oct 2026, Bharat). One skill, `skills/playbook/` — `SKILL.md` (rules, statuses, risk register, appendices), `stages/s0…s11`, `orchestrator.md` — and 13 Claude Code wrappers in `.claude/agents/`. Checklist items are copied verbatim; agents add method and evidence requirements, never new facts. Not run yet.

| Agent | Stage |
|---|---|
| **playbook-orchestrator** | Status board per app/portfolio, stage order and gates, cross-stage checks, dispatches stage agents |
| s0-validation | Idea validation and go/no-go (uses app-researcher outputs) |
| s1-spec | Product and UX spec |
| s2-standards | In-app standards |
| s3-engineering | Engineering and architecture |
| s4-analytics | Analytics, attribution and measurement |
| s5-monetization | Monetization and pricing |
| s6-legal | Legal and compliance (prepares lawyer/CA questions; no legal advice) |
| s7-submission | App Store submission and ASO (uses aso agent for listing copy) |
| s8-marketing | Marketing and growth |
| s9-launch | Launch (T-30 to T+30) |
| s10-operations | Post-launch operations (recurring) |
| s11-finance | Finance and company operations (recurring) |

Output: `members/<builder>/drafts/<app>/playbook/s<N>-<slug>.md`, one note per app per stage. Founder-owned items are ticked only with a logged founder decision.
