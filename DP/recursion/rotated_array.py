class Solution:

    def is_rotated(self, sorted_arr, arr, k):

        if k >= len(arr):
            return False

        if arr == sorted_arr[k:] + sorted_arr[0:k]:
            return True

        return self.is_rotated(sorted_arr, arr, k + 1)


check_for_rotated = [6, 7, 0, 1, 2, 3, 4, 9]
print(Solution().is_rotated(
    list(sorted(check_for_rotated)),
    check_for_rotated,
    0)
)
