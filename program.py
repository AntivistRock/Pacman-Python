from game import Game
from map import create_map
from ui import SimpleUI

map_as_strings = [
    "##########",
    "#..*#....#",
    "#*****...#",
    "#......#.#",
    "#......#.#",
    "##########"
]

map_as_array_of_game_objects = create_map(map_as_strings)
ui = SimpleUI()
game = Game(map_as_array_of_game_objects, ui)
game.play()


''' Objects joined positions
    "##########",
    "#R.*#..B.#",
    "#*****...#",
    "#P....@#.#",
    "#......#Y#",
    "##########"
'''