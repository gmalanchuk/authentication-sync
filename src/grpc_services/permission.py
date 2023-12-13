import grpc

from protos.permission_pb2 import RoleUserIDRequest, RoleUserIDResponse
from protos.permission_pb2_grpc import PermissionServicer
from src.enums.tag import TagEnum
from src.services.permission import PermissionService


class Permission(PermissionServicer):
    def __init__(self) -> None:
        self.permission_service = PermissionService(tag=TagEnum.GRPC)

    async def CheckRoleUserID(
        self, request: RoleUserIDRequest, context: grpc.aio.ServicerContext
    ) -> RoleUserIDResponse:
        role, user_id = await self.permission_service.check_role_and_userid(token_dict={"token": request.token})
        return RoleUserIDResponse(role=role, user_id=user_id)
