from copy import deepcopy

from src.logic.datastructures import Piece, Empty
from src.tools.tools import build_piece


def join_map_and_moving_object(map_, moving_object):
    x = moving_object.x
    y = moving_object.y
    map_[x][y] = moving_object


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

    def pill_collected(self, pill_piece):
        self._map[pill_piece.x][pill_piece.y] = Empty(
            pill_piece.x, pill_piece.y
        )

    def join_moving_objects_and_background(self, pacman, ghosts):
        joined_map = deepcopy(self)
        for object_ in [pacman] + ghosts:
            # print(object_)
            join_map_and_moving_object(joined_map._map, object_)
        return joined_map


def create_map(map_array) -> Map:
    new_map = []

    for x in range(len(map_array)):
        row = []
        for y in range(len(map_array[x])):
            row.append(build_piece(map_array[x][y], x, y))
        new_map.append(row)

    return Map(new_map)
