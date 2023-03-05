"""
https://leetcode.com/problems/trapping-rain-water/
"""
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:

        max_left, max_right = 0, 0
        l = 0
        r = len(height) - 1
        total = 0

        while (l <= r):
            if height[l] < height[r]:
                if max_left < height[l]:
                    max_left = height[l]
                else:
                    total += max_left - height[l]

                l += 1
            else:
                if max_right < height[r]:
                    max_right = height[r]
                else:
                    total += max_right - height[r]

                r -= 1

        return total
