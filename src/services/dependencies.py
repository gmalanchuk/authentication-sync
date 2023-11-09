from src.services.auth import AuthService
from src.services.permission import PermissionService


async def get_auth_service() -> AuthService:
    return AuthService()


async def get_permission_service() -> PermissionService:
    return PermissionService()
