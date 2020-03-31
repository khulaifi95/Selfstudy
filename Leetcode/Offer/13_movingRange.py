
# Find the moving range of a robot.
# Input: m, n, k
# Example: [9, 9], k = 5
# Output: 10


class Solution:

    def movingRange_dfs(self, m, n, k):
        """Find the moving range in [m-1, n-1].

        The sum of digits in coordinates < k.

        Arguments:
            m {[int]} -- Boundary.
            n {[int]} -- Boundary.
            k {[int]} -- Upper bound for sum of digits.
        """
        def sumDigits(n):
            r = 0
            while n:
                r, n = r + n % 10, n // 10
            return r

        def dfs(i, j):
            if i == m or j == n or (i, j) in marked:
                return False
            if sumDigits(i) + sumDigits(j) > k:
                return False
            marked.add((i, j))
            dfs(i + 1, j)
            dfs(i, j + 1)

        marked = set()
        dfs(0, 0)
        return len(marked)

    def movingRange_bfs(self, m, n, k):

        def sumDigits(n):
            r = 0
            while n:
                r, n = r + n % 10, n // 10
            return r

        marked = set()
        queue = collections.deque()
        queue.append((0, 0))
        while queue:
            x, y = queue.popleft()

        def bfs(i, j):
            while queue:

            if i == m or j == n or (i, j) in marked:
                return False
            if sumDigits(i) + sumDigits(j) > k:
                return False
            marked.add(i, j)
            queue.append((i+1, j), (i, j+1))


