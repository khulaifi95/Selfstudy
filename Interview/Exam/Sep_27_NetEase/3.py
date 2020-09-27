C = int(input())    # group
for _ in range(C):
    n, d = map(int, input().split())    # num of data, dimension
    X = [[0 for i in range(d)] for j in range(n)]
    Y = [0 for i in range(n)]
    for i in range(n):
        line = list(map(int, input().split()))
        X[i] = line[:d]
        Y[i] = line[-1]

    m, k = map(int, input().split())    # num of hidden layer, num of edge
    t = list(map(int, input().split())) # num of neurons in hidden layers
    w_i = [[0 for i in range(d)] for j in range(t[0])]  # input w
    w_o = [0 for i in range(t[0])]                      # output w
    if m == 2:
        w_m = [[0 for i in range(t[0])] for j in range(t[1])] # hidden w

    for j in range(k):
        line = input().split()
        print(line)
        if 'input' in line[0]:
            a = int(line[0][-1])
            b = int(line[1][-1])
            w_i[a-1][b-1] = int(line[2])
        if 'output' in line[1]:
            c = int(line[0][-1])
            w_o[c-1] = int(line[2])
        if m == 2 and 'hidden' in line[0] and 'hidden' in line[1]:
            d = int(line[0][-1])
            e = int(line[1][-1])
            w_m[d-1][e-1] = int(line[2])


def main():
    return -1



if __name__ == '__main__':
    main()



