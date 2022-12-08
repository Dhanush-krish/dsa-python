#   https://leetcode.com/problems/leaf-similar-trees/description/

# TC => 
# SC => 


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import *


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        def dfs(node):
            if node is None: return []
            if node.left is None and node.right is None:
                return [node.val] 
            return dfs(node.left).extend(dfs(node.right))
        
        return dfs(root1) == dfs(root2)



if __name__ == "__main__":
    obj = Solution()

    node1 = TreeNode(3)
    node2 = TreeNode(5)
    node3 = TreeNode(1)
    node4 = TreeNode(6)
    node5 = TreeNode(2)
    node6 = TreeNode(9)
    node7 = TreeNode(8)
    node8 = TreeNode(7)
    node9 = TreeNode(4)
    
    
    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    node3.left = node6
    node3.right = node7
    node5.left = node8
    node5.right = node9

    ans = obj.leafSimilar(node1, node1)
    print(ans)