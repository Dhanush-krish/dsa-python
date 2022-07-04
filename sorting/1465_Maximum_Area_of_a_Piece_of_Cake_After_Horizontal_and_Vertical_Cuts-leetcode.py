#   https://leetcode.com/problems/maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts/




from typing import *


class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.sort()
        verticalCuts.sort()
        
        lengths = [horizontalCuts[index]-horizontalCuts[index-1] for index in range(1, len(horizontalCuts))]
        lengths.extend([horizontalCuts[0], h-horizontalCuts[-1]])
        heights = [verticalCuts[index]-verticalCuts[index-1] for index in range(1, len(verticalCuts))]
        heights.extend([verticalCuts[0], w-verticalCuts[-1]])
        length = max(lengths)
        height = max(heights)
        
        return (length*height)%(10**9+7)


if __name__ == '__main__':
    obj = Solution()
    h = 5
    w = 4
    horizontalCuts = [3]
    verticalCuts = [3]
    ans = obj.maxArea(h, w, horizontalCuts, verticalCuts)
    print(ans)
    
"""
Input: h = 5, w = 4, horizontalCuts = [3,1], verticalCuts = [1]
Output: 6
Explanation: The figure above represents the given rectangular cake. Red lines are the horizontal and vertical cuts. After you cut the cake, the green and yellow pieces of cake have the maximum area.
Example 3:

Input: h = 5, w = 4, horizontalCuts = [3], verticalCuts = [3]
Output: 9
"""