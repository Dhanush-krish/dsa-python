class Solution:
    def longestPalindrome(self, s: str) -> str:

        resLen = 0
        resStr = ""
        n = len(s)

        for idx in range(n):

            l, r = idx, idx

            while(l >= 0 and r < n and s[l] == s[r]):
                if (r - l + 1) > resLen:
                    resLen = (r - l + 1)
                    resStr = s[l:r+1]
                l -= 1
                r += 1
            l, r = idx, idx + 1

            while(l >= 0 and r < n and s[l] == s[r]):
                if (r - l + 1) > resLen:
                    resLen = (r - l + 1)
                    resStr = s[l:r+1]
                l -= 1
                r += 1

        return resStr
        