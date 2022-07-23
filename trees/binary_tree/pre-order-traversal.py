#   https://leetcode.com/explore/learn/card/data-structure-tree/134/traverse-a-tree/928/




from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        stack = []
        output_list = []
        node = root

        while(node or stack):
            if node:
                output_list.append(node.val)
                stack.append(node)
                node = node.left
            if node is None:
                node = stack.pop()
                node = node.right

        return output_list



if __name__ == '__main__':
    obj = Solution()
    
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node6 = TreeNode(6)
    node7 = TreeNode(7)
    
    
    node1.left = node2
    node1.right = node5
    node2.left = node3
    node2.right = node4
    node5.left = node6
    node5.right = node7
    
    ans = obj.preorderTraversal(node1)
    print(ans)