#   https://leetcode.com/problems/flip-string-to-monotone-increasing/


# TC => 
# SC => 
# 


from typing import *


class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        count1 = result = 0

        for c in s:
            if c == "1":
                count1 += 1
            else:
                result = min(result+1, count1)

        return result



if __name__ == "__main__":
    obj = Solution()
    s = "0101100011"
    ans = obj.minFlipsMonoIncr(s)
    print(ans)