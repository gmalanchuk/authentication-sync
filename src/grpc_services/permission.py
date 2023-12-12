import grpc

from protos.permission_pb2 import CheckRoleRequest, CheckRoleResponse
from protos.permission_pb2_grpc import PermissionServicer
from src.enums.tag import TagEnum
from src.services.permission import PermissionService


class Permission(PermissionServicer):
    def __init__(self) -> None:
        self.permission_service = PermissionService(tag=TagEnum.GRPC)

    async def CheckRole(self, request: CheckRoleRequest, context: grpc.aio.ServicerContext) -> CheckRoleResponse:
        print(999)
        role = await self.permission_service.check_role(token_dict={"token": request.token})
        return CheckRoleResponse(role=role)

    # async def CheckUserID(self, request, context) -> None:
    #     print(100)
