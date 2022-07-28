#   https://leetcode.com/problems/path-sum/





from typing import *


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, curr_sum):
            nonlocal path
            if node :
                curr_sum += node.val
                
                if (node.left is None and node.right is None):
                    path.append(curr_sum)
                dfs(node.left, curr_sum)
                dfs(node.right, curr_sum)
        
        path = []
        dfs(root,0)
        return targetSum in path


if __name__ == '__main__':
    
    node1 = TreeNode(1)
    # node2 = TreeNode(4)
    # node3 = TreeNode(8)
    # node4 = TreeNode(11)
    # node5 = TreeNode(7)
    # node6 = TreeNode(2)
    # node7 = TreeNode(13)
    # node8 = TreeNode(4)
    # node9 = TreeNode(1)
    
    # node1.left = node2
    # node1.right = node3
    # node2.left = node4
    # node4.left = node5
    # node4.right = node6
    # node3.left = node7
    # node3.right = node8
    # node8.right = node9
    
    
    obj = Solution()
    ans = obj.hasPathSum(node1, 1)
    print(ans)