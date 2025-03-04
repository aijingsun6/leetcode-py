class Solution:
    src: str
    n: int
    dp: list[list[int]]
    result: int

    def dfs(self, start: int, end: int) -> bool:

        if start == end:
            self.dp[start][end] = 1
            return True

        if start + 1 == end:
            if self.src[start] == self.src[end]:
                self.dp[start][end] = 1
                return True
            else:
                self.dp[start][end] = 2
                return False
        if self.dp[start][end] == 1:
            return True
        if self.dp[start][end] == 2:
            return False

        if self.dfs(start + 1, end - 1) and self.src[start] == self.src[end]:
            self.dp[start][end] = 1
            return True
        self.dp[start][end] = 2
        return False

    def minCut(self, s: str) -> int:
        self.src = s
        self.n = len(s)
        self.dp = []
        for i in range(self.n):
            self.dp.append([0] * self.n)
        self.result = self.n
        return self.min_cnt(0, self.n)

    def min_cnt(self, start, end) -> int:
        if self.dfs(start, end - 1):
            return 0
        res = self.n
        for i in range(start + 1, end):
            a = self.min_cnt(start, i)
            b = self.min_cnt(i, end)
            res = min(res, a + b + 1)
        return res

import unittest
class TestSolution(unittest.TestCase):
    def test(self):
        sol = Solution()
        s = "aab"
        r = sol.minCut(s)
        exp = 1
        self.assertEqual(exp, r)

        s = "aaa"
        r = sol.minCut(s)
        exp = 0
        self.assertEqual(exp, r)

        s = "eegiicgaeadbcfacfhifdbiehbgejcaeggcgbahfcajfhjjdgj"
        r = sol.minCut(s)
        exp = 0
        self.assertEqual(exp, r)




if __name__ == '__main__':
    unittest.main()
