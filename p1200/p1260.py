from typing import List
class P1260:
    def __init__(self):
        pass

    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        row = len(grid)
        col = len(grid[0])
        size = row * col
        offset = k % size
        if offset == 0:
            return grid

        data = []
        for i in range(row):
            for j in range(col):
                data.append(grid[i][j])

        res = []
        for i in range(row):
            line = []
            for j in range(col):
                idx = i * col + j - offset
                v = data[idx % size]
                line.append(v)
            res.append(line)
        return res

import unittest
class P1260Test(unittest.TestCase):
    def test(self):
        grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        k = 1
        p = P1260()
        res = p.shiftGrid(grid,k)
        e = [[9,1,2],[3,4,5],[6,7,8]]
        self.assertEqual(e, res)

    def test_2(self):
        grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]]
        k = 4
        p = P1260()
        res = p.shiftGrid(grid, k)
        e = [[12,0,21,13],[3,8,1,9],[19,7,2,5],[4,6,11,10]]
        self.assertEqual(e, res)

    def test_3(self):
        grid = [[1,2,3],[4,5,6],[7,8,9]]
        k = 9
        p = P1260()
        res = p.shiftGrid(grid, k)
        e = [[1,2,3],[4,5,6],[7,8,9]]
        self.assertEqual(e, res)

    def test_4(self):
        grid = [[1],[2],[3],[4],[7],[6],[5]]
        k = 23
        p = P1260()
        res = p.shiftGrid(grid, k)
        e = [[6],[5],[1],[2],[3],[4],[7]]
        self.assertEqual(e, res)

if __name__ == '__main__':
    unittest.main()