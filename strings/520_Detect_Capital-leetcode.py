#   https://leetcode.com/problems/detect-capital/

# TC => 
# SC => 
# 


from typing import *



class Solution:
    def detectCapitalUse(self, word: str) -> bool:

        return word.islower() or word.isupper() or word.istitle()
    


if __name__ == "__main__":
    obj = Solution()
    word = "Leetcode"
    ans = obj.detectCapitalUse(word)
    print(ans)