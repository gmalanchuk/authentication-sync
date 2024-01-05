from src.enums.tag import TagEnum
from src.repositories.user import UserRepository
from src.services.exceptions.base_exceptions import BaseExceptions
from src.utils.jwt_token import JWTToken


class UserGRPCService:
    def __init__(self) -> None:
        self.user_repo = UserRepository()
        self.exception = BaseExceptions(TagEnum.GRPC)
        self.jwt_token = JWTToken(TagEnum.GRPC)

    async def get_user_info_by_token(self, token_dict: dict) -> tuple[int, str, str, str, str]:
        payload = await self.jwt_token.decode_token(token_dict["token"])

        user = await self.user_repo.get_one(model_field="id", value=payload["user_id"])

        if not user.is_verified:
            return await self.exception.must_be_confirmed(value="email")

        return user.id, user.username, user.email, user.name, user.role.value

    async def get_user_info_by_id(self, user_dict: dict) -> tuple[int, str, str, str, str]:
        user = await self.user_repo.get_one(model_field="id", value=user_dict["user_id"])

        if not user:
            return await self.exception.not_found(value="User")

        return user.id, user.username, user.email, user.name, user.role.value
