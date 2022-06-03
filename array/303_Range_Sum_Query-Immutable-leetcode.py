#   https://leetcode.com/problems/range-sum-query-immutable/

from typing import *

class NumArray:

    def __init__(self, nums: List[int]):
        self.arr = nums
        

    def sumRange(self, left: int, right: int) -> int:
        
        total = 0
        for index in range(left, right+1):
            total += self.arr[index]

        return total
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)


if __name__ == '__main__':
    nums = [-2, 0, 3, -5, 2, -1]
    obj = NumArray(nums)
    ans = obj.sumRange(2,5)
    print(ans)