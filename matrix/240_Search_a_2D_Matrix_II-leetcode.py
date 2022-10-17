#   https://leetcode.com/problems/search-a-2d-matrix-ii/

# TC => O(R + C)
# SC => O(1)


from typing import *


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROW, COL = len(matrix), len(matrix[0])
        r, c = 0, COL - 1

        while(r < ROW and c >= 0):

            pivot = matrix[r][c]
            if pivot == target:
                return True
            elif(pivot < target):
                r += 1
            else:
                c -= 1

        return False



if __name__ == "__main__":
    obj = Solution()
    matrix = [
        [1,4,7,11,15],
        [2,5,8,12,19],
        [3,6,9,16,22],
        [10,13,14,17,24],
        [18,21,23,26,30]
        ]
    target = 20
    ans = obj.searchMatrix(matrix, target)
    print(ans)