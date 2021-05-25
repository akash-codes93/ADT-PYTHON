"""
Find ways to calculate a target from elements of the specified array
Consider the array { 5, 3, -6, 2 }.

The total number of ways to reach a target of 6 using only + and – operators is 4 as:

(-)-6 = 6
(+) 5 (+) 3 (-) 2 = 6
(+) 5 (-) 3 (-) -6 (-) 2 = 6
(-) 5 (+) 3 (-) -6 (+) 2 = 6

Similarly, there are 4 ways to calculate the target of 4:

(-)-6 (-) 2 = 4
(-) 5 (+) 3 (-)-6 = 4
(+) 5 (-) 3 (+) 2 = 4
(+) 5 (+) 3 (+)-6 (+) 2 = 4
"""


class Solution:

    def calculate(self, nums, p, sum_till_now, k, output):
        # print(nums, p, sum_till_now, k, output)

        if sum_till_now == k:
            print(output)
            return

        if p == len(nums):
            return

        for operator in ['+', '-']:

            if operator == '+':
                sum_till_now += nums[p]
                output.append(operator)
                output.append(nums[p])
                self.calculate(nums, p + 1, sum_till_now, k, output)

                output.pop()
                output.pop()
                sum_till_now -= nums[p]

            else:
                sum_till_now -= nums[p]
                output.append(operator)
                output.append(nums[p])
                self.calculate(nums, p + 1, sum_till_now, k, output)

                output.pop()
                output.pop()

                sum_till_now += nums[p]

        self.calculate(nums, p + 1, sum_till_now, k, output)

    def driver(self, nums, k):

        self.calculate(nums, 0, 0, k, [])


Solution().driver([5, 3, -6, 2], 4)
