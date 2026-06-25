from __future__ import annotations

from bt_api_base.balance_utils import simple_balance_handler
from bt_api_base.registry import ExchangeRegistry

from bt_api_btcturk.exchange_data import BTCTurkExchangeDataSpot
from bt_api_btcturk.feeds.live_btcturk.spot import BTCTurkRequestDataSpot


def register_btcturk(
    registry: ExchangeRegistry | type[ExchangeRegistry] = ExchangeRegistry,
) -> None:
    registry.register_feed("BTCTURK___SPOT", BTCTurkRequestDataSpot)
    registry.register_exchange_data("BTCTURK___SPOT", BTCTurkExchangeDataSpot)
    registry.register_balance_handler("BTCTURK___SPOT", simple_balance_handler)


__all__ = ["register_btcturk"]
