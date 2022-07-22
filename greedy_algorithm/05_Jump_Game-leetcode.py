#   https://leetcode.com/problems/jump-game/




from typing import *


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        end = len(nums)
        
        for index in range(end-1,-1,-1):
            if index+nums[index] >= end:
                end = index
            
        return end == 0


if __name__ == '__main__':
    obj = Solution()
    nums = [2,3,1,1,4]
    ans = obj.canJump(nums)
    print(ans)