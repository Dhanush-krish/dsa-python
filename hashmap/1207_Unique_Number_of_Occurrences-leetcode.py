#   https://leetcode.com/problems/unique-number-of-occurrences/


# TC => O(n)
# SC => O(n)
# where n is the size of the array


from typing import *
from collections import Counter


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = Counter(arr)
        seen = set()

        for key, val in freq.items():
            if val in seen:
                return False
            seen.add(val)
        
        return True



if __name__ == "__main__":
    obj = Solution()
    arr = [-3,0,1,-3,1,1,1,-3,10,0]
    ans = obj.uniqueOccurrences(arr)
    print(ans)