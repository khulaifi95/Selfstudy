# nums = [1,2,3,0,0,0]
# print(bool(stack))
# print(nums[3:6])
# stack = [0]

# import sys
# print(sys.version)

# def myisalnum(self, a: str) -> bool:
#     return (a >= 'a' and a <= 'z') or (a >= 'A' and a <= 'Z') or (a >= '0' and a <= '9')


# print(myisalnum('k'))


# queue = [1,3,4,6]

# print(queue.pop(0))


# mapp = {1:5, 2:6}

# mapp[1] = 12
# print(mapp[1])

# import sqlite3
# print(dir(sqlite3))

# for i in range(5, -1, -1):
#     print(i)

# stack = [-1, -5]

# print(stack.pop(0))

# import collections

# s = 'mississippi'

# d = collections.defaultdict(int)
# for k in s:
#     d[k] += 1

# print(d.items())

# minl = float('inf')
# print(minl)

from collections import defaultdict
d = defaultdict(int)
t = "ABCDA"
for i in t:
    d[i] += 1
print(list(d.items()))