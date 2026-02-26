class P1404:
    def numSteps(self, s: str) -> int:
        v = int(s, base=2)
        step = 0
        while v > 1:
            if (v & 1) == 1:
                v = v +1
                step += 1
            else:
                v = v >> 1
                step += 1
        return step


import unittest


class P1404Test(unittest.TestCase):
    def test(self):
        s = '1101'
        p = P1404()
        r = p.numSteps(s)
        self.assertEqual(6, r)

        s = '10'
        r = p.numSteps(s)
        self.assertEqual(1, r)

        s = '1'
        r = p.numSteps(s)
        self.assertEqual(0, r)

