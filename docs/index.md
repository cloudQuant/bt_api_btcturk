# BTCTurk Exchange Plugin for bt_api

## English

### Overview

`bt_api_btcturk` is a runtime plugin for [bt_api](https://github.com/cloudQuant/bt_api_py) that connects to **BTCTurk** exchange — a Turkish cryptocurrency exchange. It provides unified REST API access for **Spot** trading with TRY pairs.

### Features

- **Market Data** — Ticker, order book, k-lines, trades
- **Account** — Balance, account info
- **Trading** — Place orders, cancel orders, query orders

### Supported Operations

| Operation | Description |
|-----------|-------------|
| `get_tick` | 24hr rolling ticker |
| `get_depth` | Order book depth |
| `get_kline` | K-line/candlestick |
| `get_trades` | Recent trade history |
| `get_balance` | All asset balances |
| `get_account` | Full account info |
| `make_order` | Place limit order |
| `cancel_order` | Cancel order by ID |
| `query_order` | Query order by ID |
| `get_open_orders` | All open orders |

### Architecture

```
bt_api_btcturk/
├── src/bt_api_btcturk/
│   ├── plugin.py              # Plugin entry point
│   ├── registry_registration.py  # Exchange registry
│   ├── exchange_data/
│   │   └── __init__.py      # BTCTurkExchangeDataSpot
│   ├── feeds/
│   │   └── live_btcturk/
│   │       ├── spot.py       # BTCTurkRequestDataSpot
│   │       └── request_base.py  # Base request class
│   ├── containers/           # Data containers
│   └── errors/
│       └── __init__.py       # Error translator
└── configs/
    └── btcturk.yaml         # Exchange config
```

### Installation

```bash
pip install bt_api_btcturk
```

### Quick Start

```python
from bt_api_py import BtApi

# Public market data (no API key)
api = BtApi()
ticker = api.get_tick("BTCTURK___SPOT", "BTCUSDT")
print(f"BTC price: {ticker}")

# Authenticated requests
api = BtApi(exchange_kwargs={
    "BTCTurk___SPOT": {
        "api_key": "your_api_key",
        "secret": "your_secret",
    }
})

balance = api.get_balance("BTCTURK___SPOT")
order = api.make_order(
    exchange_name="BTCTURK___SPOT",
    symbol="BTCUSDT",
    volume=0.001,
    price=500000,
    order_type="limit",
)
```

### Supported Symbols

BTCTurk trading pairs (TRY base currency):

- `BTCUSDT`, `ETHUSDT`, `XRPUSDT`, `SOLUSDT`, `DOGEUSDT` ...
- `TRY` pairs: `BTCTRY`, `ETHTRY`, `XRPTRY` ...

### Error Handling

| Code | Error | Description |
|------|-------|-------------|
| `0` | `SUCCESS` | Success |
| `-1` | `AUTH_ERROR` | Authentication error |
| `-2` | `AUTH_ERROR` | Invalid signature |
| `-3` | `RATE_LIMIT` | Rate limit exceeded |
| `-4` | `INSUFFICIENT_BALANCE` | Insufficient balance |
| `-5` | `ORDER_NOT_FOUND` | Order not found |
| `-6` | `INVALID_ORDER_TYPE` | Invalid order type |

### Rate Limits

BTCTurk API rate limits:

- **Public endpoints**: 60 requests/minute
- **Private endpoints**: 120 requests/minute

---

## 中文

### 概述

`bt_api_btcturk` 是 [bt_api](https://github.com/cloudQuant/bt_api_py) 的运行时插件，连接 **BTCTurk** 交易所——土耳其加密货币交易所。为 **现货** 交易（TRY 交易对）提供统一的 REST API 访问。

### 功能特点

- **行情数据** — 行情、订单簿、K线、成交
- **账户** — 余额、账户信息
- **交易** — 下单、撤单、查询订单

### 支持的操作

| 操作 | 说明 |
|------|------|
| `get_tick` | 24小时滚动行情 |
| `get_depth` | 订单簿深度 |
| `get_kline` | K线/蜡烛图 |
| `get_trades` | 近期成交历史 |
| `get_balance` | 所有资产余额 |
| `get_account` | 完整账户信息 |
| `make_order` | 限价下单 |
| `cancel_order` | 按ID撤单 |
| `query_order` | 按ID查询订单 |
| `get_open_orders` | 所有挂单 |

### 架构

```
bt_api_btcturk/
├── src/bt_api_btcturk/
│   ├── plugin.py              # 插件入口
│   ├── registry_registration.py  # 交易所注册
│   ├── exchange_data/
│   │   └── __init__.py      # BTCTurkExchangeDataSpot
│   ├── feeds/
│   │   └── live_btcturk/
│   │       ├── spot.py       # BTCTurkRequestDataSpot
│   │       └── request_base.py  # 基础请求类
│   ├── containers/           # 数据容器
│   └── errors/
│       └── __init__.py       # 错误翻译器
└── configs/
    └── btcturk.yaml         # 交易所配置
```

### 安装

```bash
pip install bt_api_btcturk
```

### 快速开始

```python
from bt_api_py import BtApi

# 公开市场数据（无需 API key）
api = BtApi()
ticker = api.get_tick("BTCTURK___SPOT", "BTCUSDT")
print(f"BTC 价格: {ticker}")

# 认证请求
api = BtApi(exchange_kwargs={
    "BTCTURK___SPOT": {
        "api_key": "your_api_key",
        "secret": "your_secret",
    }
})

balance = api.get_balance("BTCTURK___SPOT")
order = api.make_order(
    exchange_name="BTCTURK___SPOT",
    symbol="BTCUSDT",
    volume=0.001,
    price=500000,
    order_type="limit",
)
```

### 支持的交易对

BTCTurk 交易对（TRY 基础货币）：

- `BTCUSDT`, `ETHUSDT`, `XRPUSDT`, `SOLUSDT`, `DOGEUSDT` ...
- `TRY` 交易对: `BTCTRY`, `ETHTRY`, `XRPTRY` ...

### 错误处理

| 错误码 | 错误类型 | 说明 |
|--------|----------|------|
| `0` | `SUCCESS` | 成功 |
| `-1` | `AUTH_ERROR` | 认证错误 |
| `-2` | `AUTH_ERROR` | 无效签名 |
| `-3` | `RATE_LIMIT` | 请求过于频繁 |
| `-4` | `INSUFFICIENT_BALANCE` | 余额不足 |
| `-5` | `ORDER_NOT_FOUND` | 订单不存在 |
| `-6` | `INVALID_ORDER_TYPE` | 无效订单类型 |

### 限流配置

BTCTurk API 限流：

- **公开接口**: 60 次/分钟
- **私有接口**: 120 次/分钟

---

## Resources

| Resource | Link |
|----------|------|
| English Docs | https://bt-api-btcturk.readthedocs.io/ |
| Chinese Docs | https://bt-api-btcturk.readthedocs.io/zh/latest/ |
| GitHub | https://github.com/cloudQuant/bt_api_btcturk |
| PyPI | https://pypi.org/project/bt_api_btcturk/ |
| Issues | https://github.com/cloudQuant/bt_api_btcturk/issues |
| bt_api_base | https://bt-api-base.readthedocs.io/ |
| Main Project | https://cloudquant.github.io/bt_api_py/ |
