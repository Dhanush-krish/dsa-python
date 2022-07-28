#   https://leetcode.com/problems/number-complement/




from typing import *


class Solution:
    def findComplement(self, num: int) -> int:
        result = 0
        while(num):
            result = result<<(num&1)^1| (num&1)^1
            num>>=1
        return result

if __name__ == '__main__':
    obj = Solution()
    ans = obj.findComplement(4)
    print(ans)