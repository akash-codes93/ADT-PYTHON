"""
Given an integer array, find all distinct combinations of a given length <code>k</code>,
where the repetition of elements is allowed.</p>

Input:  {1, 2, 3}, k = 2
Output: {1, 1}, {1, 2}, {1, 3}, {2, 2}, {2, 3}, {3, 3}
"""


# class Solution:
#
#     def combination_k(self, a, i, n, q):
#         if i == len(a):
#             print(a)
#             return
#
#         for p in range(q, n + 1):
#
#             if a[i] == -1:
#                 a[i] = p
#                 self.combination_k(a, i + 1, n, p)
#                 a[i] = -1
#
#     def trigger(self, k, p):
#
#         a = [-1] * p
#
#         self.combination_k(a, 0, k, 1)


class Solution:

    def combination_k(self, a, i, arr, q):
        if i == len(a):
            print(a)
            return

        for j in range(q, len(arr)):

            if j > 0 and arr[j] == arr[j - 1]:
                continue
            else:
                if a[i] == -1:
                    a[i] = arr[j]

                    self.combination_k(a, i + 1, arr, j)
                    a[i] = -1

    def trigger(self, arr, k):
        a = [-1] * k
        self.combination_k(a, 0, arr, 0)

array = [1, 2, 1]
Solution().trigger(list(sorted(array)), 2)
