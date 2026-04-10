from typing import List

class P3740:

    def minimumDistance(self, nums: List[int]) -> int:
        value_map: dict[int, list[int]] = dict()
        res = 10000
        found = False
        for index, num  in enumerate(nums):
            if num not in value_map:
                value_map[num] = [index]
            else:
                value_map[num].append(index)
            if len(value_map[num]) > 2:
                s = len(value_map[num])
                dist = 2 * (value_map[num][s-1] - value_map[num][s-3])
                res = min(res, dist)
                found = True
        if found:
            return res
        return -1



import unittest
class P3740Test(unittest.TestCase):
    def test(self):
        nums = [1,2,1,1,3]
        p3740 = P3740()
        r = p3740.minimumDistance(nums)
        expect = 6
        self.assertEqual(expect, r)

        nums = [1,1,2,3,2,1,2]
        r = p3740.minimumDistance(nums)
        expect = 8
        self.assertEqual(expect, r)

        nums = [1]
        r = p3740.minimumDistance(nums)
        expect = -1
        self.assertEqual(expect, r)


