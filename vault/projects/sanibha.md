---
type: project
status: active
updated: 2026-10-03
summary: Sanibha Pvt. Ltd. — company-level notes, brain setup, cross-category research
repo: https://github.com/Sanibha-Pvt-Ltd/company-brain
---

# Sanibha

Technical service provider building iOS apps for US App Store users. Founder Bharat Bhatia; tech Harshil. Team of 4.

## State

Brain and app-researcher agent scaffolded. Pilot category: storage cleaner (`research/categories/storage-cleaner/`). Members work in `members/<name>/`; admins promote drafts to `research/`.

## Next

Deploy brain, onboard members, run stage 0 → A → B → C on the pilot.

## Rules

See [[rules/company]].

## Sessions

```dataview
TABLE date, summary
FROM "logs/sessions"
WHERE type = "session"
SORT date DESC
LIMIT 10
```
