#   https://leetcode.com/problems/island-perimeter/




from operator import ne
from typing import *


class Solution:
    def dfs(self, grid, position, seen):
        if position not in seen:
            seen.add(position)
            # print(position, self.perimeter(position, grid))
            self.result += self.perimeter(position, grid)
            
            for neighbour in self.direction(position, grid):
                if neighbour not in seen:
                    self.dfs(grid, neighbour, seen)
        
    def pos(self, grid):
        for row in range(len(grid)):
            for column in range(len(grid[0])):
                if grid[row][column] == 1:
                    return (row,column)
                    
    def direction(self, position, grid):
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

    def perimeter(self, position, grid):
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
        
        count = 0
        for r,c in moves:
            if r < 0 or c < 0:
                count += 1
            elif r >= rl or c >= cl:
                count += 1
            elif r >=0 and c >=0  and r <rl and c <cl and grid[r][c] == 0:
                count += 1
            
        return count
    
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        self.result = 0
        self.dfs(grid, self.pos(grid), set())
        return self.result 
                            
                    

                
                    
               


if __name__ == '__main__':
    obj = Solution()
    grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
    ans = obj.islandPerimeter(grid) 
    print(ans)