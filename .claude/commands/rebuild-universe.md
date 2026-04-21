---
description: Manually rebuild UNIVERSE.md — quality screen on all Nifty 100 names
---

Use this before day-1 launch (the weekly-review routine will handle rebuilds
after that, but you need a populated UNIVERSE.md before the first pre-market).

1. Refresh the fundamentals cache (slow on first run — ~3-4 minutes):
```bash
bash scripts/universe-cache.sh refresh
bash scripts/universe-cache.sh status
```

2. For each symbol in the Full Nifty 100 roster in `memory/UNIVERSE.md`:
   - Read cached fundamentals: `bash scripts/universe-cache.sh get <SYM>`
   - If cache miss (exit 4), **skip this symbol** for this rebuild. Do not
     fall back to any other source — Screener is the single source of truth for
     fundamentals. A symbol with no Screener data is simply not tradable this week.
   - If passes quality screen: fetch momentum with `bash scripts/nse.sh momentum <SYM>`

   Quality screen:
   - ROCE > 15%
   - ROE > 15%
   - D/E < 1.0 (< 2.0 for names in STRATEGY.md financials list)
   - promoter_pledge_pct < 20%

3. Write the filtered universe to `memory/UNIVERSE.md`, replacing the filtered
   table. Rank survivors by `mom_12_1_pct` descending. Keep the `## Full Nifty 100 roster`
   section unchanged.

4. Commit:
```bash
git add memory/UNIVERSE.md memory/.fundamentals-cache/
git commit -m "universe rebuild $(date +%Y-%m-%d)"
```

Print summary: "X of 100 names pass quality screen. Top 5 by momentum: SYM1, SYM2, ..."
