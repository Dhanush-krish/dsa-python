#   https://leetcode.com/problems/baseball-game/



# T.C => 
# S.C => 


from curses.ascii import isdigit
from typing import *



class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack = []
        
        for val in ops:
            
            if val == "+":
                stack.append(stack[-1] + stack[-2])
            elif val == "C":
                stack.pop()
            elif val == "D":
                stack.append(stack[-1] * 2)
            else:
                stack.append(int(val))
                
        
        return sum(stack)


if __name__ == '__main__':
    obj = Solution()
    ops = ["5","-2","4","C","D","9","+","+"]
    ans = obj.calPoints(ops)
    print(ans)