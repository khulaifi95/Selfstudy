import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('ggplot')

data = pd.read_csv('5_data.csv')

ages = data['Age']
dev_salaries = data['All_Devs']
py_salaries = data['Python']
js_salaries = data['JavaScript']


plt.plot(ages, dev_salaries, linestyle='--', label='All_Devs')

plt.plot(ages, py_salaries, label='Python')

overall_median = 57287  # y2

plt.fill_between(ages, py_salaries, overall_median,
                 where=(py_salaries > dev_salaries),
                 interpolate=True, alpha=0.25, label='Above Dev')

plt.fill_between(ages, py_salaries, overall_median,
                 where=(py_salaries <= overall_median),
                 interpolate=True, alpha=0.25, label='Below Avg')

plt.legend()

plt.title('Median Salary by Age')
plt.xlabel('Ages')
plt.ylabel('Median Salary')

plt.savefig('img/5.png', dpi=300)

plt.show()