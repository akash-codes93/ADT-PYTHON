nums = [-2, -3, 4, -1, -2, 1, 5, 3, -2, -9, 19]

meh = 0
msf = float('-inf')
_start = 0
start = 0
end = 0

for i in range(0, len(nums)):

    prev_meh = meh

    meh += nums[i]

    if meh < nums[i]:
        meh = nums[i]
        _start = i

    if msf < meh:
        msf = meh
        start = _start

    if prev_meh > meh:
        end = i - 1

if end < start:
    end = start

print("msf:", msf)

print("start: ", start)
print("end : ", end)
