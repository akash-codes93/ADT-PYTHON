"""
Given a string, find out if string follows a given pattern or not without using any regular expressions.
Input:
string - GraphTreesGraph
pattern - aba
Output:
a->Graph
b->Trees

Input:
string - GraphGraphGraph
pattern - aaa
Output:
a->Graph

"""


class Solution:

    def get_association(self, string, pattern, p, mapping):

        if p == len(pattern) - 1:
            if pattern[p] in mapping and string == mapping[pattern[p]]:
                print(mapping)
            return

        if pattern[p] in mapping:
            match = mapping[pattern[p]]
            self.get_association(string[len(match):], pattern, p + 1, mapping)
            return

        for i in range(0, len(string)):
            mapping[pattern[p]] = string[:i + 1]
            remaining_str = string[i + 1:]

            self.get_association(remaining_str, pattern, p + 1, mapping)

            mapping.pop(pattern[p])


Solution().get_association("NJGMNJ", "GfG", 0, {})
