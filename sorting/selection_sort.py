def selection_sort(arr):
    # loop over the array
    for i in range(0, len(arr)-1):

        min_elem = arr[i]
        min_index = i

        # finding min element in the sub array
        for j in range(i, len(arr)):

            if min_elem > arr[j]:
                min_elem = arr[j]
                min_index = j

        # swapping element with the start index
        p = arr[i]
        arr[i] = min_elem
        arr[min_index] = p

    print(arr)


if __name__ == '__main__':
    a = [5, 3, 6, 3, 4, 5, 6, 1]
    selection_sort(a)
    # not stable and in-place
