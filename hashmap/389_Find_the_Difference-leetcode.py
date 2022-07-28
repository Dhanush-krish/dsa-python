#   https://leetcode.com/problems/find-the-difference/





from typing import *
import collections


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        hmap1 = collections.Counter(s)
        hmap2 = collections.Counter(t)
        
        result = hmap2-hmap1
        return list(result.keys())[0]


if __name__ == '__main__':
    obj = Solution()
    s = "abcd"
    t = "abcde"
    ans = obj.findTheDifference(s,t)
    print(ans)