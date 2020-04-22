import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('ggplot')

data = pd.read_csv('10_data.csv')

ages = data['Age']
dev_salaries = data['All_Devs']
py_salaries = data['Python']
js_salaries = data['JavaScript']

fig, ([ax1, ax2], [ax3, ax4]) = plt.subplots(2, 2, sharex=True)


ax1.plot(ages, py_salaries, label='Python', color='blue')
ax2.plot(ages, js_salaries, label='JavaScript', color='orange')
ax3.plot(ages, dev_salaries, label='All Devs', color='red')
ax4.plot(ages, py_salaries, label='Python')
ax4.plot(ages, js_salaries, label='JavaScript')
ax4.plot(ages, dev_salaries, label='All Devs')

ax1.legend()
ax2.legend()
ax3.legend()
ax4.legend()

# ax.set_title('Median Salary by Age')
ax4.set_xlabel('Ages')
# ax.set_ylabel('Median Salary')

plt.tight_layout()

plt.savefig('img/10.png', dpi=300)

plt.show()

