# Weekly Reviews

Friday 5:00 PM IST reviews append here. The most recent 2-3 reviews are read
by the weekly-review routine to spot trends across weeks. Older reviews stay
for long-run audit.

Each entry follows the template in `routines/weekly-review.md`, STEP 4.

A review without a **Grade** line is considered incomplete.

---

_(Seed — first review will be written on the first Friday after launch.)_

## Week ending 2026-06-05

### Stats
| Metric | Value |
|---|---|
| Starting equity | ₹5,00,000.00 |
| Ending equity | ₹5,00,000.00 |
| Week return | ₹0 (0.00%) |
| Nifty 50 | -0.56% (23,547.75 → 23,416.55) |
| Alpha | +0.56% (held cash during a down week) |
| Trades (W/L/open) | 0 (W:0 / L:0 / open:0) |
| Win rate | N/A (no closed trades) |
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
| _none_ | | | | | |

### Benchmark context
- Nifty 50: Fri 5/29 close 23,547.75 → Fri 6/5 close 23,416.55 = **-0.56%**
- Sector readout (week): IT +2.66%, Media +1.37%, Metal +0.49% led; FMCG -2.30%, PSU Bank -1.85%, Realty -1.83% lagged
- No FOMC, no RBI MPC, no Union Budget this week → no blackout days hit

### What worked (3-5 bullets)
- Rule discipline: every pre-market scan rejected all candidates because none cleared both the DMA and pullback gates. Zero trades is a valid outcome per STRATEGY.md, and patience preserved ₹5,00,000 cash during a -0.56% Nifty week.
- Tonight's UNIVERSE rebuild **resolved the 3-cycle VEDL data anomaly** flagged in journal (2026-05-06, 05-19, 05-22). With fresh momentum, VEDL collapsed from +56.75% rank-1 to -31.69% rank-last and now sits below both DMAs. The DMA gate had been correctly screening it out the whole time — defense-in-depth worked.
- Universe screen produced 38 names (vs 37 last rebuild) — well inside the 25-50 expected band. Quality screen healthy, no scraper drift.

### What didn't work (3-5 bullets)
- **0% capital deployed** sits below the 60-80% STRATEGY target. Justified by gate logic this week, but if 3 more weeks pass with zero entries the **trigger definitions themselves** may be too strict for the current regime (most UNIVERSE leaders below 50DMA after April-May drawdown — narrow pullback window collapses to nothing).
- **Journal coverage gap**: no pre-market entries Mon-Thu (June 1-4). Either the cron didn't fire or pre-market routines aren't appending. Needs investigation outside this routine — cannot self-diagnose from inside the review.
- Sector momentum read this week skewed defensive vs IT-led — strict sector-momentum gate would have rejected most setups anyway. No edge missed.

### Key lessons
- None codified this week. VEDL momentum-feed glitch was caught by the live DMA gate every time; the system worked as designed, no new rule warranted.

### Adjustments for next week
- No rule changes. Week 1 is far too early to tweak STRATEGY.md.
- Watchlist focus for next week: **ADANIPOWER** (Power, +106.88%, above both DMAs — only true momentum leader; watch for 2-7% pullback zone around 20DMA), **CGPOWER** (Capital Goods, +28.78%, above both DMAs), **TITAN** (Cons Durables, +28.10%, above both DMAs), **BAJAJ-AUTO** (Auto, +25.09%, above both DMAs), **NESTLEIND** (FMCG, +23.98%, above both DMAs).
- Auto sector now has 3 names above both DMAs (BAJAJ-AUTO, BOSCHLTD, EICHERMOT/HEROMOTOCO partial) — respect the 2-per-sector cap if multiple PEAD/pullback signals fire.
- Q1FY27 results season starts mid-July → expect PEAD triggers to reappear ~6-8 weeks out. No earnings on the tape this week.

### Grade: B
**Justification**: Alpha +0.56% (> 0), zero rule violations, but alpha was passive (cash beat a down market) rather than earned. Not an A — no positive lesson was extracted, no edge was demonstrated, and the deployed % is at the floor. Solid B for discipline.
