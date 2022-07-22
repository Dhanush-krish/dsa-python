#   https://leetcode.com/problems/3sum/




from typing import *


class Solution:
    def threeSum(self, nums):
        
        nums.sort()
        result = []
        
        for index,element in enumerate(nums):
            
            if index > 0 and element == nums[index-1]:
                continue
            
            left = index + 1
            right = len(nums)-1
            
            while (left < right):
                temp = nums[left] + nums[right]
                if(temp + element) > 0:
                    right -= 1
                elif (temp + element) < 0:
                    left += 1
                else:
                    result.append([element, nums[left], nums[right]])
                    while (left < right and nums[left] == nums[left+1]):
                        left += 1
                    left  += 1
                
        return result
                    
            


if __name__ == '__main__':
    obj = Solution()
    nums = [-1,0,1,0]
    ans = obj.threeSum(nums)
    print(ans)