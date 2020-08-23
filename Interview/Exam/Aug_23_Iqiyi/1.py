import sys

line1 = sys.stdin.readline().strip()
m = list(map(str, line1.split()))

line2 = sys.stdin.readline().strip()
d = list(map(str, line2.split()))

q = list('|'.join(m))

import re

for i in d:
    q = re.sub(i, '|'+i+'|', q)

q = re.split(r'\W+', q)