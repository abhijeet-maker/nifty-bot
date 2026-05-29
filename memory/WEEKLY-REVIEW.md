# Weekly Reviews

Friday 5:00 PM IST reviews append here. The most recent 2-3 reviews are read
by the weekly-review routine to spot trends across weeks. Older reviews stay
for long-run audit.

Each entry follows the template in `routines/weekly-review.md`, STEP 4.

A review without a **Grade** line is considered incomplete.

---

_(Seed — first review will be written on the first Friday after launch.)_

---

## Week ending 2026-05-29

### Stats
| Metric | Value |
|---|---|
| Starting equity | ₹5,00,000.00 |
| Ending equity | ₹5,00,000.00 |
| Week return | ₹0 (0.00%) |
| Nifty 50 | +1.07% (23,654.70 → 23,907.15) |
| Alpha | -1.07% |
| Trades (W/L/open) | 0 (W:0 / L:0 / open:0) |
| Win rate | N/A (no closed trades) |
| Best trade | N/A |
| Worst trade | N/A |
| Profit factor | N/A |
| Paper capital deployed % avg | 0% |

### Closed trades this week
| Ticker | Entry | Exit | Days | P&L ₹ | P&L % | Reason |
| _none_ | | | | | | |

### Open positions at week end
| Ticker | Entry | Close | Unreal % | Stop | Days held |
| _none — still 100% cash_ | | | | | |

### What worked
- Discipline held. Three pre-market scans (2026-05-06, 2026-05-19, 2026-05-22) and every UNIVERSE leader was correctly rejected for failing the DMA gate or the 2-7% pullback window. No "it looks good" entries crept in.
- ADANIPOWER was repeatedly the cleanest setup but never entered the pullback zone — correctly held back rather than chased on breakout. Rule did its job.
- Cache + Screener pipeline ran clean; rebuild took ~3 min, 38 of 99 names pass the quality screen (well within the 25-50 expected band, far above the 15-name collapse threshold).
- **VEDL "divergence" turned out to be stale-UNIVERSE rot, not a feed bug.** Today's rebuild resyncs VEDL to mom -39.05% / below both DMAs — fully coherent with the live ₹352.6 vs ₹549/₹553 DMAs (a real drawdown story, not a corporate-action error). The 3-cycle flag in the journal correctly identified the problem; the fix was rebuilding the table on schedule.

### What didn't work
- **0% deployed during a +1.07% Nifty week → -1.07% alpha**. Process-correct, but the entry gates as currently calibrated produced zero candidates for the third week running. Not a rule break; a rule-outcome to watch.
- **UNIVERSE.md was 23 days stale** (last rebuild 2026-05-06). Within the 30-day TTL, but the May 22 journal already flagged it as overdue. Symptom: VEDL kept ranking #1 by stale mom +56.75% while live momentum was deeply negative. Lesson is timeliness, not data integrity.
- **Pre-market routine did NOT fire this week** (last journal entry is 2026-05-22 — Friday last week). Mon-Thu of this week have no decision trail. Whether the cron missed or the routine silently produced no candidates, the journal should reflect each scan attempt.

### Key lessons
- Nothing genuinely new (one week of zero-trade paper data is insufficient for a durable rule). LESSONS.md left untouched. The VEDL flag dissolved on rebuild.

### Adjustments for next week
- **Audit the pre-market schedule.** Confirm whether the routine fired Mon-Thu 2026-05-25 to 2026-05-28 and silently produced no candidates, or whether the cron didn't trigger. Either way, the journal should show evidence of a scan, even on no-trade days.
- **Consider tightening the UNIVERSE TTL.** 30-day cache works for fundamentals but momentum staleness within a stale UNIVERSE table is the real risk. Worth weighing a mid-week mini-rebuild (momentum + DMA only — no Screener calls) if pre-market keeps citing UNIVERSE leaders whose live DMAs disagree.
- No strategy rule changes. One sub-benchmark week is not signal.

### Grade: D
**Reasoning**: Alpha was -1.07%, just inside the D band (-1% to -3%). No rule break — every gate worked as designed and there were genuinely no qualifying setups. But D is the honest grade by the published criteria; rewarding "correct rejections" with a higher letter would erode the alpha discipline this scorecard exists to enforce. Process A, outcome D. Expected over a 90-day window: more weeks like this when the universe is in a broad pullback. Hold the line.

