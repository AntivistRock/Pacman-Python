import random

from datastructures import Piece


class MovingPiece(Piece):
    def __init__(self, *args):
        super().__init__(*args)

    # the base moving object moves randomly every step
    def move(self, map_, game, **kwargs):
        possible_directions = [
            [self.x, self.y + 1],  # x,   y+1
            [self.x + 1, self.y],  # x+1, y
            [self.x, self.y - 1],  # x,   y-1
            [self.x - 1, self.y]   # x-1, y
        ]

        random_movement = random.randint(0, 3)
        target_x = possible_directions[random_movement][0]
        target_y = possible_directions[random_movement][1]

        if not map_.is_valid_coordinates(target_x, target_y):
            return

        target_piece = map_.get(target_x, target_y)

        if not target_piece.is_wall() and \
                not target_piece.is_ghost() and \
                not target_piece.is_pill():

            if target_piece.is_pacman():
                game.lost()
            else:
                map_.move(self, target_piece)


class Pacman(MovingPiece):
    def __init__(self, *args):
        super().__init__(*args)

    def move(self, map_, game, **kwargs):

        target_piece = self.get_new_position(kwargs['key'], self, map_)

        if target_piece.is_wall():
            return

        if target_piece.is_pill():
            game.pills_amount -= 1

        map_.move(self, target_piece)

        if target_piece.is_ghost():
            game.lost()

        if game.pills_amount == 0:
            game.win()

    @staticmethod
    def is_pacman():
        return True

    @staticmethod
    def get_new_position(key, piece: Piece, map_):
        target_x = piece.x
        target_y = piece.y
        if key == 'a':  # left
            target_y -= 1
        elif key == 's':  # down
            target_x += 1
        elif key == 'w':  # up
            target_x -= 1
        elif key == 'd':  # right
            target_y += 1

        if not map_.is_valid_coordinates(target_x, target_y):
            raise IndexError("Pacman movement is out of range.")

        return map_.get(target_x, target_y)


class Red(MovingPiece):
    def __init__(self, *args):
        super().__init__(*args)

    @staticmethod
    def is_ghost():
        return True


class Blue(MovingPiece):
    def __init__(self, *args):
        super().__init__(*args)

    @staticmethod
    def is_ghost():
        return True


class Pink(MovingPiece):
    def __init__(self, *args):
        super().__init__(*args)

    @staticmethod
    def is_ghost():
        return True


class Yellow(MovingPiece):
    def __init__(self, *args):
        super().__init__(*args)

    @staticmethod
    def is_ghost():
        return True
