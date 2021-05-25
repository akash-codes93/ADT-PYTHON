"""
Find all combinations of non-overlapping substrings of a string
Input: ABC

Output:

(A) (B) (C)
(A) (BC)
(AB) (C)
(ABC)
"""


class Solution:

    def process_output(self, output):
        string = ''
        for i in output:
            string = string + '(' + i + ')'

        return string

    def get_string(self, actual, output, to_be_added):
        return actual + ''.join(output) + to_be_added

    def find_substrings(self, string, out):

        if not string:
            print(self.process_output(out))
            return

        for i in range(0, len(string)):
            out.append(string[: i+1])

            self.find_substrings(string[i+1:], out)
            out.pop()

    def driver(self, string):

        output = []
        main_output = []
        self.find_substrings(string, [])
        return main_output


op = Solution().driver('ABCD')
print(op)
