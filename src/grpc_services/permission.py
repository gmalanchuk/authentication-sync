import grpc

from protos.permission_pb2 import PermissionRequest, PermissionResponse
from protos.permission_pb2_grpc import PermissionServicer


class CheckPermission(PermissionServicer):
    async def CheckPermission(
        self,
        request: PermissionRequest,
        context: grpc.aio.ServicerContext,
    ) -> PermissionResponse:
        print(request.token)
        return PermissionResponse(role=f"{request.token}")
