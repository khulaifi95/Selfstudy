# 1


class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findTarget(self, root, k):
        '''Find 2 elements in a BSD that sums up to a given target.
        
        Return: boolean
        
        Arguments:
            root {[TreeNode]}
            k {[int]} 
        ''' 


    def inOrder(self, root):
        if root:
            inOrder(root.left)
            print(root.val)
            inOrder(root.right)




