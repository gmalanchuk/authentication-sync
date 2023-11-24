import grpc

from protos.helloworld_pb2 import HelloReply, HelloRequest
from protos.helloworld_pb2_grpc import GreeterServicer


class Greeter(GreeterServicer):
    async def SayHello(
        self,
        request: HelloRequest,
        context: grpc.aio.ServicerContext,
    ) -> HelloReply:
        return HelloReply(message="HELLA, %s!" % request.name)
