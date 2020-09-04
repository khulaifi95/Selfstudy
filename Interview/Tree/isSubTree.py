class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        def check(s, t):
            if not s and not t:
                return True
            if s and not t or not s and t or s.val != t.val:
                return False
            return check(s.left, t.left) and check(s.right, t.right)

        def dfs(s, t):
            if not s:
                return False
            return check(s, t) or dfs(s.left, t) or dfs(s.right, t)

        return dfs(s, t)