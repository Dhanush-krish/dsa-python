#   https://leetcode.com/problems/power-of-two/




from typing import *


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        return n&n-1 == 0

if __name__ == '__main__':
    obj = Solution()
    ans = obj.isPowerOfTwo(16)
    print(ans)