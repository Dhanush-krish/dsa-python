#   https://leetcode.com/problems/find-the-duplicate-number/


from typing import *


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        duplicate = 0
        for val in nums:
            duplicate ^= val
            print(duplicate)
            
        return duplicate
        


if __name__ == '__main__':
    obj = Solution()
    nums = [1,1,3,4,3,4,2,2,6]
    ans = obj.findDuplicate(nums)
    print(ans)