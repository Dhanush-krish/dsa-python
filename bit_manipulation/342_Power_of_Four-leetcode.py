#   https://leetcode.com/problems/power-of-four/




from typing import *


##bit manipulation        
class Solution:
    def isPowerOfFour(self, n: int):
        
        if n <= 0:
            return False
            
        return ((not n&(n-1)) and (n.bit_length()&1))


if __name__ == '__main__':
    obj = Solution()
    ans = obj.isPowerOfFour(16)
    print(ans)