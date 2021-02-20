"""
Merge function for 2048 game.
"""


def merge(line):
    """
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


# print merge([0, 0, 2, 2])
