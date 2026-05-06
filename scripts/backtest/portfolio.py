"""Portfolio state machine for the MVP backtest.

Mirrors the live strategy rules from memory/STRATEGY.md but simplified for v1:
  - Position sizing: 20% of equity per name
  - Max positions: 5
  - Max trades per week: 2 (entries only, exits don't count)
  - Stop loss: -8% from entry fill
  - Time stop: 8 weeks (40 trading days) flat (±3%)
  - Sector cap: max 2 positions per sector
  - Slippage: 0.15% on entry and exit
  - Fees: 0.055% on buy, 0.105% on sell (CNC delivery, mirrors paper.sh)

Out of scope for v1 (added in v2):
  - Trail tightening at +10/+20/+35% milestones
  - Thesis-break exits
  - Sector momentum filter
  - Blackout calendar
"""
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
import datetime


SLIPPAGE_PCT = 0.15            # 0.15% paper-mode slippage
BUY_FEES_PCT = 0.055           # CNC buy
SELL_FEES_PCT = 0.105          # CNC sell
STOP_PCT = -8.0                # hard stop loss
TIME_STOP_DAYS = 40            # 8 weeks of trading days
TIME_STOP_FLAT_BAND = 3.0      # ±3% counts as "flat"
POSITION_PCT = 20.0            # 20% of equity per name
MAX_POSITIONS = 5
MAX_TRADES_PER_WEEK = 2
MAX_PER_SECTOR = 2


@dataclass
class Position:
    symbol: str
    sector: str
    qty: int
    entry_price: float          # post-slippage, post-fees execution price
    entry_date: str             # YYYY-MM-DD
    entry_cost: float           # qty × entry_price (incl fees)
    bars_held: int = 0          # incremented every trading day


@dataclass
class ClosedTrade:
    symbol: str
    sector: str
    qty: int
    entry_price: float
    entry_date: str
    exit_price: float
    exit_date: str
    pnl_inr: float
    pnl_pct: float
    bars_held: int
    exit_reason: str            # "stop", "time-stop", "end-of-backtest"


@dataclass
class Portfolio:
    starting_equity: float
    cash: float = field(init=False)
    positions: dict[str, Position] = field(default_factory=dict)
    closed: list[ClosedTrade] = field(default_factory=list)
    equity_curve: list[tuple[str, float]] = field(default_factory=list)
    _entries_by_week: dict[str, int] = field(default_factory=dict)

    def __post_init__(self):
        self.cash = self.starting_equity

    # ----- helpers -----------------------------------------------------------

    @staticmethod
    def _week_key(date: str) -> str:
        d = datetime.date.fromisoformat(date)
        # ISO week (Mon-Sun) — same week == same key
        y, w, _ = d.isocalendar()
        return f"{y}-W{w:02d}"

    def equity(self, prices_today: dict[str, float]) -> float:
        eq = self.cash
        for sym, pos in self.positions.items():
            mark = prices_today.get(sym, pos.entry_price)
            eq += pos.qty * mark
        return eq

    def positions_in_sector(self, sector: str) -> int:
        return sum(1 for p in self.positions.values() if p.sector == sector)

    def can_open_new(self, date: str, sector: str) -> tuple[bool, str]:
        if len(self.positions) >= MAX_POSITIONS:
            return False, "max_positions"
        wk = self._week_key(date)
        if self._entries_by_week.get(wk, 0) >= MAX_TRADES_PER_WEEK:
            return False, "max_trades_per_week"
        if self.positions_in_sector(sector) >= MAX_PER_SECTOR:
            return False, "max_per_sector"
        return True, ""

    # ----- order execution ---------------------------------------------------

    def buy(
        self,
        symbol: str,
        sector: str,
        date: str,
        market_close: float,
    ) -> Optional[Position]:
        """Simulate a buy at market close + slippage. Returns None if no fill
        (no cash, no shares, etc.)."""
        if symbol in self.positions:
            return None
        # slippage: pay above market close on the way in
        fill_px = market_close * (1.0 + SLIPPAGE_PCT / 100.0)
        # target trade notional
        target_notional = self.equity({symbol: market_close}) * POSITION_PCT / 100.0
        # cap by available cash (leave a tiny buffer)
        max_notional = min(target_notional, self.cash * 0.999)
        qty = int(max_notional / fill_px)
        if qty < 1:
            return None
        gross = qty * fill_px
        fees = gross * BUY_FEES_PCT / 100.0
        total_cost = gross + fees
        if total_cost > self.cash:
            qty -= 1
            if qty < 1:
                return None
            gross = qty * fill_px
            fees = gross * BUY_FEES_PCT / 100.0
            total_cost = gross + fees
        self.cash -= total_cost
        pos = Position(
            symbol=symbol,
            sector=sector,
            qty=qty,
            entry_price=fill_px,
            entry_date=date,
            entry_cost=total_cost,
            bars_held=0,
        )
        self.positions[symbol] = pos
        wk = self._week_key(date)
        self._entries_by_week[wk] = self._entries_by_week.get(wk, 0) + 1
        return pos

    def sell(
        self,
        symbol: str,
        date: str,
        market_close: float,
        reason: str,
    ) -> Optional[ClosedTrade]:
        pos = self.positions.pop(symbol, None)
        if pos is None:
            return None
        fill_px = market_close * (1.0 - SLIPPAGE_PCT / 100.0)
        gross = pos.qty * fill_px
        fees = gross * SELL_FEES_PCT / 100.0
        proceeds = gross - fees
        self.cash += proceeds
        pnl_inr = proceeds - pos.entry_cost
        pnl_pct = (pnl_inr / pos.entry_cost) * 100.0 if pos.entry_cost > 0 else 0.0
        ct = ClosedTrade(
            symbol=symbol,
            sector=pos.sector,
            qty=pos.qty,
            entry_price=pos.entry_price,
            entry_date=pos.entry_date,
            exit_price=fill_px,
            exit_date=date,
            pnl_inr=pnl_inr,
            pnl_pct=pnl_pct,
            bars_held=pos.bars_held,
            exit_reason=reason,
        )
        self.closed.append(ct)
        return ct

    # ----- daily ops ---------------------------------------------------------

    def check_exits(
        self,
        date: str,
        prices_today: dict[str, float],
    ) -> list[ClosedTrade]:
        """Apply -8% stop and 8-week time stop. Returns list of closed trades."""
        exits: list[ClosedTrade] = []
        # Iterate over a snapshot since sell() mutates self.positions
        for sym in list(self.positions.keys()):
            pos = self.positions[sym]
            mark = prices_today.get(sym)
            if mark is None:
                continue  # no quote today, hold
            unreal_pct = (mark / pos.entry_price - 1.0) * 100.0
            if unreal_pct <= STOP_PCT:
                ct = self.sell(sym, date, mark, "stop")
                if ct: exits.append(ct)
                continue
            if pos.bars_held >= TIME_STOP_DAYS and abs(unreal_pct) <= TIME_STOP_FLAT_BAND:
                ct = self.sell(sym, date, mark, "time-stop")
                if ct: exits.append(ct)
                continue
        return exits

    def record_eod(self, date: str, prices_today: dict[str, float]) -> float:
        eq = self.equity(prices_today)
        self.equity_curve.append((date, eq))
        # Increment bars_held for everything still open
        for pos in self.positions.values():
            pos.bars_held += 1
        return eq

    def force_close_all(self, date: str, prices_today: dict[str, float]) -> None:
        """Liquidate at end of backtest so equity == cash for final metrics."""
        for sym in list(self.positions.keys()):
            mark = prices_today.get(sym)
            if mark is not None:
                self.sell(sym, date, mark, "end-of-backtest")
