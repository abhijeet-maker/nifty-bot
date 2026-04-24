#!/usr/bin/env bash
# NSE + Yahoo Finance wrapper for Indian equity price data.
# Usage:
#   bash scripts/nse.sh quote RELIANCE         -> last price, OHLC, delivery %
#   bash scripts/nse.sh history RELIANCE 250   -> 250 days of closes (for 12-1 momentum)
#   bash scripts/nse.sh earnings 2026-04-21    -> companies reporting on that date
#   bash scripts/nse.sh momentum RELIANCE      -> 12-1 momentum + DMA crossovers
#
# Now uses nsepython (handles Akamai) + yfinance (handles Yahoo crumb/cookie).
# See scripts/lib/nse_data.py for implementation.

set -euo pipefail
ROOT="$(git -C "$(dirname "$0")" rev-parse --show-toplevel)"
ENV_FILE="$ROOT/.env"
[[ -f "$ENV_FILE" ]] && { set -a; source "$ENV_FILE"; set +a; }

# Delegate to Python module which handles all HTTP + auth
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
python3 "${SCRIPT_DIR}/lib/nse_data.py" "$@"
