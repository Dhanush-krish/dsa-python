#   https://leetcode.com/problems/duplicate-zeros/



# T.C => 
# S.C => 


from typing import *


# class Solution:
#     def duplicateZeros(self, arr: List[int]) -> None:
#         length = len(arr)
#         ptr1 = ptr2 = 0
        
#         while(ptr1 < length):
            
#             if (arr[ptr1] == 0):
#                 temp = 0
#                 for index in range(ptr1+1, length):
#                     temp1 = arr[index]
#                     arr[index] = temp
#                     temp = temp1
#                 ptr1 += 2
#             else:
#                 ptr1 += 1
        
#         print(arr)   


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        length = len(arr)
        left, right = 0, length-1
        zeros = 0
        
        while(left < right):
            if arr[left] == 0:
                zeros += 1
                right -= 1
            left += 1
            
        left, right = length-zeros-1, length-1
        print(left, right)
        while(left >= 0):
            
            if (arr[left] == 0):
                arr[right] = 0
                arr[right-1] = 0
                right -= 2
                left -= 1
            else:
                arr[right] = arr[left]
                right -= 1
                left -= 1
        print(arr)
            



if __name__ == '__main__':
    obj = Solution()
    arr = [8,4,5,0,0,0,0,7]
    ans = obj.duplicateZeros(arr)
    print(ans)