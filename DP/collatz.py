class Solution:
    mem = {1: 1}
    def collatz(self, N):

        if N in self.mem:
            return self.mem[N]

        if N % 2 == 0:
            return 1 + self.collatz(N/2)

        return 1 + self.collatz(3*N + 1)

    def collatzLength(self, N):
        # code here
        if N == 1:
            return 1

        max_till_now = 1
        for i in range(3, N + 1):
            val = self.collatz(i)
            # print(i, self.count[0])
            max_till_now = max(max_till_now, val)
            self.mem[i] = val

        # print(max_till_now)
        return max_till_now


Solution().collatzLength(3)



