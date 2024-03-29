def getInvCount(arr, n):

    inv_count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if (arr[i] > arr[j]):
                inv_count += 1

    return inv_count


class Solution:
    # @param A : list of integers
    # @return an integer
    def countInversions(self, A):
        flips = [0]

        def merge(arr1, arr2):
            f = 0
            i = 0
            j = 0
            final = []
            while i < len(arr1) and j < len(arr2):
                if arr1[i] <= arr2[j]:
                    final.append(arr1[i])
                    i += 1
                elif arr2[j] < arr1[i]:
                    final.append(arr2[j])
                    j += 1
                    f += (len(arr1) - i)
                    flips[0] += (len(arr1) - i)
                elif arr1[i] == arr2[j]:
                    # f += (len(arr1) - i - 1)
                    # flips[0] += (len(arr1) - i - 1)
                    final.append(arr2[j])
                    final.append(arr1[i])
                    i += 1
                    j += 1

            while i < len(arr1):
                final.append(arr1[i])
                i += 1
            while j < len(arr2):
                final.append(arr2[j])
                j += 1
            f1 = getInvCount(arr1 + arr2, len(arr1 + arr2))
            print(f - f1)
            if (f - f1) != 0:
                print(f, f1)
                print(arr1, arr2)
            return final

        def mergeSort(l, r):
            if l == r:
                return [A[l]]

            if l < r:
                mid = (l + r) // 2
                a1 = mergeSort(l, mid)
                a2 = mergeSort(mid + 1, r)

                com = merge(a1, a2)
                return com

        merged = mergeSort(0, len(A)-1)
        return flips

# flips[0] = 0

def merge(arr1, arr2):
    f = 0
    i = 0
    j = 0
    final = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            final.append(arr1[i])
            i += 1
        elif arr2[j] < arr1[i]:
            final.append(arr2[j])
            j += 1
            f += (len(arr1) - i)
            # flips[0] += (len(arr1) - i)
        elif arr1[i] == arr2[j]:
            # f += (len(arr1) - i - 1)
            # flips[0] += (len(arr1) - i - 1)
            final.append(arr2[j])
            final.append(arr1[i])
            i += 1
            j += 1

    while i < len(arr1):
        final.append(arr1[i])
        i += 1
    while j < len(arr2):
        final.append(arr2[j])
        j += 1
    f1 = getInvCount(arr1 + arr2, len(arr1 + arr2))
    print(f - f1)
    if (f - f1) != 0:
        print(f, f1)
        print(arr1, arr2)
    print(final)
    return final


# f = Solution().countInversions([ 84, 2, 37, 3, 67, 82, 19, 97, 91, 63, 27, 6, 13, 90, 63, 89, 100, 60, 47, 96, 54, 26, 64, 50, 71, 16, 6, 40, 84, 93, 67, 85, 16, 22, 60 ])
# f = Solution().countInversions([ 61, 88, 77, 30, 66, 84, 87, 91, 26, 44, 24, 53, 94, 87, 58, 77, 2, 77, 58, 28, 92, 6, 21, 40, 61, 24, 53, 17, 90, 74, 60, 52, 32, 74, 85, 69, 76, 87, 92, 25, 78, 4, 67, 14, 66, 24, 98, 77, 15] )
# f = Solution().countInversions([59,29])
# f = Solution().countInversions([1,8,24,26,30,3,4,5,24])
# f = Solution().countInversions([397, 461, 116, 405, 100, 137, 181, 199, 33, 388, 85, 241, 18, 7, 171, 242, 383, 250, 24, 259, 106, 122, 96, 297, 417, 179, 179, 80, 59, 78, 251, 8, 230, 82, 496, 179, 177, 254, 400, 285, 66, 94, 109, 173, 244, 430, 15, 169, 56, 192, 474, 423, 249, 152, 487, 145, 447, 78, 18, 130, 417, 375, 292])
# f = Solution().countInversions([5,4,3,2,1])
# f = Solution().countInversions([24, 24, 24, 23, 24, 24])
# f = getInvCount([1,8,24,26,30,3,4,5,24], 9)
f = getInvCount([397, 461, 116, 405, 100, 137, 181, 199, 33, 388, 85, 241, 18, 7, 171, 242, 383, 250, 24, 259, 106, 122, 96, 297, 417, 179, 179, 80, 59, 78, 251, 8, 230, 82, 496, 179, 177, 254, 400, 285, 66, 94, 109, 173, 244, 430, 15, 169, 56, 192, 474, 423, 249, 152, 487, 145, 447, 78, 18, 130, 417, 375, 292], 63)
print(f)



# merge([7, 8, 18, 24, 33, 59, 78, 80, 85, 96, 100, 106, 116, 122, 137, 171, 179, 179, 181, 199, 241, 242, 250, 251, 259, 297, 383, 388, 397, 405, 417, 461], [15, 18, 56, 66, 78, 82, 94, 109, 130, 145, 152, 169, 173, 177, 179, 192, 230, 244, 249, 254, 285, 292, 375, 400, 417, 423, 430, 447, 474, 487, 496])

merge([24,24,24,], [23,24,24])


class Node:
    def __init__(self, starttime, endtime):
        self.starttime = starttime
        self.endtime = endtime

    def __lt__(self, other):
        if self.endtime < other.endtime:
            return True
        elif self.starttime < other.starttime:
            return True
        return False


def min_heapify(arr, i, heap_size):
    left = 2 * i + 1
    right = 2 * i + 2

    smallest = i
    if left < heap_size and arr[left] < arr[smallest]:
        smallest = left

    if right < heap_size and arr[right] < arr[smallest]:
        smallest = right

    if smallest != i:
        arr[smallest], arr[i] = arr[i], arr[smallest]
        min_heapify(arr, smallest, heap_size)


def build_heap(arr):
    for i in range(math.floor(len(arr) / 2) - 1, -1, -1):
        min_heapify(arr, i, len(arr))


class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:

        arr = []
        for starttime, endtime in events:
            arr.append(Node(starttime, endtime))

        build_heap(arr)

        day = 1
        total = 0
        while arr:

            node = arr[0]
            if node.starttime <= day <= node.endtime:
                total += 1
                arr[0] = arr[-1]
                arr.pop()
                min_heapify(arr, 0, len(arr))

            elif day > node.endtime:
                arr[0] = arr[-1]
                arr.pop()
                min_heapify(arr, 0, len(arr))

            day += 1

        return total

