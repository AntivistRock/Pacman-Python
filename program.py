from game import Game
from map import create_map
from ui import SimpleUI

map_as_strings = [
    "##########",
    "#G..#..G.#",
    "#...PP...#",
    "#G....@#.#",
    "#...P..#.#",
    "##########"
]

map_as_array_of_game_objects = create_map(map_as_strings)
ui = SimpleUI()
game = Game(map_as_array_of_game_objects, ui)
game.play()
