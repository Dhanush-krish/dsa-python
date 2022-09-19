#   https://leetcode.com/problems/next-greater-element-i/

from typing import *


# class Solution:
#     def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
#         output = []
#         for val in nums1:
#             seen = False
#             for val2 in nums2:
#                 result = -1
#                 if seen and val2 > val:
#                     result = val2
#                     break
#                 if val == val2:
#                     seen = True

#             output.append(result)

#         return output


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        table = {}
        for i in nums2[::-1]:
            while stack and i > stack[-1]:
                stack.pop()
            table[i] = stack[-1] if stack else -1
            stack.append(i)
        return [table[i] for i in nums1]


if __name__ == "__main__":
    obj = Solution()
    nums1 = [10, 5]
    nums2 = [10, 1, 2, 5, 4, 6]
    ans = obj.nextGreaterElement(nums1, nums2)
    print(ans)


"""
Example 1:

Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
Output: [-1,3,-1]
Explanation: The next greater element for each value of nums1 is as follows:
- 4 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
- 1 is underlined in nums2 = [1,3,4,2]. The next greater element is 3.
- 2 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
Example 2:

Input: nums1 = [2,4], nums2 = [1,2,3,4]
Output: [3,-1]
Explanation: The next greater element for each value of nums1 is as follows:
- 2 is underlined in nums2 = [1,2,3,4]. The next greater element is 3.
- 4 is underlined in nums2 = [1,2,3,4]. There is no next greater element, so the answer is -1.
"""
