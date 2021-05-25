def is_sequence(arr, i):
    if i == 0:
        return True
    else:
        return is_sequence(arr, i - 1) and (arr[i] - arr[i - 1] == 1)


if __name__ == '__main__':
    a = [1]
    print(is_sequence(a, len(a)-1))
