class Board:
    def __init__(self, size):
        self.size = size
        self.board = [['-'] * size for _ in range(size)]
        self.vacant_pos = size  * size

    def print(self):
        for i in range(self.size):
            print(" ".join(self.board[i]))

    def set_place(self, row, col, val):
        if row >= self.size or row < 0 or col >= self.size or col < 0:
            raise Exception("Invalid move")

        if self.board[row][col] != '-':
            raise Exception("Invalid move")

        self.board[row][col] = val.value
        self.vacant_pos -= 1

    def is_pos_left(self):
        if self.vacant_pos == 0:
            return False
        return True

    def check_winner(self, x, y, piecetype):
        row_match = True
        col_match = True
        diagonal_match_left = True
        diagonal_match_right = True

        # row match
        for i in range(self.size):
            if self.board[x][i] == '-' or self.board[x][i] != piecetype.value:
                row_match = False

        # column match
        for i in range(self.size):
            if self.board[i][y] == '-' or self.board[i][y] != piecetype.value:
                col_match = False

        # 00, 11, 22
        for i in range(self.size):
            if self.board[i][i] == '-' or self.board[i][i] != piecetype.value:
                diagonal_match_left = False

        # 02, 11, 20
        for i in range(self.size):
            if self.board[i][self.size-i-1] == '-' or self.board[i][self.size-i-1] != piecetype.value:
                diagonal_match_right = False

        # return row_match or col_match or diagonal_match_left or diagonal_match_right
        return any([row_match, col_match, diagonal_match_right, diagonal_match_left])
