class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.maxSum = float('-inf')

    def maxPathSum(self, root: TreeNode) -> int:
        def maxGain(node):
            if not node:
                return 0

            leftGain = max(maxGain(node.left), 0)
            rightGain = max(maxGain(node.right), 0)

            newPath = node.val + leftGain + rightGain

            self.maxSum = max(self.maxSum, newPath)

            return node.val + max(leftGain, rightGain)

        maxGain(root)
        return self.maxSum
