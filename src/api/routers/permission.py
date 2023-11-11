from typing import NoReturn

from fastapi import APIRouter, Depends
from starlette.responses import JSONResponse

from src.api.schemas.permission.check_permission import TokenSchema
from src.services.dependencies import get_permission_service
from src.services.permission import PermissionService


permission_router = APIRouter(prefix="/v1/permission", tags=["Permissions"])


@permission_router.post(path="/check/")
async def check_permission(
    request_token: TokenSchema, permission_service: PermissionService = Depends(get_permission_service)
) -> JSONResponse | NoReturn:
    return await permission_service.check(request_token)
