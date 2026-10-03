#!/bin/bash
# log-decision.sh "Title"  [body on stdin] — append to vault/logs/decisions.md, newest last.
set -euo pipefail
. "$(dirname "$0")/common.sh"

title="${1:?usage: log-decision.sh \"Title\" [body on stdin]}"
body=""
[ -t 0 ] || IFS= read -r -d '' -t 5 body || true
{
  printf '\n## %s — %s\n\n' "$(date +%Y-%m-%d)" "$title"
  [ -n "$body" ] && printf '%s\n' "$body"
} >> "$LOGS/decisions.md"
echo "logged: $title"
