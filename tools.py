from enum import Enum

from config import PACMAN_BASE_POSITION, RED_BASE_POSITION, BLUE_BASE_POSITION, \
    PINK_BASE_POSITION
from datastructures import Piece, Empty, Wall, Pill
from MovingPieces import Pacman, Red, Blue, Pink, Yellow


class MovingPieceType(Enum):
    PACMAN = 0,
    RED = 1,
    BLUE = 2,
    PINK = 3,
    # YELLOW = 4


class MovingPiecesCreator:
    def __init__(self):
        self._moving_pieces = {
            MovingPieceType.PACMAN: Pacman,
            MovingPieceType.RED: Red,
            MovingPieceType.BLUE: Blue,
            MovingPieceType.PINK: Pink,
            # MovingPieceType.YELLOW: Yellow
        }

        self._moving_pieces_start_coordinates = {
            MovingPieceType.PACMAN: PACMAN_BASE_POSITION,
            MovingPieceType.RED: RED_BASE_POSITION,
            MovingPieceType.BLUE: BLUE_BASE_POSITION,
            MovingPieceType.PINK: PINK_BASE_POSITION,
            # MovingPieceType.YELLOW: Yellow
        }

    def create_moving_piece(self, piece_type: MovingPieceType):
        x = self._moving_pieces_start_coordinates[piece_type].x
        y = self._moving_pieces_start_coordinates[piece_type].y
        return self._moving_pieces[piece_type](x, y)


def build_piece(piece: str, x, y) -> Piece:
    if piece == '.':
        return Empty(x, y)
    if piece == '#' or piece == '-':
        return Wall(x, y)
    if piece == '@':
        return Pacman(x, y)
    if piece == 'G':
        return Red(x, y)
    if piece == 'P':
        return Pill(x, y)