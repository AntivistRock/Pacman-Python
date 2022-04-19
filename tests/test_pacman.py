from unittest import TestCase
from pacman import find_packman, move_pacman, play


class Test(TestCase):
    def test_find_packman(self):
        map_ = [
            "|--------|",
            "|G..|..G.|",
            "|...PP...|",
            "|G...@.|.|",
            "|........|",
            "|--------|"
        ]
        self.assertEqual(find_packman(map_), (3, 5))

    def test_find_pacman_when_it_not_exists(self):
        map_ = [
            "|--------|",
            "|G..|..G.|",
            "|...PP...|",
            "|G.....|.|",
            "|........|",
            "|--------|"
        ]
        self.assertEqual(find_packman(map_), (-1, -1))

    def test_move_pacman(self):
        map_ = [
            "|--------|",
            "|G..|..G.|",
            "|...PP...|",
            "|G...@.|.|",
            "|........|",
            "|--------|"
        ]
        move_pacman(map_, 4, 3)

        self.assertEqual(find_packman(map_), (4, 3))

    def test_play_movements(self):
        map_ = [
            "|--------|",
            "|G..|..G.|",
            "|...PP...|",
            "|G...@.|.|",
            "|........|",
            "|--------|"
        ]

        self.assertEqual(play(map_, 'w'), (True, True, False))
        play(map_, 's')

        play(map_, 'd')
        self.assertEqual(find_packman(map_), (3, 6))
        play(map_, 's')
        self.assertEqual(find_packman(map_), (4, 6))
        play(map_, 'a')
        self.assertEqual(find_packman(map_), (4, 5))
        play(map_, 'w')
        self.assertEqual(find_packman(map_), (3, 5))

        self.assertEqual(play(map_, 'c'), (False, True, False))

    def test_play_do_not_cross_bounders(self):
        map_ = [
            "|--------|",
            "|G..|..G.|",
            "|...PP...|",
            "|G.....|.|",
            "|........@",
            "|--------|"
        ]
        self.assertEqual(play(map_, 'd'), (False, True, False))

    def test_play_do_not_cross_walls(self):
        map_ = [
            "|--------|",
            "|G..|..G.|",
            "|...PP...|",
            "|G.....|.|",
            "|.......@|",
            "|--------|"
        ]
        self.assertEqual(play(map_, 'd'), (False, True, False))

    def test_play_player_dies_when_meet_ghost(self):
        map_ = [
            "|--------|",
            "|G..|..G.|",
            "|...PP...|",
            "|G@....|.|",
            "|........|",
            "|--------|"
        ]
        self.assertEqual(play(map_, 'a'), (False, False, False))

    def test_are_you_won(self):
        map_ = [
            "|--------|",
            "|G..|..G.|",
            "|....P@..|",
            "|G.....|.|",
            "|........|",
            "|--------|"
        ]
        self.assertEqual(play(map_, 'a'), (True, True, True))
