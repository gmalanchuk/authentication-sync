from typing import NoReturn

import grpc

from src.config import logger
from src.services.exceptions.base_exceptions import BaseExceptions


class GRPCExceptions(BaseExceptions):
    def is_invalid(self, value1: str, value2: str | None = None) -> NoReturn:
        detail, _ = self._is_invalid(value1=value1, value2=value2)
        logger.info(detail)
        raise grpc.RpcError(grpc.StatusCode.UNAUTHENTICATED, detail)

    def has_expired(self, value: str) -> NoReturn:
        detail, _ = self._has_expired(value=value)
        logger.info(detail)
        raise grpc.RpcError(grpc.StatusCode.UNAUTHENTICATED, detail)

    def must_be_confirmed(self, value: str) -> NoReturn:
        detail, _ = self._must_be_confirmed(value=value)
        logger.info(detail)
        raise grpc.RpcError(grpc.StatusCode.UNAUTHENTICATED, detail)

    def login_required(self) -> NoReturn:
        detail, _ = self._login_required()
        logger.info(detail)
        raise grpc.RpcError(grpc.StatusCode.UNAUTHENTICATED, detail)

    def not_found(self, value: str) -> NoReturn:
        detail, _ = self._not_found(value=value)
        logger.info(detail)
        raise grpc.RpcError(grpc.StatusCode.NOT_FOUND, detail)
