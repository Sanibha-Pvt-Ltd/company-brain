#!/bin/bash
# Install the Sanibha capture hooks into ~/.claude/settings.json and the 5-minute sync
# timer. Idempotent: re-running replaces only entries whose command contains
# /company-brain/hooks/. Other hooks (including a personal brain's) are untouched.
# usage: install.sh                       you keep a personal brain: capture only sessions under ~/Sanibha
#        install.sh --all <your-name>     capture EVERY Claude Code session on this machine
set -euo pipefail

SCOPE=sanibha; WHO="${BRAIN_NAME:-$(id -un)}"
if [ "${1:-}" = "--all" ]; then SCOPE=all; WHO="${2:?usage: install.sh --all <your-name, lowercase>}"; fi

HOOKS="$(cd "$(dirname "$0")" && pwd)"
BRAIN="$(cd "$HOOKS/.." && pwd)"
SETTINGS="$HOME/.claude/settings.json"
LABEL="com.sanibha.brain-sync"
DEST="$HOME/Library/LaunchAgents/$LABEL.plist"

printf 'CAPTURE_SCOPE=%s\nBRAIN_NAME=%s\nBRAIN_DIR=%s\n' "$SCOPE" "$WHO" "$BRAIN" > "$HOOKS/.env"
[ -f "$SETTINGS" ] || echo '{}' > "$SETTINGS"
cp "$SETTINGS" "$SETTINGS.bak"
jq --arg d "$HOOKS" '
  def strip(ev): (.hooks[ev] // [])
    | map(.hooks |= map(select(.command | contains("/company-brain/hooks/") | not)))
    | map(select((.hooks | length) > 0));
  .hooks = (.hooks // {})
  | .hooks.SessionStart = strip("SessionStart") + [{hooks: [{type: "command", command: ($d + "/session-start.sh"), timeout: 20}]}]
  | .hooks.PostToolUse  = strip("PostToolUse")  + [{matcher: "*", hooks: [{type: "command", command: ($d + "/post-tool-use.sh"), timeout: 10}]}]
  | .hooks.Stop         = strip("Stop")         + [{hooks: [{type: "command", command: ($d + "/stop.sh"), timeout: 15}]}]
  | .hooks.SessionEnd   = strip("SessionEnd")   + [{hooks: [{type: "command", command: ($d + "/brain-sync.sh"), timeout: 60}]}]
' "$SETTINGS.bak" > "$SETTINGS"
echo "hooks installed -> $SETTINGS (backup: $SETTINGS.bak)"

mkdir -p "$HOME/Library/LaunchAgents"
sed -e "s|__HOOKS__|$HOOKS|g" -e "s|__BRAIN__|$BRAIN|g" "$HOOKS/$LABEL.plist" > "$DEST"
launchctl bootout "gui/$UID/$LABEL" 2>/dev/null || true
launchctl bootstrap "gui/$UID" "$DEST"
launchctl enable "gui/$UID/$LABEL"
echo "timer installed -> $DEST (log: $HOOKS/sync.log)"
echo "Restart Claude Code for the hooks to take effect."
