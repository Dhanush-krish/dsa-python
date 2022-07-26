#   https://structy.net/problems/max-root-to-leaf-path-sum


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxPath(root):
    
    if root is None: return 0
    
    return root.val+max(maxPath(root.right), maxPath(root.left))


if __name__ == '__main__':
    
    node1 = TreeNode(3)
    node2 = TreeNode(5)
    node3 = TreeNode(4)
    node4 = TreeNode(-2)
    node5 = TreeNode(4)
    node6 = TreeNode(1)
    # node7 = TreeNode(7)
    # node8 = TreeNode(8)
    # node9 = TreeNode(9)
    
    
    node1.left = node2
    node1.right = node5
    node2.left = node3
    node2.right = node4
    node5.right = node6
    # node5.right = node7
    # node3.right = node8
    # node8.right = node9

    ans = maxPath(node1)
    print(ans)