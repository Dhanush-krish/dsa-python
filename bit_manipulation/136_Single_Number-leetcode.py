#   https://leetcode.com/problems/single-number/


from typing import *


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        distinct = 0
        for val in nums:
            distinct ^= val
            
        return distinct


if __name__ == '__main__':
    obj = Solution()
    nums = [4,1,2,1,2]
    ans = obj.singleNumber(nums)
    print(ans)
    
    
"""
Example 1:

Input: nums = [2,2,1]
Output: 1
Example 2:

Input: nums = [4,1,2,1,2]
Output: 4
Example 3:

Input: nums = [1]
Output: 1
"""