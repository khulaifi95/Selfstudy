# import sys
# if __name__ == "__main__":
#     # 读取第一行的n
#     n = int(sys.stdin.readline().strip())
#     ans = 0
#     for i in range(n):
#         # 读取每一行
#         line = sys.stdin.readline().strip()
#         # 把每一行的数字分隔后转化成int列表
#         values = list(map(int, line.split()))
#         for v in values:
#             ans += v
#     print(ans)

# import collections
# nums = [1,3,4,5,1,3,3]
# cnt = collections.defaultdict(int)
# for i in nums:
#     cnt[i] += 1
# print(cnt)

# import math

# print(math.exp(0.5))

res = [{1,2,3}, {1,2}]


import collections


cnt = collections.Counter(res)
print(cnt)