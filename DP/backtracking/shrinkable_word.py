"""
startling starting staring string sting sing sin in i  → → → → → → → → → (empty)
Write a function that accepts as input a string and a set of all the words in English, then
reports whether the input word is shrinkable.
"""
from typing import List


class Solution:

    def is_shrinkable(self, string: str, dictionary: List) -> bool:

        if len(string) == 1 and string in dictionary:
            return True

        for i in range(0, len(string)):

            remaining_str = string[0:i] + string[i + 1:]

            if remaining_str in dictionary and self.is_shrinkable(remaining_str, dictionary):
                return True

        return False


is_shrinkable = Solution().is_shrinkable("startling",
                                         ["starting", "staring", "string", "sting", "sing", "sin", "in", "i"])
print(is_shrinkable)
