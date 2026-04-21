from __future__ import annotations

import json
import time
from typing import Any

from bt_api_base._compat import Self
from bt_api_base.containers.orders.order import OrderData
from bt_api_base.functions.utils import from_dict_get_float, from_dict_get_string


_STATUS_MAP = {
    0: "NEW",
    1: "OPEN",
    2: "FILLED",
    3: "CANCELLED",
    4: "PARTIAL_FILLED",
    5: "PENDING",
}

_SIDE_MAP = {0: "BUY", 1: "SELL"}
_TYPE_MAP = {0: "MARKET", 1: "LIMIT"}


class BTCTurkOrderData(OrderData):
    def __init__(
        self,
        order_info: str | dict[str, Any],
        symbol_name: str,
        asset_type: str,
        has_been_json_encoded: bool = False,
    ) -> None:
        super().__init__(order_info, has_been_json_encoded)
        self.exchange_name = "BTCTURK"
        self.local_update_time = time.time()
        self.symbol_name = symbol_name
        self.asset_type = asset_type
        self.order_data: dict[str, Any] | None = (
            order_info if has_been_json_encoded and isinstance(order_info, dict) else None
        )
        self.order_id: str | None = None
        self.side: str | None = None
        self.order_type: str | None = None
        self.price: float | None = None
        self.quantity: float | None = None
        self.status: str | None = None
        self.has_been_init_data = False

    def init_data(self) -> Self:
        if not self.has_been_json_encoded:
            self.order_data = json.loads(self.order_info)
            self.has_been_json_encoded = True
        if self.has_been_init_data:
            return self

        if isinstance(self.order_data, dict):
            data = self.order_data
            self.order_id = from_dict_get_string(data, "id") or from_dict_get_string(data, "orderId")
            raw_status = data.get("status")
            if raw_status is not None:
                self.status = _STATUS_MAP.get(int(raw_status), str(raw_status))
            raw_side = data.get("side")
            if raw_side is not None:
                self.side = _SIDE_MAP.get(int(raw_side), str(raw_side))
            raw_type = data.get("type")
            if raw_type is not None:
                self.order_type = _TYPE_MAP.get(int(raw_type), str(raw_type))
            self.price = from_dict_get_float(data, "price")
            self.quantity = from_dict_get_float(data, "quantity") or from_dict_get_float(data, "qty")

        self.has_been_init_data = True
        return self

    def get_exchange_name(self) -> str:
        return self.exchange_name

    def get_symbol_name(self) -> str:
        return self.symbol_name

    def get_asset_type(self) -> str:
        return self.asset_type

    def get_order_id(self) -> str | None:
        return self.order_id


class BTCTurkRequestOrderData(BTCTurkOrderData):
    pass