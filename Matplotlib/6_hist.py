import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('ggplot')

data = pd.read_csv('6_data.csv')
ids = data['Responder_id']
ages = data['Age']

bins = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

plt.hist(ages, bins, edgecolor='black', log=True)

median_age = 29

plt.axvline(median_age, color='purple', label='Age Median')

plt.legend()

plt.title('Median Salary by Age')
plt.xlabel('Ages')
plt.ylabel('Median Salary')

plt.savefig('img/6.png', dpi=300)

plt.show()