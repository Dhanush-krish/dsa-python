#   https://leetcode.com/problems/unique-paths/




from typing import *


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        def dfs(row, column):
            if row > m-1 or column > n-1: return 0
            if dp[row][column] != -1: return dp[row][column]
            if row == m-1 and  column == n-1: return 1
            
            dp[row][column] =  dfs(row+1, column) + dfs(row, column+1)
            
            return dp[row][column]
            
        dp = [[-1 for _ in range(n)] for _ in range(m)]
        return dfs(0, 0)


if __name__ == '__main__':
    obj = Solution()
    ans = obj.uniquePaths(3, 7)
    print(ans)