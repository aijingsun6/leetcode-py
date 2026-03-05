class P1758:

    def minOperations(self, s: str) -> int:
        size = len(s)
        c1 = self.diff_str(s, '10')
        c2 = self.diff_str(s,'01')
        return min([c1, c2])

    def diff_str(self, s, values='') -> int:
        c = 0
        for i in range(len(s)):
            expect = values[i % 2]
            if s[i] != expect:
                c += 1
        return c
