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
            if pattern[p] in mapping:
                if string == mapping[pattern[p]]:
                    print(mapping)
            else:
                mapping[pattern[p]] = string
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


# Solution().get_association("akisak", "pqp", 0, {})
# Solution().get_association("akashisisakash", "aiia", 0, {})
# Solution().get_association("tree1treetree", "aaa", 0, {})
Solution().get_association("akisak", "pqp", 0, {})


'''
python -c " 
from pattern_matching import Solution 
Solution().get_association('akashisakash', 'aia', 0, {})
"
'''