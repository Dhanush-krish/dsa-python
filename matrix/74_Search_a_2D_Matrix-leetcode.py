#   https://leetcode.com/problems/search-a-2d-matrix/




from typing import *


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)-1
        columns = len(matrix[0])
        
        for row in range(rows, -1, -1):
            if  matrix[row][0] <= target:
                for column in range(columns):
                    if matrix[row][column] == target:
                        return True
        
        
        return False


if __name__ == '__main__':
    obj = Solution()
    matrix = [[1,2,5,7],
              [10,11,16,20],
              [23,30,34,60]]
    target = 7
    ans = obj.searchMatrix(matrix, target)
    print(ans)