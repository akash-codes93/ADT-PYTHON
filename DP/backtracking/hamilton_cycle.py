"""
URL: https://www.geeksforgeeks.org/hamiltonian-cycle-backtracking-6/
Hamiltonian Path in an undirected graph is a path that visits each vertex exactly once. A Hamiltonian cycle
(or Hamiltonian circuit) is a Hamiltonian Path such that there is an edge (in the graph) from the last vertex to the
first vertex of the Hamiltonian Path. Determine whether a given graph contains Hamiltonian Cycle or not.
If it contains, then prints the path. Following are the input and output of the required function

Input:
A 2D array graph[V][V] where V is the number of vertices in graph and graph[V][V] is adjacency matrix representation
of the graph. A value graph[i][j] is 1 if there is a direct edge from i to j, otherwise graph[i][j] is 0.

Output:
An array path[V] that should contain the Hamiltonian Path. path[i] should represent the ith vertex in the
Hamiltonian Path. The code should also return false if there is no Hamiltonian Cycle in the graph.

For example, a Hamiltonian Cycle in the following graph is {0, 1, 2, 4, 3, 0}.

(0)--(1)--(2)
 |   / \   |
 |  /   \  |
 | /     \ |
(3)-------(4)

"""
######solved own##########


class Solution:

    def hamiltonian_path(self, graph, path, p, initial):
        if len(path) == len(graph[0]):
            if graph[p][initial]:
                path.append(0)
                print(path)
                path.pop()
            return

        for i in range(0, len(graph[0])):
            if graph[p][i] == 1 and i not in path:
                path.append(i)
                self.hamiltonian_path(graph, path, i, initial)
                path.pop()

    def driver(self, graph):
        initial = 3
        self.hamiltonian_path(graph, [initial], initial, initial)


_graph = [
    [0, 1, 0, 1, 0],
    [1, 0, 1, 1, 1],
    [0, 1, 0, 0, 1],
    [1, 1, 0, 0, 1],
    [0, 1, 1, 1, 0]
]

Solution().driver(_graph)
