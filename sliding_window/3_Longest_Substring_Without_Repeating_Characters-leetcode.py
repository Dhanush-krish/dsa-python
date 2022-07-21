#   https://leetcode.com/problems/longest-substring-without-repeating-characters/


from typing import *


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left,result = 0,0
        lookup = set()
        
        for right in range(len(s)):
            
            
            while(s[right] in lookup):
                lookup.remove(s[left])
                left += 1
                
            lookup.add(s[right])
            
            result = max(result, right-left+1)
        
        return result         


if __name__ == '__main__':
    obj = Solution()
    ip_str = "abcabcbb"
    ans = obj.lengthOfLongestSubstring(ip_str)
    print(ans)