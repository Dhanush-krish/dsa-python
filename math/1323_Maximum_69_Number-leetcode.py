#   https://leetcode.com/problems/maximum-69-number/

# TC => O(N)
# SC => O(1)
# where N is the number of digits 

from typing import *



class Solution:
    def maximum69Number (self, num: int) -> int:
        power, result = 4, 0
        swap = True

        while(power >= 0):
            digit = (num//(10**power))%10
            if swap and digit == 6:
                result += (9 * (10**power))
                swap = False
            else:
                result += (digit * (10**power))
            
            power -= 1
        
        return result


if __name__ == "__main__":
    obj = Solution()
    num = 9996
    ans = obj.maximum69Number(num)
    print(ans)