"""
incomplete
"""


class Solution:
    n = 10

    def is_pos_valid(self, board, position, covered_positions):

        i, j = position

        if i >= self.n or j >= self.n or i < 0 or j < 0:
            return False

        if not board[i][j]:
            return False

        if position in covered_positions:
            return False

        return True

    def find_shortest_path(self, board, position, covered_positions, end_position):

        i, j = position

        if position == end_position:
            return 0

        value = board[i][j]

        position_left = (i, j - value)
        position_right = (i, j + value)
        position_down = (i + value, j)
        position_up = (i - value, j)

        # if self.is_valid(board, position_left, covered_positions):
        #     pass

        covered_positions.append(position)

        # return min(self.find_shortest_path(board, position_up, covered_positions, end_position),
        #            self.find_shortest_path(board, position_down, covered_positions, end_position),
        #            self.find_shortest_path(board, position_left, covered_positions, end_position),
        #            self.find_shortest_path(board, position_right, covered_positions, end_position),
        #            ) + 1

        d1, d2, d3, d4 = 9999, 9999, 9999, 9999

        if self.is_pos_valid(board, position_down, covered_positions):
            d2 = self.find_shortest_path(board, position_down, covered_positions, end_position)
        if self.is_pos_valid(board, position_right, covered_positions):
            d4 = self.find_shortest_path(board, position_right, covered_positions, end_position)
        if self.is_pos_valid(board, position_left, covered_positions):
            d3 = self.find_shortest_path(board, position_left, covered_positions, end_position)
        if self.is_pos_valid(board, position_up, covered_positions):
            d1 = self.find_shortest_path(board, position_up, covered_positions, end_position)

        min_dist = min(d1, d2, d3, d4) + 1

        covered_positions.remove(position)

        return min_dist


_board = [
    [1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
    [0, 1, 1, 1, 1, 1, 0, 1, 0, 1],
    [0, 0, 1, 0, 1, 1, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
    [0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 0, 0, 1, 1, 0],
    [0, 0, 0, 0, 1, 0, 0, 1, 0, 1],
    [0, 1, 1, 1, 1, 1, 1, 1, 0, 0],
    [1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
    [0, 0, 1, 0, 0, 1, 1, 0, 0, 1]
]

# _board = [
#     [1, 1, 1],
#     [0, 1, 1],
#     [0, 1, 0]
# ]

shortest_path_length = Solution().find_shortest_path(_board, (0, 0), [], (7, 5))
print(shortest_path_length)
