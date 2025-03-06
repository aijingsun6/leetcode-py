class P2588:
    def beautifulSubarrays(self, nums: list[int]) -> int:
        pre_sum: dict[int,int] = dict()
        pre_sum[0] = 1
        sum = 0
        result = 0
        for v in nums:
            sum = sum ^ v
            if sum in pre_sum:
                c = pre_sum[sum]
                result += c
                pre_sum[sum] = c + 1
            else:
                pre_sum[sum] = 1
        return result

import unittest


class TestSolution(unittest.TestCase):
    def test(self):
        s = P2588()
        nums = [4,3,1,2,4]
        r  = s.beautifulSubarrays(nums)
        self.assertEqual(2, r)
        nums = [1,10,4]
        r = s.beautifulSubarrays(nums)
        self.assertEqual(0, r)



if __name__ == '__main__':
    unittest.main()
