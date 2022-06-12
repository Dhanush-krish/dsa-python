#   https://leetcode.com/problems/move-zeroes/


from typing import *

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        
        size = len(nums)
        ip = 0
        rp = 1
        while(ip <= rp and rp < size):
            if nums[rp] == 0:
                ip = rp
                
            nums[ip],nums[rp] = nums[rp],nums[ip]
            rp +=1
            ip += 1
        
        return nums

if __name__ == '__main__':
    obj = Solution()
    # nums = [0,1,0,3,12]
    nums = [4,2,4,0,0,3,0,5,1,0]
    ans = obj.moveZeroes(nums)
    print(ans)