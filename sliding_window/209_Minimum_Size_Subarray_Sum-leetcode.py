#   https://leetcode.com/problems/minimum-size-subarray-sum/





from typing import *


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left,run_sum = 0,0
        result = float("inf")
        
        for right in range(len(nums)):
            run_sum += nums[right]
            
            while(run_sum >= target):
                result = min(result, right-left+1)
                run_sum -= nums[left]
                left += 1
        
        return result
            
            


if __name__ == '__main__':
    obj = Solution()
    target = 7
    nums = [2,3,1,2,4,3]
    ans = obj.minSubArrayLen(target, nums)
    print(ans)