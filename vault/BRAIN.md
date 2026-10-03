---
type: index
updated: 2026-10-03
---

# BRAIN

Sanibha company brain. Everything below is generated from frontmatter — nothing here is hand-maintained.

## Now

![[_activity/NOW]]

## Products

```dataview
TABLE status, updated, summary
FROM "projects"
WHERE type = "project"
SORT updated DESC
```

## Binding rules

```dataview
TABLE project, updated
FROM "rules"
WHERE type = "rules"
```

## Category research

```dataview
TABLE category, status, updated
FROM "research/categories"
WHERE type = "category-lens" OR type = "category-market" OR type = "category-mvp" OR type = "build-spec"
SORT category ASC
```

## App teardowns

```dataview
TABLE category, member, reviews_analysed, updated
FROM "research/apps"
WHERE type = "app"
SORT category ASC, updated DESC
```

## Recent sessions

```dataview
TABLE project, date, summary
FROM "logs/sessions"
WHERE type = "session"
SORT date DESC
LIMIT 10
```

## Decisions

[[logs/decisions|Decision log]] — append-only, newest last.
