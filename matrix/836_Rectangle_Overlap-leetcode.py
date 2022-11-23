#   https://leetcode.com/problems/rectangle-overlap/

# TC => 
# SC => 


from typing import *


class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        x1,y1,x2,y2 = rec1
        a1,b1,a2,b2 = rec2
        if(((x1<a1<x2) and (y1<b1<y2)) or 
            ((x1<a2<x2) and (y1<b2<y2)) or 
            ((x1<a1<x2) and (y1<b2<y2)) or 
            ((x1<a2<x2) and (y1<b1<y2))):
            return True
        return False



if __name__ == "__main__":
    obj = Solution()
    rec1 = [0,0,1,1]
    rec2 = [2,2,3,3]
    ans = obj.isRectangleOverlap(rec1, rec2)
    print(ans)