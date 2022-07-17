#   https://leetcode.com/problems/group-anagrams/




from collections import defaultdict, Counter
from typing import *


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        
        for word in strs:
            result[str(sorted(word))].append(word)
        
        return list(result.values())


if __name__ == '__main__':
    obj = Solution()
    strs = ["eat","tea","tan","ate","nat","bat"]
    ans = obj.groupAnagrams(strs)
    print(ans)
    
    
"""
Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
"""