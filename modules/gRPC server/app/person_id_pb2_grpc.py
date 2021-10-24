# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import person_id_pb2 as person__id__pb2


class PesronIDServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetID = channel.unary_unary(
                '/PesronIDService/GetID',
                request_serializer=person__id__pb2.PersonIDMessage.SerializeToString,
                response_deserializer=person__id__pb2.PersonIDMessage.FromString,
                )


class PesronIDServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetID(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_PesronIDServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetID': grpc.unary_unary_rpc_method_handler(
                    servicer.GetID,
                    request_deserializer=person__id__pb2.PersonIDMessage.FromString,
                    response_serializer=person__id__pb2.PersonIDMessage.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'PesronIDService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class PesronIDService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetID(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/PesronIDService/GetID',
            person__id__pb2.PersonIDMessage.SerializeToString,
            person__id__pb2.PersonIDMessage.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
