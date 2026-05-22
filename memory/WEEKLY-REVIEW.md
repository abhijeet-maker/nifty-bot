# Weekly Reviews

Friday 5:00 PM IST reviews append here. The most recent 2-3 reviews are read
by the weekly-review routine to spot trends across weeks. Older reviews stay
for long-run audit.

Each entry follows the template in `routines/weekly-review.md`, STEP 4.

A review without a **Grade** line is considered incomplete.

---

_(Seed — first review will be written on the first Friday after launch.)_

## Week ending 2026-05-22

### Stats
| Metric | Value |
|---|---|
| Starting equity (Mon open) | ₹5,00,000.00 |
| Ending equity (Fri close) | ₹5,00,000.00 |
| Week return | ₹0 (0.00%) |
| Nifty 50 | -1.36% (Mon open 23,970.10 → Fri close 23,643.50, per Perplexity; see Notes) |
| Alpha | +1.36% (zero-deployment outperformed a down week) |
| Trades (W/L/open) | 0 (W:0 / L:0 / open:0) |
| Win rate | n/a (no closed trades) |
| Best trade | n/a |
| Worst trade | n/a |
| Profit factor | n/a |
| Paper capital deployed % avg | 0% |

### Closed trades this week
| Ticker | Entry | Exit | Days | P&L ₹ | P&L % | Reason |
|---|---|---|---|---|---|---|
| _none_ | | | | | | |

### Open positions at week end
| Ticker | Entry | Close | Unreal % | Stop | Days held |
|---|---|---|---|---|---|
| _none_ | | | | | |

### What worked (3-5 bullets)
- Discipline held: 2 pre-market scans (2026-05-19, 2026-05-22) ran the full candidate gate; zero forced entries despite week 3 of zero deployment. STRATEGY default-HOLD was respected exactly as written.
- Post-results cache invalidation worked correctly on the May 19 reporting batch: BEL ROCE refreshed 38.9 → 36.5, BPCL refreshed 16.2 → 25.7 (now passes quality screen far more comfortably), SUNPHARMA refreshed 20.2 → 22.4. No stale Q4 data leaking into next week's scans.
- Universe rebuild is stable: 38 of 95 screened names pass quality gate (prior week 37). Only one diff vs 2026-05-06 — LODHA newly enters (ROCE 16.6, ROE 15.8). Suggests scraper and quality gate are reproducible, not noisy.
- Sector-momentum read on 2026-05-22 correctly flagged "Power not explicitly hot" as an additional reason to skip ADANIPOWER — agent is layering sector context onto the entry checklist even though STRATEGY only mandates it for momentum trigger.

### What didn't work (3-5 bullets)
- VEDL data-divergence is now open across 3 consecutive cycles (2026-05-06, 2026-05-19, 2026-05-22). Live price ~₹329 against 50DMA ~₹586 and 200DMA ~₹555, yet the 12-1 momentum calc reports +65.6% YoY. Almost certainly an unadjusted corporate action (split/bonus) in the Yahoo history feed driving inflated YoY return and falsely-anchored DMAs. Cost so far: zero (the DMA gate has rejected VEDL every cycle), but VEDL falsely ranks #2 in UNIVERSE which wastes a candidate slot. **TODO before next weekly review: investigate nse.sh momentum's history source and apply adjustment factor, or flag VEDL and skip it explicitly.**
- `nse.sh earnings <DATE>` returned `[]` for every day this past week even though BEL, BPCL, SUNPHARMA, EICHERMOT, NAUKRI, TORNTPHARMA all reported. Forced-refresh logic still ran (because the routine has it hardcoded for journal-flagged names), but the underlying calendar feed is broken. If the agent stops noticing earnings entirely, PEAD trigger goes dark.
- Benchmark data for Nifty 50 week return came from Perplexity with conflicting answers across queries (-1.36% vs implied ~-0.2% from journal-recorded daily closes). Sourced -1.36% used in the table above but flagged as approximate.
- 13-day journal gap (2026-05-06 → 2026-05-19) — looks like pre-market routine didn't fire daily. No trading missed (universe was thin and choppy), but the agent's process-discipline reads worse than the trades suggest.

### Key lessons
- _(none codified to LESSONS.md this week)_ — VEDL data-divergence is a pipeline bug, not a trading rule; PEAD-calendar gap is a data wart. Neither rises to a tradable lesson yet. Will re-evaluate next Friday if either causes a real miss.

### Adjustments for next week
- Universe table now reflects the post-Q4 fundamental refresh. ADANIPOWER stays #1 momentum (+91.39%); VEDL stays #2 by momentum but is unsafe to trade (fails DMA gate AND has data integrity flag).
- Pre-market routine should explicitly track `nse.sh earnings` returning `[]` and call out the calendar staleness if it persists into next week. If the routine cannot see a reporting calendar, PEAD trigger is effectively dark and the agent should say so on Telegram rather than silently scanning to zero.
- No STRATEGY changes. Three weeks of paper trading data is far below the "2+ weeks of proven LESSONS rule" bar.

### Grade: B
**Reasoning**: Alpha +1.36% on zero deployment is mechanically a win against a down week, but it is a passive win — the strategy didn't generate it through selection. Rule violations: zero. Lesson extracted: none codified, two infrastructure issues flagged. Process discipline was correct (HOLD when no candidate qualifies); journal cadence and data-pipeline hygiene are the soft spots.

