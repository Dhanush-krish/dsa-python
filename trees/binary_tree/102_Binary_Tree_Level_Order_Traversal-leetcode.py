#   https://leetcode.com/problems/binary-tree-level-order-traversal/






import collections
from typing import *


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if root is None: return []
        
        def bfs(root):
            queue = [root]
            result = []
            
            while(queue):
                level = []
                for _ in range(len(queue)):
                    node = queue.pop(0)
                    level.append(node.val)
                    
                    if node.left is not None: queue.append(node.left)
                    if node.right is not None: queue.append(node.right)
                result.append(level)
                
            return result
        
        return bfs(root)

                


if __name__ == '__main__':
    
    node1 = TreeNode(3)
    node2 = TreeNode(9)
    node3 = TreeNode(20)
    node4 = TreeNode(15)
    node5 = TreeNode(7)
    # node6 = TreeNode(6)
    # node7 = TreeNode(7)
    # node8 = TreeNode(8)
    # node9 = TreeNode(9)
    
    
    node1.left = node2
    node1.right = node3
    node3.left = node4
    node3.right = node5
    # node5.left = node6
    # node5.right = node7
    # node3.right = node8
    # node8.right = node9    
    
    
    
    obj = Solution()
    ans = obj.levelOrder(node1)
    print(ans)