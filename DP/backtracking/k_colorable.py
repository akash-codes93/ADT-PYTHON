from typing import Dict, List
from collections import defaultdict


class Solution:
    n = 0

    def k_colorable(self, graph: Dict[int, set], colors: Dict[int, set], node_list: List, index: int, k) -> None:

        if index == len(node_list):
            self.n += 1
            print(self.n)
            print(dict(colors))
            return

        node = node_list[index]
        for color in range(k):

            neighbors = graph[node]
            already_colored = colors[color]

            if len(neighbors.intersection(already_colored)) == 0:
                colors[color].add(node)

                self.k_colorable(graph, colors, node_list, index + 1, k)

                colors[color].remove(node)

    def start_code(self, graph: Dict[int, set], k: int):
        node_list = list(graph.keys())
        colors = defaultdict(set)

        self.k_colorable(graph, colors, node_list, 0, k)


# _graph = {
#     0: {1, 5, 4},
#     1: {0, 4, 3},
#     2: {4, 3},
#     3: {1, 2},
#     4: {0, 1, 5},
#     5: {0, 4},
# }
_graph = {
    0: {1},
    1: {0, 2},
    2: {1}
}

Solution().start_code(_graph, 2)
