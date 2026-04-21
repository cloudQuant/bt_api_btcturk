from __future__ import annotations

import base64
import hashlib
import hmac
import time
from typing import Any, Optional

from bt_api_base.feeds.capability import Capability
from bt_api_base.feeds.feed import Feed
from bt_api_base.feeds.http_client import HttpClient
from bt_api_base.containers.requestdatas.request_data import RequestData
from bt_api_btcturk.exchange_data import BTCTurkExchangeDataSpot


class BTCTurkRequestData(Feed):
    @classmethod
    def _capabilities(cls) -> set[Capability]:
        return {
            Capability.GET_TICK,
            Capability.GET_DEPTH,
            Capability.GET_KLINE,
            Capability.GET_EXCHANGE_INFO,
            Capability.GET_BALANCE,
            Capability.GET_ACCOUNT,
            Capability.MAKE_ORDER,
            Capability.CANCEL_ORDER,
        }

    def __init__(self, data_queue: Any = None, **kwargs: Any) -> None:
        super().__init__(data_queue, **kwargs)
        self.data_queue = data_queue
        self.exchange_name = kwargs.get("exchange_name", "BTCTURK___SPOT")
        self.asset_type = kwargs.get("asset_type", "SPOT")
        self._params = BTCTurkExchangeDataSpot()
        self._params.api_key = kwargs.get("public_key") or kwargs.get("api_key")
        self._params.api_secret = kwargs.get("private_key") or kwargs.get("api_secret") or kwargs.get("secret_key")
        self._http_client = HttpClient(venue=self.exchange_name, timeout=10)

    def _generate_signature(self, timestamp: int) -> str:
        public_key = self._params.api_key
        private_key = self._params.api_secret
        if public_key and private_key:
            message = public_key + str(timestamp)
            private_key_bytes = base64.b64decode(private_key)
            signature = base64.b64encode(
                hmac.new(private_key_bytes, message.encode("utf-8"), hashlib.sha256).digest()
            ).decode("utf-8")
            return signature
        return ""

    def _get_headers(
        self, method: str, request_path: str, params: dict = None, body: str = ""
    ) -> dict:
        timestamp = int(time.time() * 1000)
        headers = {"Content-Type": "application/json"}
        if self._params.api_key:
            headers["X-PCK"] = self._params.api_key
            headers["X-Stamp"] = str(timestamp)
            headers["X-Signature"] = self._generate_signature(timestamp)
        return headers

    def request(
        self, path: str, params=None, body: Any = None, extra_data=None, timeout=10
    ) -> RequestData:
        method = path.split()[0] if " " in path else "GET"
        request_path = "/" + path.split()[1] if " " in path else path
        headers = self._get_headers(method, request_path, params, body)
        try:
            response = self._http_client.request(
                method=method,
                url=self._params.rest_url + request_path,
                headers=headers,
                json_data=body if method == "POST" else None,
                params=params,
            )
            return RequestData(response, extra_data or {})
        except Exception as e:
            self.logger.error(f"Request failed: {e}")
            raise

    async def async_request(
        self, path: str, params=None, body: Any = None, extra_data=None, timeout=5
    ) -> RequestData:
        method = path.split()[0] if " " in path else "GET"
        request_path = "/" + path.split()[1] if " " in path else path
        headers = self._get_headers(method, request_path, params, body)
        try:
            response = await self._http_client.async_request(
                method=method,
                url=self._params.rest_url + request_path,
                headers=headers,
                json_data=body if method == "POST" else None,
                params=params,
            )
            return RequestData(response, extra_data or {})
        except Exception as e:
            self.async_logger.error(f"Async request failed: {e}")
            raise

    def async_callback(self, future: Any) -> None:
        try:
            result = future.result()
            if result is not None:
                self.push_data_to_queue(result)
        except Exception as e:
            self.async_logger.error(f"Async callback error: {e}")

    def push_data_to_queue(self, data: Any) -> None:
        if self.data_queue is not None:
            self.data_queue.put(data)
