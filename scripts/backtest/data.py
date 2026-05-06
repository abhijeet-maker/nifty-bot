"""Price data layer for the backtest.

Wraps `scripts/nse.sh history SYM N` (Yahoo Finance v8 chart API) and caches
the JSON output as CSV per symbol in `memory/.bt-cache/`. The cache is
gitignored (see .gitignore) — it can be regenerated anytime.

Public API:
    load_prices(symbols, days=900) -> {sym: {date_str: close_float}}
    get_close(prices, sym, date_str) -> float | None
    trading_days(prices) -> sorted list of all date strings observed
"""
from __future__ import annotations
import csv
import json
import os
import subprocess
import sys
from pathlib import Path

# Repo root: walk up from this file (scripts/backtest/data.py) two levels.
REPO_ROOT = Path(__file__).resolve().parents[2]
CACHE_DIR = REPO_ROOT / "memory" / ".bt-cache"
NSE_SCRIPT = REPO_ROOT / "scripts" / "nse.sh"


def _ensure_cache_dir() -> None:
    CACHE_DIR.mkdir(parents=True, exist_ok=True)


def _fetch_history(symbol: str, days: int) -> list[dict]:
    """Call scripts/nse.sh history and parse the JSON list."""
    result = subprocess.run(
        ["bash", str(NSE_SCRIPT), "history", symbol, str(days)],
        capture_output=True,
        text=True,
        timeout=60,
    )
    if result.returncode != 0:
        raise RuntimeError(
            f"nse.sh history failed for {symbol}: {result.stderr.strip()}"
        )
    return json.loads(result.stdout)


def _cache_path(symbol: str) -> Path:
    return CACHE_DIR / f"{symbol}.csv"


def _load_from_cache(symbol: str) -> dict[str, float] | None:
    p = _cache_path(symbol)
    if not p.exists():
        return None
    out: dict[str, float] = {}
    with p.open() as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                out[row["date"]] = float(row["close"])
            except (KeyError, ValueError):
                continue
    return out if out else None


def _save_to_cache(symbol: str, bars: list[dict]) -> None:
    _ensure_cache_dir()
    p = _cache_path(symbol)
    with p.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["date", "close", "volume"])
        w.writeheader()
        for b in bars:
            if b.get("close") is None:
                continue
            w.writerow({
                "date": b["date"],
                "close": b["close"],
                "volume": b.get("volume", 0),
            })


def load_prices(
    symbols: list[str],
    days: int = 900,
    refresh: bool = False,
) -> dict[str, dict[str, float]]:
    """Load close prices for SYMBOLS. Cached as CSV in memory/.bt-cache/.

    Returns: {sym: {date_str: close_float}}.  Symbols that fail to fetch are
    silently dropped (with a warning to stderr).
    """
    _ensure_cache_dir()
    out: dict[str, dict[str, float]] = {}
    for sym in symbols:
        if not refresh:
            cached = _load_from_cache(sym)
            if cached:
                out[sym] = cached
                continue
        try:
            bars = _fetch_history(sym, days)
        except Exception as e:
            print(f"[data] WARN {sym}: {e}", file=sys.stderr)
            continue
        if not bars:
            print(f"[data] WARN {sym}: empty history", file=sys.stderr)
            continue
        _save_to_cache(sym, bars)
        out[sym] = {b["date"]: float(b["close"]) for b in bars
                    if b.get("close") is not None}
    return out


def trading_days(prices: dict[str, dict[str, float]]) -> list[str]:
    """Sorted unique trading dates across all symbols' data."""
    days: set[str] = set()
    for d in prices.values():
        days.update(d.keys())
    return sorted(days)


def get_close(prices: dict[str, dict[str, float]], sym: str, date: str):
    return prices.get(sym, {}).get(date)


if __name__ == "__main__":
    # Quick smoke test
    p = load_prices(["RELIANCE", "TCS"], days=10)
    for sym, bars in p.items():
        print(f"{sym}: {len(bars)} bars, last 3 = {dict(list(bars.items())[-3:])}")
