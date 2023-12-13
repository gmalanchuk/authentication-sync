# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from protos import permission_pb2 as protos_dot_permission__pb2


class PermissionStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CheckRoleUserID = channel.unary_unary(
                '/permission.Permission/CheckRoleUserID',
                request_serializer=protos_dot_permission__pb2.RoleUserIDRequest.SerializeToString,
                response_deserializer=protos_dot_permission__pb2.RoleUserIDResponse.FromString,
                )


class PermissionServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CheckRoleUserID(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_PermissionServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CheckRoleUserID': grpc.unary_unary_rpc_method_handler(
                    servicer.CheckRoleUserID,
                    request_deserializer=protos_dot_permission__pb2.RoleUserIDRequest.FromString,
                    response_serializer=protos_dot_permission__pb2.RoleUserIDResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'permission.Permission', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Permission(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CheckRoleUserID(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/permission.Permission/CheckRoleUserID',
            protos_dot_permission__pb2.RoleUserIDRequest.SerializeToString,
            protos_dot_permission__pb2.RoleUserIDResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
