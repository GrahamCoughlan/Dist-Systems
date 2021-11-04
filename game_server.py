
import grpc
import time
from concurrent import futures
import logging

from app . gameimpl import x01_match

from user_pb2 import VisitResponse, RegisterResponse,  GameResponse, FinalizeResponse, Player,Game

from user_pb2_grpc import SpellingGameServicer,  add_SpellingGameServicer_to_server

from app.game_server.create_game import CreateGame

from domain import user, visit

from pattern import object_factory

class GameServer(SpellingGameServicer):
    def __init__(self):
        self.game_type = "X01"
        self.factory = object_factory.ObjectFactory()



