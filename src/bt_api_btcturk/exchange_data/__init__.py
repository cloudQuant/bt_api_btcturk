from __future__ import annotations

from bt_api_base.containers.exchanges.exchange_data import ExchangeData


class BTCTurkExchangeData(ExchangeData):
    def __init__(self) -> None:
        super().__init__()
        self.exchange_name = "BTCTURK"
        self.rest_url = "https://api.btcturk.com"
        self.wss_url = ""
        self.rest_paths = {
            "get_exchange_info": "GET /api/v2/server/exchangeinfo",
            "get_tick": "GET /api/v2/ticker",
            "get_depth": "GET /api/v2/orderbook",
            "get_kline": "GET /api/v2/ohlcs",
            "get_trades": "GET /api/v2/trades",
            "get_account": "GET /api/v1/users/balances",
            "get_balance": "GET /api/v1/users/balances",
            "make_order": "POST /api/v1/order",
            "cancel_order": "DELETE /api/v1/order",
            "query_order": "GET /api/v1/order",
            "get_open_orders": "GET /api/v1/openOrders",
        }
        self.wss_paths = {}
        self.kline_periods = {
            "1m": "1",
            "5m": "5",
            "15m": "15",
            "30m": "30",
            "1h": "60",
            "4h": "240",
            "1d": "1440",
            "1w": "10080",
        }
        self.reverse_kline_periods = {v: k for k, v in self.kline_periods.items()}
        self.legal_currency = ["TRY"]


class BTCTurkExchangeDataSpot(BTCTurkExchangeData):
    def __init__(self) -> None:
        super().__init__()
        self.asset_type = "SPOT"

    def get_symbol(self, symbol: str) -> str:
        return symbol

    def get_period(self, key: str) -> str:
        return self.kline_periods.get(key, key)

    def get_rest_path(self, key: str, **kwargs) -> str:
        if key not in self.rest_paths or self.rest_paths[key] == "":
            raise ValueError(f"[{self.exchange_name}] REST path not found: {key}")
        return self.rest_paths[key]
