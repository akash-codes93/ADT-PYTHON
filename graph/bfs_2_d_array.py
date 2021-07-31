class Solution:

    def bfs(self, array):
        queue = [(2, 2)]
        traverse = {}

        while queue:
            pos = queue.pop(0)
            i, j = pos[0], pos[1]

            if traverse.get((i, j), 0):
                continue

            print(array[i][j])
            traverse[(i, j)] = 1

            # up
            if i - 1 >= 0:
                queue.append((i - 1, j))
            if j + 1 < len(array[i]):
                queue.append((i, j + 1))
            if i + 1 < len(array):
                queue.append((i + 1, j))
            if j - 1 >= 0:
                queue.append((i, j - 1))


d2_array = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20]
]

Solution().bfs(d2_array)
