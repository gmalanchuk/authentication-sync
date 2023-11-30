from starlette import status
from starlette.responses import JSONResponse

from src.repositories.permission import PermissionRepository
from src.services.enums.tag import TagEnum
from src.services.exceptions.base_exceptions import BaseExceptions
from src.utils.jwt_token import JWTToken


class PermissionService:
    def __init__(self, tag: TagEnum) -> None:
        self.permission_repository = PermissionRepository()
        self.exception = BaseExceptions(tag)
        self.jwt_token = JWTToken(tag)
        self.tag = tag

    async def check(self, token_dict: dict) -> str | None:
        payload = await self.jwt_token.decode_token(token_dict["token"])

        user = await self.permission_repository.get_one(model_field="id", value=payload["user_id"])

        if not user.is_verified:
            return await self.exception.must_be_confirmed("email")

        if self.tag == self.tag.HTTP:
            return JSONResponse(content={"role": user.role.value}, status_code=status.HTTP_200_OK)
        elif self.tag == self.tag.GRPC:
            return user.role.value

        return None
