import grpc

from protos.permission_pb2 import PermissionRequest, PermissionResponse
from protos.permission_pb2_grpc import PermissionServicer
from src.services.enums.tag import TagEnum
from src.services.permission import PermissionService


class CheckPermission(PermissionServicer):
    def __init__(self) -> None:
        self.permission_service = PermissionService()

    async def CheckPermission(
        self, request: PermissionRequest, context: grpc.aio.ServicerContext
    ) -> PermissionResponse:
        role = await self.permission_service.check(token_dict={"token": request.token}, tag=TagEnum.GRPC)
        return PermissionResponse(role=role)
