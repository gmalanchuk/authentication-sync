from src.enums.tag import TagEnum
from src.repositories.permission import PermissionRepository
from src.services.exceptions.base_exceptions import BaseExceptions
from src.utils.jwt_token import JWTToken


class PermissionService:
    def __init__(self, tag: TagEnum) -> None:
        self.permission_repository = PermissionRepository()
        self.exception = BaseExceptions(tag)
        self.jwt_token = JWTToken(tag)

    async def get_user_info_by_token(self, token_dict: dict) -> tuple[int, str, str, str, str]:
        payload = await self.jwt_token.decode_token(token_dict["token"])

        user = await self.permission_repository.get_one(model_field="id", value=payload["user_id"])

        if not user.is_verified:  # TODO ВЫНЕСТИ В STATICMETHOD
            return await self.exception.must_be_confirmed("email")

        return user.id, user.username, user.email, user.name, user.role.value
