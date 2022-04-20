import os


def get_valid_key():
    valid_keys = ['a', 's', 'w', 'd']
    while True:
        key = input()
        if key in valid_keys:
            return key


def clean_screen():
    os.system('clear')


class SimpleUI:

    @staticmethod
    def print_(map_):

        clean_screen()
        for row in map_.map:
            for point in row:

                # if it's a ghost
                if point.is_ghost():
                    print(point.get_symbol(), end='')
                # if it's a wall
                elif point.is_wall():
                    print('#', end='')
                # if it's a pacman
                elif point.is_pacman():
                    print('@', end='')
                # if it's empty
                elif point.is_empty():
                    print('.', end='')
                # if it's a pill
                elif point.is_pill():
                    print('*', end='')
            print("", end='\n')

    @staticmethod
    def show_win_message():
        clean_screen()
        print("You win!")

    @staticmethod
    def show_lose_message():
        clean_screen()
        print("You died.")
