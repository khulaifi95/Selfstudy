import sys
n = int(input())
l = []

# def insert_(l, a, b):
#     if a > 0:
#         l.insert(a - 1, b)
#         print(l)

# def remove_(l, a):
#     l = l[:a-1] + l[a:]
#     print(l)

# def check_(l):
#     res = ''
#     for i in l:
#         res += str(i) + ' '
#     print(res.strip())


for i in range(n):
    inp = sys.stdin.readline().strip()
    op = list(map(int, inp.split()))
    if op[0] == 1:
        l.insert(op[1]-1, op[2])
    if op[0] == 2:
        l = l[:op[1]-1] + l[op[1]:]
    if op[0] == 3:
        res = ''
        for i in l:
            res += str(i) + ' '
        print(res.strip())