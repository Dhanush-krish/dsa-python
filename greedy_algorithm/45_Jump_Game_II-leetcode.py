#   https://leetcode.com/problems/jump-game-ii/




from typing import *


class Solution:
    def jump(self, nums: List[int]) -> int:
        
        result = 0
        left = right = 0
        length = len(nums)
        
        while (right <= length-1):
            newRight = 0
            
            for index in range(left, right+1):
                newRight = max(newRight, index+nums[index])
            
            left = right + 1
            right = newRight
            result += 1
        
        return result


if __name__ == '__main__':
    obj = Solution()
    nums = [2,3,1,1,4]
    ans = obj.jump(nums)
    print(ans)