#   https://leetcode.com/problems/matrix-diagonal-sum/




from typing import *


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        length = len(mat)
        result = 0
        
        for index in range(length):
            if ((index,index) == (index,(length-1)-index)):
                result += mat[index][index]
            else:
                result += mat[index][index]
                result += mat[index][(length-1)-index]
                        
        return result 
            

if __name__ == '__main__':
    obj = Solution()
    mat = [[1,2,3],
            [4,5,6],
            [7,8,9]]
    ans = obj.diagonalSum(mat)
    print(ans)