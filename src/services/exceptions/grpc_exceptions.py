from typing import NoReturn

import grpc

from protos.permission_pb2_grpc import PermissionServicer
from src.config import logger


class GRPCExceptions(PermissionServicer):
    @staticmethod
    async def is_invalid(value1: str, value2: str | None = None) -> NoReturn:
        value2 = f"or {value2} " if value2 else ""
        logger.info(f"{value1} {value2}is invalid")
        raise grpc.RpcError(grpc.StatusCode.UNAUTHENTICATED, f"{value1} {value2}is invalid")

    @staticmethod
    async def has_expired(value: str) -> NoReturn:
        logger.info(f"{value} has expired")
        raise grpc.RpcError(grpc.StatusCode.UNAUTHENTICATED, f"{value} has expired")

    @staticmethod
    async def must_be_confirmed(value: str) -> NoReturn:
        logger.info(f"To perform this action, your {value} must be confirmed")
        raise grpc.RpcError(grpc.StatusCode.UNAUTHENTICATED, f"To perform this action, your {value} must be confirmed")
