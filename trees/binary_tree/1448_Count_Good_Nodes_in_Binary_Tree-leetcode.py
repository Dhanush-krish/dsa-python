#   https://leetcode.com/problems/count-good-nodes-in-binary-tree/




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
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(node, maxi):
            if node is None: return 0
            
            new_max = max(node.val, maxi)
            
            return int(node.val >= maxi) + dfs(node.left, new_max) + dfs(node.right, new_max)
        
        return dfs(root, root.val)


if __name__ == '__main__':
    obj = Solution()
    
    node1 = TreeNode(2)
    node2 = TreeNode(4)
    node3 = TreeNode(10)
    node4 = TreeNode(8)
    node5 = TreeNode(4)
    # node6 = TreeNode(5)
    # node7 = TreeNode(1)
    # node8 = TreeNode(8)
    # node9 = TreeNode(9)
    
    
    node1.right = node2
    node2.left = node3
    node2.right = node4
    # node2.right = node5
    node4.left = node5
    # node3.right = node6
    # node5.right = node7
    # node3.right = node8
    # node8.right = node9  
    ans = obj.goodNodes(node1)
    print(ans)