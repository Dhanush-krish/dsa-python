#   https://leetcode.com/problems/toeplitz-matrix/

# TC => O(N*M)
# SC => O(1)
# where N, M is the number of rows and column in matrix


from typing import *


class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        ROW,COL = len(matrix), len(matrix[0])

        for r in range(1, ROW):
            for c in range(1, COL):
                if matrix[r - 1][c - 1 ] != matrix[r][c]:
                    return False
        
        return True






if __name__ == "__main__":
    obj = Solution()
    matrix = [[1,2],[2,2]]
    ans = obj.isToeplitzMatrix(matrix)
    print(ans)