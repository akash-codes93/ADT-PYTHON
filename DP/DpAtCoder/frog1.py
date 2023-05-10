

def frog1(heights):

    first = 0
    second = min(abs(heights[1] - heights[0]))

    for p in range(2, len(heights)):

        temp = min(
            abs(heights[p] - heights[p-1]) + second,
            abs(heights[p] - heights[p - 2]) + first
        )

        first = second
        second = temp

    return second


num = int(input())

heights = [int(i) for i in input().split(' ')]

# heights = []
# for i in range(0, num):
#     h = int(input())
#     heights.append(h)

p = frog1(heights)
print(p)
# ans = frog1([30, 10, 60, 10, 60, 50])
# print(ans)

