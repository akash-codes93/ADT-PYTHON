import copy

VOWELS = {0, 4, 8, 14}

NEXT_POS = {'A': ['H', 'L'], 'B': ['K', 'M', 'I'], 'C': ['L', 'N', 'J', 'F'], 'D': ['M', 'O', 'G'], 'E': ['H', 'N'],
            'F': ['C', 'M', '1'], 'G': ['2', 'N', 'D'], 'H': ['O', 'K', 'A', 'E', '1', '3'], 'I': ['B', 'L', '2'],
            'J': ['C', 'M', '3'], 'K': ['B', '2', 'H'], 'L': ['C', 'I', '3', 'A'], 'M': ['B', 'D', 'F', 'J'],
            'N': ['C', 'E', 'G', '1'], 'O': ['H', '2', 'D'], '1': ['F', 'H', 'N'], '2': ['G', 'I', 'K', 'O'],
            '3': ['H', 'L', 'J']}

# NEXT_POS = {0: [7, 11], 1: [10, 12, 8], 2: [11, 13, 9, 5], 3: [12, 14, 6], 4: [7, 13], 5: [2, 12, 15], 6: [16, 13, 3],
#             7: [14, 10, 0, 4, 15, 17], 8: [1, 11, 16], 9: [2, 12, 17], 10: [1, 16, 7], 11: [2, 8, 17, 0],
#             12: [1, 3, 5, 9], 13: [2, 4, 6, 15], 14: [7, 16, 3], 15: [5, 7, 13], 16: [6, 8, 10, 14], 17: [7, 11, 9]}

# variable = {
#     'A': 0,
#     'B': 1,
#     'C': 2,
#     'D': 3,
#     'E': 4,
#     'F': 5,
#     'G': 6,
#     'H': 7,
#     'I': 8,
#     'J': 9,
#     'K': 10,
#     'L': 11,
#     'M': 12,
#     'N': 13,
#     'O': 14,
#     '1': 15,
#     '2': 16,
#     '3': 17
# }

total_vowels = 2
n = 10
dp = [[1] * 18 for _ in range(total_vowels + 1)]

for j in VOWELS:
    dp[0][j] = 0

for _ in range(2, n + 1):
    prev = copy.deepcopy(dp)

    # iterating on rows
    for v in range(total_vowels + 1):

        # iterating over keypad
        for j in range(18):
            total_moves = 0
            remain_v = v

            if j in VOWELS:
                if remain_v > 0:
                    remain_v -= 1
                else:
                    continue

            for pos in NEXT_POS[j]:
                total_moves += prev[remain_v][pos]

            dp[v][j] = total_moves

print(sum(dp[-1]))

print(dp)

from typing import Tuple

VOWELS = {"A", "E", "I", "O", "U"}

INVALID_CHAR = "X"

KEYPAD = [
    ["A", "B", "C", "D", "E"],
    ["F", "G", "H", "I", "J"],
    ["K", "L", "M", "N", "O"],
    [INVALID_CHAR, "1", "2", "3", INVALID_CHAR]
]

# dict of list of valid next positions for a position
NEXT_POS = {
    (0, 0): [(1, 2), (2, 1)],
    (0, 1): [(2, 0), (2, 2), (1, 3)],
    (0, 2): [(2, 1), (2, 3), (1, 4), (1, 0)],
    (0, 3): [(2, 2), (2, 4), (1, 1)],
    (0, 4): [(1, 2), (2, 3)],
    (1, 0): [(0, 2), (2, 2), (3, 1)],
    (1, 1): [(3, 2), (2, 3), (0, 3)],
    (1, 2): [(2, 4), (2, 0), (0, 0), (0, 4), (3, 1), (3, 3)],
    (1, 3): [(0, 1), (2, 1), (3, 2)],
    (1, 4): [(0, 2), (2, 2), (3, 3)],
    (2, 0): [(0, 1), (3, 2), (1, 2)],
    (2, 1): [(0, 2), (1, 3), (3, 3), (0, 0)],
    (2, 2): [(0, 1), (0, 3), (1, 0), (1, 4)],
    (2, 3): [(0, 2), (0, 4), (1, 1), (3, 1)],
    (2, 4): [(1, 2), (3, 2), (0, 3)],
    (3, 1): [(1, 0), (1, 2), (2, 3)],
    (3, 2): [(1, 1), (1, 3), (2, 0), (2, 4)],
    (3, 3): [(1, 2), (2, 1), (1, 4)]

}

M = len(KEYPAD)
N = len(KEYPAD[0])


class Solution:
    """
    Approach: Top down + memoization
    State = (position, remaining length, remaining vowels)
    """
    mem = {}

    def __init__(self, total_len: int = 10, vowel_count: int = 2):
        self.total_len = total_len
        self.vowel_count = vowel_count

    def dfs(self, rem: int, vowel: int, pos: Tuple[int, int], condtion: int):
        """
        :param rem: no of chars remaining
        :param vowel: no of vowel remaining
        :param pos: current position on pad
        :return: int
        """

        if rem == 0:
            return 1

        # prefetching using mem table
        if (pos[0], pos[1], rem, vowel, condtion) in self.mem:
            return self.mem[(pos[0], pos[1], rem, vowel, condtion)]

        count = 0

        for n_pos in NEXT_POS[pos]:
            char = KEYPAD[n_pos[0]][n_pos[1]]

            if condtion == 0:
                if char in VOWELS:
                    if vowel > 0:
                        count += self.dfs(rem - 1, vowel - 1, n_pos, 1)
                else:
                    count += self.dfs(rem - 1, vowel, n_pos, 0)
            elif condtion == 1:
                if char not in VOWELS:
                    count += self.dfs(rem - 1, vowel, n_pos, 2)
            elif condtion == 2:
                if char in VOWELS:
                    if vowel > 0:
                        count += self.dfs(rem - 1, vowel - 1, n_pos, 3)
            elif condtion == 3:
                if char not in VOWELS:
                    count += self.dfs(rem - 1, vowel, n_pos, 0)

        # storing in mem table
        self.mem[(pos[0], pos[1], rem, vowel, condtion)] = count
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
                        if self.vowel_count > 0:
                            # vowel that decrease count  by 1
                            total_count += self.dfs(self.total_len - 1, self.vowel_count - 1, (r, c), 1)
                    else:
                        total_count += self.dfs(self.total_len - 1, self.vowel_count, (r, c), 0)
        return total_count


if __name__ == "__main__":
    resp = Solution(total_len=3, vowel_count=2).count_sequences()
    print(resp)

    # more test cases
    # resp = Solution(total_len=11).count_sequences()
    # print(resp)
