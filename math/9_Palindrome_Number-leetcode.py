#   https://leetcode.com/problems/palindrome-number/



# T.C => 
# S.C => 


from typing import *


class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if x < 0: return False
        
        temp, digits = x, 0
        
        while(temp):
            digits += 1
            temp //= 10
        # print(digits)
        times = digits//2
        lsb, msb = 0, digits-1
        while(times):
            if ((x//(10**lsb)%10) != (x//(10**msb)%10)):
                print(times)
                return False
            lsb += 1
            msb -= 1
            times -= 1
        
        return True


if __name__ == '__main__':
    obj = Solution()
    ans = obj.isPalindrome(1221)
    print(ans)