#   https://leetcode.com/problems/sort-colors/




from typing import *


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        memory = [0, 0, 0]
        for val in nums:
            memory[val]  += 1
        
        for index in range(len(nums)):
            if memory[0]:
                nums[index] = 0
                memory[0] -= 1
            elif memory[1]:
                nums[index] = 1
                memory[1] -= 1
            else:
                nums[index] = 2
                memory[2] -= 1
                
        return nums
    


if __name__ == '__main__':
    obj = Solution()
    nums = [2,0,2,1,1,0]
    ans = obj.sortColors(nums)
    print(ans)