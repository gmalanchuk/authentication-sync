from fastapi import APIRouter

from src.api.schemas.permission.check_permission import TokenSchema
from src.enums.tag import TagEnum
from src.services.permission import PermissionService


permission_router = APIRouter(prefix="/v1/permission", tags=["Permissions"])


@permission_router.post(path="/check/")
async def check_permission(request_token: TokenSchema) -> str | None:
    return await PermissionService(TagEnum.HTTP).check(token_dict=request_token.model_dump())
