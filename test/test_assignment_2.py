import unittest
from assignment_2 import TwentyFortyEight


class TestTwentyFortyEight(unittest.TestCase):

    def test_initial_board(self):
        twentyFortyEight = TwentyFortyEight(10, 10)
        board_height = twentyFortyEight.get_grid_height()
        board_width = twentyFortyEight.get_grid_width()

        self.assertEqual(board_height, 10)
        self.assertEqual(board_width, 10)

        twentyFortyEight = TwentyFortyEight()

    @unittest.skip('Not yet tested')
    def test_reset(self):
        self.fail()

    @unittest.skip('Not yet tested')
    def test_get_grid_height(self):
        self.fail()

    @unittest.skip('Not yet tested')
    def test_get_grid_width(self):
        self.fail()

    @unittest.skip('Not yet tested')
    def test_move(self):
        self.fail()

    @unittest.skip('Not yet tested')
    def test_new_tile(self):
        self.fail()

    @unittest.skip('Not yet tested')
    def test_set_tile(self):
        self.fail()

    @unittest.skip('Not yet tested')
    def test_get_tile(self):
        self.fail()
