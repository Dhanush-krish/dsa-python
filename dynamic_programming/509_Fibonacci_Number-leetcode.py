#   https://leetcode.com/problems/fibonacci-number/




from typing import *


class Solution:
    def fib(self, n: int) -> int:
        if n <= 2: return 1
        
        return self.fib(n-1)+ self.fib(n-2)


if __name__ == '__main__':
    obj = Solution()
    ans = obj.fib(3)
    print(ans)