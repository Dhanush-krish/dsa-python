#   https://leetcode.com/problems/diagonal-traverse/




import re
from typing import *




class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        ROW, COL = len(mat), len(mat[0])
        up = True
        result, elements  = [], 0
        curr_row, curr_col = 0, 0
        
        while(elements != ROW*COL):
            
            if(up):
                
                while(curr_row >=0 and curr_col < COL):
                    result.append(mat[curr_row][curr_col])
                    elements += 1
                    
                    curr_row -= 1
                    curr_col += 1
                
                if curr_col == COL:
                    curr_row += 2
                    curr_col -= 1
                else:
                    curr_row += 1
                
                up = False
            
            else:
                
                while(curr_col >= 0 and curr_row < ROW):
                    result.append(mat[curr_row][curr_col])
                    elements += 1
                    
                    curr_col -= 1
                    curr_row += 1
                
                if curr_row == ROW:
                    curr_row  -= 1
                    curr_col += 2 
                else:
                    curr_col += 1
                    
                up = True
        
        return result



if __name__ == '__main__':
    obj = Solution()
    mat = [[1,2,3,10],
           [4,5,6,11],
           [7,8,9,12]]
    ans = obj.findDiagonalOrder(mat)
    print(ans)
    


"""
Input: mat = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,4,7,5,3,6,8,9]
Example 2:

Input: mat = [[1,2],[3,4]]
Output: [1,2,3,4]
"""