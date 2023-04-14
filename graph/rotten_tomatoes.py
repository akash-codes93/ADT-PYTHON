"""
@url: https://leetcode.com/problems/rotting-oranges/
T: O(M*N)
S: O(M+N)
"""

from typing import List


class Solution:

    def check_all_rotten(self, grid):
        for i in range(0, len(grid)):

            for j in range(0, len(grid[i])):

                if grid[i][j] == 1:
                    return 0

        return 1

    def rotadjacenttomato(self, arr, i, j, queue):
        if i - 1 >= 0 and arr[i - 1][j] == 1:
            arr[i - 1][j] = 2
            queue.append((i - 1, j, 2))

        if j - 1 >= 0 and arr[i][j - 1] == 1:
            arr[i][j - 1] = 2
            queue.append((i, j - 1, 2))

        if i + 1 < len(arr) and arr[i + 1][j] == 1:
            arr[i + 1][j] = 2
            queue.append((i + 1, j, 2))

        if j + 1 < len(arr[i]) and arr[i][j + 1] == 1:
            arr[i][j + 1] = 2
            queue.append((i, j + 1, 2))

    def orangesRotting(self, grid: List[List[int]]) -> int:

        count = 0
        queue = []

        for i in range(0, len(grid)):

            for j in range(0, len(grid[i])):

                if grid[i][j] == 2:
                    queue.append((i, j, 2))

        queue.append((-1, -1, 3))

        while queue:
            pos = queue.pop(0)

            is_tomato = pos[-1]

            if is_tomato == 2:
                self.rotadjacenttomato(grid, pos[0], pos[1], queue)
            else:
                if len(queue) > 0:
                    queue.append((-1, -1, 3))
                    count += 1
                else:
                    break

        if self.check_all_rotten(grid):
            return count
        else:
            return -1
