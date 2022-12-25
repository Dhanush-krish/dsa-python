#   https://leetcode.com/problems/minimum-falling-path-sum/

# TC => O(n*n)
# SC => O(n*n)
# where n is the number of rows in a square matrix


from typing import *



class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        ROW = COL = len(matrix)
        result = float("inf")
        dp = {}

        def find_min_sum(row, col, dp):
            if not (0 <= col < COL): return float("inf")
            if row == ROW - 1: return matrix[row][col]
            if (row,col) in dp: return dp[(row,col)]

            dp[(row, col)] =  min( matrix[row][col] + find_min_sum(row + 1, col - 1, dp),
                                    matrix[row][col] + find_min_sum(row + 1, col, dp),
                                    matrix[row][col] + find_min_sum(row + 1, col + 1, dp))
            
            return dp[(row,col)]
        
        for col in range(COL):
            result = min(result, find_min_sum(0, col, dp))
        
        # print(dp)

        return result 




# TC => O(n*n)
# SC => O(n)
# where n is the number of rows in a square matrix
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        ROW = COL = len(matrix)
        prev = matrix[0]

        for row in range(1, ROW):
            curr = []
            for col in range(COL):
                center = matrix[row][col] + prev[col]
                right = matrix[row][col] + prev[col-1] if col - 1 >= 0 else float("inf") 
                left = matrix[row][col] + prev[col+1] if col + 1 < COL else float("inf") 

                curr.append(min(right, center, left))
            prev = curr
        
        return min(prev)


if __name__ == "__main__":
    obj = Solution()
    matrix = [[2,1,3],[6,5,4],[7,8,9]]
    ans = obj.minFallingPathSum(matrix)
    print(ans)