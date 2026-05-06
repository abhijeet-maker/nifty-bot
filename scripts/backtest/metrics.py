"""Performance metrics for the backtest.

All inputs are simple lists/dataclasses to keep this stdlib-only (no numpy).
"""
from __future__ import annotations
import datetime
import math
from dataclasses import dataclass


TRADING_DAYS_PER_YEAR = 252


@dataclass
class Metrics:
    period_start: str
    period_end: str
    starting_equity: float
    ending_equity: float
    total_return_pct: float
    cagr_pct: float
    sharpe: float
    max_drawdown_pct: float
    calmar: float
    n_trades: int
    n_winners: int
    n_losers: int
    win_rate_pct: float
    avg_winner_pct: float
    avg_loser_pct: float
    profit_factor: float
    benchmark_return_pct: float | None = None


def _daily_returns(curve: list[tuple[str, float]]) -> list[float]:
    rets = []
    prev = None
    for _, eq in curve:
        if prev is not None and prev > 0:
            rets.append(eq / prev - 1.0)
        prev = eq
    return rets


def _stdev(xs: list[float]) -> float:
    n = len(xs)
    if n < 2:
        return 0.0
    mean = sum(xs) / n
    var = sum((x - mean) ** 2 for x in xs) / (n - 1)
    return math.sqrt(var)


def _years_between(d1: str, d2: str) -> float:
    a = datetime.date.fromisoformat(d1)
    b = datetime.date.fromisoformat(d2)
    return (b - a).days / 365.25


def max_drawdown(curve: list[tuple[str, float]]) -> float:
    """Max peak-to-trough drawdown, returned as a NEGATIVE percent (e.g. -12.5)."""
    if not curve:
        return 0.0
    peak = curve[0][1]
    max_dd = 0.0
    for _, eq in curve:
        if eq > peak:
            peak = eq
        dd = (eq - peak) / peak * 100.0
        if dd < max_dd:
            max_dd = dd
    return max_dd


def sharpe_annualized(curve: list[tuple[str, float]]) -> float:
    rets = _daily_returns(curve)
    if not rets:
        return 0.0
    mean = sum(rets) / len(rets)
    sd = _stdev(rets)
    if sd == 0:
        return 0.0
    return (mean / sd) * math.sqrt(TRADING_DAYS_PER_YEAR)


def compute(
    curve: list[tuple[str, float]],
    closed_trades,
    benchmark_curve: list[tuple[str, float]] | None = None,
) -> Metrics:
    if not curve:
        raise ValueError("Empty equity curve")

    start_date, start_eq = curve[0]
    end_date, end_eq = curve[-1]
    total_ret = (end_eq / start_eq - 1.0) * 100.0
    yrs = max(_years_between(start_date, end_date), 1e-6)
    cagr = ((end_eq / start_eq) ** (1.0 / yrs) - 1.0) * 100.0

    sharpe = sharpe_annualized(curve)
    mdd = max_drawdown(curve)
    calmar = (cagr / abs(mdd)) if mdd != 0 else 0.0

    winners = [t for t in closed_trades if t.pnl_pct > 0]
    losers = [t for t in closed_trades if t.pnl_pct <= 0]
    n_trades = len(closed_trades)
    win_rate = (len(winners) / n_trades * 100.0) if n_trades else 0.0
    avg_w = sum(t.pnl_pct for t in winners) / len(winners) if winners else 0.0
    avg_l = sum(t.pnl_pct for t in losers) / len(losers) if losers else 0.0
    sum_w_inr = sum(t.pnl_inr for t in winners) if winners else 0.0
    sum_l_inr = abs(sum(t.pnl_inr for t in losers)) if losers else 0.0
    pf = (sum_w_inr / sum_l_inr) if sum_l_inr > 0 else float("inf")

    bench = None
    if benchmark_curve and len(benchmark_curve) >= 2:
        bench = (benchmark_curve[-1][1] / benchmark_curve[0][1] - 1.0) * 100.0

    return Metrics(
        period_start=start_date,
        period_end=end_date,
        starting_equity=start_eq,
        ending_equity=end_eq,
        total_return_pct=total_ret,
        cagr_pct=cagr,
        sharpe=sharpe,
        max_drawdown_pct=mdd,
        calmar=calmar,
        n_trades=n_trades,
        n_winners=len(winners),
        n_losers=len(losers),
        win_rate_pct=win_rate,
        avg_winner_pct=avg_w,
        avg_loser_pct=avg_l,
        profit_factor=pf,
        benchmark_return_pct=bench,
    )


def equity_sparkline(curve: list[tuple[str, float]], width: int = 60) -> str:
    """ASCII sparkline of the equity curve."""
    if not curve:
        return ""
    eqs = [e for _, e in curve]
    lo, hi = min(eqs), max(eqs)
    if hi == lo:
        return "─" * width
    blocks = "▁▂▃▄▅▆▇█"
    # Down-sample to width buckets
    step = max(1, len(eqs) // width)
    sampled = eqs[::step][:width]
    chars = []
    for e in sampled:
        idx = int((e - lo) / (hi - lo) * (len(blocks) - 1))
        chars.append(blocks[idx])
    return "".join(chars)
