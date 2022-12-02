#   https://leetcode.com/problems/determine-if-two-strings-are-close/

# TC => nlog(n)
# SC => O(n)
# where n is the length of largest string


from typing import *
from collection import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        
        freq1 = Counter(word1)
        freq2 = Counter(word2)
        
        if freq1.keys() != freq2.keys():
            return False
        
        if sorted(freq1.values()) != sorted(freq2.values()):
            return False

        return True



if __name__ == "__main__":
    obj = Solution()
    word1 = "cabbba"
    word2 = "abbccc"
    ans = obj.closeStrings(word1, word2)
    print(ans)