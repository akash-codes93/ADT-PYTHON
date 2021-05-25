class Solution:
    n = 3
    unique_paths = []

    def is_pos_valid(self, board, position, covered_positions):

        i, j = position

        if i >= self.n or j >= self.n or i < 0 or j < 0:
            return False

        if not board[i][j]:
            return False

        if position in covered_positions:
            return False

        return True

    def get_all_unique_path(self, board, position, paths, end_position):

        total_path = 0

        i, j = position

        if position == end_position:
            # print(paths)
            paths.append(position)
            self.unique_paths.append(paths.copy())
            paths.remove(position)
            return 1

        value = board[i][j]

        position_left = (i, j - value)
        position_right = (i, j + value)
        position_down = (i + value, j)
        position_up = (i - value, j)

        paths.append(position)

        if self.is_pos_valid(board, position_down, paths):
            total_path += self.get_all_unique_path(board, position_down, paths, end_position)
        if self.is_pos_valid(board, position_right, paths):
            total_path += self.get_all_unique_path(board, position_right, paths, end_position)
        if self.is_pos_valid(board, position_left, paths):
            total_path += self.get_all_unique_path(board, position_left, paths, end_position)
        if self.is_pos_valid(board, position_up, paths):
            total_path += self.get_all_unique_path(board, position_up, paths, end_position)

        paths.remove(position)

        return total_path


_board = [
    [1, 1, 1],
    [0, 1, 1],
    [0, 1, 1],
]

sol = Solution()
total_paths = sol.get_all_unique_path(_board, (0, 0), end_position=(2, 1), paths=[])
print("Total paths: ", total_paths)
print("All unique paths", sol.unique_paths)
