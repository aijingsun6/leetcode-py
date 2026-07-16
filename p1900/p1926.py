from typing import List
class P1926:

    def check_exit(self, pos:tuple[int,int], entrance:tuple[int,int], row:int, col:int) -> bool:
        if pos == entrance:
            return False
        x,y = pos
        if x == 0 or x == (row-1):
            return True
        if y == 0 or y == (col-1):
            return True
        return False

    def expand(self,maze: List[List[str]], x, y, row, col,q:list[tuple[int,int]]):
        step_list = [ (0,1),(0,-1),(1,0),(-1,0)]
        for (dx,dy) in step_list:
            x2,y2 = x+dx,y+dy
            if 0 <= x2 < row and 0 <= y2 < col and maze[x2][y2] == '.':
                q.append((x2,y2))
                maze[x2][y2] = '-'

    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        row = len(maze)
        col = len(maze[0])
        start_row = entrance[0]
        start_col = entrance[1]
        entrance = (start_row, start_col)
        q:list[tuple[int,int]] = []
        res = 0
        q.append( entrance )
        maze[entrance[0]][entrance[1]] = '-'
        while len(q) > 0:
            q2 = []
            for x, y in q:
                if self.check_exit((x,y), entrance, row, col):
                    return res
                self.expand(maze, x,y,row,col,q2)

            res += 1
            if len(q2) ==0:
                break
            q = q2
        return -1

import unittest

class P1926Test(unittest.TestCase):
    def test(self):
        maze = [["+", "+", ".", "+"], [".", ".", ".", "+"], ["+", "+", "+", "."]]
        entrance = [1, 2]
        p = P1926()
        r = p.nearestExit(maze, entrance)
        e = 1
        self.assertEqual(e,r)

    def test_2(self):
        maze = [["+","+","+"],[".",".","."],["+","+","+"]]
        entrance = [1, 0]
        p = P1926()
        r = p.nearestExit(maze, entrance)
        e = 2
        self.assertEqual(e,r)

    def test_3(self):
        maze = [[".","+"]]
        entrance = [0,0]
        p = P1926()
        r = p.nearestExit(maze, entrance)
        e = -1
        self.assertEqual(e,r)


if __name__ == '__main__':
    unittest.main()