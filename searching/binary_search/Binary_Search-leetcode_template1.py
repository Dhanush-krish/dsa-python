#   https://leetcode.com/problems/binary-search/




from typing import *

#Iterative
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        
        while(left <= right):
            mid = left+(right-left)//2
            
            if nums[mid] == target:
                return mid
            elif(nums[mid] < target):
                left = mid + 1
            else:
                right = mid - 1
        
        return -1


##Recursive
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def binary(arr, target, left, right):
            if left > right: return -1
            
            mid = left + (right-left)//2
            if arr[mid] == target:
                return mid
            elif target < arr[mid]: 
                return binary(arr, target, left, mid-1)
            else:
                return binary(arr, target, mid+1, right)
        
        return binary(nums, target, 0, len(nums)-1)
            


if __name__ == '__main__':
    obj = Solution()
    nums = [-1,0,3,5,9,12]
    target = 13
    ans = obj.search(nums, target)
    print(ans)