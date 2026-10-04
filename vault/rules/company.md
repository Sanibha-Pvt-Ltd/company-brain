---
type: rules
project: "[[projects/sanibha]]"
updated: 2026-10-04
---

# Rules — Sanibha

Binding. A direct instruction from Bharat or Harshil overrides these; nothing else does.

## Secrets
- No key, token or password in the vault, in notes, or in chat. Store a pointer to the password manager entry.
- Each member has their own brain key. Lost key: ask Harshil to revoke and mint a new one.

## Accuracy (applies to every agent and every chat)
1. **No made-up data points.** A number, price, date, count, quote or screen detail goes in only if it is directly in a source we have (screenshot, file, listing, API, cited page) or was explicitly given by a team member. Otherwise write `[UNKNOWN]`. Arithmetic on sourced numbers is allowed only when shown and tagged `[INFERRED]`.
2. **No hallucinating from responses.** Another agent's or chat's output, a summary, or an earlier note is not evidence. Before repeating its claim, trace it to the original source; if you can't, mark it unverified or drop it. Never round, merge, or embellish a claim when passing it on.
3. **Double-check before final output.** Before delivering, re-open the source for every key number, quote and claim in the output and confirm it matches. Say what was checked; list anything that could not be verified.

## Research
- Every claim carries an evidence tag; every number a source and date. Invent nothing — write UNKNOWN.
- Members write only inside `vault/members/<name>/` (enforced by the key). Canonical `research/` notes are promoted from drafts by an admin after team review.
- An MVP is `draft` until the team reviews it and Bharat signs off; log the sign-off as a decision.

## Vault
- Harshil manages the vault. `knowledge/` is read-only for everyone else; ask Harshil to add or change a file there.

## Git
- Commit subjects are one line. No co-author trailers.

## Sessions
- Every session is recorded. Claude Code: the capture hooks log it automatically (`hooks/install.sh`; `--all <name>` captures every session on that machine).
- claude.ai: any chat with the brain connected logs as it works (`append_session_log`) and ends with `save_session`. Say "save" if Claude forgets.
- Never put a secret in a command, a chat, or a note — captured sessions are pushed to the shared repo.
