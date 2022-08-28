#   https://leetcode.com/problems/largest-number-at-least-twice-of-others/




from typing import *


class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        
        ans = -1
        maxi = float("-inf")
        for index, value in enumerate(nums):
            if value > maxi:
                maxi = value
                ans = index
        
        for val in nums:
            if val == maxi:
                continue
            elif not (val*2 <= maxi):
                return -1   
        
        return ans


if __name__ == '__main__':
    obj = Solution()
    nums = [1,2,3,4]
    ans = obj.dominantIndex(nums)
    print(ans)
    
"""
Example 1:

Input: nums = [3,6,1,0]
Output: 1
Explanation: 6 is the largest integer.
For every other number in the array x, 6 is at least twice as big as x.
The index of value 6 is 1, so we return 1.
Example 2:

Input: nums = [1,2,3,4]
Output: -1
Explanation: 4 is less than twice the value of 3, so we return -1.
"""