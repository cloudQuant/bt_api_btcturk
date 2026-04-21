from __future__ import annotations

import json
import time
from typing import Any

from bt_api_base._compat import Self
from bt_api_base.containers.tickers.ticker import TickerData
from bt_api_base.functions.utils import from_dict_get_float


class BTCTurkTickerData(TickerData):
    def __init__(
        self,
        ticker_info: str | dict[str, Any],
        symbol_name: str,
        asset_type: str,
        has_been_json_encoded: bool = False,
    ) -> None:
        super().__init__(ticker_info, has_been_json_encoded)
        self.exchange_name = "BTCTURK"
        self.local_update_time = time.time()
        self.symbol_name = symbol_name
        self.asset_type = asset_type
        self.ticker_data: dict[str, Any] | None = (
            ticker_info if has_been_json_encoded and isinstance(ticker_info, dict) else None
        )
        self.ticker_symbol_name: str | None = None
        self.last_price: float | None = None
        self.bid_price: float | None = None
        self.ask_price: float | None = None
        self.high: float | None = None
        self.low: float | None = None
        self.volume: float | None = None
        self.timestamp: int | None = None
        self.has_been_init_data = False

    def init_data(self) -> Self:
        if not self.has_been_json_encoded:
            self.ticker_data = json.loads(self.ticker_info)
            self.has_been_json_encoded = True
        if self.has_been_init_data:
            return self

        data = (self.ticker_data or {}).get("data", {}) if isinstance(self.ticker_data, dict) else {}
        if isinstance(data, list) and len(data) > 0:
            ticker = data[0]
        elif isinstance(data, dict):
            ticker = data
        else:
            ticker = {}

        if ticker:
            self.ticker_symbol_name = ticker.get("pairSymbol")
            self.last_price = from_dict_get_float(ticker, "last")
            self.bid_price = from_dict_get_float(ticker, "bid")
            self.ask_price = from_dict_get_float(ticker, "ask")
            self.volume = from_dict_get_float(ticker, "volume")
            self.high = from_dict_get_float(ticker, "high")
            self.low = from_dict_get_float(ticker, "low")
            self.timestamp = from_dict_get_float(ticker, "timestamp")

        self.has_been_init_data = True
        return self

    def get_exchange_name(self) -> str:
        return self.exchange_name

    def get_symbol_name(self) -> str:
        return self.symbol_name

    def get_asset_type(self) -> str:
        return self.asset_type

    def get_last_price(self) -> float | None:
        return self.last_price

    def get_bid_price(self) -> float | None:
        return self.bid_price

    def get_ask_price(self) -> float | None:
        return self.ask_price


class BTCTurkRequestTickerData(BTCTurkTickerData):
    pass


class BTCTurkWssTickerData(BTCTurkTickerData):
    pass