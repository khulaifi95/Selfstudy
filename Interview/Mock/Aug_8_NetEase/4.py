import sys
import math

class Sol:
    def __init__(self, n):
        id = [i for i in range(n)]

    def connected(self, p, q):
        return q==self.root[p]

    def root(self, i):
        while i != self.id[i]:
            i = self.id[i]
        return i

    def union(self, p, q):
        self.id[q] = p

    def main(self, pairs):
        res = []
        for rel in pairs:
            if self.connected(rel[0], rel[1]):
                res.append(rel)
            self.union(rel[0], rel[1])

        num = 0
        for i in res:
            count = 0
            while self.id[res[0]] != res[0]:
                count += 1
            num += math.factorial(count)

        return num






if __name__ == '__main__':

    line = sys.stdin.readline().strip()
    values = list(map(int, line.split()))

    n, m = values[0], values[1]
    id = [i for i in range(n)]
    pairs = [[] for _ in range(m)]

    for i in range(m):
        rel_line = sys.stdin.readline().strip()
        rel_pair = list(map(int, rel.split()))
        pairs[i] = rel_pair

    k = Sol(n)
    k.main(pairs)



        
