#   https://leetcode.com/problems/pseudo-palindromic-paths-in-a-binary-tree/




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
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        
        def dfs(node, curr_xor, root_val):
            if node is None: return 0
            
            curr_xor += node.val
            left_val = dfs(node.left, curr_xor, root_val)
            right_val = dfs(node.right, curr_xor, root_val)
            
            if left_val == 0 and right_val == 0:
                print(curr_xor)


if __name__ == '__main__':
    
    node1 = TreeNode(2)
    node2 = TreeNode(3)
    node3 = TreeNode(1)
    node4 = TreeNode(3)
    node5 = TreeNode(1)
    node6 = TreeNode(1)
    # node7 = TreeNode(7)
    
    
    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    node3.right = node6
    # node5.right = node7    
    
    obj = Solution()
    ans = obj.pseudoPalindromicPaths()
    print(ans)