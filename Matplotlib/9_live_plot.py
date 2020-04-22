import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.style.use('ggplot')

index = count()

def animate(i):
	data = pd.read_csv('9_data.csv')
	x = data['x_value']
	y1 = data['total_1']
	y2 = data['total_2']

	plt.cla()

	plt.plot(x, y1, label='Channel 1')
	plt.plot(x, y2, label='Channel 2')

	plt.legend(loc='upper left')
	plt.tight_layout()
	plt.savefig('img/9.png', dpi=300)


ani = FuncAnimation(plt.gcf(), animate, interval=1000)

plt.tight_layout()

plt.show() 


