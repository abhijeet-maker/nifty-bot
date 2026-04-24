#!/usr/bin/env python3
"""
Screener.in fundamentals fetcher.
Uses Beautiful Soup for robust HTML parsing + requests for cookie handling.
"""

import json
import os
import re
import sys
from typing import Any, Dict, Optional
from urllib.parse import urljoin

try:
    import requests
    from bs4 import BeautifulSoup
except ImportError:
    raise ImportError("requests and beautifulsoup4 not installed. Run: pip install requests beautifulsoup4")


UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36"


def _to_num(s: Optional[str]) -> Optional[float]:
    """Parse a string to float, handling %, ₹, and commas."""
    if s is None:
        return None
    s = s.replace("%", "").replace("₹", "").replace(",", "").strip()
    try:
        return float(s)
    except (ValueError, AttributeError):
        return None


def get_fundamentals(symbol: str, session: Optional[requests.Session] = None) -> Dict[str, Any]:
    """
    Fetch fundamentals for a symbol from screener.in.
    Returns JSON-serializable dict.
    
    Args:
        symbol: Stock symbol (e.g., "RELIANCE")
        session: Optional requests.Session with cookies/auth configured
    
    Returns:
        Dict with market_cap_cr, pe, roce_pct, roe_pct, debt_to_equity, etc.
        On failure, raises Exception (caller should fall back to Perplexity).
    """
    if not session:
        session = requests.Session()
    
    session.headers.update({"User-Agent": UA})
    
    # Try consolidated first (group-level numbers)
    urls_to_try = [
        f"https://www.screener.in/company/{symbol}/consolidated/",
        f"https://www.screener.in/company/{symbol}/",
    ]
    
    html = None
    url_used = None
    
    for url in urls_to_try:
        try:
            resp = session.get(url, timeout=10)
            resp.raise_for_status()
            if "company-ratios" in resp.text:
                html = resp.text
                url_used = url
                break
        except Exception as e:
            print(f"Failed to fetch {url}: {e}", file=sys.stderr)
            continue
    
    if not html:
        raise Exception(f"Could not fetch valid data for {symbol} from screener.in")
    
    # Parse HTML
    soup = BeautifulSoup(html, "html.parser")
    
    # Extract sector from breadcrumb or navigation
    sector = None
    sector_link = soup.find("a", href=re.compile(r"/company/compare/[^/]+/[^/]+/"))
    if sector_link:
        sector_href = sector_link.get("href", "")
        match = re.search(r"/compare/[^/]+/([^/]+)/", sector_href)
        if match:
            sector = match.group(1).replace("-", " ").title()
    
    def grab_ratio(label_patterns):
        """
        Find a ratio value by label text.
        Searches for li with label text, then finds the 'number' span inside.
        """
        if isinstance(label_patterns, str):
            label_patterns = [label_patterns]
        
        for li in soup.find_all("li", class_="flex flex-space-between"):
            span_name = li.find("span", class_="name")
            if not span_name:
                continue
            
            label_text = span_name.get_text(strip=True)
            
            for pattern in label_patterns:
                if pattern.lower() in label_text.lower():
                    # Found the right li, now grab the number
                    span_number = li.find("span", class_="number")
                    if span_number:
                        return span_number.get_text(strip=True)
            break
        
        return None
    
    out = {
        "symbol": symbol,
        "source": "screener.in",
        "url": url_used,
        "market_cap_cr": _to_num(grab_ratio("Market Cap")),
        "current_price": _to_num(grab_ratio("Current Price")),
        "pe": _to_num(grab_ratio("Stock P/E")),
        "pb": _to_num(grab_ratio("Price to Book")),
        "book_value": _to_num(grab_ratio("Book Value")),
        "dividend_yield_pct": _to_num(grab_ratio("Dividend Yield")),
        "roce_pct": _to_num(grab_ratio("ROCE")),
        "roe_pct": _to_num(grab_ratio("ROE")),
        "debt_to_equity": _to_num(grab_ratio(["Debt / Equity", "D/E Ratio"])),
        "face_value": _to_num(grab_ratio("Face Value")),
        "sector": sector,
    }
    
    # Try to find promoter holding in tables
    promoter_text = None
    for td in soup.find_all("td"):
        if "promoter" in td.get_text(strip=True).lower():
            # Find the next td that has the percentage
            next_td = td.find_next("td")
            if next_td:
                promoter_text = next_td.get_text(strip=True)
                break
    
    out["promoter_holding_pct"] = _to_num(promoter_text)
    
    # Promoter pledge percentage (critical for quality screen)
    for td in soup.find_all("td"):
        if "pledg" in td.get_text(strip=True).lower():
            next_td = td.find_next("td")
            if next_td:
                out["promoter_pledge_pct"] = _to_num(next_td.get_text(strip=True))
                break
    
    # Next results date (if announced)
    for text in soup.stripped_strings:
        if "results on" in text.lower():
            # Extract date after "on"
            match = re.search(r"Results\s+on\s+([A-Za-z]+\s+\d{1,2}(?:,\s*\d{4})?)", text, re.IGNORECASE)
            if match:
                out["next_results_date"] = match.group(1).strip()
                break
    
    return out


def main():
    """CLI for testing."""
    if len(sys.argv) < 2:
        print("Usage: python screener_data.py SYMBOL [SCREENER_SESSION_COOKIE]")
        sys.exit(1)
    
    symbol = sys.argv[1]
    screener_session = sys.argv[2] if len(sys.argv) > 2 else os.getenv("SCREENER_SESSION")
    
    session = requests.Session()
    if screener_session:
        session.cookies.set("sessionid", screener_session, domain="screener.in")
    
    try:
        result = get_fundamentals(symbol, session)
        print(json.dumps(result, indent=2))
    except Exception as e:
        print(f"SCREENER_PARSE_FAILED symbol={symbol}", file=sys.stderr)
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(4)


if __name__ == "__main__":
    main()
