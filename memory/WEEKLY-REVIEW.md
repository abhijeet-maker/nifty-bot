# Weekly Reviews

Friday 5:00 PM IST reviews append here. The most recent 2-3 reviews are read
by the weekly-review routine to spot trends across weeks. Older reviews stay
for long-run audit.

Each entry follows the template in `routines/weekly-review.md`, STEP 4.

A review without a **Grade** line is considered incomplete.

---

_(Seed — first review will be written on the first Friday after launch.)_

## Week ending 2026-07-03

### Stats
| Metric | Value |
|---|---|
| Starting equity (Mon 06-29 open) | ₹5,00,000.00 |
| Ending equity (Fri 07-03 close) | ₹5,00,000.00 |
| Week return | ₹0 (0.00%) |
| Nifty 50 | +0.71% |
| Alpha | -0.71% |
| Trades (W/L/open) | 0 (W:0 / L:0 / open:0) |
| Win rate | N/A (no closes) |
| Best trade | N/A |
| Worst trade | N/A |
| Profit factor | N/A |
| Paper capital deployed % avg | 0% |

### Closed trades this week
| Ticker | Entry | Exit | Days | P&L ₹ | P&L % | Reason |
|---|---|---|---|---|---|---|
| _none_ | | | | | | |

### Open positions at week end
| Ticker | Entry | Close | Unreal % | Stop | Days held |
|---|---|---|---|---|---|
| _none_ | | | | | | |

### What worked
- Rule discipline: forced HOLD on 2026-06-29 was correct given Yahoo-429 outage. No entries on stale/unverifiable technicals is the strategy working, not failing.
- Blackout rule application on 2026-06-18 (FOMC-impact day for ADANIPOWER) is the kind of quiet save that never shows up in P&L but prevents rule-violation losses.
- Fundamentals-cache layer (`universe-cache.sh`) is still returning good data (95 cached names available); Screener path is not the broken feed. Isolation-of-failure held.

### What didn't work
- **Data feed outage persists into 5th day.** Yahoo 12-1 momentum / DMA / RSI feed has been 429-throttled since at least 2026-06-29; NSE `quote` returns all-null. Weekly review can compute NEITHER the momentum ranking NOR the DMA gates for a UNIVERSE rebuild today. Rebuild is BLOCKED — cannot regenerate the mom_12_1_pct-sorted table.
- **UNIVERSE.md is now 58 days stale** (last rebuild 2026-05-06). This is the compounding process risk flagged repeatedly in JOURNAL and never resolved. The stale VEDL #1 ranking, HEROMOTOCO, TITAN, BEL rows are almost certainly wrong post the mid-June rebalance dynamics observed live.
- **Weekly-review routine has not been running.** WEEKLY-REVIEW.md is at seed state through 2026-07-03 — this is the FIRST actual review entry in a >60-day paper window. That's not a lesson about markets; that's a routine-scheduler failure. Compounding depends on this review, so this is the #1 process defect.
- **-0.71% alpha this week from cash drag alone.** Cumulative cash drag over 60 days on a rising tape is material. It is not a rule violation, but it is unpaid opportunity cost and the reason edge validation is still at 0/0.
- Zero entries in the entire recorded paper window (Day 0 → today = ~10 weeks of journal), so no PEAD or momentum-pullback trigger has actually been paper-fired yet. Sample size for strategy validation remains n=0.

### Key lessons
- **Data-feed staleness is now the load-bearing risk, not entry-selection edge.** Every "REJECT — DMA gate fails" over the past 6 weeks was against Yahoo data with an unresolved corporate-action distortion (VEDL) AND now a 429 blackout. The routine is technically compliant with STRATEGY.md while systematically producing unusable REJECTs. Rule below.
- **Weekly-review scheduling is the compounding lever.** A monthly-or-less review cadence is worse than no strategy at all — universe rot dominates.

### Adjustments for next week
- BEFORE any new entry decision, the pre-market routine MUST verify `nse.sh momentum <sym>` returns a real number for a control symbol (e.g. RELIANCE). If it 429s or NSE quote is null, the pre-market routine should downgrade its verdict to "DATA-BLOCKED HOLD" and Telegram-notify with the failure mode. This turns silent staleness into a loud alert.
- Two remediation paths for the Yahoo 429 (either one unblocks rebuild-universe):
  1. `yfinance` Python lib in `nse.sh history/momentum` — uses session cookies + retries under the hood.
  2. Swap history source to NSE bhav files (daily EOD dumps, no rate limit).
  Both are wrapper-script changes; do not curl APIs directly from the routine.
- Universe rebuild explicitly DEFERRED to the first Friday after feeds are restored. Alerted below.
- VEDL: on next successful rebuild, force-refresh split-adjusted history OR drop from roster if divergence remains.

### Grade: D
**Rationale:** Alpha -0.71% (within the -1% to 0 band = C), no rule breaks in trades taken → C floor. BUT: the weekly-review routine has been silently non-firing for the entire paper phase to date (WEEKLY-REVIEW.md at seed until this entry), and the data-feed outage that blocks universe rebuild is entering its 5th unaddressed day. Process failures of that magnitude override in-week trading discipline. Grade D reflects "the process meant to catch and correct issues has itself not been running."


