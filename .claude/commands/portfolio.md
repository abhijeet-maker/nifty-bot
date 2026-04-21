---
description: Read-only snapshot of current paper portfolio with live marks
---

Print a clean ad-hoc portfolio snapshot. No state changes. No file writes.

1. Read `memory/PORTFOLIO.md` for current positions
2. For each open position, call `bash scripts/nse.sh quote <SYM>` to get live price
3. Compute unrealized P&L in ₹ and %
4. Print as a single table

Format:
```
Portfolio — <today's date IST>

Paper equity: ₹X,XX,XXX | Cash: ₹X,XX,XXX (X%) | Deployed: X%
Open positions: N of 5 max | Trades this week: N of 2 max

| Symbol | Sector | Qty | Entry | Live | Unreal % | Unreal ₹ | Stop | Dist to stop |

Sector exposure: <per-sector count line>
```

Only flag (in a short "Concerns" block below the table) if:
- Any position is within 2% of its stop
- Any position has been held > 8 weeks (time-stop breach)
- Total deployed > 85% (over cap)

Otherwise just print the table and stop.
