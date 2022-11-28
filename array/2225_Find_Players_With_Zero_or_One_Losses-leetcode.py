#   https://leetcode.com/problems/find-players-with-zero-or-one-losses/

# TC => O(N)
# SC => 

from collections import deque
from typing import *


class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        lookup = [0]*(10**5 + 1)
        result = deque([[],[]])
        for w,l in matches:
            if lookup[w] >= 0:
                lookup[w] += 1
            if lookup[l] > 0:
                lookup[l] = -1
            else:
                lookup[l] -= 1
        
        for index, value in enumerate(lookup):
            if value > 0:
                result[0].append(index)
            elif value == -1:
                result[1].append(index)
        
        return result
        



if __name__ == "__main__":
    obj = Solution()
    matches = [[2,3],[1,3],[5,4],[6,4]]
    ans = obj.findWinners(matches)
    print(ans)