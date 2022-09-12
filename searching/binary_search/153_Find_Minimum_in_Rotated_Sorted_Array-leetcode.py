#   https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/


# T.C =>
# S.C =>


from typing import *


class Solution:
    def findMin(self, nums: List[int]) -> int:
        length = len(nums)

        if length == 1:
            return nums[0]

        left, right = 0, length - 1

        if nums[left] < nums[right]:
            return nums[0]

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            if nums[mid] < nums[mid - 1]:
                return nums[mid]

            if nums[mid] > nums[0]:
                left = mid + 1
            else:
                right = mid - 1


if __name__ == "__main__":
    obj = Solution()
    nums = [4, 5, 6, 7, 0, 1, 2]
    ans = obj.findMin(nums)
    print(ans)
