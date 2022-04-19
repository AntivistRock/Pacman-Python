from datastructures import Piece, Empty
from tools import build_piece


class Map:
    def __init__(self, map_):
        self._map = map_
        self._rows = len(map_)
        self._columns = len(map_[0])

    def is_valid_coordinates(self, x: int, y: int):
        return 0 <= x < self._rows and 0 <= y < self._columns

    @property
    def rows(self):
        return self._rows

    @property
    def columns(self):
        return self._columns

    @property
    def map(self):
        return self._map

    def get(self, x, y) -> Piece:
        return self._map[x][y]

    def move(self, piece: Piece, target: Piece):

        self._map[piece.x][piece.y] = Empty(piece.x, piece.y)
        self._map[target.x][target.y] = piece
        piece.x = target.x
        piece.y = target.y

        return True


def create_map(map_array) -> Map:
    new_map = []

    for x in range(len(map_array)):
        row = []
        for y in range(len(map_array[x])):
            row.append(build_piece(map_array[x][y], x, y))
        new_map.append(row)

    return Map(new_map)
