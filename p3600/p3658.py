class P3658:
    def gcdOfOddEvenSums(self, n: int) -> int:
        sum_odd = 0
        sum_even = 0
        c = 0
        idx = 0
        while c < n:
            sum_odd += (idx+1)
            sum_even += (idx+2)
            idx += 2
            c += 1

        def gcd(a, b):
            while b > 0:
                tmp = b
                b = a % b
                a = tmp
            return a
        return gcd(sum_even, sum_odd)

import unittest

class P3658Test(unittest.TestCase):

    def test(self):
        p = P3658()
        r = p.gcdOfOddEvenSums(4)
        e = 4
        self.assertEqual(e, r)
        r = p.gcdOfOddEvenSums(5)
        e = 5
        self.assertEqual(e, r)




if __name__ == '__main__':
    unittest.main()