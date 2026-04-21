from __future__ import annotations

from bt_api_base.registry import ExchangeRegistry

from bt_api_btcturk.feeds.live_btcturk.spot import BTCTurkRequestDataSpot
from bt_api_btcturk.plugin import BTCTurkPlugin


def register_btcturk():
    plugin = BTCTurkPlugin()
    info = plugin.get_plugin_info()
    exchange_data = plugin.get_exchange_data("SPOT")
    ExchangeRegistry.register(
        exchange_name=info.name.upper() + "___SPOT",
        exchange_data=exchange_data,
        feed_class=BTCTurkRequestDataSpot,
        plugin_info=info,
    )


__all__ = ["register_btcturk"]
