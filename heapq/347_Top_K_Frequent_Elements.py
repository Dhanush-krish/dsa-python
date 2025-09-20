from collections import defaultdict
import heapq as hq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = defaultdict(int)

        for val in nums:
            hmap[val] += 1
        
        heap = []
        for key, value in hmap.items():
            hq.heappush(heap, (value, key))

            if len(heap) > k:
                hq.heappop(heap)
        
        result = []
        while(heap):
            result.insert(0, hq.heappop(heap)[1])

        return result

        