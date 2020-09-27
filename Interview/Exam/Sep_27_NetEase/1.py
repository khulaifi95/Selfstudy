c = int(input())
for _ in range(c):
    n, m = map(int, input().split())
    search = [() for _ in range(m)]
    for i in range(m):
        search[i] = tuple(list(map(int, input().split())))

    # print(n, m)
    # print(search)

    # Build the matrix
    l, r, t, b = 0, n - 1, 0, n - 1
    grid = [[0 for i in range(n)] for j in range(n)]
    cur = 1
    tar = n * n
    ro = 0

    while cur <= tar:
        if ro % 2 == 0:
            for i in range(l, r + 1):
                grid[t][i] = cur
                cur += 1
            t += 1

            for i in range(t, b + 1):
                grid[i][r] = cur
                cur += 1
            r -= 1

            for i in range(r, l - 1, -1):
                grid[b][i] = cur
                cur += 1
            b -= 1

            for i in range(b, t - 1, -1):
                grid[i][l] = cur
                cur += 1
            l += 1

        else:
            for i in range(t, b + 1):
                grid[i][l] = cur
                cur += 1
            l += 1

            for i in range(l, r + 1):
                grid[b][i] = cur
                cur += 1
            b -= 1

            for i in range(b, t - 1, -1):
                grid[i][r] = cur
                cur += 1
            r -= 1

            for i in range(r, l - 1, -1):
                grid[t][i] = cur
                cur += 1
            t += 1

        ro += 1


    # Search in matrix
    for i in search:
        print(grid[i[0]][i[1]])