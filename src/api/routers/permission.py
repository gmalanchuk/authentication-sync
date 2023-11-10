from fastapi import APIRouter, Depends

from src.api.schemas.permission.check_permission import TokenSchema
from src.services.dependencies import get_permission_service
from src.services.permission import PermissionService


permission_router = APIRouter(prefix="/v1/permission", tags=["Permissions"])


@permission_router.post(path="/check/")
async def check_permission(
    token: TokenSchema, permission_service: PermissionService = Depends(get_permission_service)
) -> None:
    # сюда поступает жвт токен
    # этот токен декодируется и достаётся из него айдишник пользователя
    # берём пользователя по этому айдишнику
    # проверяем, потвердил ли он почту (is_verified должно быть True)
    # если is_verified=False, то рейзить ошибку о том, что нужно подтвердить почту
    # иначе
    # возвращаем роль пользователя(права)
    return await permission_service.check(token.model_dump())
