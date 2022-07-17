#   https://leetcode.com/problems/valid-anagram/




from typing import *

from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if(Counter(s) == Counter(t)):
            return True
        else:
            return False


if __name__ == '__main__':
    obj = Solution()
    s = "anagram"
    t = "nagaram"
    ans = obj.isAnagram(s, t)
    print(ans)
    
    
"""

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false


"""