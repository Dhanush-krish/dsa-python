#   https://leetcode.com/problems/hamming-distance/




from typing import *


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xor = x^y
        result = 0
        while(xor):
            result += (xor&1)
            xor >>= 1
        return result


if __name__ == '__main__':
    obj = Solution()
    ans = obj.hammingDistance(1,4)
    print(ans)