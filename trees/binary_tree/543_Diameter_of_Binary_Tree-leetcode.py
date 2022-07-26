#   https://leetcode.com/problems/diameter-of-binary-tree/




from typing import *


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        pass   


if __name__ == '__main__':
    obj = Solution()
    ans = obj.diameterOfBinaryTree()
    print(ans)