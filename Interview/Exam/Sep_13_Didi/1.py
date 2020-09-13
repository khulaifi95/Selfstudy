import sys

class UnionFind:
    def __init__(self, N):
        self.id = [i for i in range(N)]

    def root(self, i):
        while i != self.id[i]:
            i = self.id[i]
        return i

    def connected(self):
        for i in self.id:
            if self.root(i) != self.root(0):
                return False
        return True

    def union(self, p, q):
        i, j = self.root(p), self.root(q)
        self.id[i] = j

    def islands(self):
        return self.id


t = int(sys.stdin.readline().strip())

for i in range(t):
    line = sys.stdin.readline().strip()
    par = list(map(int, line.split()))
    n, m, k = par

    sol = UnionFind(n)

    for j in range(m):
        subline = sys.stdin.readline().strip()
        val = list(map(int, subline.split()))
        a, b, cost = val
        # i >= j
        if cost <= k:
            sol.union(a - 1, b - 1)

    if sol.connected():
        print("Yes")
    else:
        print("No")