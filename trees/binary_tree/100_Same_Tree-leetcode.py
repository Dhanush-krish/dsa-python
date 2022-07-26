#   https://leetcode.com/problems/same-tree/




from typing import *


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def dfs(node1, node2):
            if node1 is None and node2 is None: return True
            if node1 is None or node2 is None: return False
            if node1.val != node2.val: return False
            
            
            return dfs(node1.right, node2.right) and dfs(node1.left, node2.left)
        
        return dfs(p,q)


if __name__ == '__main__':
    
    
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(1)
    node5 = TreeNode(2)
    node6 = TreeNode(3)
    # node7 = TreeNode(7)
    # node8 = TreeNode(8)
    # node9 = TreeNode(9)
    
    
    node1.left = node2
    node1.right = node3
    node4.left = node5
    node4.right = node6
    # node5.left = node6
    # node5.right = node7
    # node3.right = node8
    # node8.right = node9       
    
    obj = Solution()
    ans = obj.isSameTree(node1, node4)
    print(ans)