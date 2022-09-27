#   https://leetcode.com/problems/next-greater-element-ii/


# TC =>
# SC =>


from typing import *


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        LEN = len(nums)
        output = [-1] * LEN
        stack = []

        for index, value in enumerate(nums):
            while stack and value > stack[-1][1]:
                idx, value = stack.pop()
                output[idx] = value
            stack.append((index, value))

        return output


if __name__ == "__main__":
    obj = Solution()
    nums = [1, 2, 3, 4, 3]
    ans = obj.nextGreaterElements(nums)
    print(ans)
