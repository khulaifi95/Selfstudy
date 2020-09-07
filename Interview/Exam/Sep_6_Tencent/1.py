# len = 2n
# n -- | n ++

import sys
import collections

def sol(nums):
    def search(a, b, l):
        left, right = 0, 0
        vl = l[a], vr = l[b]
        for i in l[:a+1]:
            if i > vl:
                left += 1
                vl = i
        for j in l[b:]:
            if j < vr:
                right += 1
                vr = j
        return left + right

    cnt = collections.defaultdict(int)
    pairs = collections.defaultdict(list)
    for i in range(len(nums)):
        cnt[nums[i]] += 1
        pairs[nums[i]].append(i)

    val = [i for i in cnt if cnt[i] > 1]
    res = 0
    for i in val:
        queue = sorted(pairs[i])
        mid = len(queue) // 2
        res = max(res, max(search(mid - 1, mid, nums), search(mid, mid + 1, nums)))

    return res




t = int(sys.stdin.readline().strip())

for i in range(t):
    n = int(sys.stdin.readline().strip())
    line = sys.stdin.readline().strip()
    values = list(map(int, line.split()))
    print(sol(values))




