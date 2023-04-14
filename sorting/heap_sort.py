from heapq import heappop, heappush, heapify


def heap_sort(array):
    heap = []
    for element in array:
        heappush(heap, element)

    print(heap)

    # ordered = []
    #
    # # While we have elements left in the heap
    # while heap:
    #     ordered.append(heappop(heap))
    #
    # return ordered


array = [13, 21, 15, 5, 26, 4, 17, 18, 24, 2]
print(heap_sort(array))
