#   https://leetcode.com/problems/binary-tree-pruning/



# T.C => 
# S.C => 


from typing import *



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        
        def dfs(node):
            if node is None : return 0
            
            left_val = dfs(node.left)
            right_val = dfs(node.right)
            
            
            if left_val  == 0: node.left = None
            if right_val  == 0: node.right = None
            print(left_val, right_val, node.left, node.right, node.val + right_val + left_val)
            return node.val + right_val + left_val
        
        val = dfs(root)
        
        return None if val == 0 else root
            
            




if __name__ == '__main__':
    node1 = TreeNode(1)
    node2 = TreeNode(0)
    node3 = TreeNode(1)
    node4 = TreeNode(0)
    node5 = TreeNode(0)
    node6 = TreeNode(0)
    node7 = TreeNode(1)
    # node8 = TreeNode(8)
    # node9 = TreeNode(9)
    
    
    # node1.left = node2
    # node1.right = node3
    # node2.left = node4
    # node2.right = node5
    # node3.left = node6
    # node3.right = node7
    # node3.right = node8
    # node8.right = node9       
    
    obj = Solution()
    ans = obj.pruneTree(node1)
    print(ans)
    