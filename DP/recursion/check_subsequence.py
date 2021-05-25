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


if __name__ == '__main__':
    print(is_subsequence("he", "then"))
