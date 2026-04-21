---
description: Day-0 smoke test — verify all wrappers and external services are reachable
---

Run before creating any cloud routines. Catches credential and connectivity
problems on your machine instead of at 8:15 AM tomorrow.

Execute each test and print PASS/FAIL for each:

### 1. Env vars
```bash
for v in PERPLEXITY_API_KEY TELEGRAM_BOT_TOKEN TELEGRAM_CHAT_ID; do
  [[ -n "${!v:-}" ]] && echo "  $v: set" || echo "  $v: MISSING"
done
```

### 2. NSE quote (should return JSON with last/open/close)
```bash
bash scripts/nse.sh quote RELIANCE
```
Expect: JSON with non-null `last` price around current market level.

### 3. NSE history (should return ~250 rows)
```bash
bash scripts/nse.sh history RELIANCE 250 | python3 -c "
import json, sys
d = json.load(sys.stdin)
print(f'  {len(d)} rows, last close {d[-1][\"close\"]}, earliest {d[0][\"date\"]}')
"
```

### 4. NSE momentum calc
```bash
bash scripts/nse.sh momentum RELIANCE
```
Expect: JSON with `mom_12_1_pct`, `dma50`, `dma200`, above_50dma bool.

### 5. Screener fundamentals
```bash
bash scripts/screener.sh RELIANCE
```
Expect: JSON with `roce_pct`, `roe_pct` populated. If exit 4, note the fallback hint.

### 6. Perplexity
```bash
bash scripts/perplexity.sh "What is the current level of Nifty 50? Just the number."
```
Expect: text response with a number and a citation URL.

### 7. Telegram
```bash
bash scripts/telegram.sh "🧪 Smoke test from Nifty Bot. If you see this, Telegram works."
```
Expect: Message on your phone within 2 seconds. `sent ok` printed locally.

### 8. Paper fill simulator
```bash
bash scripts/paper.sh buy RELIANCE 10 3000.00
```
Expect: JSON with fill_price ~3004.5 (0.15% slippage).

### 9. Git push permissions
```bash
echo "smoke test $(date)" >> scratch/smoke-log.txt
mkdir -p scratch
# Don't actually commit — just verify git is configured
git status
git remote -v
```

### Final report
Print a clean summary:
```
Day-0 smoke test results:
  [PASS/FAIL] Env vars
  [PASS/FAIL] NSE quote
  [PASS/FAIL] NSE history
  [PASS/FAIL] NSE momentum
  [PASS/FAIL] Screener
  [PASS/FAIL] Perplexity
  [PASS/FAIL] Telegram
  [PASS/FAIL] Paper fill
  [PASS/FAIL] Git

Ready to launch: YES/NO
```

If any FAIL, do not create cloud routines yet. Fix locally first.
