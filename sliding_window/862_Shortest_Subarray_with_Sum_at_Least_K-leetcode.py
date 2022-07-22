#   https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/




from typing import *


class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        left,run_sum = 0,0
        result = float("inf")
        
        for right in range(len(nums)):
            run_sum += nums[right]
            
            while(run_sum >= k or left < right):
                result = min(result, right-left+1)
                run_sum -= nums[left]
                left += 1
        
        return result


if __name__ == '__main__':
    obj = Solution()
    nums = [84,-37,32,40,95]
    k = 167
    ans = obj.shortestSubarray(nums, k)
    print(ans)