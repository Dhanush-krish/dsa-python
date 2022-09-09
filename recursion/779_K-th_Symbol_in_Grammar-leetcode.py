#   https://leetcode.com/problems/k-th-symbol-in-grammar/



# T.C => 
# S.C => 


from typing import *

class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        return self.finder(n, "0", k-1) 
    
    def finder(self, n, pattern, k):
        if n == 1:
            # print(pattern)
            return pattern[k]
        
        new_str = self.generator(pattern)
        return self.finder(n-1, new_str, k)
    
    def generator(self, pattern):
        if pattern == "0": return "01"
        if pattern == "1": return "10"
        
        result = ""
        for val in pattern:
            result += self.generator(val)
        
        return result



if __name__ == '__main__':
    obj = Solution()
    ans = obj.kthGrammar(3, 4)
    print(ans)