from typing import NoReturn

from src.database.models.base import Base
from src.services.exceptions.base import BaseHTTPException


class BaseValidator(BaseHTTPException):
    async def already_exists_validator(self, exists: None | Base, model_name: str, model_field: str) -> None | NoReturn:
        if exists:
            await self.already_exists_exception(model_name=model_name, model_field=model_field)
        return None
