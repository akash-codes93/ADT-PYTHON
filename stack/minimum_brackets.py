"""
@url: https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/
"""


class Stack:

    def __init__(self):
        self.s = []
        self._len = 0

    def push(self, a):
        self.s.append(a)
        self._len += 1

    def pop(self):
        try:
            a = self.s.pop()
            self._len -= 1
            return a
        except IndexError:
            return None

    def isEmpty(self):
        if self._len == 0:
            return True
        return False


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:

        s = list(s)
        p = Stack()

        for i in range(0, len(s)):

            if s[i] == '(':
                p.push(i)

            elif s[i] == ')':

                if not p.isEmpty():
                    p.pop()

                else:
                    s[i] = ""

        while not p.isEmpty():
            s[p.pop()] = ""

        # print(s)

        return "".join(s)