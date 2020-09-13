import sys

line = sys.stdin.readline().strip()
par = list(map(int, line.split()))
n, m = par

map = [[int(1e9) for i in range(n)] for i in range(n)]

for i in range(m):
    subline = sys.stdin.readline().strip()
    val = list(map(int, subline.split()))
    u, v, time = val
    map[u][v] = time

line = sys.stdin.readline().strip()
test = list(map(int, line.split()))
s, e, start = test

print(map)

