from fastapi import APIRouter, Depends

from src.api.schemas.permission.check_permission import TokenSchema
from src.services.dependencies import get_permission_service
from src.services.permission import PermissionService


permission_router = APIRouter(prefix="/v1/permission", tags=["Permissions"])


@permission_router.post(path="/check/")
async def check_permission(
    request_token: TokenSchema, permission_service: PermissionService = Depends(get_permission_service)
) -> str | None:
    return await permission_service.check(token_dict=request_token.model_dump())
