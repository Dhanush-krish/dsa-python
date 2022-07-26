#   https://leetcode.com/problems/balanced-binary-tree/




from typing import *


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        #base condition
        def dfs(root):
            if root is None: return [True, 0]
        
            right = dfs(root.right)
            left = dfs(root.left)
            
            balanced =  right[0] and left[0] and abs(right[1]-left[1]) <= 1
            height = 1+ max(right[1], left[1])
            
            return [balanced, height]
        
        return dfs(root)[0]


if __name__ == '__main__':

    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(10)
    node5 = TreeNode(5)
    node6 = TreeNode(6)
    node7 = TreeNode(7)
    # node8 = TreeNode(8)
    # node9 = TreeNode(9)
    
    
    node1.left = node2
    node1.right = node5
    node2.left = node3
    node2.right = node4
    node5.left = node6
    node5.right = node7
    # node3.right = node8
    # node8.right = node9    
    
    obj = Solution()
    ans = obj.isBalanced(node1)
    print(ans)