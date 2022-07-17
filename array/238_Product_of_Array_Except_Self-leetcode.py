#   https://leetcode.com/problems/product-of-array-except-self/




from typing import *


# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         prod = 1
#         for val in nums:
#             prod *= val
        
#         result = []
#         for val in nums:
#             result.append((prod//val))
        
#         return result


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        length = len(nums) 
        
        left_to_right = [1]*length
        right_to_left = [1]*length
        
        for index in range(1,length):
            left_to_right[index] = left_to_right[index-1] * nums[index-1]

        for index in range(length-2,-1,-1):
            right_to_left[index] = right_to_left[index+1] * nums[index+1]
        
        print(left_to_right, right_to_left)
            
        for index in range(length):
            right_to_left[index] = right_to_left[index] * left_to_right[index]
            
        return right_to_left
    
            
        


if __name__ == '__main__':
    obj = Solution()
    nums = [1,2,3,4]
    ans = obj.productExceptSelf(nums)
    print(ans)