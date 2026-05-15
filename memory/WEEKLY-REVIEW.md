# Weekly Reviews

Friday 5:00 PM IST reviews append here. The most recent 2-3 reviews are read
by the weekly-review routine to spot trends across weeks. Older reviews stay
for long-run audit.

Each entry follows the template in `routines/weekly-review.md`, STEP 4.

A review without a **Grade** line is considered incomplete.

---

## Week ending 2026-05-15

### Stats
| Metric | Value |
|---|---|
| Starting equity | ₹5,00,000 |
| Ending equity | ₹5,00,000 |
| Week return | ₹0 (0.00%) |
| Nifty 50 | +0.47% |
| Alpha | -0.47% |
| Trades (W/L/open) | 0 (W:0 / L:0 / open:0) |
| Win rate | n/a (no closes) |
| Best trade | n/a |
| Worst trade | n/a |
| Profit factor | n/a |
| Paper capital deployed % avg | 0% |

### Closed trades this week
| Ticker | Entry | Exit | Days | P&L ₹ | P&L % | Reason |
| _none_ | | | | | | |

### Open positions at week end
| Ticker | Entry | Close | Unreal % | Stop | Days held |
| _none_ | | | | | |

### What worked (3-5 bullets)
- Rule discipline held: pre-market 2026-05-06 correctly REJECTED all three top-momentum names (VEDL DMA mismatch, BEL below 50DMA, ADANIPOWER +13.7% above 20DMA — not a pullback). The default-HOLD did its job; no FOMO entries forced.
- VEDL DMA divergence flagged for Friday rather than ignored. The Friday rebuild confirmed VEDL momentum is real (+80.87%) but it remains below both DMAs — STRATEGY gate keeps it OUT despite the eye-catching number. The framework saw what intuition would have missed.
- Sector mix on this week's filtered universe is now skewed toward Metals, Capital Goods, Auto, Healthcare — same sectors that actually outperformed (Pharma +2.74%, Metals +2.04%). Quality screen + 12-1 momentum is pointing at the right rooms.
- Universe rebuild produced 38 quality survivors (within expected 25-50 band). No collapse alert needed. Cache hit rate 95/99 → ~3 Screener calls actually executed.

### What didn't work (3-5 bullets)
- Agent fired pre-market only ONCE this week (2026-05-06). Mon-Fri 2026-05-11→15 has zero journal/trade-log entries. Missing 4+ trading days of EOD snapshots breaks day-over-day P&L math going forward. Root cause: cron/trigger gap, not strategy.
- Alpha was -0.47% because Nifty drifted up while the agent sat in 100% cash. Process was correct; the cost of patience is showing up. Acceptable in a paper-validation phase, but if 4 weeks straight of zero-trade weeks compound, the strategy isn't being tested.
- Entry gates are very tight in combination: momentum AND above-both-DMAs AND 2-7% below 20DMA AND positive sector momentum. On 2026-05-06, three of the top four momentum names were rejected for DMA or extension reasons. Either the filtered universe needs a deeper bench, or the 20DMA pullback band may be too narrow when the market is trending.
- No PEAD candidates surfaced (`nse.sh earnings` returned `[]` for all 7 days). Q4 results season is largely past; PEAD trigger will be dormant until Q1FY27 results in late July. Strategy is mono-engine (momentum only) for ~2 months.

### Key lessons
- None promoted to LESSONS.md this week. One zero-trade, zero-mistake week is not a pattern. The PEAD-dormancy and entry-gate tightness observations need 2+ more weeks of evidence before becoming rules.

### Adjustments for next week
- No STRATEGY.md changes. Rule churn kills edge.
- Watchlist refreshed: top-of-list momentum-pullback candidates to monitor next week — **CGPOWER** (+18.81%, above both DMAs, in trend), **BAJAJ-AUTO** (+21.21%, above both DMAs), **BOSCHLTD** (+20.75%, above both DMAs), **NESTLEIND** (+8.48%, above both DMAs, FMCG), **APOLLOHOSP** (+11.30%, above both DMAs, healthcare = leading sector). Need a 2-7% dip below 20DMA on any of these to trigger.
- Operational: investigate why daily routines didn't fire 2026-05-11→15. If trigger config is broken, the agent will have the same problem next week.
- **VEDL watch**: now +80.87% momentum but below both DMAs. If it reclaims 50DMA next week, it becomes a clean momentum-pullback candidate. Do NOT enter early.

### Grade: C
**Rationale**: Alpha -0.47% sits in the C band (-1% to 0). Zero rule violations. Zero trades is process-correct given the gates, but an operational gap (4 missing trading days of routine execution) caps the grade — a healthy week needs daily EOD snapshots even when no trade fires.

