def is_palindrome(s, i, j) -> bool:

    # if len(s) % 2 != 0:
    #     if i == j:
    #         return True
    # else:
    #     if (i+1) == j:
    #         return True

    if i == j or i > j:
        return True

    return is_palindrome(s, i+1, j-1) and s[i] == s[j]


if __name__ == '__main__':
    s = "tabpbat"
    str_len = len(s)-1
    print(is_palindrome(s, 0, str_len))
