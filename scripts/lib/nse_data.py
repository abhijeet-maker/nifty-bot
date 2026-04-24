#!/usr/bin/env python3
"""
NSE data fetcher using nsepython (handles Akamai + cookies) and yfinance.
Replaces curl-based wrapper that was hitting bot-detection walls.
"""

import json
import sys
from datetime import datetime, timedelta
from typing import Any, Dict, List, Optional

import yfinance as yf

try:
    import nsepython
except ImportError:
    raise ImportError("nsepython not installed. Run: pip install nsepython")


def get_quote(symbol: str) -> Dict[str, Any]:
    """
    Fetch live quote and OHLC for a symbol using nsepython.
    Returns JSON-serializable dict.
    """
    try:
        # nsepython.quote_equity() handles all Akamai auth + cookie rotation for equity symbols
        quote_data = nsepython.quote_equity(symbol)
        
        if not quote_data:
            raise ValueError(f"No data returned for {symbol}")
        
        # Normalize to our schema
        info = quote_data.get("info", {})
        price_info = quote_data.get("priceInfo", {})
        metadata = quote_data.get("metadata", {})
        
        result = {
            "symbol": info.get("symbol", symbol),
            "name": info.get("companyName"),
            "sector": metadata.get("industry"),
            "last": price_info.get("lastPrice"),
            "open": price_info.get("open"),
            "high": price_info.get("intraDayHighLow", {}).get("max"),
            "low": price_info.get("intraDayHighLow", {}).get("min"),
            "close_prev": price_info.get("previousClose"),
            "change_pct": price_info.get("pChange"),
            "vwap": price_info.get("vwap"),
            "volume": price_info.get("volumeTradedValue"),
            "week52_high": price_info.get("weekHighLow", {}).get("max"),
            "week52_low": price_info.get("weekHighLow", {}).get("min"),
            "lower_circuit": price_info.get("lowerCP"),
            "upper_circuit": price_info.get("upperCP"),
        }
        
        return result
    except Exception as e:
        print(f"Error fetching quote for {symbol}: {e}", file=sys.stderr)
        raise


def get_history(symbol: str, days: int = 300) -> List[Dict[str, Any]]:
    """
    Fetch historical OHLCV using yfinance (handles crumb + cookies).
    Returns list of {date, close, volume} dicts, most recent last.
    """
    try:
        # yfinance transparently handles Yahoo's cookie/crumb requirements
        ticker = yf.Ticker(f"{symbol}.NS")
        
        # Fetch historical data
        period_str = f"{days}d"
        hist = ticker.history(period=period_str)
        
        if hist.empty:
            raise ValueError(f"No history returned for {symbol}")
        
        # Normalize to our schema
        result = []
        for date, row in hist.iterrows():
            result.append({
                "date": date.strftime("%Y-%m-%d"),
                "close": float(row["Close"]),
                "open": float(row["Open"]),
                "high": float(row["High"]),
                "low": float(row["Low"]),
                "volume": int(row["Volume"]),
            })
        
        return result
    except Exception as e:
        print(f"Error fetching history for {symbol}: {e}", file=sys.stderr)
        raise


def get_earnings_calendar(date_str: str) -> List[Dict[str, Any]]:
    """
    Fetch earnings calendar for a given date.
    
    NOTE: nsepython may not expose NSE's earnings calendar API reliably.
    This function attempts to fetch via nsepython if available, but the caller
    (nse.sh wrapper in CLAUDE.md) should fall back to Perplexity for
    earnings calendar queries, as per the agent's design.
    
    date_str format: YYYY-MM-DD
    Returns list of {symbol, company, period, broadcast} dicts.
    """
    try:
        # Attempt to use nsepython's available methods
        # If nsepython doesn't have this, we return empty and caller falls back to Perplexity
        
        # Check if nsepython has a method for earnings/results calendar
        if hasattr(nsepython, "get_nse_results_calendar"):
            results = nsepython.get_nse_results_calendar(date_str)
        elif hasattr(nsepython, "get_results_calendar"):
            results = nsepython.get_results_calendar(date_str)
        else:
            # nsepython doesn't expose earnings calendar
            # Per CLAUDE.md, fallback to Perplexity.sh for results calendar queries
            print(
                f"Warning: nsepython does not expose earnings calendar API.",
                file=sys.stderr,
            )
            print(
                f"For date {date_str}, use perplexity.sh to query earnings instead.",
                file=sys.stderr,
            )
            return []
        
        if not results:
            return []
        
        # Normalize results
        out = []
        for item in results:
            out.append(
                {
                    "symbol": item.get("symbol"),
                    "company": item.get("companyName"),
                    "period": item.get("period"),
                    "broadcast": item.get("broadcastTimestamp"),
                }
            )
        
        return out
    except Exception as e:
        print(
            f"Error fetching earnings calendar for {date_str}: {e}", file=sys.stderr
        )
        # Return empty list to signal fallback
        return []


def get_momentum(symbol: str, days: int = 260) -> Dict[str, Any]:
    """
    Compute 12-1 month momentum (Jegadeesh-Titman signal).
    Also returns 50/200 DMA and price relationship to them.
    """
    try:
        hist = get_history(symbol, days)
        
        if len(hist) < 252:
            return {
                "symbol": symbol,
                "mom_12_1_pct": None,
                "reason": "insufficient history",
            }
        
        # Price 252 days ago (12 months), price 21 days ago (1 month)
        p_12m = float(hist[-252]["close"])
        p_1m = float(hist[-21]["close"])
        mom = (p_1m - p_12m) / p_12m
        
        # 50/200 DMA from latest data
        closes_50 = [float(c["close"]) for c in hist[-50:]]
        closes_200 = [float(c["close"]) for c in hist[-200:]]
        
        dma50 = sum(closes_50) / len(closes_50)
        dma200 = sum(closes_200) / len(closes_200)
        
        last = float(hist[-1]["close"])
        
        return {
            "symbol": symbol,
            "last": round(last, 2),
            "mom_12_1_pct": round(mom * 100, 2),
            "dma50": round(dma50, 2),
            "dma200": round(dma200, 2),
            "above_50dma": last > dma50,
            "above_200dma": last > dma200,
        }
    except Exception as e:
        print(f"Error computing momentum for {symbol}: {e}", file=sys.stderr)
        raise


if __name__ == "__main__":
    # Simple CLI for testing
    if len(sys.argv) < 2:
        print("Usage: python nse_data.py <quote|history|earnings|momentum> [args]")
        sys.exit(1)
    
    cmd = sys.argv[1]
    
    if cmd == "quote":
        symbol = sys.argv[2] if len(sys.argv) > 2 else "RELIANCE"
        result = get_quote(symbol)
        print(json.dumps(result, indent=2))
    
    elif cmd == "history":
        symbol = sys.argv[2] if len(sys.argv) > 2 else "RELIANCE"
        days = int(sys.argv[3]) if len(sys.argv) > 3 else 300
        result = get_history(symbol, days)
        print(json.dumps(result, indent=2))
    
    elif cmd == "earnings":
        date_arg = sys.argv[2] if len(sys.argv) > 2 else datetime.now().strftime("%Y-%m-%d")
        result = get_earnings_calendar(date_arg)
        print(json.dumps(result, indent=2))
    
    elif cmd == "momentum":
        symbol = sys.argv[2] if len(sys.argv) > 2 else "RELIANCE"
        result = get_momentum(symbol)
        print(json.dumps(result, indent=2))
    
    else:
        print(f"Unknown command: {cmd}", file=sys.stderr)
        sys.exit(1)
