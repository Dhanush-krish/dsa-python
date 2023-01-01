#   https://leetcode.com/problems/word-pattern/description/

# TC => O(n)
# SC => O(n)
# where n is the max length


from typing import *


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        hmap = {}
        lookup = set()

        if len(s) != len(pattern): return False

        for idx, value in enumerate(pattern):
            if value not in hmap and s[idx] not in lookup:
                hmap[value] = s[idx]
                lookup.add(s[idx])
            elif hmap.get(value, "") != s[idx]:
                return False
        
        return True



if __name__ == "__main__":
    obj = Solution()
    pattern = "abba"
    s = "dog dog dog dog"
    ans = obj.wordPattern(pattern, s)
    print(ans)