"""
inp: "3(a2(c)3(d))"
out: accdd daccdd daccdddd

"""

def repeat_string(string):

    stack = []

    nums = "123456789"
    for i in string:
        if i != ")" and i != "(":
            stack.append(i)
        elif i == ")":
            temp_str = ""
            while stack and stack[-1] not in nums:
                temp_str = stack.pop() + temp_str

            num = stack.pop()
            temp_str = int(num) * temp_str

            stack.append(temp_str)

    out = ""
    while stack:
        out = stack.pop() + out

    return out


# print(repeat_string("3(a2(c)3(d))"))
# print(repeat_string("abcd"))
print(repeat_string("3(a)2(d)"))







