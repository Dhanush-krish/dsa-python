#   https://leetcode.com/problems/maximum-ice-cream-bars/

# TC => O(n*log(n))
# SC => O(1)
# where n is the length of costs


from typing import *


class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        result = 0

        for value in costs:
            if value <= coins:
                result += 1
                coins -= value
            else:
                break
        
        return result



if __name__ == "__main__":
    obj = Solution()
    costs = [1,3,2,4,1]
    coins = 7
    ans = obj.maxIceCream(costs, coins)
    print(ans)