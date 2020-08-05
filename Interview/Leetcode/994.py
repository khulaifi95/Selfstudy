import numpy as np
import collections

class Solution(object):
    def orangesRotting(self, grid):
        R, C = len(grid), len(grid[0])

        # queue - all starting cells with rotting oranges
        queue = collections.deque()
        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                if val == 2:
                    queue.append((r, c, 0))

        def neighbors(r, c):
            for nr, nc in ((r-1,c),(r,c-1),(r+1,c),(r,c+1)):
                if 0 <= nr < R and 0 <= nc < C:
                    yield nr, nc

        d = 0
        while queue:
            r, c, d = queue.popleft()
            for nr, nc in neighbors(r, c):
                if grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    queue.append((nr, nc, d+1))

        if any(1 in row for row in grid):
            return -1
        return d


class Solution2:
    def orangesRotting(self, grid):
        m, n = len(grid), len(grid[0]) # read length and width of grid
        visit = [[False] * n for y in range(m)] # initiate grid state
        stack = [[y, x] for y in range(m) for x in range(n) if grid[y][x]==2] # find rotten at initial state
        direction = [[-1, 0], [1, 0], [0, -1], [0, 1]] # define spreading method
        minute = 0
        
        while True: # start iteration of spreading
            stack_next = [] # initiate the rotten oranges in this round
            while stack: # check every rotten oranges already in the stack
                y, x = stack.pop() # read the coordinates
                for d in direction: # find routes to neighbours
                    y_new, x_new = y + d[0], x + d[0] # only if within the grid and the value is 1
                    if 0 <= y_new < m and 0 <= x_new <n and not visit[y_new][x_new] and grid[y_new][x_new]==1:
                        visit[y_new][x_new] = True # mark as visited
                        grid[y_new][x_new] = 2 # set to be rotten
                        stack_next.append([y_new, x_new]) # add the newly rotten orange into the rubbish bin
            if not stack_next: break
            stack = stack_next
            minute += 1
        
        return -1 if ['survive' for y in range(m) for x in range(n) if grid[y][x]==1] else minute


sol = Solution()
sol2 = Solution2()
grid = np.random.randint(3, size=(4,3))