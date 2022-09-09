#   https://leetcode.com/problems/sqrtx/



# T.C => 
# S.C => 


from typing import *


class Solution:
    def mySqrt(self, x: int) -> int:
        
            
        left, right = 1, x
        
        while(left <= right):
            
            mid = left + (right-left)//2
            if(mid**2) == x:
                return mid
            elif(mid**2 < x):
                left = mid + 1
            else:
                right = mid - 1
        
        return right


if __name__ == '__main__':
    obj = Solution()
    x = 16
    ans = obj.mySqrt(x)
    print(ans)