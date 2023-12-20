import grpc

from protos.user_pb2_grpc import add_UserServicer_to_server
from src.config import logger, settings
from src.grpc_services.user import User


async def grpc_server() -> None:
    server = grpc.aio.server()
    add_UserServicer_to_server(User(), server)
    listen_addr = f"[::]:{settings.GRPC_PORT}"
    server.add_insecure_port(listen_addr)
    logger.info(f"Starting server on {listen_addr}")
    await server.start()
    await server.wait_for_termination()
