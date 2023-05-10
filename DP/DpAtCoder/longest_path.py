from collections import defaultdict


outdeg = defaultdict(set)
indeg = defaultdict(set)

max_path = {}

n, m = [int(i) for i in input().split(' ')]

for i in range(1, n+1):
    max_path[i] = 0


for i in range(m):
    v1, v2 = [int(i) for i in input().split(' ')]

    outdeg[v1].add(v2)
    indeg[v2].add(v1)


zero_outdeg = lambda x: len(outdeg[x]) == 0

queue = list(filter(zero_outdeg, [i for i in range(1, n+1)]))

while queue:

    node = queue.pop(0)
    # print(node)

    for in_v in tuple(indeg[node]):
        max_path[in_v] = max(max_path[in_v], 1 + max_path[node])
        outdeg[in_v].remove(node)
        indeg[node].remove(in_v)
        if zero_outdeg(in_v):
            queue.append(in_v)

# print(outdeg)
# print(indeg)
print(max(max_path.values()))
