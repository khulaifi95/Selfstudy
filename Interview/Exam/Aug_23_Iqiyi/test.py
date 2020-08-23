
# import sys 
# for line in sys.stdin:
#     a = line.split()
#     print(int(a[0]) + int(a[1]))

# if __name__ == "__main__":
#     # 读取第一行的n
#     n = int(sys.stdin.readline().strip())
#     ans = 0
#     for i in range(n):
#         line = sys.stdin.readline().strip()
#         values = list(map(int, line.split()))

d = 'hi'

q = ' h i world'

import re

res = re.sub(r'd+"."', 'k', q)

print(res)