from datetime import datetime, timedelta
from typing import NoReturn
from uuid import uuid4

from starlette import status
from starlette.responses import JSONResponse

from src.api.schemas.auth.login import UserLoginRequestSchema
from src.api.schemas.auth.registration import UserRegistrationRequestSchema, UserRegistrationResponseSchema
from src.config import logger, settings
from src.repositories.auth import AuthRepository
from src.repositories.base import StartTransaction
from src.repositories.email import EmailRepository
from src.services.exceptions.http_exceptions import HTTPExceptions
from src.services.validators.auth import AuthValidator
from src.utils.hash_password import HashPassword
from src.utils.jwt_token import JWTHTTPToken


class AuthHTTPService:
    def __init__(self) -> None:
        self.auth_repository = AuthRepository()
        self.email_repository = EmailRepository()
        self.auth_validator = AuthValidator()
        self.hash_password = HashPassword()
        self.jwt_token = JWTHTTPToken()
        self.http_exception = HTTPExceptions()

    async def registration(self, user: UserRegistrationRequestSchema) -> JSONResponse:
        user_dict = user.model_dump()

        await self.auth_validator.already_exists_auth_validator(
            {"username": user_dict["username"], "email": user_dict["email"]}
        )

        user_dict["hashed_password"] = self.hash_password.create_hash(user_dict.pop("password"))

        async with StartTransaction() as session:
            user_obj = (
                UserRegistrationResponseSchema(
                    **await self.auth_repository.transaction_add_one(session=session, data=user_dict)
                )
            ).model_dump()

            await self.email_repository.transaction_add_one(
                session=session,
                data={
                    "code": uuid4(),
                    "expiration": datetime.utcnow() + timedelta(minutes=settings.EMAIL_UUID_EXPIRATION),
                    "user_id": user_obj["id"],
                },
            )

            await session.commit()

        logger.info(f"User registered: {user_obj['username']}")

        jwt_token = await self.jwt_token.create_token(user_id=user_obj["id"])

        response = JSONResponse(content=user_obj, status_code=status.HTTP_201_CREATED)
        response.set_cookie(
            key="access_token", value=jwt_token, expires=settings.JWT_TOKEN_EXPIRES, domain=settings.FRONTEND_DOMAIN
        )
        return response

    async def login(self, user: UserLoginRequestSchema) -> JSONResponse | NoReturn:
        user_dict = user.model_dump()

        user_exist = await self.auth_repository.get_one(model_field="email", value=user_dict["email"])
        if user_exist:
            if self.hash_password.verify_hash(user_dict["password"], user_exist.hashed_password):
                jwt_token = await self.jwt_token.create_token(user_id=user_exist.id)

                response = JSONResponse(content={"access_token": jwt_token}, status_code=status.HTTP_200_OK)
                response.set_cookie(
                    key="access_token",
                    value=jwt_token,
                    expires=settings.JWT_TOKEN_EXPIRES,
                    domain=settings.FRONTEND_DOMAIN,
                )
                return response

        return self.http_exception.is_invalid(value1="email", value2="password")
