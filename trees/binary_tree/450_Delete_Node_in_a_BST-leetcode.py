#   https://leetcode.com/problems/delete-node-in-a-bst/





from typing import *

from black import target_version_option_callback


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        node = root
        while(node):
            if node.val == key:
                break
            elif key < node.val:
                parent = node
                node = node.left
            else:
                parent = node
                node = node.right
        
        if node is not None:
            print("parent = ",parent.val)
            print("node = ", node.val)
            
            ##check the node has no child
            if node.left is None and node.right is None:
                if node.val < parent.val:
                    parent.left = None
                else:
                    parent.right = None
            
            ## check for one child        
            elif node.left is not None and  node.right is None:
                if node.val < parent.val:
                    parent.left = node.left
                else:
                    parent.right = node.left
                    
            elif node.right is not None and  node.left is None:
                if node.val < parent.val:
                    parent.left = node.right
                else:
                    parent.right = node.right
            
            else:
                ##TODO
                pass
                
        
        return root


if __name__ == '__main__':
    obj = Solution()
    
    node1 = TreeNode(5)
    node2 = TreeNode(3)
    node3 = TreeNode(2)
    node4 = TreeNode(4)
    node5 = TreeNode(6)
    node6 = TreeNode(7)
    # node7 = TreeNode(7)
    
    
    node1.left = node2
    node1.right = node5
    node2.left = node3
    node2.right = node4
    node5.right = node6
    # node5.right = node7
    ans = obj.deleteNode(node1, 6)
    
    root = ans
    
    ##check the tree 
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