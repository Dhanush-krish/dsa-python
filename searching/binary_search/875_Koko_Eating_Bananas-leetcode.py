#   https://leetcode.com/problems/koko-eating-bananas/




from typing import *
import math

## brute force
# class Solution:
#     def minEatingSpeed(self, piles: List[int], h: int) -> int:
#         k = 1
        
#         while(True):
            
#             time = 0
#             for val in piles:
#                 time  += math.ceil(val/k)
                
#             if time <= h:
#                 return k
            
#             k += 1



class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        r = max(piles)
        l = 1
        result = float("inf")
        
        while (l<=r):
            mid = l+(r-l)//2
            
            time = 0
            for val in piles:
                time  += math.ceil(val/mid)
            
            if time <= h:
                result = min(result, mid)
                r = mid-1
            else:
                l = mid + 1
        return result

if __name__ == '__main__':
    obj = Solution()
    piles = [30,11,23,4,20]
    h = 6
    ans = obj.minEatingSpeed(piles, h)
    print(ans)