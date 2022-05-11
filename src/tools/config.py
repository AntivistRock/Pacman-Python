from src.logic.datastructures import Coordinates


PACMAN_BASE_POSITION = Coordinates(3, 6)

RED_BASE_POSITION = Coordinates(1, 1)
BLUE_BASE_POSITION = Coordinates(1, 8)
PINK_BASE_POSITION = Coordinates(4, 3)
YELLOW_BASE_POSITION = Coordinates(4, 8)

PILLS_AMOUNT = 0

map_as_strings = [
    "##########",
    "#...#..*.#",
    "#...*....#",
    "#......#.#",
    "#...*..#.#",
    "##########"
]

for row in map_as_strings:
    for symbol in row:
        if symbol == "*":
            PILLS_AMOUNT += 1
