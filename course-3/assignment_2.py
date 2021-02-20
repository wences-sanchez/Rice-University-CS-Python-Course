"""
Clone of 2048 game.
"""

# import poc_2048_gui

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}


def merge(line):
    """
    Helper function that merges a single row or column in 2048
    Function that merges a single row or column in 2048.
    """

    # We initialize the output with the length
    output = [0] * len(line)

    # We fill the output with all the contents
    # of the entry list together at the leftmost.
    # The rest are trailing zeros at the end of
    # the output list
    output = move_to_left(line)

    ind = 1
    while ind < len(output):
        if output[ind - 1] == output[ind]:
            output[ind - 1] += output[ind]
            output[ind] = 0
        ind += 1

    return move_to_left(output)


def move_to_left(line):
    """
    Shifts to the left all the numbers of the
    given list which are not zeros.
    And returns a list whith those trailing zeroes at
    the last indexes.
    """
    # We initialize the output
    output = [0] * len(line)

    index_output = 0
    for ind in range(len(line)):
        if line[ind] != 0:
            output[index_output] = line[ind]
            index_output += 1
    return output

class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        self.grid_height = grid_height
        self.grid_width = grid_width

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        # replace with your code
        pass

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        # replace with your code
        return ""

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self.grid_height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self.grid_width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        # replace with your code
        pass

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        # replace with your code
        pass

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        # replace with your code
        pass

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        # replace with your code
        return 0


# poc_2048_gui.run_gui(TwentyFortyEight(4, 4))
