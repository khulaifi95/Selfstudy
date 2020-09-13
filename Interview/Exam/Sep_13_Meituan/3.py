import sys
import math

inp = sys.stdin.readline().strip()
par = list(map(int, inp.split()))
n, k, d = par

# sum(arr) = n
# arr[i] >= 1
# d <= max(arr) <= k

def sol(n, k, d):
    res = 0
    m = min(k+1, n)
    for i in range(d, m):
        res += math.factorial(i+1) - 1
    return res

print(sol(n,k,d))