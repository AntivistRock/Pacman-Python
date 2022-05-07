from dataclasses import dataclass


@dataclass
class Piece:
    x: int
    y: int

    @staticmethod
    def is_ghost():
        return False

    @staticmethod
    def is_wall():
        return False

    @staticmethod
    def is_pill():
        return False

    @staticmethod
    def is_pacman():
        return False

    @staticmethod
    def is_empty():
        return False


class Pill(Piece):
    def is_pill(self):
        return True


class Wall(Piece):
    def is_wall(self):
        return True


class Empty(Piece):
    def is_empty(self):
        return True


@dataclass
class Coordinates:
    x: int
    y: int
