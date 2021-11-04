# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import user_pb2 as user__pb2


class SpellingGameStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateGame = channel.unary_unary(
                '/app.SpellingGame/CreateGame',
                request_serializer=user__pb2.GameRequest.SerializeToString,
                response_deserializer=user__pb2.GameResponse.FromString,
                )
        self.RegisterPlayer = channel.unary_unary(
                '/app.SpellingGame/RegisterPlayer',
                request_serializer=user__pb2.RegisterRequest.SerializeToString,
                response_deserializer=user__pb2.RegisterResponse.FromString,
                )
        self.FinalizeGame = channel.unary_unary(
                '/app.SpellingGame/FinalizeGame',
                request_serializer=user__pb2.FinalizeRequest.SerializeToString,
                response_deserializer=user__pb2.FinalizeResponse.FromString,
                )
        self.PlayerVisit = channel.unary_unary(
                '/app.SpellingGame/PlayerVisit',
                request_serializer=user__pb2.VisitRequest.SerializeToString,
                response_deserializer=user__pb2.VisitResponse.FromString,
                )


class SpellingGameServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CreateGame(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RegisterPlayer(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def FinalizeGame(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PlayerVisit(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SpellingGameServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateGame': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateGame,
                    request_deserializer=user__pb2.GameRequest.FromString,
                    response_serializer=user__pb2.GameResponse.SerializeToString,
            ),
            'RegisterPlayer': grpc.unary_unary_rpc_method_handler(
                    servicer.RegisterPlayer,
                    request_deserializer=user__pb2.RegisterRequest.FromString,
                    response_serializer=user__pb2.RegisterResponse.SerializeToString,
            ),
            'FinalizeGame': grpc.unary_unary_rpc_method_handler(
                    servicer.FinalizeGame,
                    request_deserializer=user__pb2.FinalizeRequest.FromString,
                    response_serializer=user__pb2.FinalizeResponse.SerializeToString,
            ),
            'PlayerVisit': grpc.unary_unary_rpc_method_handler(
                    servicer.PlayerVisit,
                    request_deserializer=user__pb2.VisitRequest.FromString,
                    response_serializer=user__pb2.VisitResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'app.SpellingGame', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class SpellingGame(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CreateGame(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/app.SpellingGame/CreateGame',
            user__pb2.GameRequest.SerializeToString,
            user__pb2.GameResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RegisterPlayer(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/app.SpellingGame/RegisterPlayer',
            user__pb2.RegisterRequest.SerializeToString,
            user__pb2.RegisterResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def FinalizeGame(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/app.SpellingGame/FinalizeGame',
            user__pb2.FinalizeRequest.SerializeToString,
            user__pb2.FinalizeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PlayerVisit(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/app.SpellingGame/PlayerVisit',
            user__pb2.VisitRequest.SerializeToString,
            user__pb2.VisitResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
