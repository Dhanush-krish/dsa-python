#   https://leetcode.com/problems/isomorphic-strings/




from collections import defaultdict
from typing import *


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        lookup_s = defaultdict(list)
        lookup_t = defaultdict(list)
        
        for index, value in enumerate(s):
            lookup_s[value].append(index)
        for index, value in enumerate(t):
            lookup_t[value].append(index)

        
        if len(lookup_s) != len(lookup_t):
            return False
        
        for map1,map2 in zip(lookup_s, lookup_t):
            if (lookup_s[map1] != lookup_t[map2]):
                return False
        
        return True

if __name__ == '__main__':
    obj = Solution()
    str_1 = "foo"
    str_2 = "bar"
    ans = obj.isIsomorphic(str_1, str_2)
    print(ans)
    
    
"""
Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true
"""