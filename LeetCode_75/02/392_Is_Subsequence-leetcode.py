#   https://leetcode.com/problems/is-subsequence/




from typing import *


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        length = len(s)
        ptr = 0
        
        for element in t:
            if ptr == length:
                return True
            if element == s[ptr]:
                ptr += 1
        
        if ptr == length:
            return True
        
        return False


if __name__ == '__main__':
    obj = Solution()
    str_1 = "axc"
    str_2 = "ahbgdc"
    ans = obj.isSubsequence(str_1, str_2)
    print(ans)
    
"""
Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false
"""