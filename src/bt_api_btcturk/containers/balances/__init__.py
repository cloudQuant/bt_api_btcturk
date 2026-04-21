from __future__ import annotations

import json
import time
from typing import Any

from bt_api_base._compat import Self
from bt_api_base.containers.balances.balance import BalanceData
from bt_api_base.functions.utils import from_dict_get_float


class BTCTurkBalanceData(BalanceData):
    def __init__(
        self,
        balance_info: str | dict[str, Any],
        symbol_name: str,
        asset_type: str,
        has_been_json_encoded: bool = False,
    ) -> None:
        super().__init__(balance_info, has_been_json_encoded)
        self.exchange_name = "BTCTURK"
        self.local_update_time = time.time()
        self.symbol_name = symbol_name
        self.asset_type = asset_type
        self.balance_data: dict[str, Any] | None = (
            balance_info if has_been_json_encoded and isinstance(balance_info, dict) else None
        )
        self.available: float | None = None
        self.locked: float | None = None
        self.has_been_init_data = False

    def init_data(self) -> Self:
        if not self.has_been_json_encoded:
            self.balance_data = json.loads(self.balance_info)
            self.has_been_json_encoded = True
        if self.has_been_init_data:
            return self

        if isinstance(self.balance_data, dict):
            data = self.balance_data
            self.available = from_dict_get_float(data, "available")
            self.locked = from_dict_get_float(data, "locked")

        self.has_been_init_data = True
        return self

    def get_exchange_name(self) -> str:
        return self.exchange_name

    def get_symbol_name(self) -> str:
        return self.symbol_name

    def get_asset_type(self) -> str:
        return self.asset_type

    def get_available(self) -> float | None:
        return self.available

    def get_locked(self) -> float | None:
        return self.locked


class BTCTurkRequestBalanceData(BTCTurkBalanceData):
    pass