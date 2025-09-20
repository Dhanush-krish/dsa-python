import heapq as hq
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:

        heap = []

        for r in range(len(mat)):
            hq.heappush(heap, (sum(mat[r]), r))
        
        result = []
        while(k):
            k -= 1
            result.append(hq.heappop(heap)[1])
        
        return result
        