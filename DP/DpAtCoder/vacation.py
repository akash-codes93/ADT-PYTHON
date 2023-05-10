"""
https://atcoder.jp/contests/dp/tasks/dp_c
"""


num = int(input())

a = []

for i in range(0, num):
    a.append(
        [int(i) for i in input().split(' ')]
    )

F = [[0]*3 for i in range(num)]


F[0][0] = a[0][0]
F[0][1] = a[0][1]
F[0][2] = a[0][2]

for day in range(1, num):
    F[day][0] = a[day][0] + max(F[day-1][1], F[day-1][2])
    F[day][1] = a[day][1] + max(F[day-1][0], F[day-1][2])
    F[day][2] = a[day][2] + max(F[day-1][0], F[day-1][1])

print(F)
print(max(F[num-1][0], F[num-1][1], F[num-1][2]))

