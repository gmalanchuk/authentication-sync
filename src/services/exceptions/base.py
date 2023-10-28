from typing import NoReturn

from fastapi import HTTPException

from src.config import logger


class BaseHTTPException:
    @staticmethod
    async def already_exists_exception(model_name: str, model_field: str) -> NoReturn:
        logger.info(f"{model_name.title()} with this {model_field.lower()} already exists")
        raise HTTPException(
            detail=f"{model_name.title()} with this {model_field.lower()} already exists", status_code=409
        )
