#   https://leetcode.com/problems/number-of-1-bits/





from typing import *


class Solution:
    def hammingWeight(self, n: int) -> int:
        
        no_bits = 0
        
        while (n):
            no_bits += (n&1)
            n >>= 1
        
        return no_bits
    


if __name__ == '__main__':
    obj = Solution()
    nums = 11
    ans = obj.hammingWeight(nums)
    print(ans)