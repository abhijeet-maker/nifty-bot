# Weekly Reviews

Friday 5:00 PM IST reviews append here. The most recent 2-3 reviews are read
by the weekly-review routine to spot trends across weeks. Older reviews stay
for long-run audit.

Each entry follows the template in `routines/weekly-review.md`, STEP 4.

A review without a **Grade** line is considered incomplete.

---

## Week ending 2026-07-10

### Stats
| Metric | Value |
|---|---|
| Starting equity (Mon 07-06 open) | ₹5,00,000.00 |
| Ending equity (Fri 07-10 close) | ₹5,00,000.00 |
| Week return | ₹0 (0.00%) |
| Nifty 50 | +0.34% |
| Alpha | -0.34% (100% cash drag) |
| Trades (W/L/open) | 0 (W:0 / L:0 / open:0) |
| Win rate | N/A (no closed trades) |
| Best trade | N/A |
| Worst trade | N/A |
| Profit factor | N/A |
| Paper capital deployed % avg | 0% |

### Closed trades this week
| Ticker | Entry | Exit | Days | P&L ₹ | P&L % | Reason |
| — | — | — | — | — | — | none |

### Open positions at week end
| Ticker | Entry | Close | Unreal % | Stop | Days held |
| — | — | — | — | — | none |

### What worked
- Discipline held: no discretionary "it looks good" entries were forced despite a 65-day-stale UNIVERSE and a full week of unresolved data outage. Capital preserved intact through a regime where the entry-gate rules literally could not be evaluated.
- Fundamentals-cache path continues to work end-to-end — Screener refresh completed cleanly (95 fresh, 4 permanent failures on LTIM/TATAMOTORS/TORNTPHARMA/ZOMATO, same as prior cycle). One net-new name (LODHA, Realty) qualified into the universe on ROCE=16.6 / ROE=15.8 / D/E=0.42.

### What didn't work
- **Scheduled cycles silent for 11 calendar days.** No pre-market or midday routine fired between 2026-06-29 and 2026-07-10. Only two runs (2026-06-29 pre-market, 2026-07-10 EOD, and this weekly review) touched the memory files this fortnight. That's not a "no signal" week — that's a scheduler / cron heartbeat failure that a downstream trader wouldn't notice from reading the journal alone.
- **Data-feed outage now 12+ days old and no manual fix has been pushed.** `nse.sh quote` still returns all-null JSON from nsepython; `nse.sh history` / `nse.sh momentum` still return HTTP 429 from Yahoo Finance across retries. `nse.sh earnings` returned `[]` for 2026-07-09 despite TCS reporting Q1 FY27 that day — likely the earnings-calendar endpoint is degraded too, not just quotes/history. The routes-forward flagged on 2026-06-29 (nsepython cookie priming, Yahoo UA/cookie rotation, or yfinance/NSE-bhav swap) have not been actioned.
- **PEAD entry window opened blind.** Q1 FY27 results season began 2026-07-09 with TCS. No PEAD scan could be run — no gap % / close-hold read possible without live price feeds, no beat/miss read possible without earnings-calendar hits. First earnings-season week of the phase, entirely missed.
- **UNIVERSE.md momentum column is now 65 days stale** and this rebuild could only refresh the fundamentals leg. The 12-1 momentum ranks in the table are frozen at 2026-05-06 — VEDL's +56% and TRENT's -37% may bear no resemblance to actual current momentum. This directly kneecaps both entry triggers (PEAD needs sector 1-month momentum; Momentum-pullback needs live 12-1 rank + DMAs + RSI).
- **Cash-drag alpha is compounding.** -0.93% today, -0.34% this week, and roughly -1.65% cumulative alpha since 2026-06-22 EOD (Nifty ~+1.65% over that ~19-session window while book stayed 100% cash). Each week of blocked routines widens the gap.
- Perplexity sectoral rotation query returned only Monday's single-day picture — could not confidently list top-3/bottom-3 weekly sectors. Note for future weekly reviews: prompt Perplexity with an explicit "Nifty sectoral indices FULL-week close-to-close" phrasing and require Fri-close numbers.

### Key lessons
- None promoted to LESSONS.md this week. The outage is operational (infrastructure / operator response), not a candidate-gate rule per LESSONS.md's own criteria ("Every lesson should end with a crisp rule the agent can apply in pre-market's candidate gate"). LESSONS.md remains empty by design.

### Adjustments for next week
- **Escalate the outage explicitly.** This week's Telegram notification will flag the data-feed outage and the 11-day silent-cycle gap as the headline items, not the ₹0 P&L. If the operator can't get to the fix, the routine keeps missing alpha.
- **Momentum column in UNIVERSE.md is now marked STALE** at the top of the file with an explicit ⚠ banner. Pre-market routines must NOT use those columns to gate an entry until the banner is removed. Fundamentals ARE fresh.
- **Bootstrap the outage-fix path when feeds recover:** in priority order — (1) `nse.sh quote` (block: nsepython silent failure), (2) `nse.sh history` (block: Yahoo 429; try yfinance-lib or UA/cookie rotation first), (3) `nse.sh earnings` (block: unclear — test independently against known-earnings dates 2026-07-09 TCS, 2026-07-10 anyone reporting).
- **No STRATEGY.md changes.** Rule churn kills edge. Two weeks of blocked cycles is a data-plane story, not a strategy story.

### Grade: C
**Rationale**: Alpha -0.34% sits inside the [-1%, 0%] band. No rule breaks — no positions were opened, so no sizing / sector-cap / pace / blackout rule could be violated. But this is a hollow C: it's "we didn't lose because we didn't play", not "we correctly held cash". The infrastructure preventing the agent from evaluating gates is the actual story of the week.

---

