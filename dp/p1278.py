class Solution:
    src: str
    n: int
    ch_dp: list[list[int]]  # ch_dp[start][end] ch_size

    def change(self, s: str, start: int, end: int) -> int:
        acc = 0
        while start < end:
            if s[start] != s[end]:
                acc += 1
            start += 1
            end -= 1
        return acc

    def calc_ch_dp(self):
        n = self.n
        self.ch_dp = []
        for i in range(n):
            self.ch_dp.append([0] * (n + 1))
        for size in range(1, n + 1):
            for start in range(0, n + 1 - size):
                end = start + size
                if size == 1:
                    self.ch_dp[start][end] = 0
                elif size == 2:
                    if self.src[start] == self.src[end - 1]:
                        self.ch_dp[start][end] = 0
                    else:
                        self.ch_dp[start][end] = 1
                else:
                    if self.src[start] == self.src[end - 1]:
                        self.ch_dp[start][end] = self.ch_dp[start + 1][end - 1]
                    else:
                        self.ch_dp[start][end] = self.ch_dp[start + 1][end - 1] + 1


    def partition(self, k: int) -> int:
        dp: list[list[int]] = []  # dp[i][j] == s[0:i] split j
        n = self.n
        m = min(n, k)
        for i in range(n+1):
            dp.append([0] * (m + 1))
        dp[1][1] = 0
        for i in range(2, n+1):
            # src[0:i]
            for j in range(1, min(i, m+1)):
                if j == 1:
                    dp[i][j] = self.ch_dp[0][i]
                    continue
                r = n
                for p in range(1, j):
                    r = min(r, self.ch_dp[i - p][i] + dp[i - p][j - 1])
                dp[i][j] = r
        return dp[n][m]


    def palindromePartition(self, s: str, k: int) -> int:
        n = len(s)
        if k == 1:
            return self.change(s, 0, n - 1)
        if k == len(s):
            return 0
        self.src = s
        self.n = n
        self.calc_ch_dp()
        return self.partition(k)


import unittest


class TestSolution(unittest.TestCase):

    def test(self):
        sol = Solution()
        s = "abc"
        k = 2
        r = sol.palindromePartition(s,k)
        self.assertEqual(1, r)

        s = "aabbc"
        k = 3
        r = sol.palindromePartition(s, k)
        self.assertEqual(0, r)


if __name__ == '__main__':
    unittest.main()
