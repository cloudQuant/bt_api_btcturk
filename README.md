# bt_api_btcturk

BTCTurk exchange plugin for bt_api framework.

## Installation

```bash
pip install bt_api_btcturk
```

## Usage

```python
from bt_api_btcturk import BTCTurkExchangeDataSpot, BTCTurkRequestDataSpot
```

## Features

- REST API support
- HMAC-SHA256 authentication with Base64-encoded private key
- Symbol format: `BTCUSDT`
- Base URL: `https://api.btcturk.com`
- Kline periods: `1m`, `5m`, `15m`, `30m`, `1h`, `4h`, `1d` (converted to minutes internally)
