# Trading Strategy — Quality Momentum + PEAD

## Mission
Beat Nifty 50 over a 90-day paper-trading window (and beyond). Generate
alpha through two documented factor edges, not prediction. Paper-trade for
first 90 days to validate the process before any real capital is at risk.

## Capital & Constraints
- Paper starting capital: ₹5,00,000
- Platform (eventual): Zerodha CNC delivery, manual execution during paper phase
- Instruments: NSE-listed stocks ONLY from the Nifty 100 index
- No F&O, no intraday, no BTST, no options, no SME, no small-caps
- Holding period: 3-12 weeks (swing)

## The Two Entry Triggers (only these two)

### Trigger 1 — PEAD (Post-Earnings Announcement Drift)
All of the following must be true:
- Stock is in current UNIVERSE.md (passed the quality screen this week)
- Beat BOTH revenue AND EPS consensus (not just one)
- Gapped up >3% on results day and held the gain (did not fade to red)
- Sector is not in 1-month drawdown (check STEP 2 of pre-market)
- Not currently held
- Results were released in the last 1-2 trading days

### Trigger 2 — Momentum pullback
All of the following must be true:
- Stock is in current UNIVERSE.md
- 12-1 month momentum in top quartile of Nifty 100 (empirically ~> 18% YoY)
- Trading above both 50 DMA and 200 DMA
- Currently 2-7% below its 20 DMA (pullback, not extended chase)
- RSI between 50 and 70 (not overbought, not broken)
- Sector is in positive 1-month momentum
- Not currently held

**Any candidate that is neither PEAD nor momentum-pullback is REJECTED.
No discretionary "it looks good" entries. Ever.**

## Hard Rules (non-negotiable)

### Position sizing
- Max 5 open positions at any time
- Max 20% of paper equity per position (= ₹1,00,000 on ₹5L account)
- Max 2 positions in the same GICS-level sector
- Target 60-80% capital deployed (30-40% cash is acceptable; 100% deployed is not)

### Entry pace
- Max 2 new entries per calendar week
- Weeks with zero trades are valid outcomes. Patience > activity.

### Risk management
- Fixed stop: -8% below entry fill price, on every position, day one
  (Paper: simulated; Live: real GTT at Zerodha)
- Trail tightening (only move stops UP, never down):
  - Up +10%: move stop to entry (breakeven)
  - Up +20%: 5% trailing below current
  - Up +35%: 3% trailing below current
- Never set a stop within 3% of current price
- Time stop: if position is flat (±3% from entry) after 8 weeks, exit at next open
- Thesis-break exit: if the reason you bought is gone (guidance cut, sector collapse,
  major regulatory action, management exit), EXIT IMMEDIATELY — do not wait for the price stop
- If a sector has 2 consecutive losing trades, exit all remaining positions in that sector

### Blackout days (no new entries)
- Indian Union Budget day (first week of Feb)
- RBI MPC decision day (6 per year — check calendar)
- US FOMC decision day (8 per year)
- Results day of any currently held position

## Quality Screen (applied weekly to rebuild UNIVERSE.md)
A Nifty 100 name is TRADABLE only if:
- ROCE (TTM) > 15%
- ROE (TTM) > 15%
- D/E < 1.0 (< 2.0 for banks, NBFCs, insurance)
- Operating cash flow positive in 3 of last 4 quarters
- Revenue growth > 10% YoY (4-quarter average)
- Promoter pledge < 20%
- No major accounting red flags (qualified audit, etc.)

Everything else is off-limits regardless of how good the story looks.

## Entry Checklist (document in JOURNAL before acting)
For every proposed trade, the research entry must include:
- Trigger type: PEAD or Momentum
- Specific catalyst (results beat numbers, or momentum rank + sector confirm)
- Sector momentum reading
- Entry price range
- Stop price (8% below planned fill)
- Target price (minimum 2:1 R:R, usually +20% first trail-tighten level)
- Position size (shares and ₹ value)
- Gate checklist all green

## Exit Checklist
For every close, log:
- Exit price and date
- Days held
- Realized P&L ₹ and %
- Reason: stop / target-trail / time-stop / thesis-break / sector-sweep
- Post-mortem tag: was this a "good loss" (rule followed) or "bad loss" (rule violated)?
  Was this a "good win" (planned) or "lucky win" (didn't really follow thesis)?

## Strategy review cadence
- Weekly review (Friday 5 PM) produces a grade and may add to LESSONS.md
- STRATEGY.md is updated at most once every 2 weeks, and only if LESSONS.md has
  an entry proven out 2+ times OR a rule has repeatedly caused pain
- Rule churn kills edge. When in doubt, do not change.
