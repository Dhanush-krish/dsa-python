#   https://leetcode.com/problems/find-peak-element/



# T.C => 
# S.C => 


from typing import *


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        left, right = 0, len(nums) - 1
        
        while(left < right):
            mid = left + (right - left)//2
            
            if(nums[mid] > nums[right]):
                right = mid
            else:
                left = mid + 1
        
        return (left, right)
        



if __name__ == '__main__':
    obj = Solution()
    nums = [1,2,3,1]
    ans = obj.findPeakElement(nums)
    print(ans)