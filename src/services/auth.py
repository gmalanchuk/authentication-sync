from src.api.schemas.auth import UserRegistrationRequestSchema, UserRegistrationResponseSchema
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

        return UserRegistrationResponseSchema(**res)
