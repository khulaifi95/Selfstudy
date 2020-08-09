## Number of Islands



#### Question:

Given a 2d grid map of `1`s (land) and `0`s (water), count the number of islands.

- An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
- You may assume all four edges of the grid are all surrounded by water.



#### Examples:

```pseudocode
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
```

```pseudocode
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
```



#### Solution:

1. **Depth-first search**

We can take the 2d grid as an undirected graph with edge of 1 length.

Scan the whole grid,

- If one location is filled with `1`, do a depth-first search starting from it.
- Every searched `1` will be remarked as `0`.
- Return the **times** we run DFS.

```python
class Solution:
    def dfs(self, grid, r, c):
        grid[r][c] = 0
        nr, nc = len(grid), len(grid[0])
        for x, y in [(r-1, c), (r+1, c), (r, c+1), (r, c-1)]:
            if 0 <= x < nr and 0 <= y < nc and grid[x][y] == "1":
                self.dfs(grid, x, y)
                
	def numIslandsDFS(self, grid: List[List[str]]) -> int:
        nr = len(grid)
        if nr == 0:
            return 0
        nc = len(grid[0])
        
        count = 0 
        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == "1":
                    count += 1
                    self.dfs(grid, r, c)
        
        return count
```



2. **Breadth-first search**

We can also search the whole grid in breadth-first approach.

Scan the whole grid,

- If one location is filled with `1`, add to `queue` and start breadth-first search.
- Every searched `1` will be remarked as `0` until `queue` is empty.
- Return the **times** we run BFS.

```python
class Solution:
    def numIslandsBFS(self, grid: List[List[str]]) -> int:
        nr == len(grid)
        if nr == 0:
            return 0
        nc = len(grid[0])
        
        count = 0
        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == "1":
                    count += 1
                    grid[r][c] = "0"
                    neighbours = collections.deque([r, c])
                    while neighbours:
                        row, col = neightbours.popleft()
                        for x, y in [(r-1, c), (r+1, c), (r, c+1), (r, c-1)]:
                            if 0 <= x < nr and 0 <= y < nc and grid[x][y] == "1":
                                neighbours.append((x, y))
                                grid[x][y] = "0"
                                
		return count

```



3. **Union find**

We can implement a union find algorithm to replace search methods.

Scan the whole grid,

- If one location is filed with `1`, `union` it with the neighbouring `1`s.
- Return the  number of unions.

```python
class UnionFind:
    def __init__(self, grid):
        m, n = len(grid), len(grid[0])
        self.count = 0
        self.parent = [-1] * (m * n)
        self.rank = [0] * (m * n)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    self.parent[i * n + j] = i * n + j
                    self.count += 1

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx != rooty:
            if self.rank[rootx] < self.rank[rooty]:
                rootx, rooty = rooty, rootx
            self.parent[rooty] = rootx
            if self.rank[rootx] == self.rank[rooty]:
                self.rank[rootx] += 1
            self.count -= 1

    def getCount(self):
        return self.count
```



#### Code:

```python
class UnionFind:
	/* ... */

class Solution:
	def numIslands(self, grid: List[List[str]]) -> int:
        nr = len(grid)
        if nr == 0:
            return 0 
        nc = len(grid[0])

        uf = UnionFind(grid)
        num_islands = 0
        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == "1":
                    grid[r][c] = "0"
                    for x, y in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                        if 0 <= x < nr and 0 <= y < nc and grid[x][y] == "1":
                            uf.union(r * nc + c, x * nc + y)

        return uf.getCount()
```

