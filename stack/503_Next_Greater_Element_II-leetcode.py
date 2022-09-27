#   https://leetcode.com/problems/next-greater-element-ii/



# T.C => 
# S.C => 


from typing import *


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        LEN = len(nums)
        result = [0] * LEN
        stack = []
        
        for index in range(2 * LEN - 1, -1, -1):
            while(stack and stack[-1][1] <= nums[index % LEN]):
                stack.pop()
            
            result[index%LEN] = stack[-1][1] if stack else -1
            
            stack.append((index%LEN, nums[index%LEN]))
        
        return result


if __name__ == '__main__':
    obj = Solution()
    nums = [3, 8, 4, 1, 2]
    ans = obj.nextGreaterElements(nums)
    print(ans)