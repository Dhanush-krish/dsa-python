#   https://leetcode.com/problems/flood-fill/



from typing import *


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        seen = set()
        original_color = image[sr][sc]
        
        
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
            
            return [(r,c) for r,c in moves if r >=0 and c >=0  and r <rl and c <cl and grid[r][c] == original_color]
        
        def dfs(grid, pos, color, seen):
            if pos in seen: return 0
            seen.add(pos)
            grid[pos[0]][pos[1]] = color
            for neighbour in direction(pos, grid):
                if neighbour not in seen:
                    dfs(grid, neighbour, color, seen)
                    
        dfs(image, (sr,sc), newColor, seen)
        
        return image


if __name__ == '__main__':
    obj = Solution()
    image = [[1,1,1],[1,1,0],[1,0,1]]
    sr = 1
    sc = 1
    color = 2
    
    ans = obj.floodFill(image, sr, sc, color)
    print(ans)