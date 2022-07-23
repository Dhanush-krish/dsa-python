#   https://leetcode.com/problems/binary-search/




from typing import *


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        
        while(left <= right):
            mid = left+(right-left)//2
            
            if nums[mid] > target:
                right = mid-1
            elif nums[mid] < target:
                left = mid+1
            else:
                return mid
        
        return -1


if __name__ == '__main__':
    obj = Solution()
    nums = [5]
    target = 5
    ans = obj.search(nums, target)
    print(ans)