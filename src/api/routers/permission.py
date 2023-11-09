from fastapi import APIRouter, Depends

from src.api.schemas.permission.check_permission import JWTTokenSchema
from src.services.dependencies import get_permission_service
from src.services.permission import PermissionService


permission_router = APIRouter(prefix="/v1/permission", tags=["Permissions"])


@permission_router.post(path="/check/")
async def check_permission(
    token: JWTTokenSchema, permission_service: PermissionService = Depends(get_permission_service)
) -> None:
    return await permission_service.check(token.model_dump())


# @permission_router.post(path="/set/", response_model=None)
# async def set_permission(
#     request_user: UserLoginRequestSchema, auth_service: AuthService = Depends(get_auth_service)
# ) -> JSONResponse | NoReturn:
#     return await auth_service.login(request_user)
