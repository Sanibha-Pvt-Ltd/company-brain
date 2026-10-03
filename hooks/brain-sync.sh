#!/bin/bash
# Commit and push whatever the hooks wrote under vault/. Run by launchd every 5 minutes
# and at SessionEnd; safe by hand. Code (hooks/, skills/, tools/) is committed by hand —
# only vault/ is auto-committed, so this never races a human mid-edit on code.
set -uo pipefail
. "$(dirname "$0")/common.sh"
cd "$BRAIN_DIR" || exit 1

LOCK="${TMPDIR:-/tmp}/sanibha-brain-sync.lock"
mkdir "$LOCK" 2>/dev/null || exit 0
trap 'rmdir "$LOCK" 2>/dev/null' EXIT
log() { printf '%s %s\n' "$(date +%Y-%m-%dT%H:%M:%S)" "$*"; }

git pull --rebase --autostash -q 2>&1 | sed 's/^/  /'
[ -z "$(git status --porcelain vault)" ] && { log "nothing to sync"; exit 0; }

n=$(git status --porcelain vault | wc -l | tr -d ' ')
git add -A vault
git -c user.email="${BRAIN_EMAIL:-harshil@sanibha.com}" -c user.name="${BRAIN_NAME:-harshil}" \
    commit -qm "brain-sync: $n change$([ "$n" = 1 ] || echo s) at $(date +%H:%M)" -- vault
if git push -q 2>&1 | sed 's/^/  /'; then log "pushed $n change(s)"
else log "commit made, push failed — will retry next run"; exit 1; fi
