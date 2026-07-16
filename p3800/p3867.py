class P3867:

    def gcd(self, x, y):
        if x < y:
            x,y = y,x

        while y > 0:
            tmp = y
            y = x % y
            x = tmp

        return x


    def gcdSum(self, nums: list[int]) -> int:
        prefixGcd: list[int] = []
        p_max = nums[0]
        for v in nums:
            p_max = max(p_max,v)
            prefixGcd.append(self.gcd(v, p_max))
        sorted_prefix_gcd = list(sorted(prefixGcd))
        res = 0
        i = 0
        j = len(sorted_prefix_gcd) -1
        while i < j:
            res+= self.gcd(sorted_prefix_gcd[i], sorted_prefix_gcd[j])
            i +=1
            j-=1
        return res


import unittest
class P3867Test(unittest.TestCase):
    def test(self):
        nums = [2,6,4]
        p = P3867()
        r = p.gcdSum(nums)
        e = 2
        self.assertEqual(e, r)

    def test_2(self):
        nums = [3,6,2,8]
        p = P3867()
        r = p.gcdSum(nums)
        e = 5
        self.assertEqual(e, r)

if __name__ == '__main__':
    unittest.main()





