def maximum(arr: list, i):
    if i == 0:
        return arr[0]

    else:
        return max(arr[i], maximum(arr, i - 1))


if __name__ == '__main__':
    print(maximum([2, 8, 64, 0, 2], 4))
