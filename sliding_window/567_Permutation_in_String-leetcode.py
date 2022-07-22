#   https://leetcode.com/problems/permutation-in-string/




import collections
from typing import *


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        lookup1 = collections.Counter(s1)
        length1 = len(s1)
        
        lookup2 = collections.defaultdict(int)
        left = 0
        
        for right in range(len(s2)):
            lookup2[s2[right]] += 1
            
            while(right-left+1) > len(s1):
                
                if lookup2[s2[left]] == 1:
                    del lookup2[s2[left]]
                else:
                    lookup2[s2[left]] -= 1
                left += 1
                
            if lookup1 == lookup2:
                return True
        
        return False


if __name__ == '__main__':
    obj = Solution()
    s1 = "ab"
    s2 = "eidaooo"
    ans = obj.checkInclusion(s1,s2)
    print(ans)