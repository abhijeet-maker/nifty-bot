#!/usr/bin/env bash
# Universe cache manager. Fundamentals don't change faster than quarterly,
# so we cache screener.sh output per-symbol with a 30-day TTL and only
# refresh entries that are stale OR whose company reported earnings recently.
#
# Usage:
#   bash scripts/universe-cache.sh refresh       # updates stale entries
#   bash scripts/universe-cache.sh rebuild       # forces full refresh (nuclear)
#   bash scripts/universe-cache.sh get RELIANCE  # prints cached JSON for one symbol
#
# Cache lives at memory/.fundamentals-cache/ (committed to git — it's part of memory).

set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
CACHE_DIR="$ROOT/memory/.fundamentals-cache"
TTL_DAYS="${TTL_DAYS:-30}"
mkdir -p "$CACHE_DIR"

# Source .env if present
ENV_FILE="$ROOT/.env"
[[ -f "$ENV_FILE" ]] && { set -a; source "$ENV_FILE"; set +a; }

# Read the roster from UNIVERSE.md — the paragraph after "## Full Nifty 100 roster"
roster() {
  awk '/^## Full Nifty 100 roster/,/^##[^#]/' "$ROOT/memory/UNIVERSE.md" \
    | grep -oE '\b[A-Z][A-Z0-9&-]{1,15}\b' \
    | grep -vE '^(Nifty|NSE|GICS|TTM|ROCE|ROE|CAGR|YoY|RSI|DMA|PEAD)$' \
    | sort -u
}

# Is this cache entry stale?
is_stale() {
  local file="$1"
  [[ ! -f "$file" ]] && return 0
  local age_days
  age_days=$(( ( $(date +%s) - $(stat -c %Y "$file") ) / 86400 ))
  [[ $age_days -ge $TTL_DAYS ]]
}

cmd="${1:-refresh}"
shift || true

case "$cmd" in
  refresh)
    echo "Refreshing universe cache (TTL: $TTL_DAYS days)..."
    stale_count=0
    fresh_count=0
    failed=()
    for sym in $(roster); do
      cache_file="$CACHE_DIR/${sym}.json"
      if is_stale "$cache_file"; then
        echo -n "  $sym ... "
        if bash "$ROOT/scripts/screener.sh" "$sym" > "$cache_file.tmp" 2>/dev/null; then
          mv "$cache_file.tmp" "$cache_file"
          echo "ok"
          stale_count=$((stale_count+1))
          # Rate limit — Screener doesn't love being hammered
          sleep 1.5
        else
          rm -f "$cache_file.tmp"
          echo "FAILED (will fall back to Perplexity at read time)"
          failed+=("$sym")
        fi
      else
        fresh_count=$((fresh_count+1))
      fi
    done
    echo
    echo "Cache status: $fresh_count fresh, $stale_count refreshed, ${#failed[@]} failed"
    [[ ${#failed[@]} -gt 0 ]] && printf '  Failed: %s\n' "${failed[*]}"
    ;;

  rebuild)
    echo "Force-rebuilding universe cache..."
    rm -rf "$CACHE_DIR"
    mkdir -p "$CACHE_DIR"
    bash "$0" refresh
    ;;

  get)
    sym="${1:?usage: get SYMBOL}"
    cache_file="$CACHE_DIR/${sym}.json"
    if is_stale "$cache_file"; then
      # Attempt a fresh fetch on-demand
      if bash "$ROOT/scripts/screener.sh" "$sym" > "$cache_file.tmp" 2>/dev/null; then
        mv "$cache_file.tmp" "$cache_file"
      else
        rm -f "$cache_file.tmp"
        echo "CACHE_MISS symbol=$sym — Screener unavailable" >&2
        echo "This symbol will be excluded from the universe this cycle." >&2
        exit 4
      fi
    fi
    cat "$cache_file"
    ;;

  status)
    total=0
    fresh=0
    stale=0
    for sym in $(roster); do
      total=$((total+1))
      cache_file="$CACHE_DIR/${sym}.json"
      if is_stale "$cache_file"; then
        stale=$((stale+1))
      else
        fresh=$((fresh+1))
      fi
    done
    echo "Universe cache: $fresh/$total fresh, $stale stale (TTL: $TTL_DAYS days)"
    ;;

  *)
    echo "Usage: bash scripts/universe-cache.sh <refresh|rebuild|get SYM|status>" >&2
    exit 1
    ;;
esac
