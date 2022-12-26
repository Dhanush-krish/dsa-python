#   https://leetcode.com/problems/jump-game/

# TC => O(n)
# SC => O(1)
# where n is the length of the array


from typing import *


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        LEN = len(nums)
        dest = LEN - 1

        for curr in range(LEN-2, -1, -1):
            if nums[curr] >= (dest - curr):
                dest = curr
        
        return dest == 0


if __name__ == "__main__":
    obj = Solution()
    nums = [3,2,1,0,4]
    ans = obj.canJump(nums)
    print(ans)