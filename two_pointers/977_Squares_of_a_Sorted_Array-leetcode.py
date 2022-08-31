#   https://leetcode.com/problems/squares-of-a-sorted-array/




from typing import *


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        length = len(nums)
        result = [0]*length
        index = length-1
        
        left, right = 0, length-1
        
        while(left < right):
            if abs(nums[right]) >= abs(nums[left]):
                result[index] =  nums[right]*nums[right]
                right -= 1
            else:
                result[index] =  nums[left]*nums[left]
                left += 1
            index -= 1
        
        result[index] = nums[left]*nums[left]
        
        return result
                
        


if __name__ == '__main__':
    obj = Solution()
    nums = [-4,-1,1,3,10]
    ans = obj.sortedSquares(nums)
    print(ans)
    
"""
Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
Example 2:

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]
"""