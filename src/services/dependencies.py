from src.services.auth import AuthService
from src.services.enums.tag import TagEnum
from src.services.permission import PermissionService


async def get_auth_service() -> AuthService:
    return AuthService()


async def get_permission_service() -> PermissionService:
    return PermissionService(tag=TagEnum.HTTP)
