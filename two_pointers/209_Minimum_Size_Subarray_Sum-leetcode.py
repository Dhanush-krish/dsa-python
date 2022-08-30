#   https://leetcode.com/problems/minimum-size-subarray-sum/




from typing import *


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        adder, left = 0, 0
        result = float("inf")
        for right in range(len(nums)):
            adder += nums[right]
            
            while(adder >= target):
                result = min(result, right-left+1)
                adder -= nums[left]
                left += 1
            
        return 0 if result == float("inf") else result


if __name__ == '__main__':
    obj = Solution()
    target = 11
    nums = [1,1,1,1,1,1,1,1]
    ans = obj.minSubArrayLen(target, nums)
    print(ans)  


"""
Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1
Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
"""