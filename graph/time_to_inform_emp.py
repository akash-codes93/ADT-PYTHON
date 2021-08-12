"""
https://leetcode.com/problems/time-needed-to-inform-all-employees/
t: O(N)
s: O(N)
"""


class Solution:

    def dfs(self, current, adj_list, informTime):
        if len(adj_list[current]) == 0:
            return 0

        _max = 0
        sub = adj_list[current]
        for each_sub in sub:
            _max = max(_max, self.dfs(each_sub, adj_list, informTime))

        return _max + informTime[current]

    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:

        adj_list = [[] for i in range(n)]

        for i in range(n):
            _manager = manager[i]

            if _manager == -1:
                continue

            adj_list[_manager].append(i)

        return self.dfs(headID, adj_list, informTime)