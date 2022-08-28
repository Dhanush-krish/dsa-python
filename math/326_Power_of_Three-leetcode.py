#   https://leetcode.com/problems/power-of-three/




from typing import *


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        
        while(n >= 3):
            if n%3 != 0:
                return False
            n //= 3
        
        return n == 1
    
    
if __name__ == '__main__':
    obj = Solution()
    ans = obj.isPowerOfThree(27)
    print(ans)