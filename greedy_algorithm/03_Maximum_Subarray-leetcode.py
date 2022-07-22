#   https://leetcode.com/problems/maximum-subarray/




from typing import *
import sys

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        local_max = 0 
        global_max = -sys.maxsize
        
        for val in nums:
            
            local_max += val
            
            if val > local_max:
                local_max = val
            
            if local_max > global_max:
                global_max = local_max
        
        return global_max

if __name__ == '__main__':
    obj = Solution()
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    ans = obj.maxSubArray(nums)
    print(ans)