# Stage E — Portfolio (cross-category)

Run after at least 3 categories have `market.md` and `mvp.md`. Output: `research/portfolio.md`.

Read every `research/categories/*/market.md` and `mvp.md`. Score each category 1–5 with a one-line evidence cite per score:

| Dimension | Weight |
|---|---|
| Demand (revenue/downloads size + growth) | 20% |
| Monetization (revenue per download, subscription fit) | 20% |
| Competition (concentration, new-entrant success) | 15% |
| Differentiation gap (strength of unmet needs from failure matrix) | 20% |
| Acquisition (keyword opportunity, CPI vs revenue/download) | 10% |
| Build cost (6-week feasibility, iOS API limits) | 10% |
| Review/platform risk (lower risk = higher score) | 5% |

Weights are defaults; if `research/scoring.md` exists, use it instead and say so.

Write: ranked table with weighted totals; top 3 with rationale; recommended build order; what would flip the ranking; categories lacking enough evidence to score (do not guess — mark `[UNKNOWN]` and exclude).
