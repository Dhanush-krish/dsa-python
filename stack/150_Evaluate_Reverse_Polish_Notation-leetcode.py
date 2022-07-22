#   https://leetcode.com/problems/evaluate-reverse-polish-notation/




import math
from typing import *


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for element in tokens:
            
            if element in {"+", "-", "*", "/"}:
                operant2 = stack.pop()
                operant1 = stack.pop()
                if(element == "+"):
                    result = operant1 + operant2
                elif (element == "-"):
                    result = operant1 - operant2
                elif (element == "*"):
                    result = operant1 * operant2
                else:
                    result = int(operant1 / operant2)
                stack.append(result)
            else:
                stack.append(int(element))

        return stack.pop()


if __name__ == '__main__':
    obj = Solution()
    tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    ans = obj.evalRPN(tokens)
    print(ans)