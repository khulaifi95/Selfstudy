# Union find algorithms.


class QuickFindUF:
    # O(N^2)

    def __init__(self, N):
        self.id = [i for i in range(N)]

    def connected(self, p, q):
        return self.id[p] == self.id[q]

    def union(self, p, q):
        for i in range(len(self.id)):
            if self.id[i] == self.id[p]:
                self.id[i] = self.id[q]

sol = QuickFindUF(5)

sol.union(2, 3)
print(sol.connected(2, 3))
print(sol.connected(1, 4))


class QuickUnionUF:

    def __init__(self, N):
        self.id = [i for i in range(N)]

    def root(self, i):
        while i != self.id[i]:
            i = self.id[i]
        return i

    def connected(self, p, q):
        return self.id[p] == self.id[q]

    def union(self, p, q):
        i, j = self.root(p), self.root(q)
        self.id[i] = j


class WeightedQuickUnionUF:

    def __init__(self, N):
        self.id = [i for i in range(N)]

    def root(self, i):
        while i != self.id[i]:
            i = self.id[i]
        return i

    def size(self, i):
        self.id[i]

    def connected(self, p, q):
        return self.id[p] == self.id[q]

    def union(self, p, q):
        i, j = self.root(p), self.root(q)
        if i == j:
            return
        if self.size[i] < self.size[j]:
            self.id[i] = j
            self.size[j] += self.size[i]
        else:
            self.id[j] = i
            self.size[i] += self.size[j]
