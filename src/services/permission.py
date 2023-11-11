from typing import NoReturn

from starlette import status
from starlette.responses import JSONResponse

from src.api.schemas.permission.check_permission import TokenSchema
from src.repositories.permission import PermissionRepository
from src.services.exceptions.base import BaseHTTPException
from src.utils.jwt_token import JWTToken


class PermissionService:
    def __init__(self) -> None:
        self.permission_repository = PermissionRepository()
        self.exception = BaseHTTPException()
        self.jwt_token = JWTToken()

    async def check(self, token: TokenSchema) -> JSONResponse | NoReturn:
        token_dict = token.model_dump()

        payload = await self.jwt_token.decode_token(token_dict["token"])

        user = await self.permission_repository.get_one(model_field="id", value=payload["user_id"])

        if not user.is_verified:
            return await self.exception.must_be_confirmed("email")

        return JSONResponse(content={"role": user.role.value}, status_code=status.HTTP_200_OK)
