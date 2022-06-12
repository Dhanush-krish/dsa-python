#   https://leetcode.com/problems/longest-substring-without-repeating-characters/


from typing import *


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        start = 0
        lookup = set()
        
        for end,value in enumerate(s):
            if value not in lookup:
                lookup.add(value) 
        


if __name__ == '__main__':
    obj = Solution()
    ip_str = ""
    ans = obj.lengthOfLongestSubstring(ip_str)
    print(ans)