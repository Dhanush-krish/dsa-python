#   https://leetcode.com/problems/remove-duplicates-from-sorted-array/





from typing import *


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left, dup = 0, 0
        length = len(nums)
        
        for right in range(1, length):
            if nums[right] == nums[left]:
                dup += 1
            else:
                left += 1
                nums[left] = nums[right]

        return length-dup
        


if __name__ == '__main__':
    obj = Solution()
    nums = [0,0,1,1,1,2,2,3,3,4]
    ans = obj.removeDuplicates(nums)
    print(ans)
    
"""
Example 1:

Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
Example 2:

Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

"""