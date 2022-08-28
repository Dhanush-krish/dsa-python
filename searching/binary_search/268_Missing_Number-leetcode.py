#   https://leetcode.com/problems/missing-number/



from typing import *

#naive approach
# class Solution:
#     def missingNumber(self, nums: List[int]) -> int:
#         nums.sort()
        
#         for index,val in enumerate(nums):
#             if index != val:
#                 return index
#         return index+1

#binary search 

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        
        for index,val in enumerate(nums):
            if index != val:

if __name__ == '__main__':
    obj = Solution()
    nums = [3,0,1]
    ans = obj.missingNumber(nums)
    print(ans)