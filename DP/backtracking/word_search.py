"""
@url: https://leetcode.com/problems/word-search/

for every element you have to call the recursion element.
"""
from typing import List


class Solution:

    def get_adjacent_cells(self, board, i, j, path):
        output = []
        # up
        cell = (i-1, j)
        if i-1 >= 0 and cell not in path:
            output.append(cell)

        # down
        cell = (i+1, j)
        if i+1 < len(board) and cell not in path:
            output.append(cell)

        # left
        cell = (i, j-1)
        if j-1 >= 0 and cell not in path:
            output.append(cell)

        # right
        cell = (i, j+1)
        if j+1 < len(board[i]) and cell not in path:
            output.append(cell)

        print(i, j, path)

        return output

    def word_search(self, board, i, j, word, k, path: set):

        if k == len(word):
            print(path)
            return True

        main_status = False

        if board[i][j] == word[k]:
            print(i,j,k)
            if k == len(word)-1:
                print("P")
                main_status = True
            adjacency = self.get_adjacent_cells(board, i, j, path)
            for cell in adjacency:
                path.add(cell)
                status = self.word_search(board, cell[0], cell[1], word, k+1, path)
                if status:
                    main_status = status
                path.remove(cell)

        return main_status

    def exist(self, board: List[List[str]], word: str) -> bool:

        for i in range(len(board)):
            for j in range(len(board[i])):

                if self.word_search(board, i, j, word, 0, {(i, j), }):
                    return True

        return False



# print(Solution().exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB"))
# print(Solution().exist([["a"]], "a"))
print(Solution().exist([["a", "a"]], "aaa"))

