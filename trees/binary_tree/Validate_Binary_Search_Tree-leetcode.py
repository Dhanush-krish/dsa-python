#   https://leetcode.com/explore/learn/card/introduction-to-data-structure-binary-search-tree/140/introduction-to-a-bst/997/

from typing import *

from black import out

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        node = root
        stack = []
        
        output = []
        
        while(stack or node):
            if node:
                stack.append(node)
                node = node.left
            
            if node is None:
                node = stack.pop()
                output.append(node.val)
                node = node.right
        
        for index in range(1,len(output)):
            if output[index-1] >= output[index]:
                return False
        
        return True
        
    
if __name__ == '__main__':
    obj = Solution()
    
    node1 = TreeNode(2)
    node2 = TreeNode(1)
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
    
    ans = obj.isValidBST(node1)
    print(ans)