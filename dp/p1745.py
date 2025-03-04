class P1745:

    def checkPartitioning(self, s: str) -> bool:
        n = len(s)
        dp = []  # dp[i][j] [i,j)
        for i in range(n):
            dp.append([False] * (n + 1))
            dp[i][i+1] = True

        start_acc = []
        end_acc = []
        for size in range(1, n + 1):
            for start in range(0, n):
                end = start + size
                if end > n:
                    continue
                if size == 1:
                    dp[start][end] = True
                elif size == 2:
                    dp[start][end] = s[start] == s[end - 1]
                else:
                    dp[start][end] = s[start] == s[end - 1] and dp[start + 1][end - 1]
                if start == 0 and dp[start][end]:
                    start_acc.append(end)
                if end == n and dp[start][end]:
                    end_acc.append(start)

        for start in start_acc:
            for end in end_acc:
                if dp[start][end]:
                    return True
        return False

import unittest


class TestSolution(unittest.TestCase):
    def test(self):
        p1745 = P1745()
        s = "abcbdd"
        r = p1745.checkPartitioning(s)
        self.assertEqual(True,r)
        s = "bcbddxy"
        r = p1745.checkPartitioning(s)
        self.assertEqual(False, r)

if __name__ == '__main__':
    unittest.main()
