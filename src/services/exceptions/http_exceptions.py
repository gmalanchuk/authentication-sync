from typing import NoReturn

from fastapi import HTTPException
from starlette import status

from src.config import logger


class HTTPExceptions:
    @staticmethod
    async def is_invalid(value1: str, value2: str | None = None) -> NoReturn:
        value2 = f"or {value2} " if value2 else ""
        logger.info(f"{value1} {value2}is invalid")
        raise HTTPException(detail=f"{value1} {value2}is invalid", status_code=status.HTTP_401_UNAUTHORIZED)

    @staticmethod
    async def has_expired(value: str) -> NoReturn:
        logger.info(f"{value} has expired")
        raise HTTPException(detail=f"{value} has expired", status_code=status.HTTP_401_UNAUTHORIZED)

    @staticmethod
    async def must_be_confirmed(value: str) -> NoReturn:
        logger.info(f"To perform this action, your {value} must be confirmed")
        raise HTTPException(
            detail=f"To perform this action, your {value} must be confirmed", status_code=status.HTTP_401_UNAUTHORIZED
        )
