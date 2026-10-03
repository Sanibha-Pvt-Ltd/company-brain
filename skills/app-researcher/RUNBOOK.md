# Runbook — how a member runs app-researcher

## One-time
1. Connect the Sanibha brain to your Claude (claude.ai: Settings → Connectors → add custom connector with the brain URL; Claude Code: `claude mcp add`). You get a personal access key from Harshil — store it in your password manager, never paste it in notes or chat.
2. Turn on web search / Research mode.
3. Add the `app-researcher` skill: ask Claude to call `get_skill app-researcher` on the brain (it will `read_note` the stage prompts as needed), or upload this `skills/app-researcher` folder to your Claude project.

## Per app (stage A)
1. Get the app's id from its App Store URL (`.../id388627783` → `388627783`).
2. Pull data (repo root of `~/Sanibha`):
   `python3 scripts/fetch-app.py --extra <name>=<id>` — repeat for up to 4 apps in one command.
   Produces `research-data/<name>/negatives.md`, `reviews.json`, `listing.json`. `--extra` adds UK/CA/AU for volume (tagged by country; ask the agent to weigh US first).
3. Open a new chat. Upload `negatives.md`, `listing.json`, and your real screenshots/PDFs of the app.
4. Say: `Use app-researcher, stage A, category <cat>, app <name>, member <you>.`
5. Let it run; answer its open questions. Check the note landed in the brain (`research/apps/<name>/<you>-<date>.md`).
6. Rerun step 2 weekly: new reviews merge into the history, so the sample grows past Apple's 10-page cap.

## Team cadence
- Stage 0 once per category (Harshil/Bharat) → assigns apps, 4 per member.
- Stage A: everyone, in parallel.
- Stage B, then C: one person, after stage A is mostly done.
- Team reviews `mvp.md`; Bharat signs off (`status: final`, `log_decision`).
- Stage E after ≥3 categories. Stage D per chosen product.

## Quality bar
- Every number has a source and date; every quote has stars/date/version.
- `[UNKNOWN]` is fine; invented facts are not.
- Never paste keys or tokens into chats or notes.
