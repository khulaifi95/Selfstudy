import sys

n = int(input())
tri = [[] for _ in range(n)]

for i in range(n):
    inp = sys.stdin.readline().strip()
    tri[i] = list(map(int, inp.split()))

k = n - 2

while k >= 0:
    for i in range(2*k+1):
        tri[k][i] += max(tri[k+1][i:i+3])
    k -= 1

print(tri[0][0])
