#   https://leetcode.com/explore/learn/card/recursion-i/251/scenario-i-recurrence-relation/3233/


from typing import *


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        if root is None: return None
        if root.val == val: return root
        
        if val < root.val: return self.searchBST(root.left, val)
        if val > root.val: return self.searchBST(root.right, val) 
    

if __name__ == "__main__":
    node1 = TreeNode(4)
    node2 = TreeNode(2)
    node3 = TreeNode(1)
    node4 = TreeNode(3)
    node5 = TreeNode(7)
    
    node1.left = node2
    node2.left = node3
    node2.right = node4
    node1.right = node5
    
    obj = Solution()
    ans = obj.searchBST(node1, 5)
    print(ans)    
    