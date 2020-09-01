from collections import deque

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrderTraversal(self, root: TreeNode) -> [[int]]:
        if not root:
            return []
        res = []
        queue = deque([root,])

        while queue:
            size = len(queue)
            lvl = []

            for _ in range(size):
                node = queue.popleft()
                lvl.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            res.append(lvl)

        return res