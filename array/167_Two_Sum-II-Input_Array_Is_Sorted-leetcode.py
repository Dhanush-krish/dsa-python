#   https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/


from typing import *


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lp = 0
        rp = len(numbers)-1
        
        while(lp < rp):
            temp_sum = numbers[rp]+numbers[lp]
            if temp_sum > target:
                rp -= 1
            elif temp_sum < target:
                lp += 1
            else:
                return [lp+1, rp+1]
                


if __name__ == '__main__':
    obj = Solution()
    lis = [2,7,11,15]
    target = 22
    ans = obj.twoSum(lis,target)
    print(ans)