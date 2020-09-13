import sys

inp = sys.stdin.readline().strip()
par = list(map(int, inp.split()))
n, m = par

nums = [[] for i in range(n)]
for line in range(n):
    val = sys.stdin.readline().strip()
    nums[line] = list(map(int, val.split()))

def sol(nums, n):
    if nums[0:(n//2)] == nums[(n-1):(n//2-1):-1]:
        return sol(nums[0:(n//2)], n//2)
    else:
        return nums

ret = sol(nums, n)

for i in range(len(ret)):
    print(' '.join(map(str, ret[i])))
