"""
greedy method -- positive weights, no cycles
@url: https://leetcode.com/problems/network-delay-time/
S: O(V+E)
T: O(ElogV) === 2N + E + (ElogV + VlogV)
"""
import heapq
from typing import List


class Solution:

    def find_min_weight(self, heap):
        min_weight = float('inf')
        min_vertex = 0

        for vertex, weight in heap.items():

            if weight < min_weight:
                min_weight = weight
                min_vertex = vertex

        heap.pop(min_vertex)
        return min_vertex

    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        distances = [float('inf') for i in range(n)]
        adjacency = [[] for i in range(n)]

        distances[k-1] = 0

        heap = {}
        # heapq.heappush(heap, distances[k-1])
        heap[k-1] = distances[k-1]

        for i in range(len(times)):
            source = times[i][0]
            dest = times[i][1]
            weight = times[i][2]

            adjacency[source-1].append([dest-1, weight])
        print(adjacency)
        while heap:

            current_vertex = self.find_min_weight(heap)
            print("curr_vertex-", current_vertex)
            neighbours = adjacency[current_vertex]
            print("neightbours-", neighbours)
            for i in range(len(neighbours)):
                print(i, adjacency[i])
                neighbour_vertex = neighbours[i][0]
                weight = neighbours[i][1]

                if distances[current_vertex] + weight < distances[neighbour_vertex]:
                    distances[neighbour_vertex] = distances[current_vertex] + weight

                    heap[neighbour_vertex] = distances[neighbour_vertex]

        max_distance = max(distances)
        print(distances)
        if max_distance == float('inf'):
            return -1
        return max_distance