#   https://leetcode.com/problems/sum-root-to-leaf-numbers/




from locale import currency
from typing import *


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node, curr_sum):
            if node is None: return None
            
            curr_sum = ((curr_sum)*10)+node.val
            
            if node.right is None and node.left is None:return curr_sum
                
            return dfs(node.right, curr_sum)+dfs(node.left, curr_sum)
        
        return dfs(root, 0)


if __name__ == '__main__':
    
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    # node4 = TreeNode(4)
    # node5 = TreeNode(5)
    # node6 = TreeNode(6)
    # node7 = TreeNode(7)
    
    
    node1.left = node2
    node1.right = node3
    # node2.left = node3
    # node2.right = node4
    # node5.left = node6
    # node5.right = node7
        
    obj = Solution()
    ans = obj.sumNumbers(node1)
    print(ans)