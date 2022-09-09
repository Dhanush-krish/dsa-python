#   https://leetcode.com/problems/construct-string-from-binary-tree/



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
    def tree2str(self, root: Optional[TreeNode]) -> str:
        
        if root is None: return ""
        
        left_part = self.tree2str(root.left)
        left_str = "(" + left_part + ")"

        right_part = self.tree2str(root.right)
        right_str = "(" + right_part + ")"
        
        if left_part == "" and right_part == "":
            left_str = ""
            right_str = ""
        elif right_part == "":
            right_str = ""
            
        
        return str(root.val) +  left_str + right_str
        


if __name__ == '__main__':
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    # node5 = TreeNode(2)
    # node6 = TreeNode(3)
    # node7 = TreeNode(7)
    # node8 = TreeNode(8)
    # node9 = TreeNode(9)
    
    
    node1.left = node2
    node1.right = node3
    node2.left = node4
    # node5.left = node6
    # node5.right = node7
    # node3.right = node8
    # node8.right = node9      
    
    obj = Solution()
    ans = obj.tree2str(node1)
    print(ans)