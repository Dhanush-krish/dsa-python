#   https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/



from typing import *


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers)-1
        
        while(left >=0 and right <= len(numbers)-1 ):
            temp = numbers[left]+numbers[right]
            if temp < target:
                left += 1
            elif temp > target:
                right -= 1
            else:
                return [left+1, right+1]


if __name__ == '__main__':
    obj = Solution()
    numbers = [2,7,11,15]
    target = 9
    ans = obj.twoSum(numbers, target)
    print(ans)