def insertion_sort(arr):

    # loop over the array
    for i in range(1, len(arr)):

        # loop over the left array which is sorted
        for j in range(0, i):

            # find the right place and replace the element
            if arr[j] > arr[i]:
                p = 0
                p = arr[j]
                arr[j] = arr[i]
                arr[i] = p

    print(arr)


if __name__ == '__main__':
    a = [5, 3, 6, 3, 4, 5, 6, 1]
    insertion_sort(a)
    # stable and in-place
