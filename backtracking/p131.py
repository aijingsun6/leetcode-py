from typing import List


class Solution:

    def dfs(self, s: str, start: int, end: int, dp: list[list[int]]) -> bool:

        if start == end:
            dp[start][end] = 1
            return True

        if start + 1 == end:
            if s[start] == s[end]:
                dp[start][end] = 1
                return True
            else:
                dp[start][end] = 2
                return False
        if dp[start][end] == 1:
            return True
        if dp[start][end] == 2:
            return False

        if self.dfs(s, start + 1, end - 1, dp=dp) and s[start] == s[end]:
            dp[start][end] = 1
            return True
        dp[start][end] = 2
        return False

    def partition(self, s: str) -> List[List[str]]:
        return []

    def backtrace(self, s: str, start: int, end: int, dp: list[list[int]], result: list[list[str]], acc:list[str]) -> None:
        if end == len(s)-1 and self.dfs(s, start, end, dp):
            acc.append(s[start:])
            result.append(list(acc))
            

