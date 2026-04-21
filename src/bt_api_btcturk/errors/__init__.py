from __future__ import annotations

from bt_api_base.error import ErrorTranslator, UnifiedErrorCode


class BTCTurkErrorTranslator(ErrorTranslator):
    _ERROR_MAP = {
        "0": UnifiedErrorCode.SUCCESS,
        "-1": UnifiedErrorCode.INVALID_PARAMETER,
        "-2": UnifiedErrorCode.AUTH_ERROR,
        "-3": UnifiedErrorCode.RATE_LIMIT,
        "-4": UnifiedErrorCode.INSUFFICIENT_BALANCE,
        "-5": UnifiedErrorCode.ORDER_NOT_FOUND,
        "-6": UnifiedErrorCode.INVALID_ORDER_TYPE,
    }

    @classmethod
    def translate_error(cls, error_code: str | int | None) -> UnifiedErrorCode:
        if error_code is None:
            return UnifiedErrorCode.UNKNOWN
        code_str = str(error_code)
        return cls._ERROR_MAP.get(code_str, UnifiedErrorCode.UNKNOWN)

    @staticmethod
    def is_success(error_code: str | int | None) -> bool:
        return error_code == "0" or error_code == 0
