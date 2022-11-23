#   https://leetcode.com/problems/perfect-squares/

# TC => 
# SC => 


from typing import *
from collections import deque
from math import sqrt


class Solution:
    def numSquares(self, n: int) -> int:
        neighbours = [x*x for x in range(1, int(sqrt(n))+1)]
        seen = set()
        queue = deque([(n, 1)])

        while(queue):
            num, steps = queue.pop()
            if num in neighbours:
                return steps
            
            for sq in neighbours:
                if sq >= num:
                    break
                if num - sq not in seen:
                    seen.add(num-sq)
                    queue.appendleft((num-sq, steps + 1))
        return steps


            



if __name__ == "__main__":
    obj = Solution()
    ans = obj.numSquares(13)
    print(ans)