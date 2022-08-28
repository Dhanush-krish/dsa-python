#   https://leetcode.com/explore/learn/card/array-and-string/201/introduction-to-array/1144/




from typing import *


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        left = 0
        for index, value in enumerate(nums):
            right = total - value - left
            if right == left :
                return index 
            left += value
            
        return -1


if __name__ == '__main__':
    obj = Solution()
    nums = [1,7,3,6,5,6]
    ans = obj.pivotIndex(nums)
    print(ans)
    
"""
Input: nums = [1,7,3,6,5,6]
Output: 3
Explanation:
The pivot index is 3.
Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
Right sum = nums[4] + nums[5] = 5 + 6 = 11
"""