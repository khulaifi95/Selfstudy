import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(1,100,50)

y = 2 * np.sqrt(np.log(x)/(x/10))

# plt.plot(x,y)

# plt.show()

print(x[np.argmax(y)])