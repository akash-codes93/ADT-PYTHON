def fact(n):
    if n==1:
        return 1
    return n*(n-1)

def sum_digits(n):
    last = n%10
    rem = n//10
    if rem == 0:
        return last
    else:
        return last + sum_digits(rem)


if __name__ == '__main__':
    # out = fact(5)
    # print(out)
    out = sum_digits(120)
    print(out)