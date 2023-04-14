def check_sub_continuous(s1, s2, i, j):
    # stopping criteria 

    if i >= len(s1):
        return True

    if j >= len(s2):
        return False

    i = i + 1 if s1[i] == s2[j] else 0
    j = j + 1
    return check_sub_continuous(s1, s2, i, j)


def check_sub(s1, s2, i, j):
    if i >= len(s1):
        return True

    if j >= len(s2):
        return False

    var = 1 if s1[i] == s2[j] else 0

    i = i + var
    j = j + 1
    return check_sub(s1, s2, i, j)


def is_subsequence(s1: str, s2: str):
    i, j = 0, 0
    # return check_sub_continuous(s1, s2, i, j)
    return check_sub(s1, s2, i, j)


# leap of faith
def check_if_substring(sub, full):
    def looper(i, j):

        if len(sub) == j:
            return True

        if len(full) == i:
            return False

        if sub[j] == full[i]:
            return looper(i + 1, j + 1)
        else:
            return looper(i + 1, 0)

    return looper(0, 0)



def check_if_substring2(sub, full):
    def looper(i, j):

        if len(sub) == j:
            return True

        if len(full) == i:
            return False

        if sub[j] == full[i]:
            return looper(i + 1, j + 1)
        else:
            return False

    for s in range(len(full)):
        if looper(s, 0):
            return True

    return False


if __name__ == '__main__':
    # print(is_subsequence("he", "then"))
    import time
    start = time.time()
    print(check_if_substring("hetp", "ththetpththe"))
    end_time = time.time()
    p = end_time - start
    print(p)
    print(check_if_substring2("hetp", "ththetpththe"))
    q = time.time() - end_time
    print(q)
    print(p>q)

