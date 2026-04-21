#!/usr/bin/env bash
# Paper trading helper. Simulates fills with realistic slippage.
# The agent calls this when it wants to "execute" a paper trade.
# It returns a JSON fill record that the agent then appends to PORTFOLIO.md
# and TRADE-LOG.md.
#
# Usage:
#   bash scripts/paper.sh buy HDFCBANK 15 1650.00    # 15 shares at approx ₹1650
#   bash scripts/paper.sh sell HDFCBANK 15 1518.00   # exit (stop hit, target hit, or thesis break)
#
# Slippage model:
#   Buy  -> fill = quoted * (1 + slippage_pct/100)   (you pay slightly above mid)
#   Sell -> fill = quoted * (1 - slippage_pct/100)   (you receive slightly below mid)
# Default slippage: 0.15% (typical for Nifty 100 at retail size on Zerodha).
# STT/brokerage/GST/stamp: 0.11% round-trip for CNC delivery on Zerodha.

set -euo pipefail

side="${1:?usage: paper.sh <buy|sell> SYMBOL QTY PRICE}"
sym="${2:?symbol required}"
qty="${3:?quantity required}"
price="${4:?price required}"
slippage_pct="${SLIPPAGE_PCT:-0.15}"

python3 - <<PY
import json
from datetime import datetime, timezone, timedelta

side = "$side"
sym = "$sym"
qty = int("$qty")
quoted = float("$price")
slip = float("$slippage_pct") / 100.0

# Slippage direction
if side == "buy":
    fill_price = round(quoted * (1 + slip), 2)
elif side == "sell":
    fill_price = round(quoted * (1 - slip), 2)
else:
    raise SystemExit(f"side must be buy or sell, got {side}")

# Costs (one-way) — rough for CNC delivery on Zerodha
# STT: 0.1% (sell side only for delivery, but we model half each way for simplicity)
# Exchange + SEBI + stamp + GST on brokerage ≈ 0.015% per side
# Zerodha CNC brokerage = 0 (free delivery)
cost_pct = 0.055 if side == "buy" else 0.105  # buy side lighter, sell side has STT
gross = fill_price * qty
costs = round(gross * cost_pct / 100, 2)
net = round(gross + costs if side == "buy" else gross - costs, 2)

# IST timestamp
ist = timezone(timedelta(hours=5, minutes=30))
now = datetime.now(ist).strftime("%Y-%m-%d %H:%M IST")

print(json.dumps({
    "timestamp": now,
    "side": side,
    "symbol": sym,
    "qty": qty,
    "quoted_price": quoted,
    "fill_price": fill_price,
    "slippage_pct": float("$slippage_pct"),
    "gross_inr": round(gross, 2),
    "costs_inr": costs,
    "net_inr": net,
    "mode": "PAPER",
}, indent=2))
PY
