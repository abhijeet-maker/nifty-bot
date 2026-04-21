#!/usr/bin/env bash
# Perplexity Sonar wrapper — narrative market research with citations.
# Usage:
#   bash scripts/perplexity.sh "What did Infosys management say on Q3 FY26 earnings call about FY27 guidance?"
#
# Exits 3 if PERPLEXITY_API_KEY unset, so callers can decide to skip or fallback.

set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
ENV_FILE="$ROOT/.env"
[[ -f "$ENV_FILE" ]] && { set -a; source "$ENV_FILE"; set +a; }

query="${1:-}"
if [[ -z "$query" ]]; then
  echo 'usage: bash scripts/perplexity.sh "<query>"' >&2
  exit 1
fi

if [[ -z "${PERPLEXITY_API_KEY:-}" ]]; then
  echo "PERPLEXITY_API_KEY not set in environment" >&2
  exit 3
fi

MODEL="${PERPLEXITY_MODEL:-sonar}"

payload=$(python3 -c "
import json, sys
print(json.dumps({
  'model': sys.argv[1],
  'messages': [
    {'role': 'system', 'content': 'You are a precise Indian equity markets research assistant. Cite every numerical claim with a source URL. Prefer company filings, exchange announcements, and respected business press (Economic Times, Mint, Business Standard, Moneycontrol, Reuters). Be concise. Use INR and crores. When asked for fundamental data, structure as JSON.'},
    {'role': 'user', 'content': sys.argv[2]}
  ],
  'temperature': 0.1,
}))
" "$MODEL" "$query")

curl -fsS https://api.perplexity.ai/chat/completions \
  -H "Authorization: Bearer $PERPLEXITY_API_KEY" \
  -H "Content-Type: application/json" \
  -d "$payload" \
| python3 -c "
import json, sys
d = json.load(sys.stdin)
msg = d.get('choices', [{}])[0].get('message', {})
print(msg.get('content', ''))
cites = d.get('citations', [])
if cites:
    print('\n---\nSources:')
    for i, c in enumerate(cites, 1):
        print(f'  [{i}] {c}')
"
