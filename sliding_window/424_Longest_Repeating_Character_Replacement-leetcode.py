#   https://leetcode.com/problems/longest-repeating-character-replacement/




from typing import *
from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        result,left = 0,0
        lookup = defaultdict(int)
        
        for right in range(len(s)):
            lookup[s[right]] += 1
            
            while((right-left+1)-max(lookup.values())) > k:
                lookup[s[left]] -= 1
                left += 1
            
            result = max(result, right-left+1)
        
        return result
        



if __name__ == '__main__':
    obj = Solution()
    s = "AABABBA"
    k = 1
    ans = obj.characterReplacement(s, k)
    print(ans)