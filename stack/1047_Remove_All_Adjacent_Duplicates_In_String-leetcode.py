#   https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/



# T.C => 
# S.C => 


from typing import *


class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for val in s:
            if stack and stack[-1] == val:
                stack.pop()
            else:
                stack.append(val)
        
        return "".join(stack)


if __name__ == '__main__':
    obj = Solution()
    s = "abbaca"
    ans = obj.removeDuplicates(s)
    print(ans)