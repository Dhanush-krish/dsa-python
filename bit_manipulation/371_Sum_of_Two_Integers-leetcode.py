#   https://leetcode.com/problems/sum-of-two-integers/




from typing import *


class Solution:
    
    def getSum(self, a: int, b: int) -> int:
        result,carry,pos = 0, 0, 0

        while(a or b):
            bit = (a&1)^(b&1)^carry
            carry = (a&1)&(b&1)
            result = result | (bit <<pos)            
            a >>= 1
            b >>= 1
            pos += 1
        
        if carry:
            result = result | (1<<pos)
        
        return result

if __name__ == '__main__':
    obj = Solution()
    a,b = 20,30
    ans = obj.getSum(a, b)
    print(ans)