import math


def heapify(arr, index, heap_size):
    left = 2 * index + 1
    right = 2 * index + 2

    largest_index = index

    if (left < heap_size and arr[left] > arr[index]):
        largest_index = left

    if (right < heap_size and arr[right] > arr[largest_index]):
        largest_index = right

    if (largest_index != index):
        arr[largest_index], arr[index] = arr[index], arr[largest_index]
        heapify(arr, largest_index, heap_size)


def build_max_heap(arr):
    for i in range(math.floor(len(arr) / 2) - 1, -1, -1):
        heapify(arr, i, len(arr))


def heap_sort(arr):
    build_max_heap(arr)

    p = 1

    for j in range(len(arr) - 1, 0, -1):
        arr[0], arr[j] = arr[j], arr[0]
        heapify(arr, 0, len(arr) - p)
        p += 1


def insert_key(arr, num):
    arr.append(num)
    i = len(arr) -1

    while (i > 0):
        parent = math.ceil(i / 2) - 1
        if (arr[parent] > arr[i]):
            break
        arr[parent], arr[i] = arr[i], arr[parent]
        i = parent


arr1 = [2, 4, 3, 1, 10, 15, 5, 2, 1, 1, 4]
# heapify(arr1, 0, len(arr1))
# heap_sort(arr1)
build_max_heap(arr1)
insert_key(arr1, 30)
print(arr1)

