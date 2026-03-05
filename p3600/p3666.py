class P3666:

    def minOperations(self, src: str, k: int) -> int:
        m = 0
        n = 0
        for e in src:
            if e == '1':
                m += 1
            else:
                n += 1
        r = 0
        r += int(n/k)
        n = n % k
        p = self.minOperations_2(m,n,k)
        if p < 0:
            return p
        return p + r


    def minOperations_2(self, m:int,n:int, k: int) -> int:
        target = (m + n, 0)

        if (m,n) == target:
            return 0
        s = set()
        q = []
        step = 0
        s.add((m, n))
        q.append((m, n))
        while len(q) > 0:
            q2 = q
            q = []

            for e in q2:
                (m,n) = e
                if (m,n) == target:
                    return step
                for i in range(k+1):
                    # i* 1, (k-i) * 0
                    if m >= i and n >= (k-i):
                        m2 = m -i + (k-i)
                        n2 = n - (k-i) + i
                        if (m2,n2) not in s:
                            s.add((m2,n2))
                            q.append((m2,n2))
            step += 1
        return -1

import unittest
class P3666Test(unittest.TestCase):
    def test(self):
        s = '110'
        k = 1
        p = P3666()
        r = p.minOperations(s,k)
        self.assertEqual(1, r)

    def test_2(self):
        s = '0101'
        k = 3
        p = P3666()
        r = p.minOperations(s, k)
        self.assertEqual(2, r)

    def test_3(self):
        s = '101'
        k = 2
        p = P3666()
        r = p.minOperations(s, k)
        self.assertEqual(-1, r)