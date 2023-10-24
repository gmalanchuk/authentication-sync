from src.api.schemas.auth import UserRegistrationRequestSchema, UserRegistrationResponseSchema
from src.repositories.auth import AuthRepository
from src.services.validators.auth import AuthValidator


class AuthService:
    def __init__(self) -> None:
        self.auth_repository = AuthRepository()
        self.auth_validator = AuthValidator()

    async def registration(self, user: UserRegistrationRequestSchema) -> UserRegistrationResponseSchema:
        user_dict = user.model_dump()

        await self.auth_validator.already_exists_username_email_validators(
            username=user_dict["username"], email=user_dict["email"]
        )

        res = await self.auth_repository.add_one(user_dict)

        return UserRegistrationResponseSchema(**res)
