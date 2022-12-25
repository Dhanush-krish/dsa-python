#https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/

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
                sell = dfs(idx+1, not isbuy) + prices[idx]
                dp[(idx, isbuy)] = max(sell, cooldown)
            
            return dp[(idx, isbuy)]
        
        dp = {}
        result = dfs(0, True)
        return result




if __name__ == "__main__":
    obj = Solution()
    prices = [7,1,5,3,6,4]
    ans = obj.maxProfit(prices)
    print(ans)