#   https://leetcode.com/problems/determine-if-string-halves-are-alike/


# TC => O(n)
# SC => O(1)
# where n is the length of the string


from typing import *


class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        l, r  = 0, len(s) - 1
        l_count  = r_count = 0
        vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}

        while(l < r):
            if s[l] in vowels:
                l_count += 1
            if s[r] in vowels:
                r_count += 1
            r -= 1
            l += 1

        return l_count == r_count




if __name__ == "__main__":
    obj = Solution()
    bs = "textbook"
    ans = obj.halvesAreAlike(bs)
    print(ans)