from typing import NoReturn

from fastapi import HTTPException

from src.config import logger
from src.services.exceptions.base_exceptions import BaseExceptions


class HTTPExceptions(BaseExceptions):
    def is_invalid(self, value1: str, value2: str | None = None) -> NoReturn:
        detail, status_code = self._is_invalid(value1=value1, value2=value2)
        logger.info(detail)
        raise HTTPException(detail=detail, status_code=status_code)

    def has_expired(self, value: str) -> NoReturn:
        detail, status_code = self._has_expired(value=value)
        logger.info(detail)
        raise HTTPException(detail=detail, status_code=status_code)

    def must_be_confirmed(self, value: str) -> NoReturn:
        detail, status_code = self._must_be_confirmed(value=value)
        logger.info(detail)
        raise HTTPException(detail=detail, status_code=status_code)

    def login_required(self) -> NoReturn:
        detail, status_code = self._login_required()
        logger.info(detail)
        raise HTTPException(detail=detail, status_code=status_code)

    def not_found(self, value: str) -> NoReturn:
        detail, status_code = self._not_found(value=value)
        logger.info(detail)
        raise HTTPException(detail=detail, status_code=status_code)
