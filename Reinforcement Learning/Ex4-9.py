# Gambler's problem
# Value iteration

# state: [1,99] + terminal 0,100
# action: [0,min(s, 100-s)]
# reward: 0 for all except +1 for 100

import numpy as np

theta = delta = 0.01

s = v = r = [0 for i in range(101)]
r[100] = 1

a = 

ss = [s + a, s - a]

prob = 0.4


while delta >= theta:
    delta = 0
    for i in range(100):
        v = v[i]
        v[i] = r[i] + max(v[i+1])

