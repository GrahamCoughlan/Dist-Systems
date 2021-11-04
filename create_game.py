import threading
import uuid

class CreateGame:

    __instance = None

    def __init__(self):
        if CreateGame .__instance is not None:
            raise Exception("")
        else:
            CreateGame . __instance = self
        self.lock = threading.Lock()
        self.matches = {}
        self.instance = None



    def get_instance(self):
        if CreateGame .__instance is None:
            with threading.Lock():
                if CreateGame .__instance is None:
                    CreateGame()
                return CreateGame .__instance


    def add_game(self, game):
        self.lock.acquire()
        game_id = uuid.uuid4()
        self.games[game_id] = game
        self.lock.release()
        return game_id

    def get_game(self, game_id):
        return self.games[uuid.UUID(bytes=game_id)]

