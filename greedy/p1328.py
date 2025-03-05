class P1328:
    def breakPalindrome(self, palindrome: str) -> str:
        n = len(palindrome)
        if n < 2:
            return ""
        acc = list(palindrome)
        find = False
        for i in range(int(n/2)):
            if find:
                break
            elif acc[i] != 'a':
                acc[i] = 'a'
                find = True

        if not find:
            acc[n - 1] = 'b'
        return "".join(acc)

import unittest


class TestSolution(unittest.TestCase):
    def test(self):
        sol = P1328()
        s = "abccba"
        r = sol.breakPalindrome(s)
        self.assertEqual("aaccba",r)
        s = "a"
        r = sol.breakPalindrome(s)
        self.assertEqual("", r)

        s = "aa"
        r = sol.breakPalindrome(s)
        self.assertEqual("ab", r)

        s = "aba"
        r = sol.breakPalindrome(s)
        self.assertEqual("abb", r)


if __name__ == '__main__':
    unittest.main()