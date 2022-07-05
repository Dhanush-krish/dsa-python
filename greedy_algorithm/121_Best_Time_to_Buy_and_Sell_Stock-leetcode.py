#   https://leetcode.com/problems/best-time-to-buy-and-sell-stock/




import sys
from typing import *


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        length = len(prices)
        if length <= 1:
            return 0
        buy = prices[0]
        sell = prices[0]
        profit = 0
        
        for index in range(len(prices)):
            if prices[index] < buy:
                buy = prices[index]
                sell = prices[index]
            elif prices[index] > sell:
                sell = prices[index]
                profit = max(profit, sell-buy)
                
        return profit


if __name__ == '__main__':
    obj = Solution()
    lis = [7,1,5,3,6,4]
    ans = obj.maxProfit(lis)
    print(ans)