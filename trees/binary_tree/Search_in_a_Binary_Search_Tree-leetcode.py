#   https://leetcode.com/explore/learn/card/introduction-to-data-structure-binary-search-tree/141/basic-operations-in-a-bst/1000/
#   https://leetcode.com/problems/insert-into-a-binary-search-tree/



from tkinter.messagebox import NO
from typing import *


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        node = root
        while(node):
            if node.val == val:
                return node
            elif val < node.val: 
                node = node.left
            else:
                node = node.right
        
        return None
                
        


if __name__ == '__main__':
    obj = Solution()
    
    node1 = TreeNode(4)
    node2 = TreeNode(2)
    node3 = TreeNode(1)
    node4 = TreeNode(3)
    node5 = TreeNode(7)
    # node6 = TreeNode(6)
    # node7 = TreeNode(7)
    
    
    node1.left = node2
    node1.right = node5
    node2.left = node3
    node2.right = node4
    # node5.left = node6
    # node5.right = node7
    
    ans = obj.searchBST(node1, 5)
    print(ans.val if ans else None)