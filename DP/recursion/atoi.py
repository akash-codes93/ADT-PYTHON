def atoi(s, i):

    if i < 0:
        return 0
    else:
        return atoi(s, i-1) + int(s[i])*(10**(len(s)-1-i))


if __name__ == '__main__':
    string = "1234"
    integer = atoi(string, len(string)-1)

    print("Output: " + str(integer), " Type: " + str(type(integer)))
