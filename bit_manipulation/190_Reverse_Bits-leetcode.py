#   https://leetcode.com/problems/reverse-bits/


from typing import *


class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for pos in range(32):
            last = (n>>pos)&1
            res = res | (last<<(31-pos))
        return res


if __name__ == '__main__':
    obj = Solution()
    ans = obj.reverseBits(1)
    print(ans, bin(ans))
