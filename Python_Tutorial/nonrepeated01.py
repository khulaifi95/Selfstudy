# Return the expectation of the sum of array 
# where only 1s could be replaced by a 0 with probability.

import numpy as np

p = 0.6
size = 100000
stack = np.zeros(size)

stack[0] = 1
for i in range(1, size):
    if stack[i-1] == 1 and np.random.rand() <= p:
        stack[i] = 0
    else:
        stack[i] = 1

ave = stack.mean()
# print(ave)

def expectation(p, i):
    return (p+i*(1+p)+(-p)**i)/ ((1+p)**2*i)

print(expectation(0.6, 10000))

import matplotlib.pyplot as plt

p = np.linspace(0,1,50)
q = expectation(p, 10000)
plt.plot(p, q, 'r')
plt.plot(p, 1-p, 'b')
plt.show()