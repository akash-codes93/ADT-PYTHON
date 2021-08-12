"""
n-1 iterations for the algo


detect negative cycles
after n-1 iterations if list changes then negative cycles present

T: O(VE)
S: O(N)
"""
from typing import List


class Solution:

    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        distances = [float('inf') for i in range(n)]

        distances[k - 1] = 0

        for _ in range(n - 1):
            count = 0
            for i in range(len(times)):
                source = times[i][0]
                dest = times[i][1]
                weight = times[i][2]

                if distances[source] + weight < distances[dest]:
                    distances[dest] = distances[source] + weight

                    count += 1

            if count == 0:
                break

        max_distance = max(distances)
        print(distances)
        if max_distance == float('inf'):
            return -1
        return max_distance
