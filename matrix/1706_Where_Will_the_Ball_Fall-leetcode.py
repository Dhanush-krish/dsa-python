#   https://leetcode.com/problems/where-will-the-ball-fall/

# TC => O(N*M)
# SC => O(1)
# where N and M are the number of rows and columns of the matrix


from typing import *


class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        ROW, COL = len(grid), len(grid[0])
        result = [index for index in range(COL)]

        for row in range(ROW):
            for col in range(COL):
                if result[col] != -1:
                    if result[col] < COL and grid[row][result[col]] == 1 and result[col] + 1 < COL and grid[row][result[col] + 1] == 1:
                        result[col] = result[col] + 1
                    elif result[col] < COL and grid[row][result[col]] == -1 and result[col] - 1 >= 0 and grid[row][result[col] - 1] == -1:
                        result[col] = result[col] - 1
                    else:
                        result[col] = -1

        return result



if __name__ == "__main__":
    obj = Solution()
    grid = [[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1],[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1]]
    ans = obj.findBall(grid)
    print(ans)