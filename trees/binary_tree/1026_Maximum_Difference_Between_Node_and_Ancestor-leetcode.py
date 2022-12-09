#   https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/description/



# TC => O(n)
# SC => O(n)
# where n is the number of nodes


from typing import *


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        if root is None: return 0

        def dfs(node, high, low):
            if node is None: return high - low
            
            low = min(low, node.val)
            high = max(high, node.val)

            return max(dfs(node.left, high, low),
                       dfs(node.right, high, low))
        
        return dfs(root, root.val, root.val)



if __name__ == "__main__":
    obj = Solution()
    node1 = TreeNode(8)
    node2 = TreeNode(3)
    node3 = TreeNode(10)
    node4 = TreeNode(1)
    node5 = TreeNode(6)
    node6 = TreeNode(14)
    node7 = TreeNode(4)
    node8 = TreeNode(7)
    node9 = TreeNode(13)
    
    
    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    node3.right = node6
    node5.left = node7
    node5.right = node8
    node6.left = node9

    ans = obj.maxAncestorDiff(node1)
    print(ans)