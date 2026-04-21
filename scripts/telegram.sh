#!/usr/bin/env bash
# Telegram notification wrapper. Sends markdown messages to your phone.
# Usage:
#   bash scripts/telegram.sh "PAPER BUY HDFCBANK 15 shares @ ~₹1650"
#   echo "multiline..." | bash scripts/telegram.sh
#
# If credentials are missing, appends to NOTIFICATIONS.md (gitignored via scratch/)
# and exits 0 — routines never die because of a notification issue.

set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
ENV_FILE="$ROOT/.env"
FALLBACK="$ROOT/scratch/NOTIFICATIONS.md"
mkdir -p "$(dirname "$FALLBACK")" 2>/dev/null || true

[[ -f "$ENV_FILE" ]] && { set -a; source "$ENV_FILE"; set +a; }

if [[ $# -gt 0 ]]; then
  msg="$*"
else
  msg="$(cat)"
fi

if [[ -z "${msg// /}" ]]; then
  echo 'usage: bash scripts/telegram.sh "<message>"' >&2
  exit 1
fi

stamp=$(date '+%Y-%m-%d %H:%M IST')

if [[ -z "${TELEGRAM_BOT_TOKEN:-}" || -z "${TELEGRAM_CHAT_ID:-}" ]]; then
  printf "\n---\n## %s (fallback — Telegram not configured)\n%s\n" "$stamp" "$msg" >> "$FALLBACK"
  echo "[telegram fallback] appended to scratch/NOTIFICATIONS.md"
  echo "$msg"
  exit 0
fi

# Telegram's MarkdownV2 is strict; use plain 'Markdown' (legacy) — fewer escaping headaches.
# Truncate at 4000 chars (Telegram hard limit is 4096).
truncated=$(printf '%s' "$msg" | head -c 4000)

payload=$(python3 -c "
import json, sys
print(json.dumps({
  'chat_id': sys.argv[1],
  'text': sys.argv[2],
  'parse_mode': 'Markdown',
  'disable_web_page_preview': True,
}))
" "$TELEGRAM_CHAT_ID" "$truncated")

response=$(curl -fsS -X POST \
  "https://api.telegram.org/bot${TELEGRAM_BOT_TOKEN}/sendMessage" \
  -H "Content-Type: application/json" \
  -d "$payload" 2>&1) || {
  echo "Telegram API call failed: $response" >&2
  # Still fall back to file so the message isn't lost
  printf "\n---\n## %s (API error)\n%s\n" "$stamp" "$msg" >> "$FALLBACK"
  exit 0
}

# Verify ok=true in response
echo "$response" | python3 -c "
import json, sys
d = json.load(sys.stdin)
if not d.get('ok'):
    print('Telegram response not ok:', d, file=sys.stderr)
    sys.exit(1)
print('sent ok')
"
