import collections

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def binaryTreePathsDFS(self, root: TreeNode) -> [str]:
        # Time:  O(n^2)
        # Space: O(n^2)
        def builder(root, path):
            if root:
                path += str(root.val)
                if not root.left and not root.right:
                    paths.append(path)
                else:
                    path += '->'
                    builder(root.left, path)
                    builder(root.right, path)

        paths = []
        builder(root, '')
        return paths

    def binaryTreePathsBFS(self, root: TreeNode) -> [str]:
        # Time:
        # Space:
        paths = []
        if not root:
            return paths

        node_queue = collections.deque([root])
        path_queue = collections.deque([str(root.val)])

        while node_queue:
            node = node_queue.popleft()
            path = path_queue.popleft()

            if not node.left and node.right:
                paths.append(path)
            else:
                if node.left:
                    node_queue.append(node.left)
                    path_queue.append(path + '->' + str(node.left.val))

                if node.right:
                    node_queue.append(node.right)
                    path_queue.append(path + '->' + str(node.right.val))

        return paths

