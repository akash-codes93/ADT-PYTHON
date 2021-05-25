class Solution:

    def get_collection_points(self, nums, index, collection_points):

        if index >= len(nums):
            return

        if index == 0:

            if nums[index + 1] > nums[index]:
                collection_points.append(nums[index])

        elif index == len(nums) - 1:

            if nums[index - 1] > nums[index]:
                collection_points.append(nums[index])

        elif nums[index - 1] > nums[index] and nums[index + 1] > nums[index]:
            collection_points.append(nums[index])

        return self.get_collection_points(nums, index + 1, collection_points)

    def get_total_water_stored(self, nums):
        collection_points = []
        self.get_collection_points(nums, 0, collection_points)


_collection_points = []
Solution().get_collection_points(
    [11, 8, 4, 2, 5, 3, 12, 10, 14, 15, 6],
    0,
    _collection_points
)

print(_collection_points)
