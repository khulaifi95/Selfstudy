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
        queue = [root,]

        while queue:
            size = len(queue)
            lvl = []

            for _ in range(size):
                node = queue.pop(0)
                tmp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            # Add level list to result.
            res.append(lvl)
        return res
        # Time:
        # Space: 


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
