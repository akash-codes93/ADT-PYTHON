"""
@url: https://www.geeksforgeeks.org/tug-of-war/
Given a set of n integers, divide the set in two subsets of n/2 sizes each such that the difference of the sum of two
subsets is as minimum as possible. If n is even, then sizes of two subsets must be strictly n/2 and if n is odd,
then size of one subset must be (n-1)/2 and size of other subset must be (n+1)/2.
"""
##########################
#                        #
#       solved own       #
#                        #
##########################


class Solution:

    def set_len_diff(self, set1, set2):

        len1 = len(set1)
        len2 = len(set2)

        diff = abs(len1 - len2)

        return diff <= 1

    def get_val_diff(self, set1, set2):
        return abs(sum(set1) - sum(set2))

    def tug_of_war(self, nums, set1, set2, min_val, p, output):

        if p == len(nums):
            if self.set_len_diff(set1, set2):
                val = self.get_val_diff(set1, set2)
                # print(set1, set2, val)
                if val <= min_val:
                    output.clear()
                    output += [tuple(set1), tuple(set2), val]
                    min_val = val
            return min_val

        for option in [0, 1]:

            if option:
                set1.append(nums[p])
                min_val = self.tug_of_war(nums, set1, set2, min_val, p + 1, output)
                set1.pop()

            else:
                set2.append(nums[p])
                min_val = self.tug_of_war(nums, set1, set2, min_val, p + 1, output)
                set2.pop()

        return min_val


_output = []
# Solution().tug_of_war([3, 4, 5, -3, 100, 1, 89, 54, 23, 20], [], [], 9999, 0, _output)
Solution().tug_of_war([23, 45, -34, 12, 0, 98, -99, 4, 189, -1, 4], [], [], 9999, 0, _output)
print(_output)
