"""
inp: "3(a2(c)3(d))"
out: accdd daccdd daccdddd

"""

def repeat_string(s):
    stack = []

    nums = "0123456789"
    for i in s:
        if i != "]":
            stack.append(i)
        elif i == "]":
            temp_str = ""
            num = ""
            while stack and stack[-1] not in nums and stack[-1] != "[":
                temp_str = stack.pop() + temp_str

            if stack and stack[-1] == '[':
                stack.pop()

            while stack and stack[-1] in nums and stack[-1] != "[":
                num = stack.pop() + num

            if stack and stack[-1] == '[':
                stack.pop()

            if num:
                temp_str = int(num) * temp_str

            stack.append(temp_str)

        print(stack)

    out = ""
    while stack:
        out = stack.pop() + out

    return out


# print(repeat_string("3(a2(c)3(d))"))
# print(repeat_string("abcd"))
# print(repeat_string("3(a)2(d)"))
# "100[leetcode]"
# "3[z]2[2[y]pq4[2[jk]e1[f]]]ef"
print(repeat_string("3[z]2[2[y]pq4[2[jk]e1[f]]]ef"))







