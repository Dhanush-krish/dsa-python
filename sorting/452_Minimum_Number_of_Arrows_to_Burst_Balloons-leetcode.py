#   https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

# TC => 
# SC => 
# 


from typing import *


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        count = 1
        print(points)

        l,r = points[0][0], points[0][1]

        for rl, rr in points:
            if l <= rl <= r:
                l = max(l, rl)
                r = min(r, rr)
            else:
                count += 1
                r = rr
                l = rl
        
        return count
        



if __name__ == "__main__":
    obj = Solution()
    points = [[1,2],[2,3],[3,4],[4,5]]
    ans = obj.findMinArrowShots(points)
    print(ans)