---
type: reference
updated: 2026-10-03
---

# Tools and access

No secrets here. Keys live in each person's password manager.

| Thing | Where |
|---|---|
| Vault repo | github.com/Sanibha-Pvt-Ltd/company-brain (`vault/` opens in Obsidian) |
| Server repo | github.com/Sanibha-Pvt-Ltd/brain-mcp (Cloudflare Worker + D1) |
| Brain URL | set after first deploy (see [[projects/sanibha]]) |
| Brain keys | one per person, minted by Harshil; members write only in `members/<name>/` |
| Review/listing puller | `tools/fetch-app.py` in company-brain (plain Python, no installs) |
| Raw data and screenshots | local per member + shared Drive folder `Sanibha/Research/<category>/<app>/`; notes link to them |
| Runbook | `skills/app-researcher/RUNBOOK.md` |

Connecting: claude.ai → Settings → Connectors → add custom connector with the brain URL, sign in with your key. Claude Code: `claude mcp add`. A connector that was dead when a chat started stays dead for that chat — start a new chat after fixing.
