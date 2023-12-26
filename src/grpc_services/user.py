import grpc

from protos.user_pb2 import UserRequestID, UserRequestToken, UserResponse
from protos.user_pb2_grpc import UserServicer
from src.enums.tag import TagEnum
from src.services.permission import PermissionService


class User(UserServicer):
    def __init__(self) -> None:
        self.permission_service = PermissionService(tag=TagEnum.GRPC)

    async def CheckUserToken(self, request: UserRequestToken, context: grpc.aio.ServicerContext) -> UserResponse:
        user_id, username, email, name, role = await self.permission_service.get_user_info_by_token(
            token_dict={"token": request.token}
        )
        return UserResponse(user_id=user_id, username=username, email=email, name=name, role=role)

    async def CheckUserID(self, request: UserRequestID, context: grpc.aio.ServicerContext) -> UserResponse:
        user_id, username, email, name, role = await self.permission_service.get_user_info_by_id(
            user_dict={"user_id": request.user_id}
        )
        return UserResponse(user_id=user_id, username=username, email=email, name=name, role=role)
