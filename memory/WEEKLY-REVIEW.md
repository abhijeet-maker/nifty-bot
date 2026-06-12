# Weekly Reviews

Friday 5:00 PM IST reviews append here. The most recent 2-3 reviews are read
by the weekly-review routine to spot trends across weeks. Older reviews stay
for long-run audit.

Each entry follows the template in `routines/weekly-review.md`, STEP 4.

A review without a **Grade** line is considered incomplete.

---

_(Seed — first review will be written on the first Friday after launch.)_

## Week ending 2026-06-12

### Stats
| Metric | Value |
|---|---|
| Starting equity | ₹5,00,000.00 |
| Ending equity | ₹5,00,000.00 |
| Week return | ₹0 (0.00%) |
| Nifty 50 | -0.11% |
| Alpha | +0.11% |
| Trades (W/L/open) | 0 (W:0 / L:0 / open:0) |
| Win rate | N/A (no closes) |
| Best trade | none |
| Worst trade | none |
| Profit factor | N/A |
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
- **Patience held the line.** Five pre-market scans across the launch phase (May 6 → Jun 12) all returned HOLD because no candidate passed both UNIVERSE quality AND entry gates. Default-action discipline (STRATEGY: "patience > activity") preserved capital while Nifty drifted -0.11% on the week.
- **Sector breadth scan caught the right thing this week.** Top-3 sectors (Bank +1.60%, Pharma +0.53%, FMCG positive) vs bottom-3 (Metal -5.23%, IT -5.05%, Energy -4.43%). UNIVERSE momentum leaders are concentrated in Auto, Capital Goods, Power, Healthcare — exactly the cohort the strategy is biased toward.
- **VEDL data divergence resolved organically.** The unadjusted-corporate-action divergence flagged in journal across 2026-05-06, 2026-05-19, 2026-05-22 has now corrected: VEDL momentum reads -28.27% (was +56.75% on 2026-05-06 UNIVERSE) with both DMAs below price. Whatever historical-feed quirk caused the inflated 12-1 has cycled out — no code change needed, and VEDL has correctly dropped out of the tradable momentum cohort.

### What didn't work (3-5 bullets)
- **Zero trades is the correct outcome but not a celebrated one.** Five scans, zero entries means the strategy is currently very narrow given the tape. ADANIPOWER (the cleanest momentum leader, now +85.66%) was rejected three times — twice for being extended (not in 2-7% pullback zone), once for sector not confirmed. If ADANIPOWER never pulls back, the strategy will sit on the sidelines through its run.
- **No PEAD candidates surfaced.** Several UNIVERSE names reported (BAJAJ-AUTO, GODREJCP on May 5; BEL, BPCL on May 18; SUNPHARMA, EICHERMOT, NAUKRI, TORNTPHARMA on May 21) but no agent-detected PEAD trigger fired. Need to verify next week: are these earnings being missed by `nse.sh earnings` returning empty arrays, or are none of them actually meeting the +3%/beat-both gate? The empty-earnings results pattern is suspicious.
- **All banks/NBFCs structurally excluded.** ROCE gate (> 15%) gates out HDFCBANK (7.04%), ICICIBANK (7.2%), SBIN (6.47%), AXISBANK (6.24%), KOTAKBANK (6.93%), BAJFINANCE (10.8%). With Nifty Bank the week's top performer (+1.60%), this is a real opportunity cost. Documented in UNIVERSE.md as a known structural quirk; not changing the rule on one week's evidence.

### Key lessons
- None new this week. The "earnings calendar returns empty" pattern is a candidate observation but not yet a confirmed lesson — needs one more week of verification before it qualifies for LESSONS.md.

### Adjustments for next week
- **Verify `nse.sh earnings` is actually returning data.** If it remains empty for known-results dates next week, escalate to a smoke-test of the wrapper and Perplexity-cross-check the PEAD scan for UNIVERSE names that reported. Do NOT add a rule yet — could be calendar wrapper bug, not strategy weakness.
- **Watch ADANIPOWER for the pullback window** (₹205-215 zone = 2-7% under 20DMA). It is now +85.66% momentum, above both DMAs, in a sector that wasn't on the top-3 list this week but isn't in the bottom-3 either. First clean pullback into the zone is the textbook setup.
- **No STRATEGY.md changes.** Five weeks is too early for rule churn. Re-evaluate after 4-6 more weeks of data.

### Grade: **B**
Alpha +0.11% (positive, modest) and zero rule violations. Cash-held the week through Nifty's slight pullback. No genuine new lesson — review captures observations but does not bloat LESSONS.md. Per criteria (Alpha > 0 AND ≤1 rule violation), this is a B. The grade would be A only if a planned, deliberate setup had been entered and worked — which is not the case yet.

