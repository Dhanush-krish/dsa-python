#   https://leetcode.com/problems/maximum-product-of-three-numbers/





from typing import *


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        last3 = nums[-3]*nums[-2]*nums[-1]
        last1first2 = nums[-1]*nums[0]*nums[1]
        return max(last3, last1first2)


if __name__ == '__main__':
    obj = Solution()
    lis = [1,2,3,4]
    ans = obj.maximumProduct(lis)
    print(ans)