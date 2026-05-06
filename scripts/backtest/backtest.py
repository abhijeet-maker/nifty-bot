"""MVP momentum-pullback backtest for Nifty Bot.

Goal: answer "does the strategy have edge?" with enough rigor to greenlight
(or vetо) 90 days of paper trading.

Scope (kept deliberately small — see plan):
  - 1 year, 2024-01-01 to 2024-12-31
  - Top 50 Nifty 100 names by market cap (filtered by quality screen)
  - Momentum pullback signal only (no PEAD)
  - 8% stop, 8-week time stop (no trail tightening)
  - 20% per name, max 5 positions, max 2 per sector, max 2 trades/week
  - Slippage 0.15%, fees 0.055% buy / 0.105% sell
  - Fills at the SIGNAL bar's close (next-day open is omitted for v1
    simplicity since data.py only has closes)

Usage:
    python3 scripts/backtest/backtest.py --start 2024-01-01 --end 2024-12-31
    python3 scripts/backtest/backtest.py --refresh   # force re-fetch prices

Output:
    memory/BACKTEST-RESULTS.md   (committed)
    Stdout summary
"""
from __future__ import annotations
import argparse
import datetime
import json
import sys
from pathlib import Path

# Make sibling modules importable
sys.path.insert(0, str(Path(__file__).resolve().parent))

import data
import signals
import portfolio as pf_mod
import metrics as mt


REPO_ROOT = Path(__file__).resolve().parents[2]


# ---------------------------------------------------------------------------
# Universe selection
# ---------------------------------------------------------------------------

def load_quality_universe(top_n: int = 50) -> list[tuple[str, str, float]]:
    """Top N names by market cap that pass the quality screen.
    Returns list of (symbol, sector, market_cap_cr).
    """
    cache = REPO_ROOT / "memory" / ".fundamentals-cache"
    candidates = []
    for f in sorted(cache.glob("*.json")):
        try:
            d = json.loads(f.read_text())
        except Exception:
            continue
        sym = f.stem
        roce = d.get("roce_pct")
        roe = d.get("roe_pct")
        de = d.get("debt_to_equity")
        sector = d.get("sector") or "-"
        mc = d.get("market_cap_cr") or 0.0
        pledge = d.get("promoter_pledge_pct") or 0.0
        # Quality gates
        if roce is None or roce < 15: continue
        if roe is None or roe < 15: continue
        if pledge >= 20: continue
        if de is not None:
            limit = 2.0 if sector == "Financial Services" else 1.0
            if de >= limit: continue
        candidates.append((sym, sector, mc))
    candidates.sort(key=lambda x: -x[2])
    return candidates[:top_n]


# ---------------------------------------------------------------------------
# Trading-day helpers
# ---------------------------------------------------------------------------

def build_trading_calendar(prices: dict, start: str, end: str) -> list[str]:
    """Sorted list of trading days that appear in the dataset within [start, end]."""
    all_days: set[str] = set()
    for sym_prices in prices.values():
        all_days.update(sym_prices.keys())
    return sorted(d for d in all_days if start <= d <= end)


def closes_today(prices: dict, date: str) -> dict[str, float]:
    return {sym: p[date] for sym, p in prices.items() if date in p}


# ---------------------------------------------------------------------------
# Entry candidate scoring
# ---------------------------------------------------------------------------

def find_entries(
    universe: list[tuple[str, str, float]],
    prices: dict,
    sym_dates: dict[str, list[str]],
    date: str,
    held_symbols: set[str],
) -> list[tuple[str, str, dict]]:
    """Return ranked list of (symbol, sector, metrics) that pass the gate today.
    Sorted by 12-1 momentum descending."""
    out = []
    for sym, sector, _mc in universe:
        if sym in held_symbols:
            continue
        sym_prices = prices.get(sym)
        if not sym_prices:
            continue
        sym_dates_sorted = sym_dates[sym]
        m = signals.score(sym, date, sym_prices, sym_dates_sorted)
        if m is None:
            continue
        out.append((sym, sector, m))
    out.sort(key=lambda x: -x[2]["mom_12_1"])
    return out


# ---------------------------------------------------------------------------
# Main loop
# ---------------------------------------------------------------------------

def run(
    start: str,
    end: str,
    starting_equity: float,
    universe_size: int,
    refresh: bool,
) -> tuple[pf_mod.Portfolio, mt.Metrics, list[str], list[tuple[str, str, dict]]]:
    print(f"[backtest] Universe: top {universe_size} Nifty 100 by market cap (quality-screened)")
    universe = load_quality_universe(universe_size)
    print(f"[backtest] {len(universe)} names passed quality screen")
    if not universe:
        raise SystemExit("No universe — aborting")

    symbols = [s for s, _, _ in universe]
    # Need ~252 days of history before `start` for 12-1 momentum.
    # 900 days = ~3.5 years calendar = ~620 trading days, plenty.
    print(f"[backtest] Fetching prices ({len(symbols)} symbols, ~900 days)...")
    prices = data.load_prices(symbols, days=900, refresh=refresh)
    print(f"[backtest] Loaded {len(prices)}/{len(symbols)} symbols")
    if len(prices) < len(symbols):
        missing = set(symbols) - set(prices.keys())
        print(f"[backtest] Missing: {sorted(missing)}")

    # Pre-sort each symbol's dates once (avoids re-sorting per signal call)
    sym_dates = {sym: sorted(p.keys()) for sym, p in prices.items()}

    # Build trading calendar (intersection within [start, end])
    cal = build_trading_calendar(prices, start, end)
    print(f"[backtest] Trading days in window: {len(cal)} ({cal[0]} -> {cal[-1]})")

    # Set up portfolio
    portfolio = pf_mod.Portfolio(starting_equity=starting_equity)

    # Track entries for the spot-check report
    entries_log: list[tuple[str, str, dict]] = []

    # Build a sym->sector lookup for the buy() call
    sym_sector = {s: sec for s, sec, _ in universe}

    for date in cal:
        prices_today = closes_today(prices, date)

        # 1) Apply exits using today's close
        portfolio.check_exits(date, prices_today)

        # 2) Look for new entries
        held = set(portfolio.positions.keys())
        candidates = find_entries(universe, prices, sym_dates, date, held)
        for sym, sector, sig in candidates:
            ok, _ = portfolio.can_open_new(date, sector)
            if not ok:
                break  # caps reached — stop trying this day
            close_today = prices_today.get(sym)
            if close_today is None:
                continue
            pos = portfolio.buy(sym, sector, date, close_today)
            if pos is not None:
                entries_log.append((date, sym, {**sig, "fill": pos.entry_price, "qty": pos.qty}))
                # Re-check caps after this fill
                ok2, _ = portfolio.can_open_new(date, sector)
                if not ok2:
                    break

        # 3) Mark-to-market end-of-day
        portfolio.record_eod(date, prices_today)

    # Force-close everything at the end so metrics use cash equity.
    # Don't add another curve point — the last record_eod() entry already
    # marked-to-market the final positions; liquidation just realizes them.
    last_date = cal[-1]
    last_prices = closes_today(prices, last_date)
    portfolio.force_close_all(last_date, last_prices)

    # Compute metrics
    metrics_out = mt.compute(portfolio.equity_curve, portfolio.closed)
    return portfolio, metrics_out, cal, entries_log


# ---------------------------------------------------------------------------
# Reporting
# ---------------------------------------------------------------------------

def write_report(
    metrics_out: mt.Metrics,
    portfolio: pf_mod.Portfolio,
    entries_log: list[tuple[str, str, dict]],
    benchmark_pct: float | None,
) -> str:
    closed = portfolio.closed
    if closed:
        best = sorted(closed, key=lambda t: -t.pnl_pct)[:5]
        worst = sorted(closed, key=lambda t: t.pnl_pct)[:5]
    else:
        best = worst = []

    spark = mt.equity_sparkline(portfolio.equity_curve)
    decision = (
        "EDGE EXISTS — proceed to paper trading"
        if metrics_out.sharpe > 0.8
        else "MARGINAL — build full-rule backtest before going live"
        if metrics_out.sharpe > 0.4
        else "NO EDGE — revisit STRATEGY.md before risking capital"
    )

    lines = []
    lines.append(f"# Backtest results — momentum pullback (MVP)\n")
    lines.append(f"**Period:** {metrics_out.period_start} -> {metrics_out.period_end}")
    lines.append(f"**Run date:** {datetime.date.today().isoformat()}")
    lines.append(f"**Universe:** top 50 Nifty 100 names by market cap, quality-screened")
    lines.append(f"**Signal:** momentum-pullback only (no PEAD in v1)")
    lines.append(f"**Decision: {decision}**\n")

    lines.append("## Key metrics\n")
    lines.append("| Metric | Value |")
    lines.append("|---|---|")
    lines.append(f"| Starting equity | ₹{metrics_out.starting_equity:,.0f} |")
    lines.append(f"| Ending equity | ₹{metrics_out.ending_equity:,.0f} |")
    lines.append(f"| Total return | {metrics_out.total_return_pct:+.2f}% |")
    lines.append(f"| CAGR | {metrics_out.cagr_pct:+.2f}% |")
    lines.append(f"| **Sharpe (annualized)** | **{metrics_out.sharpe:.2f}** |")
    lines.append(f"| **Max drawdown** | **{metrics_out.max_drawdown_pct:.2f}%** |")
    lines.append(f"| Calmar | {metrics_out.calmar:.2f} |")
    lines.append(f"| Trades closed | {metrics_out.n_trades} |")
    lines.append(f"| Win rate | {metrics_out.win_rate_pct:.1f}% ({metrics_out.n_winners}W / {metrics_out.n_losers}L) |")
    lines.append(f"| Avg winner | {metrics_out.avg_winner_pct:+.2f}% |")
    lines.append(f"| Avg loser | {metrics_out.avg_loser_pct:+.2f}% |")
    pf_str = "∞" if metrics_out.profit_factor == float("inf") else f"{metrics_out.profit_factor:.2f}"
    lines.append(f"| Profit factor | {pf_str} |")
    if benchmark_pct is not None:
        lines.append(f"| Nifty 50 buy & hold | {benchmark_pct:+.2f}% |")
        lines.append(f"| **Alpha vs Nifty 50** | **{metrics_out.total_return_pct - benchmark_pct:+.2f}%** |")
    lines.append("")

    lines.append("## Equity curve\n")
    lines.append(f"```\n{spark}\n```\n")

    lines.append("## Best 5 trades\n")
    if best:
        lines.append("| Symbol | Entry | Exit | Bars | P&L % | Reason |")
        lines.append("|---|---|---|---|---|---|")
        for t in best:
            lines.append(f"| {t.symbol} | {t.entry_date} | {t.exit_date} | {t.bars_held} | {t.pnl_pct:+.2f}% | {t.exit_reason} |")
    else:
        lines.append("*(no trades)*")
    lines.append("")

    lines.append("## Worst 5 trades\n")
    if worst:
        lines.append("| Symbol | Entry | Exit | Bars | P&L % | Reason |")
        lines.append("|---|---|---|---|---|---|")
        for t in worst:
            lines.append(f"| {t.symbol} | {t.entry_date} | {t.exit_date} | {t.bars_held} | {t.pnl_pct:+.2f}% | {t.exit_reason} |")
    else:
        lines.append("*(no trades)*")
    lines.append("")

    lines.append("## Decision rule (from plan)\n")
    lines.append("- Sharpe > 0.8 -> edge exists, proceed to paper trading")
    lines.append("- Sharpe 0.4–0.8 -> marginal; build full-rule backtest before going live")
    lines.append("- Sharpe < 0.4 -> rules don't work in Indian markets; revisit STRATEGY.md")
    lines.append("")

    lines.append("## Out of scope (future v2)\n")
    lines.append("- PEAD signal (needs historical earnings-date lookup)")
    lines.append("- Trail tightening at +10%/+20%/+35% milestones")
    lines.append("- Sector momentum filter")
    lines.append("- Blackout calendar (FOMC, RBI, Budget)")
    lines.append("- Multi-year window (2022 chop, 2023 bull, 2024 mixed)")
    lines.append("- Walk-forward / out-of-sample testing")
    lines.append("")

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Benchmark (Nifty 50 buy & hold)
# ---------------------------------------------------------------------------

def fetch_benchmark(start: str, end: str) -> tuple[list[tuple[str, float]], float | None]:
    """Use ^NSEI proxy via yfinance (or a representative ETF like NIFTYBEES).
    Returns (curve, total_return_pct)."""
    # Use NIFTYBEES (Nifty 50 ETF) — same source as our nse.sh history
    try:
        prices = data.load_prices(["NIFTYBEES"], days=900)
    except Exception:
        return [], None
    if "NIFTYBEES" not in prices:
        return [], None
    p = prices["NIFTYBEES"]
    cal = sorted(d for d in p.keys() if start <= d <= end)
    if len(cal) < 2:
        return [], None
    curve = [(d, p[d]) for d in cal]
    ret = (curve[-1][1] / curve[0][1] - 1.0) * 100.0
    return curve, ret


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--start", default="2024-01-01")
    ap.add_argument("--end", default="2024-12-31")
    ap.add_argument("--equity", type=float, default=500000.0)
    ap.add_argument("--universe-size", type=int, default=50)
    ap.add_argument("--refresh", action="store_true",
                    help="Force re-fetch all prices, ignore cache")
    ap.add_argument("--out", default=str(REPO_ROOT / "memory" / "BACKTEST-RESULTS.md"))
    args = ap.parse_args()

    portfolio, metrics_out, _cal, entries_log = run(
        args.start, args.end, args.equity, args.universe_size, args.refresh
    )

    # Benchmark
    _bench_curve, bench_ret = fetch_benchmark(args.start, args.end)

    # Stdout summary
    print()
    print("=" * 60)
    print(f"  Total return:  {metrics_out.total_return_pct:+.2f}%")
    print(f"  CAGR:          {metrics_out.cagr_pct:+.2f}%")
    print(f"  Sharpe:        {metrics_out.sharpe:.2f}")
    print(f"  Max DD:        {metrics_out.max_drawdown_pct:.2f}%")
    print(f"  Win rate:      {metrics_out.win_rate_pct:.1f}% ({metrics_out.n_trades} trades)")
    pf_str = "inf" if metrics_out.profit_factor == float('inf') else f"{metrics_out.profit_factor:.2f}"
    print(f"  Profit factor: {pf_str}")
    if bench_ret is not None:
        print(f"  Nifty 50 B&H:  {bench_ret:+.2f}%  (alpha {metrics_out.total_return_pct - bench_ret:+.2f}%)")
    print("=" * 60)

    # Write markdown report (UTF-8 for ₹ etc.)
    report = write_report(metrics_out, portfolio, entries_log, bench_ret)
    Path(args.out).write_text(report, encoding="utf-8")
    print(f"\nWrote {args.out}")

    # Also dump the trade log + entries log as JSON sidecars for spot-checking
    log_path = Path(args.out).with_suffix(".trades.json")
    log_path.write_text(json.dumps({
        "config": vars(args),
        "metrics": metrics_out.__dict__,
        "entries": [{"date": d, "symbol": s, **m} for d, s, m in entries_log],
        "closed": [t.__dict__ for t in portfolio.closed],
    }, indent=2, default=str), encoding="utf-8")
    print(f"Wrote {log_path}")


if __name__ == "__main__":
    main()
