#   https://leetcode.com/problems/container-with-most-water/




from typing import *
import sys

# class Solution:
#     def maxArea(self, height: List[int]) -> int:
#         result = -sys.maxsize
#         for left, element in enumerate(height):
#             for right in range(left+1, len(height)):
#                 result = max(result, (right-left)*min(element, height[right]))
#         return result   


class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        result = 0
        left,right = 0, len(height)-1
        
        while(left < right):
            area = (right-left)*min(height[left], height[right])
            result = max(result, area)
            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return result
        

if __name__ == '__main__':
    obj = Solution()
    # height = [1,8,6,2,5,4,8,3,7]
    height = [1,1]
    ans = obj.maxArea(height)
    print(ans)