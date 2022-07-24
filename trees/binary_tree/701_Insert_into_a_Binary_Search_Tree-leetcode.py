#   https://leetcode.com/problems/insert-into-a-binary-search-tree/




from typing import *


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        node = root
        new = TreeNode(val)
        
        if root is None: return new
        
        while(node):
            parent = node
            if val < node.val:
                node = node.left
            else:
                node = node.right
                
        if val < parent.val:
            parent.left = new
        else:
            parent.right = new
        
        return root


if __name__ == '__main__':
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
    
    obj = Solution()
    ans = obj.insertIntoBST(node1, 5)
    root = ans
    
    stack = []
    node = root
    while(node or stack):
        if node :
            stack.append(node)
            node = node.left
            
        if node is None:
            node = stack.pop()
            print(node.val, end=" ")
            node = node.right
    