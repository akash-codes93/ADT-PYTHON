
num=25
pos =1
value = 0

l = 2
r = 4

while num:
    if l <= pos <=r:
        if not (num & 1):
            value += 2 ** (pos-1)
    else:
        if (num & 1):
            value += 2 ** (pos-1)

    pos += 1
    num >>=1

print(value)
