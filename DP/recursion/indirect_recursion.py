n = 10


def odd(i):
    if i > n:
        exit(0)
    print(i + 1)

    even(i + 1)


def even(i):
    print(i - 1)

    odd(i + 1)


odd(1)
