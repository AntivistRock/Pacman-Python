from src.tools.config import PILLS_AMOUNT
from src.logic.map import Map
from src.tools.tools import MovingPiecesCreator, MovingPieceType
from src.ui.ui import get_valid_key, SimpleUI


class Game:
    def __init__(self, map_: Map, ui: SimpleUI):
        self._map = map_
        self._game_finished = False
        self._win = False
        self._ui = ui

        self.pills_amount = PILLS_AMOUNT

        moving_objects_creator = MovingPiecesCreator()

        self.pacman, *self.ghosts = [
            moving_objects_creator.create_moving_piece(type_)
            for type_ in MovingPieceType
        ]
        self.ghosts = dict(
            zip(
                ['red', 'blue', 'pink', 'yellow'],
                self.ghosts
            )
        )

    def win(self):
        self._game_finished = True
        self._win = True

    def lost(self):
        self._game_finished = True
        self._win = False

    def pill_collected(self):
        self.pills_amount -= 1

    def play(self):
        while not self._game_finished:
            self._ui.print_(self._map.join_moving_objects_and_background(
                    self.pacman, list(self.ghosts.values())
                ), self.pills_amount
            )

            key = get_valid_key()
            self.move_pacman(key)

            self._move_ghosts()

        self.end_game()

    def _move_ghosts(self):
        for ghost in self.ghosts.values():
            ghost.move(self._map, self)

        self.check_is_ghost_ate_pacman()

    def move_pacman(self, key):
        self.pacman.move(self._map, self, key=key)

        self.check_is_ghost_ate_pacman()

        if self.pills_amount == 0:
            self.win()

    def check_is_ghost_ate_pacman(self):
        for ghost in self.ghosts.values():
            if self.pacman.x == ghost.x and self.pacman.y == ghost.y:
                self.lost()

    def end_game(self):
        # game is over!
        if self._win:
            self._ui.show_win_message()
        else:
            self._ui.show_lose_message()
