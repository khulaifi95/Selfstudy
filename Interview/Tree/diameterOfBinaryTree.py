class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.maxd = 0

        def depth(node):
            if not node:
                return 0
            left = depth(node.left)
            right = depth(node.right)
            self.maxd = max(left+right, maxd)
            return max(left, right) + 1

        depth(root)
        return self.maxd