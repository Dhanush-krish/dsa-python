'''
Choices → what moves/actions can I take? -> buy, sell

State → what information uniquely defines a subproblem? money

Transition → how do smaller states combine into the larger one? max(prev_start , currn + previous -1 )

Base Case → what’s the simplest answer I know immediately? at 1 max is 1, at 2 max is 1,2

Answer → what state(s) give me the final solution? 
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_profit = 0
        min_sofar = prices[0]

        for val in prices:
            max_profit = max(max_profit, val - min_sofar)
            min_sofar = min(min_sofar, val)
        
        return max_profit
        
                                                                                                                                                                                                       