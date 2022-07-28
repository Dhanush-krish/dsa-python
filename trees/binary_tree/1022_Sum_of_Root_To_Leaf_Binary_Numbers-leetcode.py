#   https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/




from typing import *


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node, curr_sum):
            nonlocal result
            if node:
                current_sum = (curr_sum << 1) | node.val
                
                if not(node.right or node.left):
                    result += current_sum
                
                dfs(node.right, current_sum)
                dfs(node.left, current_sum)
        
        result = 0
        dfs(root, 0)
        return result


if __name__ == '__main__':
    
    node1 = TreeNode(1)
    node2 = TreeNode(0)
    node3 = TreeNode(1)
    node4 = TreeNode(0)
    node5 = TreeNode(1)
    node6 = TreeNode(0)
    node7 = TreeNode(1)
    # node8 = TreeNode(8)
    # node9 = TreeNode(9)
    
    
    node1.left = node2
    node1.right = node3
    # node2.left = node4
    # node2.right = node5
    # node3.left = node6
    # node3.right = node7
    # node5.right = node7
    # node3.right = node8
    # node8.right = node9  
    
    obj = Solution()
    ans = obj.sumRootToLeaf(node1)
    print(ans)