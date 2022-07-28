#   https://leetcode.com/problems/rotting-oranges/





from typing import *


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        ROW,COLUMN = len(grid), len(grid[0])
        fresh,time = 0,0
        queue = []
        
        
        def neighbours(r,c):
            all_neigh = [
                (r+1,c),
                (r-1,c),
                (r,c+1),
                (r,c-1)
            ]
            filtered = [(r,c) for r,c in all_neigh if 
                        (r>=0 and r <= ROW-1) and 
                        (c >= 0 and c <= COLUMN-1) 
                        and grid[r][c]==1
                        ]
            
            return filtered
        
        ## Traverse the grid
        for r in range(ROW):
            for c in range(COLUMN):
                if grid[r][c] == 2:
                    queue.append((r,c))
                elif grid[r][c] == 1:
                    fresh += 1
        
        while(queue and fresh):
            for _ in range(len(queue)):
                r,c = queue.pop(0)
                for neighbour in neighbours(r,c):
                    grid[neighbour[0]][neighbour[1]] = 2
                    fresh -= 1
                    queue.append(neighbour)
            time += 1
        return time if fresh == 0 else -1


if __name__ == '__main__':
    grid = [[2,1,1],
            [1,1,0],
            [0,1,1]]
    obj = Solution()
    ans = obj.orangesRotting(grid)
    print(ans)