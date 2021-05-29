"""
https://www.geeksforgeeks.org/sudoku-backtracking-7/

Input:
grid = { {3, 0, 6, 5, 0, 8, 4, 0, 0},
         {5, 2, 0, 0, 0, 0, 0, 0, 0},
         {0, 8, 7, 0, 0, 0, 0, 3, 1},
         {0, 0, 3, 0, 1, 0, 0, 8, 0},
         {9, 0, 0, 8, 6, 3, 0, 0, 5},
         {0, 5, 0, 0, 9, 0, 6, 0, 0},
         {1, 3, 0, 0, 0, 0, 2, 5, 0},
         {0, 0, 0, 0, 0, 0, 0, 7, 4},
         {0, 0, 5, 2, 0, 6, 3, 0, 0} }
Output:
          3 1 6 5 7 8 4 9 2
          5 2 9 1 3 4 7 6 8
          4 8 7 6 2 9 5 3 1
          2 6 3 4 1 5 9 8 7
          9 7 4 8 6 3 1 2 5
          8 5 1 7 9 2 6 4 3
          1 3 8 9 4 7 2 5 6
          6 9 2 3 5 1 8 7 4
          7 4 5 2 8 6 3 1 9
"""


class Solution:
    n = 9

    def is_valid(self, grid, num, row, col):

        # Check if we find the same num
        # in the similar row , we
        # return false
        for x in range(self.n):
            if grid[row][x] == num:
                return False

        # Check if we find the same num in
        # the similar column , we
        # return false
        for x in range(self.n):
            if grid[x][col] == num:
                return False

        # Check if we find the same num in
        # the particular 3*3 matrix,
        # we return false
        start_row = row - row % 3
        start_col = col - col % 3
        for i in range(3):
            for j in range(3):
                if grid[i + start_row][j + start_col] == num:
                    return False
        return True

    def sudoku(self, matrix, i, j):

        if i == (self.n - 1) and j == self.n:
            # print(matrix)
            return True

        if j == self.n:
            i = i + 1
            j = 0

        p, q = i, j
        # print(p, q)
        if matrix[p][q] == 0:
            for num in range(1, 10):

                if self.is_valid(matrix, num, p, q):
                    # print(p, q)
                    matrix[p][q] = num

                    if self.sudoku(matrix, p, q + 1):
                        return True

                    matrix[p][q] = 0
        else:
            return self.sudoku(matrix, p, q + 1)
        return False


def print_grid(matrix):
    for i in range(9):
        for j in range(9):
            print(matrix[i][j], end=' ')
        print()


grid = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0]]

Solution().sudoku(grid, 0, 0)
print_grid(grid)
