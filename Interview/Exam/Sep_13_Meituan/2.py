import sys

inp = sys.stdin.readline().strip()
par = list(map(int, inp.split()))
n, m, k = par

val = sys.stdin.readline().strip()
nums = list(map(int, val.split()))

def sol(nums, n, m, k):
    ret = [1 if nums[i] >= k else 0 for i in range(n)]
    l = 0
    res = 0
    while l + m <= n:
        if sum(ret[l:l+m]) >= m:
            res += 1
        l += 1

    return res


print(sol(nums, n, m, k))