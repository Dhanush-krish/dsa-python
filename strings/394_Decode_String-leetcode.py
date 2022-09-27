#   https://leetcode.com/problems/decode-string/

from curses.ascii import isalpha, isdigit
from lib2to3.pgen2.token import LPAR




# T.C => 
# S.C => 


from typing import *


class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        
        for element in s:
            if element != "]":
                stack.append(element)
            else:
                
                temp = ""
                while (stack and stack[-1] != "["):
                    temp = stack.pop() + temp
                
                stack.pop()
                
                digit = ""
                while(stack and stack[-1].isdigit()):
                    digit = stack.pop() + digit
                
                stack.append(int(digit) * temp)
                
        return "".join(stack)

if __name__ == '__main__':
    obj = Solution()
    s = "20[abc]3[cd]ef"
    ans = obj.decodeString(s)
    print(ans)