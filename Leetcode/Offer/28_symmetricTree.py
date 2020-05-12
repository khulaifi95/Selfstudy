# Check if a tree is symmetric
class Solution:

    def isSymmetric(self, root):
        def recur(L, R):
            if not L and not R:
                return True
            if not L or not R or L.var != R.var:
                return False
            return recur(L.right, R.left) and recur(L.left, R.right)

        return recur(root.left, root.right) if root else True
