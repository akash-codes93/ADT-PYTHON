import uuid
from collections import defaultdict


class Node(object):

    def __init__(self, value):
        self.value = value
        self.id = uuid.uuid4()


class Graph(object):

    def __init__(self):

        self.graph = defaultdict(list)

    def add_edge(self, u, v):

        if isinstance(u, Node) and isinstance(v, Node):
            self.graph[u].append(v)

    def bfs(self, s):

        if not isinstance(s, Node):
            raise ValueError("BFS input must be a node type")

        # visited = [False] * len(self.graph)
        visited = defaultdict(bool)

        queue = list()

        queue.append(s)
        visited[s.id] = True

        while queue:

            node = queue.pop()
            print(node.value)

            for neighbour in self.graph[node]:
                if visited[neighbour.id] is False:
                    queue.append(neighbour)
                    visited[node.id] = True

    def dfs(self, s):

        if not isinstance(s, Node):
            raise ValueError("BFS input must be a node type")

        visited = defaultdict(bool)

        self._dfs_utils(s, visited)

    def _dfs_utils(self, s, visited):

        visited[s.id] = True

        print(s.value)

        for neighbour in self.graph[s]:
            if visited[neighbour.id] is False:
                self._dfs_utils(neighbour, visited)


if __name__ == '__main__':

    n0 = Node(0)
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)

    graph = Graph()

    graph.add_edge(n0, n1)
    graph.add_edge(n1, n0)
    graph.add_edge(n0, n2)
    graph.add_edge(n2, n3)
    graph.add_edge(n2, n4)
    graph.add_edge(n4, n2)

    print(graph.graph)

    graph.bfs(n0)
    print("---")
    graph.dfs(n0)
