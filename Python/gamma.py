import matplotlib.pyplot as plt
import numpy as np
import math

x = np.linspace(1, 5, 5)
y = [math.factorial(i-1) for i in x]

plt.plot(x,y)
plt.show()