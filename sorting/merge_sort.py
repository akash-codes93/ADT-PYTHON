def conquer(arr, l, m, r):
    a1 = arr[l: m + 1]
    a2 = arr[m + 1: r + 1]
    # print(a1)
    # print(a2)
    a3 = []

    size = len(a1) if len(a1) > len(a2) else len(a2)

    pointer_a1 = 0
    pointer_a2 = 0

    # print(size)

    while pointer_a2 <= size or pointer_a1 <= size:
        # print(pointer_a1)
        # print(pointer_a2)

        if pointer_a2 >= len(a2):
            a3.extend(a1[pointer_a1:])
            break
        elif pointer_a1 >= len(a1):
            a3.extend(a2[pointer_a2:])
            break
        else:

            if a1[pointer_a1] > a2[pointer_a2]:
                a3.append(a2[pointer_a2])
                pointer_a2 += 1
            else:
                a3.append(a1[pointer_a1])
                pointer_a1 += 1

        # print(a3)

    arr[l:r + 1] = a3[:]

    return arr


def divide(arr, l, r):
    # print(l, r)
    if l < r:
        m = (l + r) // 2

        divide(arr, l, m)
        divide(arr, m + 1, r)
        # print(l, m, r)
        arr = conquer(arr, l, m, r)

    return arr


# def merge_sort(arr):
#
#     return divide(arr, 0, len(arr)-1)

def merge_two_sorted_array(arr1, arr2):
    print(arr1, arr2)
    arr = []
    i, j = 0, 0

    while(i<len(arr1) or j < len(arr2)):
        largest = float('inf')

        if (i < len(arr1) and arr1[i] < largest):
            largest = arr1[i]

        if (j < len(arr2) and arr2[j] < largest):
            largest = arr2[j]

        arr.append(largest)

        if i < len(arr1) and largest == arr1[i]:
            i += 1

        elif j < len(arr2) and largest == arr2[j]:
            j += 1
    print(arr)
    return arr


def merge_sort(arr):

    if len(arr) == 1:
        return arr

    l = len(arr) // 2

    arr1 = merge_sort(arr[0: l])
    arr2 = merge_sort(arr[l:])

    return merge_two_sorted_array(arr1, arr2)




if __name__ == '__main__':
    sorted_arr = merge_sort([45, 5,45, 4,30, 2, 6, 1,500, 3, 5])
    print(sorted_arr)
    # print(divide([5, 4, 2, 6, 1, 3, 5], 0, 6))
    # print(conquer([5], [4]))
    pass
    # conquer([5, 4, 2, 6, 1, 3], 0, 0, 1)
    # conquer([1, 3, 2, 2, 6, 1, 3], 0, 1, 2)
    # conquer([1, 4, 5, 9, 2, 3, 5, 6, 10, 11], 0, 3, 9)
