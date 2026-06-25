from __future__ import annotations

from typing import Any

from bt_api_base.balance_utils import simple_balance_handler
from bt_api_base.plugins.protocol import PluginInfo

from bt_api_btcturk import __version__
from bt_api_btcturk.exchange_data import BTCTurkExchangeDataSpot
from bt_api_btcturk.feeds.live_btcturk.spot import BTCTurkRequestDataSpot


BTCTURK_PLUGIN_INFO = PluginInfo(
    name="bt_api_btcturk",
    version=__version__,
    core_requires=">=0.15,<1.0",
    supported_exchanges=("BTCTURK___SPOT",),
    supported_asset_types=("SPOT",),
)


class BTCTurkPlugin:
    @staticmethod
    def get_plugin_info() -> PluginInfo:
        return BTCTURK_PLUGIN_INFO

    @staticmethod
    def get_exchange_data(asset_type: str = "SPOT"):
        if asset_type == "SPOT":
            return BTCTurkExchangeDataSpot()
        raise ValueError(f"Unsupported asset type: {asset_type}")


def register_plugin(registry: Any, runtime_factory: Any | None = None) -> PluginInfo:
    """Entry point for bt_api plugin system."""
    registry.register_feed("BTCTURK___SPOT", BTCTurkRequestDataSpot)
    registry.register_exchange_data("BTCTURK___SPOT", BTCTurkExchangeDataSpot)
    registry.register_balance_handler("BTCTURK___SPOT", simple_balance_handler)
    return BTCTURK_PLUGIN_INFO
