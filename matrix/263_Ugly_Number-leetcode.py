#   https://leetcode.com/problems/ugly-number/

# TC => O(log(n))
# SC => O(n)


from typing import *

class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0 : return False

        def divisible(dividend, divisor):
            while(dividend % divisor == 0):
                dividend //= divisor
            return dividend

        for factor in [2, 3, 5]:
            n = divisible(n, factor)
        
        return n == 1




if __name__ == "__main__":
    obj = Solution()
    ans = obj.isUgly(14)
    print(ans)