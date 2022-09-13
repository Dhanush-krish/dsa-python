class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


### iterative
# def dfs(root):
# if root is None: return []

#     stack = [root]
#     result = []

#     while stack:
#         node = stack.pop()
#         result.append(node.val)

#         if node.right is not None: stack.append(node.right)
#         if node.left is not None: stack.append(node.left)

#     return result

### recursive


def dfs(node):
    if node is None:
        return []

    lis1 = dfs(node.left)
    lis2 = dfs(node.right)

    return [node.val] + lis1 + lis2


if __name__ == "__main__":

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

    print(dfs(node1))
