#   https://leetcode.com/problems/first-bad-version/



# T.C => 
# S.C => 


from typing import *


# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n
        
        while(left < right):
            mid = left + (right-left)//2
                        
            if not isBadVersion(mid):
                left = mid + 1

if __name__ == '__main__':
    obj = Solution()
    ans = obj.firstBadVersion()
    print(ans)