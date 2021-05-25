"""
Find all binary strings that can be formed from a wildcard pattern
1?11?00?1?

1011000010
1011000011
1011000110
1011000111
1011100010
1011100011
1011100110
1011100111
1111000010
1111000011
1111000110
1111000111
1111100010
1111100011
1111100110
1111100111

"""


class Solution:

    def binary(self, string, p, output):

        if p == len(string):
            # print(output)
            print(''.join(output))
            return

        if string[p] == '?':
            for i in ['0', '1']:
                output.append(i)
                self.binary(string, p + 1, output)
                output.pop()

        else:
            output.append(string[p])
            self.binary(string, p + 1, output)
            output.pop()

    def driver(self, string):
        p = 0
        output = []
        self.binary(string, 0, output)


Solution().driver('1?11?00?1?')
