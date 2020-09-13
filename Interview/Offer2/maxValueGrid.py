class Solution:
    def maxValueGrid(self, grid: [[int]]) -> int:
        # Time:  O(n)
        # Space: O(1)
        m, n = len(grid), len(grid[0])
        for i in range(1, m):   # first column
            grid[i][0] += grid[i - 1][0]
        for j in range(1, n):   # first row
            grid[0][j] += grid[0][j - 1]

        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += max(grid[i][j - 1], grid[i - 1][j])

        return grid[-1][-1]