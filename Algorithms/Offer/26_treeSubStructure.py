# Check if tree B is a sub structure of A.

class Solution:
    def isSubStructure(self, A, B):
        if A == None or B == None:
            return False
        return dfs(A, B) or self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B)



        def dfs(A, B):
            if not B: return True
            if not A: return False
            return A.val==B.val and dfs(A.left, B.left) and dfs(A.right, B.right)
