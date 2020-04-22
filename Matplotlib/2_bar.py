import numpy as np
import matplotlib.pyplot as plt

plt.style.use("ggplot")	# ggplot

ages_x = np.arange(25,36) 
width = 0.25


# Median Developer Salaries by Age
dev_y = [38496, 42000, 46752, 49320, 53200,
         56000, 62316, 64928, 67317, 68748, 73752]

plt.bar(ages_x - width, dev_y, width=width, label="All Devs")


# Median Python Developer Salaries by Age
py_dev_y = [45372, 48876, 53850, 57287, 63016,
            65998, 70003, 70000, 71496, 75370, 83640]

plt.bar(ages_x, py_dev_y, width=width, label="Python")


# Median JavaScript Developer Salaries by Age
js_dev_y = [37810, 43515, 46823, 49293, 53437,
            56373, 62375, 66674, 68745, 68746, 74583]

plt.bar(ages_x + width, js_dev_y, width=width, label="JavaScript")

plt.legend()

plt.xticks(ticks=ages_x, labels=ages_x)

plt.title("Median Salary by Age")
plt.xlabel("Ages")
plt.ylabel("Median Salaries")

plt.tight_layout()

plt.savefig('img/2_1.png', dpi=300)

plt.show() 