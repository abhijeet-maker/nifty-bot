# Weekly Reviews

Friday 5:00 PM IST reviews append here. The most recent 2-3 reviews are read
by the weekly-review routine to spot trends across weeks. Older reviews stay
for long-run audit.

Each entry follows the template in `routines/weekly-review.md`, STEP 4.

A review without a **Grade** line is considered incomplete.

---

_(Seed — first review will be written on the first Friday after launch.)_

## Week ending 2026-05-08

_First weekly review of paper-trading phase. Live runs began Wed May 6._

### Stats
| Metric | Value |
|---|---|
| Starting equity | ₹5,00,000 |
| Ending equity | ₹5,00,000 |
| Week return | ₹0 (0.00%) |
| Nifty 50 | +0.83% (23,997.55 → 24,196.75) |
| Alpha | -0.83% |
| Trades (W/L/open) | 0 (W:0 / L:0 / open:0) |
| Win rate | N/A (no closes) |
| Best trade | N/A |
| Worst trade | N/A |
| Profit factor | N/A |
| Paper capital deployed % avg | 0% |

### Closed trades this week
| Ticker | Entry | Exit | Days | P&L ₹ | P&L % | Reason |
| _none_ | | | | | | |

### Open positions at week end
| Ticker | Entry | Close | Unreal % | Stop | Days held |
| _none_ | | | | | |

### What worked
- Discipline. May 6 pre-market correctly rejected all three momentum candidates (VEDL, BEL, ADANIPOWER) for failing gates. STRATEGY.md "must be above BOTH 50/200 DMA" and "2-7% below 20DMA" rules did their job — kept us out of stale-universe trades.
- VEDL anomaly (passed UNIVERSE on Apr 24 with +56.75% mom and Yes/Yes DMAs, but live on May 5 was ₹303.9 vs 50DMA ₹677.94) was caught at the candidate-gate stage rather than acted on. Likely a corporate action / split between rebuilds; demonstrates value of the live-DMA recheck.
- Cache-aware UNIVERSE rebuild and Screener fundamentals fix from late April held — 37/95 names passed quality screen, well within the 25-50 expected band.

### What didn't work
- One missed opportunity cost: Nifty +0.83%, we sat 100% cash → -0.83% alpha. Acceptable for week 1 (rule-following beats lucky entries), but a reminder that "no candidates" is not free — patience has a price tag.
- Coverage gap: pre-market routine only ran on Wed May 6. No Mon/Tue/Thu/Fri pre-market entries in JOURNAL. Either the cron didn't fire on those days or routines weren't invoked. Need to confirm scheduler health before next week.
- PEAD scan returned nothing all week. `nse.sh earnings 2026-05-05` returned empty — but BAJAJ-AUTO and GODREJCP did report on May 6. The follow-up scan on May 7 (would have been the PEAD day) was not run because there is no May 7 journal entry.

### Key lessons
- None yet. Zero trades = zero post-mortem material. The May 6 candidate-gate rejections were textbook STRATEGY application, not new learning.

### Adjustments for next week
- **Operational**: confirm pre-market cron runs Mon-Fri before next Monday. Missing days = missing PEAD windows (results-day +1 trigger has a 1-2 trading day shelf life).
- **VEDL stale-data investigation**: Apr 24 UNIVERSE rebuild had VEDL above both DMAs at +56.75% mom; May 5 live was below both with price ₹303.9 vs 50DMA ₹677.94 — that's a >2x divergence. Almost certainly a corporate action (split/spin-off) the momentum script didn't adjust for. This Friday's UNIVERSE rebuild should resolve it; flag for next week's pre-market if still anomalous.
- No STRATEGY.md or LESSONS.md changes. Too early.

### Grade: C
Alpha -0.83% (within -1% to 0% band), zero rule violations, zero trades. A clean "patient" week — exactly what STRATEGY says is acceptable. Not graded higher because alpha is negative; not graded lower because the discipline was correct.
