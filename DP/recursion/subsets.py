from typing import List, Any


def sub_lists(l, base):
    lists = [[base]]

    for i in range(len(l)):

        orig = lists[:]

        new = l[i]

        for j in range(len(lists)):
            lists[j] = lists[j] + [new]
        lists = orig + lists

    return lists


def sub_list_recursive(l, lists, index):
    """
    Recursive through the list and append all the sub array
    :param l:
    :param lists:
    :param index:
    :return:
    """
    if index >= len(l):
        return lists
    else:
        orig = lists[:]
        new = l[index]

        for j in range(len(lists)):
            lists[j] = lists[j] + [new]

        lists = orig + lists

    return sub_list_recursive(l, lists, index + 1)


def subsets_k(nums: List, k: int) -> List[List[Any]]:
    result = []

    if k == 0:
        return []

    if k == 1:
        return [[num] for num in nums]

    for i in range(0, len(nums)):
        current_num = nums[i]
        remain_nums = nums[i + 1:]

        combinations = subsets_k(remain_nums, k - 1)

        for combination in combinations:
            result.append(
                [current_num] + combination
            )

    return result


def sub_list_driver():
    # driver code
    nums = [1, 2, 3]
    out = []
    for i in range(0, len(nums)):
        current_num = nums[i]
        remain_nums = nums[:i] + nums[i + 1:]
        out.append(sub_lists(remain_nums, current_num))

    print(out)


out = subsets_k(list(range(4)), k=3)
print(out)

