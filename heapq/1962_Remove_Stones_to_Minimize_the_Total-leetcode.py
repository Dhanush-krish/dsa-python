#   https://leetcode.com/problems/remove-stones-to-minimize-the-total/



from typing import *
import heapq



class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:

        piles = [-1 * x for x in piles]
        heapq.heapify(piles)

        while(k):
            temp = -heapq.heappop(piles)
            temp = ((temp // 2) + (temp%2))
            heapq.heappush(piles, -temp)
            k-= 1

        
        return -sum(piles)


if __name__ == "__main__":
    obj = Solution()
    piles = [2695,9184,2908,3869,3779,391,2896,5328]
    k = 10
    ans = obj.minStoneSum(piles, k)
    print(ans)