#   https://leetcode.com/problems/move-zeroes/





from typing import *



class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        
        left = 0
        for right, val in enumerate(nums):
            
            if val != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1



if __name__ == '__main__':
    obj = Solution()
    nums = [0]
    ans = obj.moveZeroes(nums)
    print(ans)
    
    
"""
Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
"""