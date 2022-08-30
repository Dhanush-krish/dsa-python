#   https://leetcode.com/problems/max-consecutive-ones/





from typing import *



class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        left = 0
        result = 0
        
        for right in range(len(nums)):
            
            if nums[right] == 0:
                left = right + 1
            
            result = max(result, right-left+1)
        
        return result


if __name__ == '__main__':
    obj = Solution()
    nums = [0, 0, 0, 1]
    ans = obj.findMaxConsecutiveOnes(nums)
    print(ans)
    

"""
Example 1:

Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
Example 2:

Input: nums = [1,0,1,1,0,1]
Output: 2
"""