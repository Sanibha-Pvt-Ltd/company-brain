#!/bin/bash
# PostToolUse: when this person's CAPTURE_SCOPE covers the session — append one record per tool call to the session's
# local verbose log (gitignored, write-only), and keep the readable mirror fresh.
set -uo pipefail
. "$(dirname "$0")/common.sh"

payload=$(cat)
cwd=$(printf '%s' "$payload" | jq -r '.cwd // empty'); cwd="${cwd:-$PWD}"
should_capture "$cwd" || exit 0

sid=$(printf '%s' "$payload" | jq -r '.session_id // "unknown"')
stem=$(stem_for "$sid")
mkdir -p "$LOGS/verbose" "$LOGS/activity"
out="$LOGS/verbose/$stem.jsonl"

printf '%s' "$payload" | jq -c --arg ts "$(date -u +%Y-%m-%dT%H:%M:%SZ)" '{
  ts: $ts,
  tool: (.tool_name // "unknown"),
  cwd: (.cwd // ""),
  input: ((.tool_input // {}) | tostring | .[0:2000]),
  ok: (if (.tool_response.error // .tool_response.is_error // false) then false else true end)
}' >> "$out" 2>/dev/null || exit 0

# ponytail: re-render at most every 5s; stop.sh forces the final render.
mirror="$LOGS/activity/$stem.md"
if [ ! -f "$mirror" ] || [ "$(( $(date +%s) - $(stat -f %m "$mirror" 2>/dev/null || echo 0) ))" -ge 5 ]; then
  python3 "$(dirname "$0")/render-verbose.py" "$out" "$mirror" 2>/dev/null || true
fi
exit 0
