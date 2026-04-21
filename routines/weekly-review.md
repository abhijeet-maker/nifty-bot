You are the equity research agent running the **weekly review** on Friday at
5:00 PM IST. This is the most important routine — it's where the agent LEARNS.
Compounding depends on this file being honest and sharp. PAPER MODE.
`DATE=$(date +%Y-%m-%d)`.

# ENVIRONMENT + PERSISTENCE
Same rules. No .env. Must commit+push at STEP 9.

# STEP 1 — Load the whole week
```bash
cat memory/STRATEGY.md
cat memory/LESSONS.md
cat memory/PORTFOLIO.md
cat memory/UNIVERSE.md
# Grab this week's journal entries (Mon-Fri)
awk '/^## '"$(date -d 'last monday' +%Y-%m-%d)"'/,0' memory/JOURNAL.md
# Grab this week's trade log entries
awk '/^## '"$(date -d 'last monday' +%Y-%m-%d)"'/,0' memory/TRADE-LOG.md
tail -n 400 memory/WEEKLY-REVIEW.md   # last 2-3 weekly reviews for trend context
```

# STEP 2 — Benchmark data
```bash
bash scripts/perplexity.sh "Nifty 50 weekly return, week ending $DATE. Starting level Monday open, Friday close, percentage. Also Bank Nifty weekly return."
bash scripts/perplexity.sh "Which Nifty sectoral indices outperformed and underperformed this week ending $DATE? Top 3 and bottom 3 with numbers."
```

# STEP 3 — Compute week stats
From this week's data in TRADE-LOG:
- Starting equity (Mon open EOD snapshot)
- Ending equity (today's EOD)
- Week return ₹ and %
- Nifty 50 week return (from STEP 2)
- Alpha: week return - Nifty
- Trades taken: new entries this week (from JOURNAL)
- Closed trades this week: W / L / count
- Win rate (closed only): wins / (wins + losses)
- Best trade of week (by realized % if closed, else unrealized %)
- Worst trade of week
- Profit factor: sum(winner P&L) / |sum(loser P&L)|

# STEP 4 — Append to WEEKLY-REVIEW.md
```markdown
## Week ending $DATE

### Stats
| Metric | Value |
|---|---|
| Starting equity | ₹X,XX,XXX |
| Ending equity | ₹X,XX,XXX |
| Week return | ±₹X,XXX (±X.X%) |
| Nifty 50 | ±X.X% |
| Alpha | ±X.X% |
| Trades (W/L/open) | N (W:X / L:Y / open:Z) |
| Win rate | XX% |
| Best trade | SYMBOL +X.X% |
| Worst trade | SYMBOL -X.X% |
| Profit factor | X.XX |
| Paper capital deployed % avg | XX% |

### Closed trades this week
| Ticker | Entry | Exit | Days | P&L ₹ | P&L % | Reason |

### Open positions at week end
| Ticker | Entry | Close | Unreal % | Stop | Days held |

### What worked (3-5 bullets)
- <specific, not generic — e.g. "PEAD on HDFCBANK caught the 3-day drift after Q4 beat — +4.2% in 3 days">

### What didn't work (3-5 bullets)
- <specific — e.g. "Cut TCS at -8% after 2 days; thesis was 'IT sector recovery' but sector was still rolling over. Should have checked sector momentum more carefully in pre-market.">

### Key lessons
- <if any — these feed LESSONS.md>

### Adjustments for next week
- <any rule tweaks, watchlist changes>

### Grade: <A-F>
**Criteria**:
- A: Alpha > +1.5% AND ≤1 rule violation AND positive lesson extracted
- B: Alpha > 0 AND ≤1 rule violation
- C: Alpha between -1% and 0, no major rule break
- D: Alpha -1% to -3%, or one major rule break (like sizing)
- F: Alpha < -3%, or major rule break (took an option, exceeded position cap, etc.)
```

# STEP 5 — Update LESSONS.md (only if genuinely learned something)
If this week revealed a durable mistake pattern, add ONE bullet to LESSONS.md
(max 20 bullets total — prune oldest if over):

```markdown
- 2026-04-25: Entered TCS on Q4 beat but IT sector was down 3% that week.
  Sector momentum overrides individual catalyst. **Rule: reject PEAD if sector
  1-month return is negative.**
```

Do NOT add a lesson if nothing genuinely new was learned. LESSONS.md bloat kills its utility.

# STEP 6 — Consider STRATEGY.md updates
If a rule has been proven out over 2+ weeks (e.g. new rule from LESSONS repeatedly
applied and prevented a loss), codify it in STRATEGY.md and call it out in the review.
If a rule has repeatedly caused bad outcomes, propose removing/modifying it.
**Be conservative — don't tweak rules weekly. This is an anti-pattern.**

# STEP 7 — Rebuild UNIVERSE.md (cache-aware)
The fundamentals cache has a 30-day TTL — so on any given Friday only ~25% of
names need to be re-scraped (the stale ones + any that reported this week).

```bash
# Refresh stale cache entries (most are fresh — this is cheap)
bash scripts/universe-cache.sh refresh

# Also forcibly refresh any symbol that reported earnings in the past 7 days,
# because their ROCE/ROE TTM will have updated
for d in 0 1 2 3 4 5 6; do
  YMD=$(date -d "$d days ago" +%Y-%m-%d)
  bash scripts/nse.sh earnings "$YMD" | python3 -c "
import json, sys
try:
  for e in json.load(sys.stdin):
    print(e['symbol'])
except: pass
"
done | sort -u | while read SYM; do
  # Delete cache file to force re-scrape on next 'get'
  rm -f "memory/.fundamentals-cache/${SYM}.json"
  bash scripts/universe-cache.sh get "$SYM" > /dev/null || true
done
```

For every symbol in the Full Nifty 100 roster:
```bash
FUND=$(bash scripts/universe-cache.sh get "$SYM" 2>/dev/null) || {
  # Screener failed (parse error, network, or rate-limit). Skip this symbol
  # for this cycle — it cannot be traded until Screener data is available again.
  echo "Skipping $SYM: fundamentals unavailable from Screener"
  continue
}
MOM=$(bash scripts/nse.sh momentum "$SYM")
```

Apply the quality screen:
- ROCE > 15% AND ROE > 15%
- D/E < 1.0 (< 2.0 for financials — see STRATEGY.md sector list)
- promoter_pledge_pct < 20%

Drop survivors into the filtered table in UNIVERSE.md, ranked by mom_12_1_pct descending.
Keep `## Full Nifty 100 roster` section UNCHANGED.

**Universe-collapse safety net**: count how many names pass the screen. Expected
range: 25-50. If fewer than 15 survive, the Screener parser is likely broken
(HTML layout changed). Send an urgent alert:

```bash
if [[ $PASS_COUNT -lt 15 ]]; then
  bash scripts/telegram.sh "🚨 UNIVERSE COLLAPSE
Only $PASS_COUNT of 100 names pass quality screen.
Normal range 25-50. Screener scraper likely broken.
Agent will have no candidates this week.
Action: check scripts/screener.sh parser, run /smoke-test locally."
fi
```

**Budget**: with caching, expect ~20-30 actual Screener calls + 100 momentum calls.
Momentum calls hit Yahoo Finance — which is free and unrate-limited. Total routine
runtime ~8-12 min on a good day.

# STEP 8 — Telegram weekly summary
```bash
bash scripts/telegram.sh "📅 Week ending $DATE
Equity: ₹X,XX,XXX (week ±X.X%, phase ±X.X%)
vs Nifty 50 (±X.X%): alpha ±X.X%
Trades: N (W:X / L:Y / open:Z), Win rate: XX%
Best: SYM +X%  Worst: SYM -X%
PF: X.XX
Lesson: <one line or 'none this week'>
Grade: <letter>"
```

# STEP 9 — COMMIT AND PUSH
```bash
cd "$(git rev-parse --show-toplevel)"
git add memory/
git commit -m "weekly review $DATE"
git push origin main || { git pull --rebase origin main && git push origin main; }
```
