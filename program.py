from src.logic.game import Game
from src.logic.map import create_map
from src.ui.ui import SimpleUI
from src.tools.config import map_as_strings

map_as_array_of_game_objects = create_map(map_as_strings)
ui = SimpleUI()
game = Game(map_as_array_of_game_objects, ui)
game.play()
