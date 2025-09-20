from collections import defaultdict
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        graph = defaultdict(list)

        for u,v,w in times:
            graph[u].append((v, w))
        
        dist = [float("inf")] * (n + 1)
        prev = [None] * (n + 1)

        dist[k] = 0
        heap = [(0, k)]

        while(heap):

            w, n = heapq.heappop(heap)

            if w > dist[n]:
                continue
            
            for nbr, nw in graph[n]:
                if dist[n] + nw  < dist[nbr]:
                    dist[nbr] = dist[n] + nw
                    prev[nbr] = n
                    heapq.heappush(heap, (dist[nbr], nbr))

        result = max(dist[1:])
        return result if result != float("inf") else -1     