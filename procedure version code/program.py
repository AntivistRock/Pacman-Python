import os
from pacman import play, move_ghosts
from ui import ui_print, ui_key, ui_msg_lost, ui_msg_win, ui_print_title

game_finished = False

map_ = [
    "|--------|",
    "|G..|..G.|",
    "|...PP...|",
    "|G...@.|.|",
    "|........|",
    "|--------|"
]

os.system('clear')

while not game_finished:
    ui_print_title()
    ui_print(map_)

    key = ui_key()
    valid_key, pacman_alive, won = play(map_, key)

    pacman_was_hit = move_ghosts(map_)

    os.system('clear')

    if (not pacman_alive) or pacman_was_hit:
        ui_msg_lost()
        game_finished = True
    if won:
        ui_msg_win()
        game_finished = True

    os.system('clear')
