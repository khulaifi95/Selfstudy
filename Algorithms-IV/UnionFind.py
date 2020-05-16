# Union find algorithms.
# Application: percolation p*=0.593

class QuickFindUF:
    # Eager approach: O(MN)

    def __init__(self, N):
        self.id = [i for i in range(N)]

    def connected(self, p, q):
        # check if have the same id
        return self.id[p] == self.id[q]

    def union(self, p, q):
        # change all entries equals id[p] to id[q]
        for i in range(len(self.id)):
            if self.id[i] == self.id[p]:
                self.id[i] = self.id[q]

sol = QuickFindUF(5)

sol.union(2, 3)
print(sol.connected(2, 3))
print(sol.connected(1, 4))


class QuickUnionUF:
    # Lazy approach: Find - O(N)
    # Trees can get tall.

    def __init__(self, N):
        # id[i] is the parent of i
        self.id = [i for i in range(N)]

    def root(self, i):
        # find the root of i until equal to the entry
        while i != self.id[i]:
            i = self.id[i]
        return i

    def connected(self, p, q):
        # check if have the same root
        return self.id[p] == self.id[q]

    def union(self, p, q):
        # assign one entry to the root of the other's
        i, j = self.root(p), self.root(q)
        self.id[i] = j


# Improvement:
# Weighted Quick Union with Path Compression Union Find:


class WQUPCUF:
# Avoid tall trees by keeping track of size of trees.
# O(N+ Mlg* N)  Proof:
# If the tree containing x is merged into another tree, it doubles at least.
# Size of the tree containing x can only double at most lg N times.

    def __init__(self, N):
        self.id = [i for i in range(N)]

    def root(self, i):
        while i != self.id[i]:
            id[i] = id[id[i]]   # path compression
            i = self.id[i]
        return i

    def size(self, i):
        # count number of objects in the tree
        self.id[i]

    def connected(self, p, q):
        return self.id[p] == self.id[q]

    def union(self, p, q):
        # link root of smaller tree to root of larger tree
        # update size[] array
        i, j = self.root(p), self.root(q)
        if i == j:
            return
        if self.size[i] < self.size[j]:
            self.id[i] = j
            self.size[j] += self.size[i]
        else:
            self.id[j] = i
            self.size[i] += self.size[j]
