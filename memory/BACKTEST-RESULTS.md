# Backtest results — momentum pullback (MVP)

**Period:** 2024-01-01 -> 2024-12-31
**Run date:** 2026-05-06
**Universe:** top 50 Nifty 100 names by market cap, quality-screened
**Signal:** momentum-pullback only (no PEAD in v1)
**Decision: EDGE EXISTS — proceed to paper trading**

## Key metrics

| Metric | Value |
|---|---|
| Starting equity | ₹500,000 |
| Ending equity | ₹660,401 |
| Total return | +32.08% |
| CAGR | +32.11% |
| **Sharpe (annualized)** | **1.34** |
| **Max drawdown** | **-17.14%** |
| Calmar | 1.87 |
| Trades closed | 9 |
| Win rate | 55.6% (5W / 4L) |
| Avg winner | +39.09% |
| Avg loser | -8.22% |
| Profit factor | 6.03 |
| Nifty 50 buy & hold | +10.04% |
| **Alpha vs Nifty 50** | **+22.04%** |

## Equity curve

```
▁▁▁▁▁▁▁▁▁▁▁▂▂▂▂▂▂▃▂▃▃▃▃▄▅▄▄▅▆▆▆▆▆▆▅▅▄▅▆▆▆▆▆▇▆▇▇▇▇▆▅▅▅▅▄▅▅▅▆▅
```

## Best 5 trades

| Symbol | Entry | Exit | Bars | P&L % | Reason |
|---|---|---|---|---|---|
| TRENT | 2024-01-30 | 2024-12-31 | 227 | +132.10% | end-of-backtest |
| HAL | 2024-03-13 | 2024-12-31 | 197 | +36.84% | end-of-backtest |
| BEL | 2024-06-04 | 2024-12-31 | 144 | +14.19% | end-of-backtest |
| BAJAJ-AUTO | 2024-02-29 | 2024-12-31 | 205 | +10.73% | end-of-backtest |
| LODHA | 2024-01-24 | 2024-10-22 | 182 | +1.59% | time-stop |

## Worst 5 trades

| Symbol | Entry | Exit | Bars | P&L % | Reason |
|---|---|---|---|---|---|
| HINDZINC | 2024-11-06 | 2024-12-20 | 30 | -9.05% | stop |
| IRCTC | 2024-05-10 | 2024-06-04 | 16 | -8.81% | stop |
| APOLLOHOSP | 2024-02-28 | 2024-05-08 | 44 | -8.53% | stop |
| VEDL | 2024-12-23 | 2024-12-31 | 6 | -6.51% | end-of-backtest |
| LODHA | 2024-01-24 | 2024-10-22 | 182 | +1.59% | time-stop |

## Decision rule (from plan)

- Sharpe > 0.8 -> edge exists, proceed to paper trading
- Sharpe 0.4–0.8 -> marginal; build full-rule backtest before going live
- Sharpe < 0.4 -> rules don't work in Indian markets; revisit STRATEGY.md

## Out of scope (future v2)

- PEAD signal (needs historical earnings-date lookup)
- Trail tightening at +10%/+20%/+35% milestones
- Sector momentum filter
- Blackout calendar (FOMC, RBI, Budget)
- Multi-year window (2022 chop, 2023 bull, 2024 mixed)
- Walk-forward / out-of-sample testing
