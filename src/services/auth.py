from src.api.schemas.auth import UserRegistrationRequestSchema, UserRegistrationResponseSchema
from src.repositories.auth import AuthRepository


class AuthService:
    def __init__(self) -> None:
        self.auth_repository = AuthRepository()

    async def registration(self, user: UserRegistrationRequestSchema) -> UserRegistrationResponseSchema:
        user_dict = user.model_dump()

        res = await self.auth_repository.add_one(user_dict)

        return UserRegistrationResponseSchema(**res)
