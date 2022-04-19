from map import Map
from tools import MovingPiecesCreator, MovingPieceType
from ui import get_valid_key, SimpleUI


class Game:
    def __init__(self, map_: Map, ui: SimpleUI):
        self._map = map_
        self._game_finished = False
        self._win = False
        self._ui = ui

        self.pills_amount = 3

        moving_objects_creator = MovingPiecesCreator()

        self.pacman, *self.ghosts = [
            moving_objects_creator.create_moving_piece(type_)
            for type_ in MovingPieceType
        ]

    def win(self):
        self._game_finished = True
        self._win = True

    def lost(self):
        self._game_finished = True
        self._win = False

    def play(self):
        while not self._game_finished:
            self._ui.print_(self._map)

            key = get_valid_key()
            self.move_pacman(key)

            self._move_ghosts()

        self.end_game()

    def _move_ghosts(self):
        for ghost in self.ghosts:
            ghost.move(self._map, self)

    def move_pacman(self, key):
        self.pacman.move(self._map, self, key=key)

    def end_game(self):
        # game is over!
        if self._win:
            self._ui.show_win_message()
        else:
            self._ui.show_lose_message()
