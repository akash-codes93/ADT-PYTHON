"""
An expression will be given which can contain open and close parentheses and optionally some characters,
No other operator will be there in string. We need to remove minimum number of parentheses to make
the input string valid. If more than one valid output are possible removing same number of parentheses
then print all such output.

Input  : str = “()())()” -
Output : ()()() (())()
There are two possible solutions
"()()()" and "(())()"

"""


class Solution:

    def check_balanced(self, string):
        output = 0
        for i in string:
            if i == '(':
                output += 1
            elif i == ')':
                output -= 1

            if output < 0:
                return False
        return output == 0

    def invalid_parenthesis(self, string, removes, output):

        if removes == 0:
            status = self.check_balanced(string)
            # print(string, status)
            if status:
                output.append(status)
                print(string)
                return

        for i in range(0, len(string)):
            if string[i] in ['(', ')']:
                remaining_str = string[:i] + string[i + 1:]
                self.invalid_parenthesis(remaining_str, removes - 1, output)

    def driver(self, string):
        for i in range(0, len(string)):
            output = []
            self.invalid_parenthesis(string, i, output)

            if any(output):
                break


Solution().driver("()())()")
