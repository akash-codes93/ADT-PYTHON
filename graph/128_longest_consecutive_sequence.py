"""
https://leetcode.com/problems/longest-consecutive-sequence/

implemented union find by rank

"""

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        dsuf = {}

        def find(v):
            if v + 1 not in dsuf:
                return dsuf[v]
            if dsuf[v] != v:
                return dsuf[v]

            dsuf[v] = find(v + 1)
            return dsuf[v]

        for i in nums:
            dsuf[i] = i

        for i in nums:
            p = i
            find(i)

        max_value = 1
        for key, value in dsuf.items():
            max_value = max(max_value, value - key + 1)
        return max_value
