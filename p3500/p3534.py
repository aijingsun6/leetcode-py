from typing import List
class P3534:

    def update_dist(self, n, dist: list[list[int]], nums:list[int], maxDiff:int, idx):
        # idx,idx_pre可联通
        for i in range(n):
            if i == idx:
                continue
            if abs(nums[i]-nums[idx]) <= maxDiff:
                dist[i][idx] = 1
                dist[idx][i] = 1
                continue

            value = -1
            for j in range(n):
                if abs(nums[j] - nums[idx]) <= maxDiff and abs(nums[j] - nums[i]) <= maxDiff:
                    if value < 0:
                        value = dist[i][j] + 1
                    else:
                        value = min(value,  dist[i][j] + 1)
            dist[i][idx] = value
            dist[idx][i] = value

    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        # dist[i,j] 表示 i,j之间的距离
        dist = []
        for i in range(n):
            line = [-1] * n
            line[i] = 0
            dist.append(line)
        # 按照value升序排列
        index: list[tuple[int,int]] = []
        for i in range(n):
            index.append((nums[i],i))
        index = list(sorted(index))
        for i in range(1,n):
            v,idx = index[i]
            v_pre,idx_pre = index[i-1]
            if v - v_pre > maxDiff:
               continue
            self.update_dist(n,dist,nums,maxDiff, idx)

        res = []
        for item in queries:
            v = dist[item[0]][item[1]]
            res.append(v)

        return res



import unittest
class P3534Test(unittest.TestCase):

    def test(self):
        n = 5
        nums = [1, 8, 3, 4, 2]
        maxDiff = 3
        queries = [[0, 3], [2, 4]]
        p = P3534()
        r = p.pathExistenceQueries(n,nums,maxDiff,queries)
        e = [1,1]
        self.assertEqual(e, r)


    def test_2(self):
        n = 5
        nums = [5,3,1,9,10]
        maxDiff = 2
        queries = [[0,1],[0,2],[2,3],[4,3]]
        p = P3534()
        r = p.pathExistenceQueries(n, nums, maxDiff, queries)
        e = [1, 2, -1, 1]
        self.assertEqual(e, r)

    def test_3(self):
        n = 3
        nums = [3,6,1]
        maxDiff = 1
        queries = [[0,0],[0,1],[1,2]]
        p = P3534()
        r = p.pathExistenceQueries(n, nums, maxDiff, queries)
        e = [0,-1,-1]
        self.assertEqual(e, r)

    def test_4(self):
        n = 2
        nums = [13,14]
        maxDiff = 2
        queries = [[1,1]]
        p = P3534()
        r = p.pathExistenceQueries(n, nums, maxDiff, queries)
        e = [0]
        self.assertEqual(e, r)

    def test_5(self):
        n = 4
        nums = [20,20,17,1]
        maxDiff = 18
        queries = [[1,3]]
        p = P3534()
        r = p.pathExistenceQueries(n, nums, maxDiff, queries)
        e = [2]
        self.assertEqual(e, r)

if __name__ == '__main__':
    unittest.main()
