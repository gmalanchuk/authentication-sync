from typing import NoReturn

from starlette.responses import JSONResponse

from src.api.schemas.auth.login import UserLoginRequestSchema
from src.api.schemas.auth.registration import UserRegistrationRequestSchema, UserRegistrationResponseSchema
from src.config import logger
from src.repositories.auth import AuthRepository
from src.services.exceptions.base import BaseHTTPException
from src.services.validators.auth import AuthValidator
from src.utils.hash_password import HashPassword


class AuthService:
    def __init__(self) -> None:
        self.auth_repository = AuthRepository()
        self.auth_validator = AuthValidator()
        self.hash_password = HashPassword()
        self.exception = BaseHTTPException()

    async def registration(self, user: UserRegistrationRequestSchema) -> UserRegistrationResponseSchema:
        user_dict = user.model_dump()

        await self.auth_validator.already_exists_auth_validator(
            {"username": user_dict["username"], "email": user_dict["email"]}
        )

        user_dict["hashed_password"] = self.hash_password.create_hash(user_dict.pop("password"))

        res = await self.auth_repository.add_one(user_dict)

        logger.info(f"User registered: {user_dict['username']}")

        return UserRegistrationResponseSchema(**res)

    async def login(self, user: UserLoginRequestSchema) -> JSONResponse | NoReturn:
        user_dict = user.model_dump()

        user_exist = await self.auth_repository.get_one(model_field="email", value=user_dict["email"])
        if user_exist:
            if self.hash_password.verify_hash(user_dict["password"], user_exist.hashed_password):
                # TODO set to cookie access/refresh tokens (не уверен в том, что нужно устанавливать два токена в куки)
                return JSONResponse(
                    content="SUCCESS!! jwt(access/refresh tokens)", status_code=200
                )  # todo возвращать jwt(access/refresh токены)

        return await self.exception.is_invalid(column_name1="email", column_name2="password")
