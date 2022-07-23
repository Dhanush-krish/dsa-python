#   https://leetcode.com/problems/number-of-islands/




from typing import *


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        count = 0
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
            
            return [(r,c) for r,c in moves if r >=0 and c >=0  and r <rl and c <cl and grid[r][c] != "0"]
        
        def dfs(grid, pos, seen):
            if pos not in seen:
                seen.add(pos)

                for neighbour in direction(pos, grid):
                    if neighbour not in seen:
                        dfs(grid, neighbour, seen)
            

        for r in range(row):
            for c in range(column):
                if grid[r][c] == '0':
                    continue
                if (r,c) not in seen:
                    count +=1
                    dfs(grid, (r,c), seen)
            
        return count

if __name__ == '__main__':
    obj = Solution()
    grid = [["1","1","0","0","0"],
            ["1","1","0","0","0"],
            ["0","0","1","0","0"],
            ["0","0","0","1","1"]]
    ans = obj.numIslands(grid)
    print(ans)