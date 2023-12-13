from fastapi import APIRouter

from src.api.schemas.permission.check_permission import TokenSchema
from src.enums.tag import TagEnum
from src.services.permission import PermissionService


permission_router = APIRouter(prefix="/v1/permission", tags=["Permissions"])


@permission_router.post(path="/check_role_and_userid/")
async def check_role_and_userid(request_token: TokenSchema) -> tuple[str, int]:
    return await PermissionService(TagEnum.HTTP).check_role_and_userid(token_dict=request_token.model_dump())
