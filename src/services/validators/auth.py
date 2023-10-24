from typing import NoReturn

from src.repositories.auth import AuthRepository
from src.services.validators.base import BaseValidator


class AuthValidator(BaseValidator):
    model_name = "user"

    def __init__(self) -> None:
        self.auth_repository = AuthRepository()

    async def already_exists_username_validator(self, username: str) -> None | NoReturn:
        exists = await self.auth_repository.get_one(model_field="username", value=username)
        return await self.already_exists_validator(exists=exists, model_name=self.model_name, model_field="username")

    async def already_exists_email_validator(self, email: str) -> None | NoReturn:
        exists = await self.auth_repository.get_one(model_field="email", value=email)
        return await self.already_exists_validator(exists=exists, model_name=self.model_name, model_field="email")

    async def already_exists_username_email_validators(self, username: str, email: str) -> None:
        await self.already_exists_username_validator(username=username)
        await self.already_exists_email_validator(email=email)
