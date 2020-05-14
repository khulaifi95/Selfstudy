import numpy as np
import matplotlib.pyplot as plt

def factorial(n):
    num = {}
    num[0] = 1
    num[1] = 1
    if n > 1:
        for i in range(2, n+1):
            num[i] = num[i-1] * i
    return num[n]

def poi(k, theta):
    res = theta**k / factorial(k)
    return res


x = [i for i in range(50)]
y = [poi(i, 0.9) for i in x]

fig = plt.figure()
ax = fig.subplots()
line, = ax.plot(y)
ax.set_yscale('log')
ax.set_xlabel('Poisson process')
# plt.plot(x,y)
plt.show()

print(y[:9])