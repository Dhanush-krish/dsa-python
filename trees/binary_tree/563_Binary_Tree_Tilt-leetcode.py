#   https://leetcode.com/problems/binary-tree-tilt/



# T.C => 
# S.C => 


from typing import *


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node):
            if node is None: return (0, 0)
            
            dfs()
            
        
        return dfs(root)
        


if __name__ == '__main__':
    obj = Solution()
    ans = obj.
    print(ans)