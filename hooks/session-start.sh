#!/bin/bash
# SessionStart: when this person's CAPTURE_SCOPE covers the session — pull teammates' notes, then inject the company
# context and binding rules. Creates nothing; files appear on the first tool call.
set -uo pipefail
. "$(dirname "$0")/common.sh"

payload=$(cat)
cwd=$(printf '%s' "$payload" | jq -r '.cwd // empty'); cwd="${cwd:-$PWD}"
should_capture "$cwd" || exit 0

git -C "$BRAIN_DIR" pull --rebase --autostash -q 2>/dev/null || true

body() { sed '/^---$/,/^---$/d' "$1"; }

ctx=$(
  printf '# Sanibha company brain\n\nThis session is logged to the Sanibha vault. Vault: %s\n\n' "$VAULT"
  [ -f "$VAULT/_activity/NOW.md" ] && { printf '## Now\n\n'; body "$VAULT/_activity/NOW.md"; printf '\n'; }
  for f in about tech-context; do
    [ -f "$VAULT/company/$f.md" ] && { printf '## company/%s\n\n' "$f"; body "$VAULT/company/$f.md"; printf '\n'; }
  done
  printf 'More company context in vault/company/: team, workflow, agents, categories, glossary, tools-and-access, open-questions.\n\n'
  if compgen -G "$VAULT/rules/*.md" > /dev/null; then
    printf '## Binding rules\n\n'
    for f in "$VAULT/rules"/*.md; do printf '### %s\n\n' "$(basename "$f" .md)"; body "$f"; printf '\n'; done
  fi
  if compgen -G "$VAULT/projects/*.md" > /dev/null; then
    printf '## Projects\n\n'
    for f in "$VAULT/projects"/*.md; do
      printf -- '- [[projects/%s]] — %s\n' "$(basename "$f" .md)" \
        "$(sed -n 's/^summary: *"\{0,1\}\(.*\)/\1/p' "$f" | head -1 | tr -d '"')"
    done
    printf '\n'
  fi
  printf 'Tool calls in this session are logged automatically. At the natural end of the work, write what happened and what is next into vault/logs/sessions/ and log decisions with hooks/log-decision.sh. Never put a secret in a command or a note.\n'
)

jq -n --arg c "$ctx" '{hookSpecificOutput: {hookEventName: "SessionStart", additionalContext: $c}}'
