#   https://leetcode.com/problems/longest-palindrome-by-concatenating-two-letter-words/

# TC => O(n)
# SC => O(n)
# where n is the length of the input list


from typing import *


class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        result, middle = 0, 0
        hmap = {}
        same = {}

        for val in words:
            reverse = val[::-1]
            if val == reverse:
                same[val] = 1 + same.get(val, 0)
            elif val in hmap and hmap[val] > 0:
                hmap[val] -= 1
                result += 4
            else:
                hmap[reverse] = 1 + hmap.get(reverse, 0)
        
        odd_allowed = True

        for key, value in same.items():
            if value % 2 == 1 and odd_allowed:
                result += (value * 2)
                odd_allowed = False
            else:
                result += (value//2) * 4

        return result



if __name__ == "__main__":
    obj = Solution()
    words = ["dd","aa","bb","dd","aa","dd","bb","dd","aa","cc","bb","cc","dd","cc"]
    ans = obj.longestPalindrome(words)
    print(ans)