from typing import List, Any


class Permutations:

    def permutations(self, elements):
        """
        All the permutations of the array
        :param elements:
        :return:
        """
        result = []
        if len(elements) == 0: return []
        if len(elements) == 1: return [elements]

        for i in range(0, len(elements)):
            current_element = elements[i]
            rem_elements = elements[:i] + elements[i + 1:]

            remain_permuts = self.permutations(rem_elements)

            for remain_permut in remain_permuts:
                result.append(
                    [current_element] + remain_permut
                )

        return result

    def permutations_k(self, nums: List, k: int) -> List[List[Any]]:
        result = []

        if k == 0:
            return []

        if k == 1:
            return [[num] for num in nums]

        for i in range(0, len(nums)):
            current_num = nums[i]
            remain_nums = nums[:i] + nums[i + 1:]

            combinations = self.permutations_k(remain_nums, k - 1)

            for combination in combinations:
                result.append(
                    [current_num] + combination
                )

        return result

    def anagrams(self, inp: str) -> List[str]:
        chars = list(inp)
        strings = self.permutations(chars)
        output = []
        for string in strings:
            output.append(
                ''.join(string)
            )

        return output


# permutations_self = Permutations().permutations_k
# res = permutations_self([3, 2, 5, 8], k=3)
# print(res)

# better
def generate_anagrams(string):

    if len(string) == 1:
        return [string]

    start = string[0]

    # trust my function that it will give correct output
    remaining = generate_anagrams(string[1:])

    output = []
    for each in remaining:
        for i in range(0, len(each) + 1):

            output.append(
                each[:i] + start + each[i:]
            )

    return output


def generate_anagrams_backtrack(nums):

    main_output = []
    nums = list(nums)

    def looper(i):

        if i == len(nums):
            main_output.append("".join(nums))
            return
        for j in range(i, len(nums)):
            nums[j], nums[i] = nums[i], nums[j]
            looper(i + 1)
            # backtrack
            nums[j], nums[i] = nums[i], nums[j]

    looper(0)

    return main_output


# anagrams = Permutations().anagrams
# op = anagrams("god")
op = generate_anagrams("god")
# op = generate_anagrams_backtrack("god")
# op = generate_anagrams_backtrack("aab")
print(op)
