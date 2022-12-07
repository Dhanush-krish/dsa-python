#   https://leetcode.com/problems/range-sum-of-bst/description/

# TC => 
# SC => 


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import *


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if root is None: return 0
        if root.val < low or root.val > high:
            return self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)
        else:
            return root.val + self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)



if __name__ == "__main__":
    obj = Solution()
    node1 = TreeNode(10)
    node2 = TreeNode(5)
    node3 = TreeNode(15)
    node4 = TreeNode(3)
    node5 = TreeNode(7)
    node6 = TreeNode(18)
    # node7 = TreeNode(1)
    # node8 = TreeNode(8)
    # node9 = TreeNode(9)
    
    
    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    node3.right = node6

    ans = obj.rangeSumBST(node1, 7, 15)
    print(ans)