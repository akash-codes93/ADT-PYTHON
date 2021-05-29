"""
@url: https://www.geeksforgeeks.org/print-palindromic-partitions-string/
Given a string s, partition s such that every string of the partition is a palindrome.
Return all possible palindrome partitioning of s.
Input  : s = "bcc"
Output : [["b", "c", "c"], ["b", "cc"]]

Input  : s = "geeks"
Output : [["g", "e", "e", "k", "s"],
          ["g", "ee", "k", "s"]]
"""


class Solution:

    @staticmethod
    def is_palindrome(string):

        if string == string[-1::-1]:
            return True

        return False

    def palindrome(self, string, output):

        if not string:
            print(output)
            return

        for i in range(len(string)):
            sub = string[: i + 1]
            sub_rest = string[i + 1:]

            if self.is_palindrome(sub):
                output.append(sub)
                self.palindrome(sub_rest, output)
                output.pop()


Solution().palindrome("akaiaka", [])
