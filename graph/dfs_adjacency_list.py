class Solution:

    def dfs(self, ada_list):
        traverse = {}

        self._dfs(ada_list, 0, traverse)

    def _dfs(self, ada_list, index, traverse):
        print(index)
        traverse[index] = 1

        for node in ada_list[index]:
            if not traverse.get(node, 0):
                self._dfs(ada_list, node, traverse)


adjacency_list = [
    [1, 3],
    [0],
    [3, 8],
    [0, 4, 5, 2],
    [3, 6],
    [3],
    [4, 7],
    [6],
    [2]
]

Solution().dfs(adjacency_list)

