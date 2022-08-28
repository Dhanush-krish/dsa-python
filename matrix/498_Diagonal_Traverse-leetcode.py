#   https://leetcode.com/problems/diagonal-traverse/




from typing import *




class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        ROW, COL = len(mat), len(mat[0])
        times = 1
        
        # for row in range(ROW):
        #     col = 0
        #     for r1 in range(row, -1, -1):
        #         if times %2 == 1:
        #             print((r1, col), end= "")
        #         else:
        #             print((col, r1), end= "")
        #         col += 1
        #     times += 1
        #     print()
        
        for col in range(1,COL):
            col1 = 0
            for r1 in range(2, -2+col, -1):
                if times %2 == 0:
                    print((r1, col+col1), end= "")
                else:
                    print((col+col1, r1), end= "")
                col1 += 1
            times += 1
            print()



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