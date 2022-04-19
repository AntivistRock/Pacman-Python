# @ -> our hero
# G -> ghosts
# P -> pills
# . -> empty spaces
# | and - -> walls
import random


def find_packman(map_):
    pacman_x = -1
    pacman_y = -1
    for x, row in enumerate(map_):
        for y, _ in enumerate(row):
            if map_[x][y] == '@':
                pacman_x = x
                pacman_y = y
    return pacman_x, pacman_y


def move_pacman(map_, new_pacman_x, new_pacman_y):
    pacman_x, pacman_y = find_packman(map_)

    move_object(map_, new_pacman_x, new_pacman_y, pacman_x, pacman_y, '@')


def move_object(map_, new_x, new_y, x, y, symbol):
    row_left_to_pacman = map_[x][:y]
    row_right_to_pacman = map_[x][y + 1:]
    map_[x] = row_left_to_pacman + '.' + row_right_to_pacman

    row_left_to_pacman = map_[new_x][:new_y]
    row_right_to_pacman = map_[new_x][new_y + 1:]
    map_[new_x] = row_left_to_pacman + symbol + row_right_to_pacman


# this function returns three values:
# is valid movement, is pacman still alive, are you won
def play(map_, key):
    next_x, next_y = next_position(key, map_)

    if is_an_invalid_key(next_x, next_y):
        return False, True, False

    if not within_borders(map_, next_x, next_y):
        return False, True, False

    if is_wall(map_, next_x, next_y):
        return False, True, False

    if is_a_ghost(map_, next_x, next_y):
        return False, False, False

    move_pacman(map_, next_x, next_y)

    remaining_pills = total_pills(map_)
    if remaining_pills == 0:
        return True, True, True
    return True, True, False


def is_a_ghost(map_, next_x, next_y):
    return map_[next_x][next_y] == 'G'


def is_a_pill(map_, next_x, next_y):
    return map_[next_x][next_y] == 'P'


def is_pacman(map_, next_x, next_y):
    return map_[next_x][next_y] == '@'


def is_an_invalid_key(next_x, next_y):
    return next_x == -1 == next_y


def is_wall(map_, next_x, next_y):
    return map_[next_x][next_y] == '|' or map_[next_x][next_y] == '-'


def within_borders(map_, next_x, next_y):
    number_of_rows = len(map_)
    x_is_valid = 0 <= next_x < number_of_rows

    number_of_columns = len(map_[0])
    y_is_valid = 0 <= next_y < number_of_columns

    is_within_borders = x_is_valid and y_is_valid
    return is_within_borders


def total_pills(map_):
    total = 0
    for row in map_:
        for symbol in row:
            if symbol == 'P':
                total += 1
    return total


def next_position(key, map_):
    x, y = find_packman(map_)
    next_x = -1
    next_y = -1
    if key == 'a':
        next_x = x
        next_y = y - 1
    elif key == 'd':
        next_x = x
        next_y = y + 1
    elif key == 's':
        next_x = x + 1
        next_y = y
    elif key == 'w':
        next_x = x - 1
        next_y = y
    return next_x, next_y


def find_ghosts(map_):
    all_ghosts = []
    for x, row in enumerate(map_):
        for y, _ in enumerate(row):
            if map_[x][y] == 'G':
                all_ghosts.append([x, y])
    return all_ghosts


def move_ghosts(map_):
    all_ghosts = find_ghosts(map_)
    for ghost in all_ghosts:
        ghost_x = ghost[0]
        ghost_y = ghost[1]

        possible_directions = [
            [ghost_x, ghost_y + 1],
            [ghost_x, ghost_y - 1],
            [ghost_x + 1, ghost_y],
            [ghost_x - 1, ghost_y],
        ]

        random_number = random.randint(0, 3)
        next_ghost_x = possible_directions[random_number][0]
        next_ghost_y = possible_directions[random_number][1]

        if not within_borders(map_, next_ghost_x, next_ghost_y):
            continue

        if is_wall(map_, next_ghost_x, next_ghost_y):
            continue

        if is_a_ghost(map_, next_ghost_x, next_ghost_y):
            continue

        if is_a_pill(map_, next_ghost_x, next_ghost_y):
            continue

        if is_pacman(map_, next_ghost_x, next_ghost_y):
            return True

        move_object(map_, next_ghost_x, next_ghost_y, ghost_x, ghost_y, 'G')

        return False
