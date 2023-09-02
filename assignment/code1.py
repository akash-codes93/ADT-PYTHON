# -*- coding: utf-8 -*-
"""
Created on Fri July 21 5:23PM 2023
@author: Akash Gupta
@question: Find My Number
"""
from collections import defaultdict
from typing import Tuple, List
import enum

VOWELS = {"A", "E", "I", "O", "U"}

INVALID_CHAR = "X"

KEYPAD = [
    ["A", "B", "C", "D", "E"],
    ["F", "G", "H", "I", "J"],
    ["K", "L", "M", "N", "O"],
    [INVALID_CHAR, "1", "2", "3", INVALID_CHAR]
]

# dict of list of valid next positions for a position
# NEXT_POS = {
#     (0, 0): [(1, 2), (2, 1)],
#     (0, 1): [(2, 0), (2, 2), (1, 3)],
#     (0, 2): [(2, 1), (2, 3), (1, 4), (1, 0)],
#     (0, 3): [(2, 2), (2, 4), (1, 1)],
#     (0, 4): [(1, 2), (2, 3)],
#     (1, 0): [(0, 2), (2, 2), (3, 1)],
#     (1, 1): [(3, 2), (2, 3), (0, 3)],
#     (1, 2): [(2, 4), (2, 0), (0, 0), (0, 4), (3, 1), (3, 3)],
#     (1, 3): [(0, 1), (2, 1), (3, 2)],
#     (1, 4): [(0, 2), (2, 2), (3, 3)],
#     (2, 0): [(0, 1), (3, 2), (1, 2)],
#     (2, 1): [(0, 2), (1, 3), (3, 3), (0, 0)],
#     (2, 2): [(0, 1), (0, 3), (1, 0), (1, 4)],
#     (2, 3): [(0, 2), (0, 4), (1, 1), (3, 1)],
#     (2, 4): [(1, 2), (3, 2), (0, 3)],
#     (3, 1): [(1, 0), (1, 2), (2, 3)],
#     (3, 2): [(1, 1), (1, 3), (2, 0), (2, 4)],
#     (3, 3): [(1, 2), (2, 1), (1, 4)]
# }

M = len(KEYPAD)
N = len(KEYPAD[0])


class PieceType(enum.Enum):
    knight = 'KNIGHT'
    rook = 'rook'


class Solution:
    """
    Approach: Top down + memoization
    State = (position, remaining length, remaining vowels)
    """
    mem = {}

    def __init__(self, keypad: List[List], piece: PieceType, total_len: int = 10, vowel_count: int = 2):
        self.keypad = keypad
        self.total_len = total_len
        self.vowel_count = vowel_count
        self.next_pos = {}
        self.piece = piece
        self.calculate_next_position()

    def calculate_next_position_knight(self):
        m = len(self.keypad)
        n = len(self.keypad[0])

        possible_adders = [(-2, 1), (-2, -1), (2, 1), (2, -1), (-1, 2), (-1, -2), (1, 2), (1, -2)]

        for i in range(0, m):
            for j in range(0, n):
                # i, j we need to find the next positions
                if self.keypad[i][j] == INVALID_CHAR:
                    continue

                for x, y in possible_adders:
                    next_i = i + x
                    next_j = j + y

                    if 0 <= next_i < m and 0 <= next_j < n:
                        if self.keypad[next_i][next_j] == INVALID_CHAR:
                            continue

                        if (i, j) in self.next_pos:
                            self.next_pos[(i, j)].append((next_i, next_j))
                        else:
                            self.next_pos[(i, j)] = [(next_i, next_j)]

    def calculate_next_position_rook(self):
        m = len(self.keypad)
        n = len(self.keypad[0])

        for i in range(0, m):
            for j in range(0, n):
                if self.keypad[i][j] == INVALID_CHAR:
                    continue

                self.next_pos[(i, j)] = []

                for x in range(0, m):
                    if (x, j) == (i, j) or self.keypad[x][j] == INVALID_CHAR:
                        continue
                    self.next_pos[(i, j)].append((x, j))

                for y in range(0, n):
                    if (i, y) == (i, j) or self.keypad[i][y] == INVALID_CHAR:
                        continue
                    self.next_pos[(i, j)].append((i, y))

    def calculate_next_position(self):
        {
            PieceType.knight: self.calculate_next_position_knight,
            PieceType.rook: self.calculate_next_position_rook
        }[self.piece]()

    def dfs(self, rem: int, vowel: int, pos: Tuple[int, int]):
        """
        :param rem: no of chars remaining
        :param vowel: no of vowel remaining
        :param pos: current position on pad
        :return: int
        """

        if rem == 0:
            return 1

        # prefetching using mem table
        if (pos[0], pos[1], rem, vowel) in self.mem:
            return self.mem[(pos[0], pos[1], rem, vowel)]

        count = 0
        # find next available position and recusing on it.
        for n_pos in self.next_pos[pos]:
            char = KEYPAD[n_pos[0]][n_pos[1]]

            if char in VOWELS:
                if vowel > 0:
                    count += self.dfs(rem - 1, vowel - 1, n_pos)
            else:
                count += self.dfs(rem - 1, vowel, n_pos)
        # storing in mem table
        self.mem[(pos[0], pos[1], rem, vowel)] = count
        return count

    def count_sequences(self):
        """
        starting from every key on the pad and finding
        count of possible combinations
        :return: int
        """
        total_count = 0
        for r in range(M):
            for c in range(N):
                val = KEYPAD[r][c]
                # skipping invalid char
                if val != INVALID_CHAR:
                    if val in VOWELS:
                        # vowel that decrease count  by 1
                        total_count += self.dfs(self.total_len - 1, self.vowel_count - 1, (r, c))
                    else:
                        total_count += self.dfs(self.total_len - 1, self.vowel_count, (r, c))
        return total_count

'''

M * N * (Average nei) ^ length

M * N * length
20 * length
'''

if __name__ == "__main__":
    resp = Solution(KEYPAD, total_len=10, vowel_count=2).count_sequences()
    print(resp)

    # more test cases
    # resp = Solution(total_len=11).count_sequences()
    # print(resp)

