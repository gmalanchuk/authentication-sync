from src.api.schemas.permission.check_permission import TokenSchema
from src.repositories.permission import PermissionRepository
from src.utils.jwt_token import JWTToken


class PermissionService:
    def __init__(self) -> None:
        self.permission_repository = PermissionRepository()
        self.jwt_token = JWTToken()

    async def check(self, token: TokenSchema) -> None:
        token_dict = token.model_dump()

        payload = await self.jwt_token.decode_token(token_dict["token"])

        print(payload)

        # берём пользователя по этому айдишнику
        # проверяем, потвердил ли он почту (is_verified должно быть True)
        # если is_verified=False, то рейзить ошибку о том, что нужно подтвердить почту
        # иначе
        # возвращаем роль пользователя(права)
