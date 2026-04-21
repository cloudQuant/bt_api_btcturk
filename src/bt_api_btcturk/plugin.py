from __future__ import annotations

from bt_api_base.plugins.protocol import PluginInfo
from bt_api_btcturk.exchange_data import BTCTurkExchangeDataSpot


class BTCTurkPlugin:
    @staticmethod
    def get_plugin_info() -> PluginInfo:
        return PluginInfo(
            name="btcturk",
            display_name="BTCTurk",
            version="0.1.0",
            supported_asset_types=["SPOT"],
        )

    @staticmethod
    def get_exchange_data(asset_type: str = "SPOT"):
        if asset_type == "SPOT":
            return BTCTurkExchangeDataSpot()
        raise ValueError(f"Unsupported asset type: {asset_type}")
