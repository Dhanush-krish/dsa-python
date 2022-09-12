#   https://leetcode.com/problems/find-peak-element/


# T.C =>
# S.C =>


from typing import *


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        left, right = 0, len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2

            if nums[mid] > nums[mid + 1]:
                right = mid
            else:
                left = mid + 1

        return left


if __name__ == "__main__":
    obj = Solution()
    nums = [1, 2, 1, 3, 5, 6, 4]
    ans = obj.findPeakElement(nums)
    print(ans)
