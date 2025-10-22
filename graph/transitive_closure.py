import copy

from collections import defaultdict

graph = defaultdict(list)

# graph[0] = [0, 1, 3]
# graph[1] = [1, 2]
# graph[2] = [0]
# graph[3] = [3]

graph[0] = [1, 2]
graph[1] = [2]
graph[2] = [0, 3]
graph[3] = [3]


tc = [[0] * 4 for _ in range(0, 4)]


def dfs(curr, start):
    print(curr, start)

    if curr == start:
        # is self edge exists in graph
        if curr in graph[start]:
            tc[start][curr] = 1
    else:
        tc[start][curr] = 1

    nodes = graph[curr]
    for node in nodes:
        # to avoid infinite loop
        if tc[start][node] == 0:
            if start == node:
                # even tough self edge does not exist we are able to reach same node
                tc[start][node] = 1
            else:
                dfs(node, start)


for i in range(0, 4):
    print("------")
    dfs(i, i)

print(tc)
