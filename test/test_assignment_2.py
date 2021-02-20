import unittest
from course_3.assignment_2 import TwentyFortyEight


class TestTwentyFortyEight(unittest.TestCase):

    def test_initial_params(self):
        game = TwentyFortyEight(10, 10)

        self.assertEqual(game.get_grid_height(), 10)
        self.assertEqual(game.get_grid_width(), 10)

    def test_common_board(self):
        game = TwentyFortyEight(10, 10)

        self.assertEqual(game.get_grid_height(), 10)
        self.assertEqual(game.get_grid_width(), 10)

        for i in range(game.get_grid_height()):
            for j in range(game.get_grid_width()):
                self.assertEqual(game.get_tile(i, j), 0)

    def test_empty_board(self):
        game = TwentyFortyEight(0, 0)

        self.assertEqual(game.get_grid_height(), 0)
        self.assertEqual(game.get_grid_width(), 0)
