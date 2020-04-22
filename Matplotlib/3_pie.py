import matplotlib.pyplot as plt

plt.style.use('fivethirtyeight')

slices = [59219, 55466, 47544, 36443, 35917]
labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java']
explode = [0, 0, 0, 0.1, 0]	# % of ratio

plt.pie(slices, explode=explode, shadow=True, labels=labels,
	wedgeprops={'edgecolor': 'black'}, autopct='%1.1f%%')

plt.title("My Awesome Pie Chart")
plt.tight_layout()

plt.show()
