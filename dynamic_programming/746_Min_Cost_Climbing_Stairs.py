class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
       n = len(cost)

       dp = [0] * (n + 1)

       for idx in range(2, n + 1):
            dp[idx] = min(cost[idx - 1] + dp[idx - 1], cost[idx - 2] + dp[idx - 2])

       return dp[-1] 