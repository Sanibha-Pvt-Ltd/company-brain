---
type: reference
updated: 2026-10-03
---

# Agents

Four agents, each a skill in `skills/<name>/` served by the brain (any member's Claude loads it with `get_skill`) and, for Claude Code, a thin wrapper in `.claude/agents/`.

| # | Agent | Job | Status |
|---|---|---|---|
| 1 | **brand-designer** | Finalise the brand design system: color, type, spacing, radius, iconography, voice. Writes `vault/brand/` | planned |
| 2 | **app-researcher** | Research apps/categories: review failure-mining, market, MVP recommendation, portfolio, build spec | **live** — [[skills/app-researcher/SKILL]] |
| 3 | **ux-designer** | Journey maps, mockups, flows from a build spec; uses Mobbin references. Writes `vault/design/` | planned |
| 4 | **ios-engineer** | iOS implementation guidance and ADRs from a build spec. Writes `vault/tech/` | planned |

Handoff chain: researcher's `build-spec.md` → ux-designer → (brand tokens) → ios-engineer. Each later agent reads the previous agents' canonical notes from the brain, so the brain is the contract between them.
