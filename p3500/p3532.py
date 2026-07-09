from typing import List

class P3532:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        parent: list[int] = []
        for i in range(n):
            parent.append(i)
        for i in range(1, n):
            if nums[i] - nums[i-1] <= maxDiff:
                parent[i] = parent[i-1]
        acc = []
        for item in queries:
            if parent[item[0]] == parent[item[1]]:
                acc.append(True)
            else:
                acc.append(False)
        return acc


import unittest
class P3532Test(unittest.TestCase):
    def test(self):
        n = 2
        nums = [1, 3]
        maxDiff = 1
        queries = [[0, 0], [0, 1]]
        p = P3532()
        r = p.pathExistenceQueries(n,nums,maxDiff,queries)
        e = [True,False]
        self.assertEqual(e,r)

    def test_2(self):
        n = 4
        nums = [2,5,6,8]
        maxDiff = 2
        queries = [[0,1],[0,2],[1,3],[2,3]]
        p = P3532()
        r = p.pathExistenceQueries(n, nums, maxDiff, queries)
        e = [False, False, True, True]
        self.assertEqual(e, r)

if __name__ == '__main__':
    unittest.main()