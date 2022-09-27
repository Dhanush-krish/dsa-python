#   https://leetcode.com/problems/find-original-array-from-doubled-array/



# T.C => 
# S.C => 


from typing import *


class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        
        LEN = len(changed)
        
        if LEN%2 == 1:
            return []
        result = [] 
        
        while(changed):
            element1 = changed.pop()
            if element1*2 in changed:
                changed.remove(element1*2)
                result.append(element1)
            elif element1//2 in changed and element1 != 1:
                changed.remove(element1//2)
                result.append(element1//2)
            else:
                return []
        
        return result
            
        


if __name__ == '__main__':
    obj = Solution()
    changed = [6,3,0,1]
    ans = obj.findOriginalArray(changed)
    print(ans)