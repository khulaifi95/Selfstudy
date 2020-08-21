import sys

def cross(n, weight):
    queue = sorted(weight)
    res = 0
    while n >= 1:
        if n == 1 or n == 3:
            res += sum(queue)
            return res
        if n == 2:
            res += queue[1]
            return res
        else:
            res += min((2 * queue[0] + queue[n-1] + queue[n-2]), (queue[0] + 2 * queue[1] + queue[n-1]))
            n -= 2
            queue.pop()
            queue.pop()
            

    return res


t = int(sys.stdin.readline().strip())
for i in range(t):
    n = int(sys.stdin.readline().strip())
    line = sys.stdin.readline().strip()
    weight = list(map(int, line.split()))
    print(cross(n, weight))