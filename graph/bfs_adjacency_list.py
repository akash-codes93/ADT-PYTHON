class Solution:

    def bfs(self, ada_list):

        queue = [0]
        traversed = {}

        while queue:
            node = queue.pop(0)
            print(node)
            traversed[node] = 1

            for each in ada_list[node]:

                if not traversed.get(each, 0):
                    queue.append(each)


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

Solution().bfs(adjacency_list)

