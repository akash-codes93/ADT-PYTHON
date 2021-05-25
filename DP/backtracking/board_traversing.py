"""
 You are given a grid of non-negative integers. You begin in the upper -left corner, and your
goal is to get to the lower -right corner. However, at each point in time, you can only move
up, down, left, or right exactly the number of squares given by the number you're standing
on. For example, if you were standing on a 3, you could move exactly three spots left, exactly three spots right,
exactly three spots up, or exactly three spots down. You can't walk
off the board. Determine if there's a path that gets you from the upper -left corner of the
grid to the lower -right corner.
"""


class Solution:
    n = 4

    def find_path(self, board, position, path, covered_positions):
        if position in covered_positions:
            return False

        covered_positions.append(position)
        i, j = position

        if i >= self.n or j >= self.n or i < 0 or j < 0:
            return False

        if position == (self.n - 1, self.n - 1):
            return True

        value = board[i][j]

        if not value:
            return False

        position_left = (i, j - value)
        position_right = (i, j + value)
        position_down = (i + value, j)
        position_up = (i - value, j)

        if self.find_path(board, position_up, path, covered_positions) or self.find_path(board, position_down, path, covered_positions) or \
                self.find_path(board, position_left, path, covered_positions) or \
                self.find_path(board, position_right, path, covered_positions):
            path.append(position)
            return True

        return False

    def check_if_path_is_possible(self, board):
        path = []
        starting_pos = (0, 0)

        status = self.find_path(board, starting_pos, path, covered_positions=[])

        if status:
            return path
        else:
            return None

_board = [
    [1, 1, 1, 1],
    [3, 2, 1, 1],
    [2, 1, 3, 1],
    [1, 2, 1, 1]
]

# _board = [
#     [1, 0, 0, 0],
#     [3, 0, 0, 2],
#     [0, 0, 0, 0],
#     [0, 0, 0, 1]
# ]

_path = Solution().check_if_path_is_possible(_board)
print(_path)
