def sum_arr(arr, i):
    if i == 0:
        return arr[0]
    else:
        return sum_arr(arr, i - 1) + arr[i]


if __name__ == '__main__':
    a = [1, 2, 3, 4, 5, 6, 7]
    a_len = len(a) - 1

    print(sum_arr(a, a_len))
