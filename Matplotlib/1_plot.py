import numpy as np
import matplotlib.pyplot as plt

plt.style.use('ggplot')	# fivethirtyeight

# plt.xkcd()	# use alternative hand-written style

# Median developer salary by age
age_x = np.arange(25, 36)

dev_y = [38496, 42000, 46752, 49320, 53200,
         56000, 62316, 64928, 67317, 68748, 73752]

plt.plot(age_x, dev_y, linewidth=3, label='All Devs')

# Median Python developer salary by age
py_dev_y = [45372, 48876, 53850, 57287, 63016,
            65998, 70003, 70000, 71496, 75370, 83640]

plt.plot(age_x, py_dev_y, label='Python Devs')	# '.b-.'

# Median JavaScript Developer Salaries by Age
js_dev_y = [37810, 43515, 46823, 49293, 53437,
            56373, 62375, 66674, 68745, 68746, 74583]

plt.plot(age_x, js_dev_y, label='Python Devs')	# 'y-'


plt.xlabel('Ages')
plt.ylabel('Median Salary')
plt.title('Median Salary by Age')

plt.legend()

plt.tight_layout()
# plt.grid(True)

plt.savefig('img/1.png', dpi=300)

plt.show()
