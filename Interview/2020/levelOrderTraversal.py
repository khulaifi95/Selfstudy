from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrderBFS(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = []
        queue = [root]

        while queue:
            size = len(queue)
            tmp = []

            for _ in xrange(size):
                r = queue.pop(0)
                tmp.append(r.val)
                if r.left:
                    queue.append(r.left)
                if r.right:
                    queue.append(r.right)
            # Add temporary to result.
            res.append(tmp)
        return res


    def levelOrderDFS(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = []

        def dfs(index, r):
            # Insert a new empty list to res.
            if len(res) < index:
                res.append([])
            # Add current value to current index.
            res[index-1].append(r.val)
            # Iterate:
            if r.left:
                dfs(index+1, r.left)
            if r.right:
                dfs(index+1, r.right)

        dfs(1, root)
        return res
