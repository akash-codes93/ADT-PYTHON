"""
Question:
Given a non-negative integer n, write a function that lists all strings formed from exactly n
pairs of balanced parentheses. For example, given n = 3, you'd list these five strings:
((())) (()()) (())() ()(()) ()()()
Use: recursion
"""
from typing import List


class Solution:

    def parentheses(self, k: int) -> List[str]:
        result = []
        if k == 0:
            return []
        if k == 1:
            return ['()']

        paras = []
        for step in range(k - 1, 0, -1):
            sub_paras = []

            for sol in self.parentheses(step):
                sub_paras.append('(' + sol + ')')

            for sol in self.parentheses(k - step - 1):
                for i, para in enumerate(sub_paras):
                    sub_paras[i] = para + sol

            paras += sub_paras

        paras += list(map(lambda x: '()' + x, self.parentheses(k - 1)))

        result = result + paras

        return result




# better
# recursion leap of faith

def generate_parenthesis(n) -> set:

    """
    not correct try for 4
    :param n:
    :return:
    """
    if n == 1:
        return {"()"}

    # faith that it gives correct output
    rem = generate_parenthesis(n-1)

    o = set()
    for each in rem:
        o.add(
            each + '()'
        )

        o.add(
            '(' + each + ')'
        )
        o.add(
            '()' + each
        )

    return o


balanced_parentheses = Solution().parentheses
print(
    balanced_parentheses(k=4)
)


op = generate_parenthesis(4)
print(op)

# ["(())()()","((()))()","()(())()","(()()())","(()(()))","(((())))","()()()()","()((()))","()()(())","((()()))","()(()())","(()())()","((())())"]
# ["(((())))","((()()))","((())())","((()))()","(()(()))","(()()())","(()())()","(())(())","(())()()","()((()))","()(()())","()(())()","()()(())","()()()()"]