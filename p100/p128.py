from typing import List, Optional

class P128:
    """
    https://leetcode.cn/problems/longest-consecutive-sequence/description/

    给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。
    请你设计并实现时间复杂度为 O(n) 的算法解决此问题
    """

    def find_remove_cont(self,values:set[int])-> int:
        if len(values) == 0:
            return 0
        first = values.pop()
        cur = first
        res = 1
        while (cur-1) in values:
            res += 1
            values.remove(cur-1)
            cur = cur-1
        cur = first
        while (cur+1) in values:
            res += 1
            values.remove(cur+1)
            cur = cur + 1
        return res

    def longestConsecutive2(self, nums: List[int]) -> int:
        values = set()
        for n in nums:
            values.add(n)
        res = 0
        while len(values) > 0:
            res = max(res, self.find_remove_cont(values))
        return res

    def longestConsecutive(self, nums: List[int]) -> int:
        longest_streak = 0
        num_set = set(nums)

        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak


import unittest
class P128Test(unittest.TestCase):

    def test_01(self):
        nums = [100, 4, 200, 1, 3, 2]
        p128  = P128()
        r = p128.longestConsecutive(nums)
        e = 4
        self.assertEqual(e, r)

    def test_02(self):
        nums = [0,3,7,2,5,8,4,6,0,1]
        p128 = P128()
        r = p128.longestConsecutive(nums)
        e = 9
        self.assertEqual(e, r)


if __name__ == '__main__':
    unittest.main()