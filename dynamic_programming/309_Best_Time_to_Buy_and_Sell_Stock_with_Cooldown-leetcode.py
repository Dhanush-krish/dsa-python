#   https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/description/


# TC => O(n)
# SC => O(n)
# where n is the length of the array


from typing import *


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        LEN = len(prices)


        def dfs(idx, isbuy):

            if idx >= LEN: return 0
            if (idx, isbuy) in dp: return dp[(idx, isbuy)] 

            cooldown = dfs(idx+1, isbuy)

            if isbuy:
                buy = dfs(idx+1, not isbuy) - prices[idx]
                dp[(idx, isbuy)] = max(buy, cooldown)       
            else:
                sell = dfs(idx+2, not isbuy) + prices[idx]
                dp[(idx, isbuy)] = max(sell, cooldown)
            
            return dp[(idx, isbuy)]
        
        dp = {}
        return dfs(0, True)



if __name__ == "__main__":
    obj = Solution()
    prices = [1,2,3,0,2]
    ans = obj.maxProfit(prices)
    print(ans)