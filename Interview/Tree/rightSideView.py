from collections import deque

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def rightSideView(self, root: TreeNode) -> [int]:
        # BFS
        # Time:  O(n)
        # Space: O(n)
        rval = dict()
        max_depth = -1

        queue = deque([(root, 0)])
        while queue:
            node, depth = queue.popleft()

            if node:
                max_depth = max(max_depth, depth)
                rval[depth] = node.val

                queue.append((node.left, depth+1))
                queue.append((node.right, depth+1))

        return [rval[depth] for depth in range(max_depth + 1)]