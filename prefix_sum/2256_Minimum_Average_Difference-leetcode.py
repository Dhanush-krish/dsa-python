#   https://leetcode.com/problems/minimum-average-difference/

# TC => O(n)
# SC => O(1)
# where n is the length of the array

from typing import *


class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        n, total = len(nums), sum(nums)
        lsum = 0
        result = (10**5+1, 10**5+1)

        for index, val in enumerate(nums):
            lsum += val
            rsum = total - lsum

            if index != (n-1):
                diff = abs((lsum//(index+1)) - (rsum//(n-(index+1))))
            else:
                diff = abs((lsum//(index+1)))

            
            if diff < result[1]:
                result = (index, diff)

        
        return result[0]



if __name__ == "__main__":
    obj = Solution()
    nums = [2,5,3,9,5,3]
    ans = obj.minimumAverageDifference(nums)
    print(ans)