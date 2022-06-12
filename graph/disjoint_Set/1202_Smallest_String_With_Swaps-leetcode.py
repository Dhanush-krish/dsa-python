#   https://leetcode.com/problems/smallest-string-with-swaps/


from typing import *
from collections import defaultdict


class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        root = [index for index in range(len(s))]
        s = list(s)
        component_root = defaultdict(list)
        
        def union(v1, v2):
            root_v1 = find(v1)
            root_v2 = find(v2)
            
            if root_v1 != root_v2:
                root[root_v2] = root_v1
                
        def find(v1):
            if v1 == root[v1]:
                return v1
            root[v1] = find(root[v1])
            return root[v1]
        
        for x,y in pairs:
            union(x, y)
            
        for vertex in range(len(s)):
            v_root = find(vertex)
            component_root[v_root].append(vertex)
        
        for cp_root, indices in component_root.items():
            
            chars = []
            for index in indices:
                chars.append(s[index])
            chars = sorted(chars)
            
            for c, i in zip(chars, indices):
                s[i] = c
        
        return "".join(s)        


if __name__ == '__main__':
    obj = Solution()
    s = "dcab"
    pairs = [[0,3],[1,2],[0,2]]
    ans = obj.smallestStringWithSwaps(s, pairs)
    print(ans)