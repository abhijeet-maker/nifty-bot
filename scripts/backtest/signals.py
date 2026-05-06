"""Signal logic for the MVP backtest — momentum pullback only.

A name passes momentum_pullback() on date `d` if ALL of:
  - 12-1 month momentum (return from t-252 to t-21) is positive AND
    in the top quartile across the universe (caller filters by rank).
  - close[d] >= 50DMA AND close[d] >= 200DMA  (uptrend confirmation)
  - close[d] is 2% to 7% below 20DMA           (a real pullback, not extended)
  - RSI(14) is between 50 and 70               (not overbought/oversold)

Public API:
    score(symbol, date, prices_for_sym) -> dict | None
        Returns metric dict if signal triggers, else None.
        dict keys: mom_12_1, ma20, ma50, ma200, rsi14, close, pullback_pct
"""
from __future__ import annotations
from typing import Optional


# Look-back constants (in trading days)
LB_MOM_LONG = 252      # 12 months
LB_MOM_SKIP = 21       # 1 month skip (the "1" in 12-1)
LB_MA20 = 20
LB_MA50 = 50
LB_MA200 = 200
LB_RSI = 14

# Signal thresholds
PULLBACK_MIN_PCT = 2.0   # at least 2% below 20DMA
PULLBACK_MAX_PCT = 7.0   # at most 7% below 20DMA
RSI_MIN = 50.0
RSI_MAX = 70.0


def _sma(values: list[float], n: int) -> float | None:
    if len(values) < n or n <= 0:
        return None
    return sum(values[-n:]) / n


def _rsi(values: list[float], n: int = 14) -> float | None:
    if len(values) < n + 1:
        return None
    gains = []
    losses = []
    for i in range(-n, 0):
        diff = values[i] - values[i - 1]
        if diff >= 0:
            gains.append(diff)
            losses.append(0.0)
        else:
            gains.append(0.0)
            losses.append(-diff)
    avg_gain = sum(gains) / n
    avg_loss = sum(losses) / n
    if avg_loss == 0:
        return 100.0 if avg_gain > 0 else 50.0
    rs = avg_gain / avg_loss
    return 100.0 - 100.0 / (1.0 + rs)


def _series_through(prices: dict[str, float], date: str, dates_sorted: list[str]) -> list[float]:
    """All closes for symbol up to and including `date`, in chronological order.
    `dates_sorted` is the symbol's own dates sorted ascending."""
    out = []
    for d in dates_sorted:
        if d > date:
            break
        out.append(prices[d])
    return out


def momentum_12_1(closes: list[float]) -> float | None:
    """Return the 12-1 momentum % computed from `closes[-1]` (today is t).
    Uses close[t-21] / close[t-252] - 1.0, expressed in %."""
    if len(closes) < LB_MOM_LONG + 1:
        return None
    # close[t-21] is closes[-22]; close[t-252] is closes[-253]
    p_then = closes[-LB_MOM_LONG - 1]
    p_skip = closes[-LB_MOM_SKIP - 1]
    if p_then <= 0:
        return None
    return (p_skip / p_then - 1.0) * 100.0


def score(
    symbol: str,
    date: str,
    sym_prices: dict[str, float],
    sym_dates_sorted: list[str],
) -> Optional[dict]:
    """Return metrics dict if all gates pass, else None.

    `sym_prices` is the {date: close} map for this symbol.
    `sym_dates_sorted` is the pre-sorted list of dates for this symbol
    (passed in to avoid re-sorting per-call).
    """
    closes = _series_through(sym_prices, date, sym_dates_sorted)
    if len(closes) < LB_MOM_LONG + 1:
        return None  # not enough history

    today = closes[-1]
    if today <= 0:
        return None

    ma20 = _sma(closes, LB_MA20)
    ma50 = _sma(closes, LB_MA50)
    ma200 = _sma(closes, LB_MA200)
    rsi = _rsi(closes, LB_RSI)
    mom = momentum_12_1(closes)

    if None in (ma20, ma50, ma200, rsi, mom):
        return None

    # Gate: must be in uptrend
    if today < ma50 or today < ma200:
        return None

    # Gate: must be a real pullback (2-7% below 20DMA)
    pullback_pct = (ma20 - today) / ma20 * 100.0   # positive means below
    if pullback_pct < PULLBACK_MIN_PCT or pullback_pct > PULLBACK_MAX_PCT:
        return None

    # Gate: RSI in 50-70 band
    if rsi < RSI_MIN or rsi > RSI_MAX:
        return None

    # Gate: positive momentum
    if mom <= 0:
        return None

    return {
        "mom_12_1": mom,
        "ma20": ma20,
        "ma50": ma50,
        "ma200": ma200,
        "rsi14": rsi,
        "close": today,
        "pullback_pct": pullback_pct,
    }


if __name__ == "__main__":
    # Quick test on synthetic data
    closes = [100 + i * 0.1 + (i % 7) * 0.5 for i in range(300)]
    today_close = closes[-1]
    print(f"mom_12_1: {momentum_12_1(closes):.2f}%")
    print(f"sma20: {_sma(closes, 20):.2f}, sma50: {_sma(closes, 50):.2f}, sma200: {_sma(closes, 200):.2f}")
    print(f"rsi14: {_rsi(closes, 14):.2f}")
