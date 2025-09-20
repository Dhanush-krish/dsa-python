import heapq as hq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        stones = [-1 * x for x in stones]
        hq.heapify(stones)

        while(len(stones) > 1):
            val1 =  hq.heappop(stones)
            val2 =  hq.heappop(stones)

            if val1 != val2:
                hq.heappush(stones, val1 - val2)

        
        return -1 * stones[0] if len(stones) else 0