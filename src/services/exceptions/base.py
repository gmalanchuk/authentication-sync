from typing import NoReturn

from fastapi import HTTPException
from starlette import status

from src.config import logger


class BaseHTTPException:
    @staticmethod
    async def _already_exists_exception(model_name: str, model_field: str) -> NoReturn:
        logger.info(f"{model_name.title()} with this {model_field.lower()} already exists")
        raise HTTPException(
            detail=f"{model_name.title()} with this {model_field.lower()} already exists",
            status_code=status.HTTP_409_CONFLICT,
        )

    @staticmethod
    async def is_invalid(column_name1: str, column_name2: str | None = None) -> NoReturn:
        column_name2 = f"or {column_name2} " if column_name2 else ""
        logger.info(f"{column_name1.title()} {column_name2}is invalid")
        raise HTTPException(
            detail=f"{column_name1.title()} {column_name2}is invalid", status_code=status.HTTP_401_UNAUTHORIZED
        )
