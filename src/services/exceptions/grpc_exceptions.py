from typing import NoReturn

import grpc

from src.config import logger


class GRPCExceptions:
    @staticmethod
    async def is_invalid(detail: str, status_code: int) -> NoReturn:
        logger.info(detail)
        raise grpc.RpcError(grpc.StatusCode.UNAUTHENTICATED, detail)

    @staticmethod
    async def has_expired(detail: str, status_code: int) -> NoReturn:
        logger.info(detail)
        raise grpc.RpcError(grpc.StatusCode.UNAUTHENTICATED, detail)

    @staticmethod
    async def must_be_confirmed(detail: str, status_code: int) -> NoReturn:
        logger.info(detail)
        raise grpc.RpcError(grpc.StatusCode.UNAUTHENTICATED, detail)

    @staticmethod
    async def login_required(detail: str, status_code: int) -> NoReturn:
        logger.info(detail)
        raise grpc.RpcError(grpc.StatusCode.UNAUTHENTICATED, detail)
