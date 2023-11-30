from typing import NoReturn

from fastapi import HTTPException
from starlette import status

from src.config import logger


class ValidatorHTTPExceptions:
    @staticmethod
    async def already_exists(model_name: str, model_field: str) -> NoReturn:
        logger.info(f"{model_name.title()} with this {model_field.lower()} already exists")
        raise HTTPException(
            detail=f"{model_name.title()} with this {model_field.lower()} already exists",
            status_code=status.HTTP_409_CONFLICT,
        )
