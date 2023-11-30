import grpc

from protos.permission_pb2 import PermissionRequest, PermissionResponse
from protos.permission_pb2_grpc import PermissionServicer
from src.enums.tag import TagEnum
from src.services.permission import PermissionService


class CheckPermission(PermissionServicer):
    def __init__(self) -> None:
        self.permission_service = PermissionService(tag=TagEnum.GRPC)

    async def CheckPermission(
        self, request: PermissionRequest, context: grpc.aio.ServicerContext
    ) -> PermissionResponse:
        role = await self.permission_service.check(token_dict={"token": request.token})
        return PermissionResponse(role=role)
