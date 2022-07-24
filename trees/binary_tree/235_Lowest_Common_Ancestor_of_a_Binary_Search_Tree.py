#   https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/




from typing import *


# Definition for a binary tree node.
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        current = root
        while current:
            if p.val > current.val and q.val > current.val:
                current = current.right
            elif p.val < current.val and q.val < current.val:
                current = current.left
            else:
                return current


if __name__ == '__main__':
    obj = Solution()

    node1 = TreeNode(6)
    node2 = TreeNode(2)
    node3 = TreeNode(0)
    node4 = TreeNode(4)
    node5 = TreeNode(3)
    node6 = TreeNode(5)
    node7 = TreeNode(8)
    node8 = TreeNode(7)
    node9 = TreeNode(9)
    
    
    node1.left = node2
    node2.left = node3
    node2.right = node4
    node4.left = node5
    node4.right = node6
    node1.right = node7
    node7.left = node8
    node7.right = node9

    ans = obj.lowestCommonAncestor(node1, TreeNode(0), TreeNode(5))
    print(ans.val)

    # root = ans
    
    # ##check the tree 
    # stack = []
    # node = root
    # while(node or stack):
    #     if node :
    #         stack.append(node)
    #         node = node.left
            
    #     if node is None:
    #         node = stack.pop()
    #         print(node.val, end=" ")
    #         node = node.right