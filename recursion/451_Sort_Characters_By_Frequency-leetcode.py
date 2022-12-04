#   https://leetcode.com/problems/sort-characters-by-frequency/


# TC => O(n)
# SC => nlog(n)
# where n is the length of the string


from typing import *



class Solution:
    def frequencySort(self, s: str) -> str:
        freq = {}

        for val in s:
            freq[val] = 1 + freq.get(val, 0)

        return "".join(sorted(s, key = lambda x: (-freq[x], ord(x))))



if __name__ == "__main__":
    obj = Solution()
    bs = "cccaaa"
    ans = obj.frequencySort(bs)
    print(ans)