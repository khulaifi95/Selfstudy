import csv
from collections import Counter
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('ggplot')

# Read csv file by built-in module
with open('2_data.csv') as csv_f:
	csv_reader = csv.DictReader(csv_f)

	language_counter = Counter()

	for row in csv_reader:
		language_counter.update(row['LanguagesWorkedWith'].split(';'))


languages, popularity = map(list, zip(*language_counter.most_common(15)))
languages.reverse()
popularity.reverse()

plt.barh(languages, popularity)

plt.title("Most Popular Languages")
# plt.ylabel("Programming Languages")
plt.xlabel("Number of People Who Use")

plt.tight_layout()

plt.savefig('img/2_2.png', dpi=300)

plt.show()