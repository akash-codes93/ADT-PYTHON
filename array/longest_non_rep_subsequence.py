class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) <= 1:
            return len(s)

        a = {}
        longest = 0

        l = 0

        for r in range(0, len(s)):

            if a.get(s[r], None) is None:
                a[s[r]] = r

            else:

                # print(a)
                # to check if it is part of current window or not
                if a[s[r]] < l:
                    a[s[r]] = r

                else:

                    window = r - l
                    if window > longest:
                        # print(r, l)
                        longest = window

                    l = a[s[r]] + 1
                    a[s[r]] = r

        # print(r, l)
        if (r - l) + 1 > longest:
            return (r - l) + 1
        return longest