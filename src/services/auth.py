from src.api.schemas.auth.login import UserLoginRequestSchema
from src.api.schemas.auth.registration import UserRegistrationRequestSchema, UserRegistrationResponseSchema
from src.config import logger
from src.repositories.auth import AuthRepository
from src.services.validators.auth import AuthValidator
from src.utils.hash_password import HashPassword


class AuthService:
    def __init__(self) -> None:
        self.auth_repository = AuthRepository()
        self.auth_validator = AuthValidator()
        self.hash_password = HashPassword()

    async def registration(self, user: UserRegistrationRequestSchema) -> UserRegistrationResponseSchema:
        user_dict = user.model_dump()

        await self.auth_validator.already_exists_auth_validator(
            {"username": user_dict["username"], "email": user_dict["email"]}
        )

        user_dict["hashed_password"] = self.hash_password.create_hash(user_dict.pop("password"))

        res = await self.auth_repository.add_one(user_dict)

        logger.info(f"User registered: {user_dict['username']}")

        return UserRegistrationResponseSchema(**res)

    async def login(self, user: UserLoginRequestSchema) -> bool | None:
        user_dict = user.model_dump()

        user_exist = await self.auth_repository.get_one(model_field="email", value=user_dict["email"])

        if user_exist:
            res = self.hash_password.verify_hash(user_dict["password"], user_exist.hashed_password)
            return res
        else:
            # вызывать исключение, что пользователь с такой почтой или паролем не найден
            pass

        return None
