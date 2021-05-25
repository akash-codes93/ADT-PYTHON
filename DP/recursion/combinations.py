from typing import List, Any


class Combination:

    def combinations_k(self, nums: List, k: int) -> List[List[Any]]:

        result = []

        if len(nums) == 0:
            return []
        if k == 1:
            return [[num] for num in nums]

        for i in range(0, len(nums)):
            num = nums[i]
            remaining_nums = nums[i + 1:]

            combinations = self.combinations_k(remaining_nums, k - 1)

            for combination in combinations:
                result.append(
                    [num] + combination
                )

        return result

    def approach_2_combination_k(self, nums: List, combination: List, start: int, k: int) -> None:
        if len(combination) == k:
            print(combination)
            return

        if start == len(nums):
            return

        for i in range(start, len(nums)):
            combination.append(nums[i])

            self.approach_2_combination_k(nums, combination, i + 1, k)

            combination.pop(-1)

        return

    def approach_3_combination_k(self, nums: List, k: int, start: int, result: List) -> None:
        if len(result) == k:
            print(result)
            return

        if start == len(nums):
            return

        # for p in range(0, len(nums)):
        for i in [0, 1]:
            if i:
                result.append(nums[start])
                self.approach_3_combination_k(nums, k, start + 1, result)
                result.pop(-1)
            else:
                self.approach_3_combination_k(nums, k, start + 1, result)

        return

    def target_to_sum(self, nums: List, target: int, start: int, result: List) -> None:
        if start == len(nums):
            return

        if start > 0 and nums[start] == nums[start - 1]:  # skipping to avoid reordered output
            return

        if sum(result) == target:
            print(result)
            return

        for i in range(start, len(nums)):
            result.append(nums[i])

            self.target_to_sum(nums, target, i + 1, result)

            result.pop(-1)

        return

    def target_to_sum_(self, nums: List, target: int, start: int, result: List) -> None:
        # print(result, target)
        if start == len(nums):
            return

        # if start > 0 and nums[start] == nums[start - 1]:  # skipping to avoid reordered output
        #     return

        if target < 0:
            return

        if target == 0:
            print(result)
            return

        for i in range(start, len(nums)):
            result.append(nums[i])
            target -= nums[i]
            self.target_to_sum_(nums, target, i + 1, result)

            result.pop(-1)
            target += nums[i]

        return

    # combinations_k = Combination().combinations_k


combinations_k = Combination().approach_2_combination_k
# combinations_k = Combination().target_to_sum_
# output = combinations_k([3, 2, 5, 8], k=3)
# print(output)

combinations_k([3, 2, 5, 8], [], 0, k=2)
# combinations_k([3, 2, 5, 8], k=3, start=0, result=[])
# combinations_k(list(sorted([2, 3, 2, 5, 8])), target=7, start=0, result=[])
