#   https://leetcode.com/problems/daily-temperatures/




from turtle import left, right
from typing import *


## bruteforce

# class Solution:
#     def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
#         output = [0]*len(temperatures)
        
#         for left, value in enumerate(temperatures):
#             for right in range(left+1, len(temperatures)):
#                 if temperatures[right] > value:
#                     output[left] = right-left
#                     break
        
#         return output


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0]*len(temperatures)
        
        for left,value in enumerate(temperatures):
            while(stack and value > stack[-1][1]):
                index2,value1 = stack.pop()
                result[index2] = left-index2
            
            stack.append([left,value])
        
        return result




if __name__ == '__main__':
    obj = Solution()
    temperatures = [73,74,75,71,69,72,76,73]
    ans = obj.dailyTemperatures(temperatures)
    print(ans)