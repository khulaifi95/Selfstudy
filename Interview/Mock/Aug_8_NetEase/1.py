import sys

if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    line = sys.stdin.readline().strip()
    arr = list(map(int, line.split()))

    tot = 0
    for i in range(n):
        tot += arr[i] // 2 

    return tot
