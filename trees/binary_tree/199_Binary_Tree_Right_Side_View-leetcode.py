#   https://leetcode.com/problems/binary-tree-right-side-view/





from typing import *


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        if root is None: return []
        
        def bfs(root):
            queue = [root]
            result = []
            
            while(queue):
                last = None
                for _ in range(len(queue)):
                    node = queue.pop(0)
                    last = node.val                    
                    if node.left is not None: queue.append(node.left)
                    if node.right is not None: queue.append(node.right)
                if result is not None:
                    result.append(last)
                
            return result
        
        return bfs(root)


if __name__ == '__main__':

    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(5)
    node4 = TreeNode(3)
    node5 = TreeNode(4)
    # node6 = TreeNode(6)
    # node7 = TreeNode(7)
    # node8 = TreeNode(8)
    # node9 = TreeNode(9)
    
    
    node1.right = node2
    node2.left = node3
    node1.left = node4
    node4.right = node5
    # node5.left = node6
    # node5.right = node7
    # node3.right = node8
    # node8.right = node9      
    
    obj = Solution()
    ans = obj.rightSideView(node1)
    print(ans)