#   https://leetcode.com/problems/single-threaded-cpu/


# TC => 
# SC => 
# 


from typing import *
from heapq import heappop, heappush
from collections import deque


class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:

        tasks = deque(sorted([(v[0], v[1], i) for i, v in enumerate(tasks)]))
        result, q, till = [], [], tasks[0][0]

        while(tasks or q):

            if not q and till < tasks[0][0] : till = tasks[0][0]

            while(tasks and tasks[0][0] <= till):
                etime, ptime, idx = tasks.popleft()
                heappush(q, (ptime, idx))

            pt, i = heappop(q)
            result.append(i)                
            till += pt

        return result



if __name__ == "__main__":
    obj = Solution()
    tasks = [[5,2],[7,2],[9,4],[6,3],[5,10],[1,1]]
    ans = obj.getOrder(tasks)
    print(ans)