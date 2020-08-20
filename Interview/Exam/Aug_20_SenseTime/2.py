import sys

inp = sys.stdin.readline().strip()
ls = list(inp)

n = len(ls) - 1
pg, po, pd = 0, 0, 0

while pg < n:
    if ls[pg] == 'G':
        po += 1

if __name__ == '__main__':
    main()