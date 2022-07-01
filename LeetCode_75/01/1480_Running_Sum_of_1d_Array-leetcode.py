#   https://leetcode.com/problems/running-sum-of-1d-array/





from typing import *

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        
        for index in range(1,len(nums)):
            nums[index] = nums[index]+nums[index-1]
        
        return nums



if __name__ == '__main__':
    obj = Solution()
    lis = [1,2,3,4]
    ans = obj.runningSum(lis)
    print(ans)
    
    
"""
Example 1:

Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
Example 2:

Input: nums = [1,1,1,1,1]
Output: [1,2,3,4,5]
Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].
Example 3:

Input: nums = [3,1,2,10,1]
Output: [3,4,6,16,17]
"""    