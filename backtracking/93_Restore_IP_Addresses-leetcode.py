#   https://leetcode.com/problems/restore-ip-addresses/

# TC => O(3**(n))
# SC => O(3**(n))
# 


from typing import *



class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:

        res = []
        LEN = len(s)

        if not (4 <= LEN <= 12): return res

        def backtrack(idx, dots, currIP):
            
            if (dots == 4 and idx == LEN):
                res.append(currIP[:-1])
                return 
            
            if (dots > 4):
                return
            
            for idx2 in range(idx, min(LEN, idx+3)):

                if int(s[idx: idx2+1]) < 256 and (idx == idx2 or s[idx] != "0"):
                    backtrack(idx2 + 1, dots + 1, currIP + s[idx: idx2+1] + ".")
        
        backtrack(0, 0, "")

        return res


if __name__ == "__main__":
    obj = Solution()
    s = "0000"
    ans = obj.restoreIpAddresses(s)
    print(ans)