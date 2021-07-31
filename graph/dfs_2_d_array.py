class Solution:
    """
    DFS traversal of a 2-D array
    """

    def dfs(self, array, i, j, traversed):

        if traversed.get((i, j), 0):
            return

        print(array[i][j])
        traversed[(i, j)] = 1

        if i - 1 >= 0:
            self.dfs(array, i - 1, j, traversed)

        if j + 1 < len(array[i]):
            self.dfs(array, i, j + 1, traversed)

        if i + 1 < len(array):
            self.dfs(array, i + 1, j, traversed)

        if j - 1 >= 0:
            self.dfs(array, i, j - 1, traversed)

        return


d2_array = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20]
]

Solution().dfs(d2_array, 0, 0, {})

"""
Also a 2-d array can be used instead of dict to keep tract of elements which we have traversed.
[
    [F,F,F,F,]...and so on
]
"""
