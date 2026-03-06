class P1784:
    def checkOnesSegment(self, s: str) -> bool:
        for i in range(1, len(s)):
            c = s[i]
            if c == '1' and s[i-1] == '0':
                return False
        return True