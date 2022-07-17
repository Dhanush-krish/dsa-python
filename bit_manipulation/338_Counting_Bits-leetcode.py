#   https://leetcode.com/problems/counting-bits/


from typing import *


class Solution:
    def countBits(self, n: int) -> List[int]:
        
        dp = [0]*(n+1)
        offset = 1
        for num in range(1,n+1):
            if offset * 2 == num:
                offset = num
            dp[num] = 1 + dp[num-offset]
            
            
        return dp
    
    
if __name__ == '__main__':
    obj = Solution()
    n = 4
    ans = obj.countBits(n)
    print(ans)
    
"""
Example 1:

Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10
Example 2:

Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101
"""