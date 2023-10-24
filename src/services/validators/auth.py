from typing import NoReturn

from src.repositories.auth import AuthRepository
from src.services.validators.base import BaseValidator


class AuthValidator(BaseValidator):
    model_name = "user"

    def __init__(self) -> None:
        self.auth_repository = AuthRepository()

    async def already_exists_auth_validator(self, fields: dict) -> None | NoReturn:
        """fields is dict, where key = model_field and value = value from that model_field"""

        for key, value in fields.items():
            exists = await self.auth_repository.get_one(model_field=key, value=value)
            await self.already_exists_validator(exists=exists, model_name=self.model_name, model_field=key)
        return None
