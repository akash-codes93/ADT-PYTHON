"""
@url: https://leetcode.com/problems/word-search/
"""
from typing import List


class Solution:

    def get_adjacent_cells(self, board, i, j, path):
        output = []
        # up
        cell = [i-1, j]
        if i-1 >= 0 and cell not in path:
            output.append(cell)

        # down
        cell = [i+1, j]
        if i+1 < len(board) and cell not in path:
            output.append(cell)

        # left
        cell = [i, j-1]
        if j-1 >= 0 and cell not in path:
            output.append(cell)

        # right
        cell = [i, j+1]
        if j+1 < len(board[0]) and cell not in path:
            output.append(cell)

        return output


    def word_search(self, board, i, j, word, k, path):

        if k == len(word):
            print(path)
            return True

        adjacency = self.get_adjacent_cells(board, i, j, path)
        main_status = False

        for cell in adjacency:

            if board[cell[0]][cell[1]] == word[k]:
                path.append(cell)
                status = self.word_search(board, cell[0], cell[1], word, k+1, path)
                if status:
                    main_status = status
                path.pop()

        return main_status

    def exist(self, board: List[List[str]], word: str) -> bool:

        for i in range(len(board)):
            for j in range(len(board[0])):

                if board[i][j] == word[0]:
                    if self.word_search(board, i, j, word, 1, [[i, j]]):
                        return True

        return False

print(Solution().exist([["C","A","A"],["A","A","A"],["B","C","D"]], "AAB"))

