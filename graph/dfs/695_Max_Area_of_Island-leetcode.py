#   https://leetcode.com/problems/max-area-of-island/




from typing import *


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        seen = set()
        row = len(grid)
        column = len(grid[0])
        
        
        def direction(position, grid):
            rl = len(grid)
            cl = len(grid[0])
            row = position[0]
            column = position[1]
            moves = [
                (row-1, column), #up
                (row+1, column), #down
                (row, column-1), #left
                (row, column+1) # right
            ]
            
            return [(r,c) for r,c in moves if r >=0 and c >=0  and r <rl and c <cl and grid[r][c] != 0]
        
        def dfs(grid, pos, seen):
            if pos in seen: return 0
            size = 1
            seen.add(pos)
            for neighbour in direction(pos, grid):
                if neighbour not in seen:
                    size += dfs(grid, neighbour, seen)
            
            return size
            
        for r in range(row):
            for c in range(column):
                if grid[r][c] == 0:
                    continue
                if (r,c) not in seen:
                    size = dfs(grid, (r,c), seen)
                    res = max(res,size)
            
        return res


if __name__ == '__main__':
    obj = Solution()
    grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
            [0,0,0,0,0,0,0,1,1,1,0,0,0],
            [0,1,1,0,1,0,0,0,0,0,0,0,0],
            [0,1,0,0,1,1,0,0,1,0,1,0,0],
            [0,1,0,0,1,1,0,0,1,1,1,0,0],
            [0,0,0,0,0,0,0,0,0,0,1,0,0],
            [0,0,0,0,0,0,0,1,1,1,0,0,0],
            [0,0,0,0,0,0,0,1,1,0,0,0,0]]
    
    ans = obj.maxAreaOfIsland(grid)
    print(ans)