import heapq as hq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        for val in nums:
            hq.heappush(heap, val)

            if len(heap) > k:
                hq.heappop(heap)
        
        return hq.heappop(heap)

        

