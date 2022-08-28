#   https://leetcode.com/explore/learn/card/array-and-string/203/introduction-to-string/1162/




from typing import *





class Solution:

    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_length = min([len(x) for x in strs])
        result = ""
        
        for element in range(min_length):
            for word  in strs:
                if word[element] != strs[0][element]:
                    return result
            result += strs[0][element]
                
        
        return result
        


if __name__ == '__main__':
    obj = Solution()
    strs = ["flower","flow","flight"]
    ans = obj.longestCommonPrefix(strs)
    print(ans)