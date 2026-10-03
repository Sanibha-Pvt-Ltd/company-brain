#!/bin/bash
# Shared by every Sanibha capture hook. Sourced, never run.
#
# These hooks are installed globally in ~/.claude/settings.json, so they fire in every
# Claude Code session on the machine; should_capture() below decides per person whether
# this session is theirs to log.

SANIBHA_HOME="${SANIBHA_HOME:-$HOME/Sanibha}"
BRAIN_DIR="${BRAIN_DIR:-$SANIBHA_HOME/company-brain}"
VAULT="$BRAIN_DIR/vault"
LOGS="$VAULT/logs"

# ponytail: launchd and cron never source ~/.zshrc; non-interactive env goes here.
[ -f "$BRAIN_DIR/hooks/.env" ] && . "$BRAIN_DIR/hooks/.env"

# CAPTURE_SCOPE (set per person in hooks/.env by install.sh):
#   sanibha  only sessions inside ~/Sanibha are captured   (default; for people who keep a personal brain)
#   all      every Claude Code session is captured          (team members without one)
CAPTURE_SCOPE="${CAPTURE_SCOPE:-sanibha}"
export BRAIN_NAME="${BRAIN_NAME:-unknown}"

# true when a session in directory $1 should be logged and synced
should_capture() {
  [ "$CAPTURE_SCOPE" = all ] && return 0
  case "$1" in "$SANIBHA_HOME"|"$SANIBHA_HOME"/*) return 0 ;; *) return 1 ;; esac
}

# Same session key -> same files, so compaction and resume append instead of forking.
stem_for() {
  local key="${1:0:8}" hit
  hit=$(ls -1 "$LOGS/verbose"/*_"$key".jsonl 2>/dev/null | head -1)
  if [ -n "$hit" ]; then basename "$hit" .jsonl; else echo "$(date +%Y-%m-%d_%H%M%S)_$key"; fi
}
