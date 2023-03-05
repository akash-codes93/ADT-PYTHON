"""
@url: https://leetcode.com/problems/group-anagrams/
T = O(N * MLogM)
S = O(LogN)
"""
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for _str in strs:
            list_str = list(_str)
            list_str.sort()
            sorted_str = "".join(list_str)

            value = anagrams.get(sorted_str, None)

            if value is None:
                anagrams[sorted_str] = [_str]
            else:
                anagrams[sorted_str].append(_str)

        ans = []
        for value in anagrams.values():
            ans.append(value)

        return ans
