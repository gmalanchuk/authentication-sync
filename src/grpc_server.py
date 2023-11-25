import grpc

from protos.helloworld_pb2_grpc import add_GreeterServicer_to_server
from protos.permission_pb2_grpc import add_PermissionServicer_to_server
from src.config import logger
from src.grpc_services.greeter import Greeter
from src.grpc_services.permission import CheckPermission


async def grpc_server() -> None:
    server = grpc.aio.server()
    add_GreeterServicer_to_server(Greeter(), server)
    add_PermissionServicer_to_server(CheckPermission(), server)
    listen_addr = "[::]:50051"
    server.add_insecure_port(listen_addr)
    logger.info(f"Starting server on {listen_addr}")
    await server.start()
    await server.wait_for_termination()
