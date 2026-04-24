#!/usr/bin/env bash
# Screener.in wrapper for fundamental data.
# Uses Beautiful Soup + requests for robust HTML parsing and cookie support.
# Automatically falls back gracefully on parse errors (exit code 4).
#
# Usage:
#   bash scripts/screener.sh RELIANCE    -> JSON of key fundamentals
#
# Exits with code 4 if the page cannot be fetched or parsed, so callers
# can fall back to Perplexity.sh with a specific structured query.

set -euo pipefail
ROOT="$(git -C "$(dirname "$0")" rev-parse --show-toplevel)"
ENV_FILE="$ROOT/.env"
[[ -f "$ENV_FILE" ]] && { set -a; source "$ENV_FILE"; set +a; }

sym="${1:-}"
if [[ -z "$sym" ]]; then
  echo "usage: bash scripts/screener.sh SYMBOL" >&2
  exit 1
fi

# Delegate to Python module which uses Beautiful Soup + proper cookie handling
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
python3 "${SCRIPT_DIR}/lib/screener_data.py" "$sym" "${SCREENER_SESSION:-}"
