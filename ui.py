from time import sleep


def ui_print(map_):
    for row in map_:
        for symbol in row:
            print(symbol, end='')
        print('')


def ui_print_title():
    print("__Pacman__")


def ui_key():
    return input()


def ui_msg_lost():
    print("You died!")
    sleep(3)


def ui_msg_win():
    print("You won the game!")
    sleep(3)
