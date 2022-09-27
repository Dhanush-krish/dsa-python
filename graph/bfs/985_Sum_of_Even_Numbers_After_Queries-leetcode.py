#   https://leetcode.com/problems/sum-of-even-numbers-after-queries/



# T.C => 
# S.C => 


from collections import deque
from typing import *


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        LEN = len(nums)
        queue = deque([(0,0)])
        
        while queue and queue[-1][0] < LEN:
            
            for _ in range(len(queue)):
                idx, val = queue.pop()
                queue.appendleft((idx + 1, val + nums[idx]))
                queue.appendleft((idx + 1, val + (-1*nums[idx])))
        
        result = 0
        for index, value in queue:
            if value == target:
                result += 1
        
        return result
            



if __name__ == '__main__':
    obj = Solution()
    nums = [1,1,1,1,1]
    target = 3
    ans = obj.findTargetSumWays(nums, target)
    print(ans)