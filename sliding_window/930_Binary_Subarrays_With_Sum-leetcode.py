#   https://leetcode.com/problems/binary-subarrays-with-sum/




from typing import *


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        left, result = 0,0
        run_sum = 0
        
        for right in range(len(nums)):
            run_sum += nums[right]
            
            if run_sum == goal:
                result+= 1
                continue
            
            while run_sum >= goal:
                run_sum -= nums[left]
                if run_sum == goal:
                    result+= 1
                left += 1
                
        return result


if __name__ == '__main__':
    obj = Solution()
    nums = [0,0,0,0,0]
    goal = 0
    ans = obj.numSubarraysWithSum(nums, goal)
    print(ans)