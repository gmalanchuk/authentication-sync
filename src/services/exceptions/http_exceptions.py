from typing import NoReturn

from fastapi import HTTPException

from src.config import logger


class HTTPExceptions:
    @staticmethod
    async def is_invalid(detail: str, status_code: int) -> NoReturn:
        logger.info(detail)
        raise HTTPException(detail=detail, status_code=status_code)

    @staticmethod
    async def has_expired(detail: str, status_code: int) -> NoReturn:
        logger.info(detail)
        raise HTTPException(detail=detail, status_code=status_code)

    @staticmethod
    async def must_be_confirmed(detail: str, status_code: int) -> NoReturn:
        logger.info(detail)
        raise HTTPException(detail=detail, status_code=status_code)

    @staticmethod
    async def login_required(detail: str, status_code: int) -> NoReturn:
        logger.info(detail)
        raise HTTPException(detail=detail, status_code=status_code)

    @staticmethod
    async def not_found(detail: str, status_code: int) -> NoReturn:
        logger.info(detail)
        raise HTTPException(detail=detail, status_code=status_code)
