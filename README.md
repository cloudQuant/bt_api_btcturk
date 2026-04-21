# bt_api_btcturk

[![PyPI Version](https://img.shields.io/pypi/v/bt_api_btcturk.svg)](https://pypi.org/project/bt_api_btcturk/)
[![Python Versions](https://img.shields.io/pypi/pyversions/bt_api_btcturk.svg)](https://pypi.org/project/bt_api_btcturk/)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![CI](https://github.com/cloudQuant/bt_api_btcturk/actions/workflows/ci.yml/badge.svg)](https://github.com/cloudQuant/bt_api_btcturk/actions)
[![Docs](https://readthedocs.org/projects/bt-api-btcturk/badge/?version=latest)](https://bt-api-btcturk.readthedocs.io/)

---

<!-- English -->
# bt_api_btcturk

> **BTCTurk exchange plugin for bt_api** — Unified REST API for **Spot** trading.

`bt_api_btcturk` is a runtime plugin for [bt_api](https://github.com/cloudQuant/bt_api_py) that connects to **BTCTurk** exchange. It depends on [bt_api_base](https://github.com/cloudQuant/bt_api_base) for core infrastructure.

| Resource | Link |
|----------|------|
| English Docs | https://bt-api-btcturk.readthedocs.io/ |
| Chinese Docs | https://bt-api-btcturk.readthedocs.io/zh/latest/ |
| GitHub | https://github.com/cloudQuant/bt_api_btcturk |
| PyPI | https://pypi.org/project/bt_api_btcturk/ |
| Issues | https://github.com/cloudQuant/bt_api_btcturk/issues |
| bt_api_base | https://bt-api-base.readthedocs.io/ |
| Main Project | https://github.com/cloudQuant/bt_api_py |

---

## Features

### 1 Asset Type

| Asset Type | Code | REST | Description |
|---|---|---|---|
| Spot | `BTCTURK___SPOT` | ✅ | Spot trading (TRY pairs) |

### REST API

- **Market Data** — Ticker, order book, k-lines, trades
- **Account** — Balance, account info
- **Trading** — Place orders, cancel orders, query orders

### Plugin Architecture

Auto-registers at import time via `ExchangeRegistry`. Works seamlessly with `BtApi`:

```python
from bt_api_py import BtApi

api = BtApi(exchange_kwargs={
    "BTCTURK___SPOT": {
        "api_key": "your_key",
        "secret": "your_secret",
    }
})

ticker = api.get_tick("BTCTURK___SPOT", "BTCUSDT")
balance = api.get_balance("BTCTURK___SPOT")
order = api.make_order(exchange_name="BTCTURK___SPOT", symbol="BTCUSDT", volume=0.001, price=500000, order_type="limit")
```

### Unified Data Containers

All exchange responses normalized to bt_api_base container types:

- `TickContainer` — 24hr rolling ticker
- `OrderBookContainer` — Order book depth
- `BarContainer` — K-line/candlestick
- `TradeContainer` — Individual trades
- `OrderContainer` — Order status and fills
- `AccountBalanceContainer` — Asset balances

---

## Installation

### From PyPI (Recommended)

```bash
pip install bt_api_btcturk
```

### From Source

```bash
git clone https://github.com/cloudQuant/bt_api_btcturk
cd bt_api_btcturk
pip install -e .
```

### Requirements

- Python `3.9` – `3.14`
- `bt_api_base >= 0.15`

---

## Quick Start

### 1. Install

```bash
pip install bt_api_btcturk
```

### 2. Get ticker (public — no API key needed)

```python
from bt_api_py import BtApi

api = BtApi()
ticker = api.get_tick("BTCTURK___SPOT", "BTCUSDT")
print(f"BTCUSDT price: {ticker}")
```

### 3. Place an order (requires API key)

```python
from bt_api_py import BtApi

api = BtApi(exchange_kwargs={
    "BTCTURK___SPOT": {
        "api_key": "your_api_key",
        "secret": "your_secret",
    }
})

order = api.make_order(
    exchange_name="BTCTURK___SPOT",
    symbol="BTCUSDT",
    volume=0.001,
    price=500000,
    order_type="limit",
)
print(f"Order placed: {order}")
```

---

## Supported Operations

| Category | Operation | Notes |
|---|---|---|
| **Market Data** | `get_tick` | 24hr rolling ticker |
| | `get_depth` | Order book depth |
| | `get_kline` | K-line/candlestick |
| | `get_trades` | Recent trade history |
| **Account** | `get_balance` | All asset balances |
| | `get_account` | Full account info |
| **Trading** | `make_order` | LIMIT order |
| | `cancel_order` | Cancel order by ID |
| | `query_order` | Query order by ID |
| | `get_open_orders` | All open orders |

---

## Supported Symbols

BTCTurk trading pairs (TRY base currency):

- `BTCUSDT`, `ETHUSDT`, `XRPUSDT`, `SOLUSDT`, `DOGEUSDT` ...
- `TRY` pairs: `BTCTRY`, `ETHTRY`, `XRPTRY` ...

---

## Error Handling

All BTCTurk API errors are translated to bt_api_base `ApiError` subclasses:

| BTCTurk Code | Error | Description |
|---|---|---|
| `0` | `SUCCESS` | Success |
| `-1` | `AUTH_ERROR` | Authentication error |
| `-2` | `AUTH_ERROR` | Invalid signature |
| `-3` | `RATE_LIMIT` | Rate limit exceeded |
| `-4` | `INSUFFICIENT_BALANCE` | Insufficient balance |
| `-5` | `ORDER_NOT_FOUND` | Order not found |
| `-6` | `INVALID_ORDER_TYPE` | Invalid order type |

---

## Documentation

| Doc | Link |
|-----|------|
| **English** | https://bt-api-btcturk.readthedocs.io/ |
| **中文** | https://bt-api-btcturk.readthedocs.io/zh/latest/ |
| bt_api_base | https://bt-api-base.readthedocs.io/ |
| Main Project | https://cloudquant.github.io/bt_api_py/ |

---

## License

MIT — see [LICENSE](LICENSE).

---

## Support

- [GitHub Issues](https://github.com/cloudQuant/bt_api_btcturk/issues) — bug reports, feature requests
- Email: yunjinqi@gmail.com

---

---

## 中文

> **bt_api 的 BTCTurk 交易所插件** — 为**现货**交易提供统一的 REST API。

`bt_api_btcturk` 是 [bt_api](https://github.com/cloudQuant/bt_api_py) 的运行时插件，连接 **BTCTurk** 交易所。依赖 [bt_api_base](https://github.com/cloudQuant/bt_api_base) 提供核心基础设施。

| 资源 | 链接 |
|------|------|
| 英文文档 | https://bt-api-btcturk.readthedocs.io/ |
| 中文文档 | https://bt-api-btcturk.readthedocs.io/zh/latest/ |
| GitHub | https://github.com/cloudQuant/bt_api_btcturk |
| PyPI | https://pypi.org/project/bt_api_btcturk/ |
| 问题反馈 | https://github.com/cloudQuant/bt_api_btcturk/issues |
| bt_api_base | https://bt-api-base.readthedocs.io/ |
| 主项目 | https://github.com/cloudQuant/bt_api_py |

---

## 功能特点

### 1 种资产类型

| 资产类型 | 代码 | REST | 说明 |
|---|---|---|---|
| 现货 | `BTCTURK___SPOT` | ✅ | 现货交易（TRY交易对） |

### REST API

- **行情数据** — 行情、订单簿、K线、成交
- **账户** — 余额、账户信息
- **交易** — 下单、撤单、查询订单

### 插件架构

通过 `ExchangeRegistry` 在导入时自动注册，与 `BtApi` 无缝协作：

```python
from bt_api_py import BtApi

api = BtApi(exchange_kwargs={
    "BTCTURK___SPOT": {
        "api_key": "your_key",
        "secret": "your_secret",
    }
})

ticker = api.get_tick("BTCTURK___SPOT", "BTCUSDT")
balance = api.get_balance("BTCTURK___SPOT")
order = api.make_order(exchange_name="BTCTURK___SPOT", symbol="BTCUSDT", volume=0.001, price=500000, order_type="limit")
```

### 统一数据容器

所有交易所响应规范化为 bt_api_base 容器类型：

- `TickContainer` — 24小时滚动行情
- `OrderBookContainer` — 订单簿深度
- `BarContainer` — K线/蜡烛图
- `TradeContainer` — 逐笔成交
- `OrderContainer` — 订单状态和成交
- `AccountBalanceContainer` — 资产余额

---

## 安装

### 从 PyPI 安装（推荐）

```bash
pip install bt_api_btcturk
```

### 从源码安装

```bash
git clone https://github.com/cloudQuant/bt_api_btcturk
cd bt_api_btcturk
pip install -e .
```

### 系统要求

- Python `3.9` – `3.14`
- `bt_api_base >= 0.15`

---

## 快速开始

### 1. 安装

```bash
pip install bt_api_btcturk
```

### 2. 获取行情（公开接口，无需 API key）

```python
from bt_api_py import BtApi

api = BtApi()
ticker = api.get_tick("BTCTURK___SPOT", "BTCUSDT")
print(f"BTCUSDT 价格: {ticker}")
```

### 3. 下单交易（需要 API key）

```python
from bt_api_py import BtApi

api = BtApi(exchange_kwargs={
    "BTCTURK___SPOT": {
        "api_key": "your_api_key",
        "secret": "your_secret",
    }
})

order = api.make_order(
    exchange_name="BTCTURK___SPOT",
    symbol="BTCUSDT",
    volume=0.001,
    price=500000,
    order_type="limit",
)
print(f"订单已下单: {order}")
```

---

## 支持的操作

| 类别 | 操作 | 说明 |
|---|---|---|
| **行情数据** | `get_tick` | 24小时滚动行情 |
| | `get_depth` | 订单簿深度 |
| | `get_kline` | K线/蜡烛图 |
| | `get_trades` | 近期成交历史 |
| **账户** | `get_balance` | 所有资产余额 |
| | `get_account` | 完整账户信息 |
| **交易** | `make_order` | 限价单 |
| | `cancel_order` | 按ID撤单 |
| | `query_order` | 按ID查询订单 |
| | `get_open_orders` | 所有挂单 |

---

## 支持的交易对

BTCTurk 交易对（TRY 基础货币）：

- `BTCUSDT`, `ETHUSDT`, `XRPUSDT`, `SOLUSDT`, `DOGEUSDT` ...
- `TRY` 交易对: `BTCTRY`, `ETHTRY`, `XRPTRY` ...

---

## 错误处理

所有 BTCTurk API 错误均翻译为 bt_api_base `ApiError` 子类：

| BTCTurk 错误码 | 错误类型 | 说明 |
|---|---|---|
| `0` | `SUCCESS` | 成功 |
| `-1` | `AUTH_ERROR` | 认证错误 |
| `-2` | `AUTH_ERROR` | 无效签名 |
| `-3` | `RATE_LIMIT` | 请求过于频繁 |
| `-4` | `INSUFFICIENT_BALANCE` | 余额不足 |
| `-5` | `ORDER_NOT_FOUND` | 订单不存在 |
| `-6` | `INVALID_ORDER_TYPE` | 无效订单类型 |

---

## 文档

| 文档 | 链接 |
|-----|------|
| **英文文档** | https://bt-api-btcturk.readthedocs.io/ |
| **中文文档** | https://bt-api-btcturk.readthedocs.io/zh/latest/ |
| bt_api_base | https://bt-api-base.readthedocs.io/ |
| 主项目 | https://cloudquant.github.io/bt_api_py/ |

---

## 许可证

MIT — 详见 [LICENSE](LICENSE)。

---

## 技术支持

- [GitHub Issues](https://github.com/cloudQuant/bt_api_btcturk/issues) — bug 报告、功能请求
- 邮箱: yunjinqi@gmail.com
