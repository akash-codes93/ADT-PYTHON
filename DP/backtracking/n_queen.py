from typing import List, Tuple


class Solution:

    def __init__(self, n):

        self.n = n
        self.board = [[0 for __ in range(n)] for _ in range(n)]

    def blocked_positions(self, _positions: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
        """
        Given position of a queen this function returns list of all the blocked position
        :param _positions:
        :return:
        """
        positions = []
        for position in _positions:
            i, j = position

            positions.append((i, j))

            def append(pos: Tuple[int, int]):

                if pos not in positions:
                    positions.append(pos)

            for k in range(0, 4):
                append((i, k))
                append((k, j))
                if (i + k < 4) and (j + k < 4):
                    append((i + k, j + k))
                if (i - k >= 0) and (j - k >= 0):
                    append((i - k, j - k))
                if (i - k >= 0) and (j + k < 4):
                    append((i - k, j + k))
                if (i + k < 4) and (j - k >= 0):
                    append((i + k, j - k))

        return positions

    def n_queen_naive(self):
        """
        naive approach
        checking each configuration is possible or not
        :return:
        """

        for i in range(0, 4):
            q1 = (0, i)

            blocked_positions_1 = self.blocked_positions([q1])

            for j in range(0, 4):
                q2 = (1, j)
                if q2 not in blocked_positions_1:
                    blocked_positions_2 = self.blocked_positions([q1, q2])

                    for k in range(0, 4):
                        q3 = (2, k)

                        if q3 not in blocked_positions_2:
                            blocked_positions_3 = self.blocked_positions([q1, q2, q3])

                            for l in range(0, 4):
                                q4 = (3, l)

                                if q4 not in blocked_positions_3:
                                    print([q1, q2, q3, q4])

    def is_position_safe(self, position: Tuple[int, int]) -> bool:
        """
        Checks that the given position in the board is safe or not
        :param position:
        :return:
        """
        row, col = position

        # Check this row on left side
        for i in range(col):
            if self.board[row][i] == 1:
                return False

        # Check upper diagonal on left side
        for i, j in zip(range(row, -1, -1),
                        range(col, -1, -1)):
            if self.board[i][j] == 1:
                return False

        # Check lower diagonal on left side
        for i, j in zip(range(row, self.n, 1),
                        range(col, -1, -1)):
            if self.board[i][j] == 1:
                return False

        return True

    def find_n_queen(self, col=0):
        """
        Check all rows of this column
        for each position in a row,col check if the position is valid
        :return:
        """
        if col >= self.n:
            return True

        for i in range(0, self.n):

            if self.is_position_safe((i, col)):

                self.board[i][col] = 1  # creating a partial solution

                if self.find_n_queen(col + 1) is True:
                    return True

                self.board[i][col] = 0  # remove the solution  as it is not valid

        return False


# print(Solution().blocked_positions([(0, 1)]))
# Solution().n_queen_naive()

# backtracking
solution = Solution(4)
print(solution.find_n_queen())
print(solution.board)
