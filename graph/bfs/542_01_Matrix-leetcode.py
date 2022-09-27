#   https://leetcode.com/problems/01-matrix/



# T.C => 
# S.C => 


from faulthandler import dump_traceback
from typing import *


class Solution:
    
    def directions(self, row, col, ROW, COL):
        possible = [(row - 1, col),
                    (row + 1, col),
                    (row, col - 1),
                    (row, col + 1),]
        
        return [(x, y) for x,y in possible if x >= 0 and x < ROW and y >= 0 and y < COL]
    
    
    def bfs(self, position , grid, ROW, COL, dp):
        
        queue = [position]
        nearest = 0
        while(queue):
            LEN = len(queue)
            for _ in range(LEN):
                r,c = queue.pop(0)
                
                if grid[r][c] == 0:
                    return nearest
                dp.add(str(r)+str(c))
                
                for r1, c1 in self.directions(r, c, ROW, COL):
                    if str(r1) + str(c1) not in dp:
                        queue.append((r1, c1))
                    
            nearest += 1
        
        return nearest
    
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        ROW, COL = len(mat), len(mat[0])
        dp = set()
        
        for row in range(ROW):
            for col in range(COL):
                if mat[row][col] == 1:
                    mat[row][col] = self.bfs((row, col), mat, ROW, COL, dp)
        
        return mat

if __name__ == '__main__':
    obj = Solution()
    mat = [[0,0,0],[0,1,0],[0,0,0]]
    ans = obj.updateMatrix(mat)
    print(ans)