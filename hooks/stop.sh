#!/bin/bash
# Stop: force a final render so the mirror is never left stale by the 5s throttle.
set -uo pipefail
. "$(dirname "$0")/common.sh"

payload=$(cat)
cwd=$(printf '%s' "$payload" | jq -r '.cwd // empty'); cwd="${cwd:-$PWD}"
should_capture "$cwd" || exit 0
stem=$(stem_for "$(printf '%s' "$payload" | jq -r '.session_id // "unknown"')")
[ -f "$LOGS/verbose/$stem.jsonl" ] || exit 0
python3 "$(dirname "$0")/render-verbose.py" "$LOGS/verbose/$stem.jsonl" "$LOGS/activity/$stem.md" 2>/dev/null || true
exit 0
