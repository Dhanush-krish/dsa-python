#   https://leetcode.com/problems/diameter-of-binary-tree/

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
    
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    # node6 = TreeNode(6)
    # node7 = TreeNode(7)
    # node8 = TreeNode(8)
    # node9 = TreeNode(9)
    
    
    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    # node5.left = node6
    # node5.right = node7
    # node3.right = node8
    # node8.right = node9

    obj = Solution()
    ans = obj.maxDepth(node1)
    print(ans)